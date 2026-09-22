#!/usr/bin/env python3
"""Nachweis für Belegerhalt und Wiederherstellung.

Schreibt repo_head (git rev-parse HEAD) und repo_tree (HEAD^{tree})
in jede Ergebnisdatei. Zwei Läufe mit demselben Prüfstand dürfen
deshalb nicht bytegleich sein: der Wiederherstellungslauf trägt
zusätzlich den SHA-256 der Belegerhalt-Datei und den Passnamen.

Aufruf im importierten Repository:

    python3 stammbaum/validate.py --pass belegerhalt
    python3 stammbaum/validate.py --pass wiederherstellung
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

VALIDATOR_VERSION = "1.1.0"
ROOT = Path(__file__).resolve().parents[1]

BELEGERHALT = ROOT / "stammbaum" / "Belegerhalt-und-Struktur.json"
WIEDERHERSTELLUNG = ROOT / "stammbaum" / "Wiederherstellung-Pruefung.json"

KEY_PATHS = [
    "stammbaum/teixeira-duarte.ged",
    "stammbaum/validate.py",
    "evidenz/linie-torre/katalog/1886-manoel-dias-guiomar.json",
    "evidenz/linie-torre/katalog/1901-antonio-dias-guiomar.json",
    "evidenz/linie-torre/narciza.md",
    "evidenz/linie-torre/zwei-reis-haeuser-pragoza.md",
    "evidenz/linie-torre/ramalha-ateanha-1873.md",
    "evidenz/linie-torre/joaquina-reis-leal.md",
    "akten/matta/casimiro-1898/README.md",
    "akten/matta/sebastiao-1871/README.md",
    "akten/matta/README.md",
    "evidenz/integration-2026-09-22.md",
]


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_identity() -> dict:
    try:
        head = git("rev-parse", "HEAD")
        tree = git("rev-parse", "HEAD^{tree}")
        porcelain = git("status", "--porcelain")
        describe = git("rev-parse", "--abbrev-ref", "HEAD")
    except subprocess.CalledProcessError as exc:
        return {
            "ok": False,
            "error": str(exc),
            "repo_head": None,
            "repo_tree": None,
            "working_tree": None,
            "branch": None,
        }
    dirty = [line for line in porcelain.splitlines() if line.strip()]
    return {
        "ok": True,
        "repo_head": head,
        "repo_tree": tree,
        "branch": describe,
        "working_tree_clean": not dirty,
        "working_tree": dirty,
        "note": (
            "repo_head und repo_tree gelten für den ausgecheckten Commit. "
            "Ein späteres Commit dieser JSON-Datei ändert HEAD; der Nachweis "
            "bezieht sich auf den Stand, gegen den geprüft wurde."
        ),
    }


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def case(ident: str, titel: str, ok: bool, detail: str) -> dict:
    return {"id": ident, "titel": titel, "ok": ok, "detail": detail}


def run_cases() -> list[dict]:
    ged = read_text("stammbaum/teixeira-duarte.ged")
    narciza = read_text("evidenz/linie-torre/narciza.md")
    seb = read_text("evidenz/linie-torre/zwei-reis-haeuser-pragoza.md")
    seb_akte = read_text("akten/matta/sebastiao-1871/README.md")
    cas = read_text("akten/matta/casimiro-1898/README.md")
    ramalha = read_text("evidenz/linie-torre/ramalha-ateanha-1873.md")
    leal = read_text("evidenz/linie-torre/joaquina-reis-leal.md")
    suche = read_text("evidenz/suche-erweitert.md")
    stamm = read_text("stammbaum/README.md")

    line_readmes = [
        ROOT / "akten" / name / "README.md"
        for name in ("matta", "guiomar", "narcisa", "jose-maria", "teixeira")
    ]
    broken = []
    for path in line_readmes:
        text = path.read_text(encoding="utf-8")
        if "](../evidenz/" in text or "](../archiv/" in text:
            broken.append(str(path.relative_to(ROOT)))

    cases = [
        case(
            "GED-01",
            "GEDCOM CHAR UTF-8",
            "1 CHAR UTF-8" in ged,
            "Kopfzeile CHAR UTF-8 muss stehen.",
        ),
        case(
            "GED-02",
            "Tippfehler geneaologische entfernt",
            "geneaologische" not in ged and "genealogische" in ged,
            "Eigene Notizen schreiben genealogische; historische Namensformen bleiben.",
        ),
        case(
            "GED-03",
            "Keine bestätigte Familie F47",
            "0 @F47@" not in ged,
            "Elternkante Joaquina → José dos Reis × Maria Ramalha bleibt aus dem bestätigten Export.",
        ),
        case(
            "GED-04",
            "I37 ohne FAMC F18",
            "1 FAMC @F18@" not in ged,
            "F18 nicht als Eltern Joaquinas wiederherstellen.",
        ),
        case(
            "GED-05",
            "F18 ohne Kind I37",
            "1 CHIL @I37@" not in ged,
            "Blattpaar Ramalho × Leal bleibt Paar ohne Joaquina-Kindkante.",
        ),
        case(
            "REIS-01",
            "Sebastião ist primeiro deste nome, nicht Erstgeburt",
            (
                "primeiro deste nome" in seb
                and "primeiro deste nome" in seb_akte
                and "Akt: primeiro filho — daneben schon José 1866" not in seb
            ),
            "Die Formel erster dieses Namens erzeugt keinen Geschwisterwiderspruch.",
        ),
        case(
            "CAS-01",
            "Casimiro Geburt 06.12.1898, Taufe 26.12.1898 getrennt",
            "06.12.1898" in cas and "26.12.1898" in cas and "Taufe selben Tag" not in cas,
            "Geburtstag und Tauftag nicht zusammenfalten; Nottaufe ohne eigenes Datum.",
        ),
        case(
            "RAM-01",
            "Heirat 1838: beide Datumslesungen",
            "Vinte e hum" in ramalha and "Vinte dois" in ramalha,
            "21.02 und 22.02 bleiben nebeneinander; Datum nicht sicher.",
        ),
        case(
            "LNK-01",
            "Relative Verweise in den fünf Linienübersichten",
            not broken,
            "Keine Treffer ../evidenz oder ../archiv in akten/*/README.md"
            if not broken
            else "noch kaputt: " + ", ".join(broken),
        ),
        case(
            "KAT-01",
            "Passkataloge 1886 und 1901 aus #14",
            (ROOT / "evidenz/linie-torre/katalog/1886-manoel-dias-guiomar.json").is_file()
            and (ROOT / "evidenz/linie-torre/katalog/1901-antonio-dias-guiomar.json").is_file(),
            "#14 ist kein überholter Vorläufer; die Katalog-JSONs bleiben.",
        ),
        case(
            "NAR-01",
            "Narciza: September- und Oktober-Lesung nebeneinander",
            "Setembro" in narciza and "Oktober" in narciza and "mez passado" in narciza,
            "Lesung #16 nicht durch Lesung #17 ersetzen.",
        ),
        case(
            "OFF-01",
            "Antonio N.º 9 und Zivilfoto 01 bleiben offen",
            (
                "Francisco José dos Santos" in stamm
                and "Manuel dos Santos" in stamm
                and "Benedita" in suche
                and "Nazareth" in suche
            ),
            "Beide Lesungspaare stehen noch; nicht zu einer sicheren Zuweisung falten.",
        ),
    ]
    _ = leal
    return cases


def checksums() -> dict:
    out = {}
    for rel in KEY_PATHS:
        path = ROOT / rel
        if path.is_file():
            out[rel] = sha256_file(path)
        else:
            out[rel] = None
    return out


def build_report(pass_name: str) -> dict:
    identity = git_identity()
    cases = run_cases()
    report = {
        "validator_version": VALIDATOR_VERSION,
        "pass": pass_name,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repo_head": identity.get("repo_head"),
        "repo_tree": identity.get("repo_tree"),
        "git": identity,
        "cases": cases,
        "cases_ok": all(c["ok"] for c in cases),
        "checksums": checksums(),
    }
    if pass_name == "wiederherstellung":
        if not BELEGERHALT.is_file():
            report["belegerhalt"] = None
            report["belegerhalt_missing"] = True
        else:
            report["belegerhalt"] = {
                "path": str(BELEGERHALT.relative_to(ROOT)),
                "sha256": sha256_file(BELEGERHALT),
            }
            belegerhalt = json.loads(BELEGERHALT.read_text(encoding="utf-8"))
            report["same_head_as_belegerhalt"] = (
                belegerhalt.get("repo_head") == report["repo_head"]
            )
            report["same_tree_as_belegerhalt"] = (
                belegerhalt.get("repo_tree") == report["repo_tree"]
            )
            report["byte_identical_to_belegerhalt"] = False
            report["why_not_byte_identical"] = (
                "Dieser Lauf trägt pass=wiederherstellung und den SHA-256 "
                "der Belegerhalt-Datei. Zwei gleiche Ergebnisdateien allein "
                "seien kein zweiter Lauf."
            )
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pass",
        dest="pass_name",
        choices=("belegerhalt", "wiederherstellung"),
        required=True,
    )
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args(argv)

    report = build_report(args.pass_name)
    out = args.out
    if out is None:
        out = BELEGERHALT if args.pass_name == "belegerhalt" else WIEDERHERSTELLUNG
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    try:
        shown = out.resolve().relative_to(ROOT)
    except ValueError:
        shown = out
    print(f"wrote {shown}")
    print(f"repo_head={report['repo_head']}")
    print(f"repo_tree={report['repo_tree']}")
    print(f"cases_ok={report['cases_ok']}")
    for item in report["cases"]:
        mark = "OK" if item["ok"] else "FAIL"
        print(f"  {mark} {item['id']} {item['titel']}")
    return 0 if report["cases_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
