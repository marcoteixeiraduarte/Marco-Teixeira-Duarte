# 03 — Ablage in GitHub

Damit Desktop, App und Cloud dieselbe Mappe sehen.
Standard ist der Rechner. Cloud nur als Ausnahme.
Dieses Repo ist **öffentlich**. Was hier liegt, liegt im Netz.
Der Server nicht — außer jemand pusht lokale Dateien.
Rechner-Verbindung: [`06-geraete.md`](06-geraete.md).
Privat: [`04-privat.md`](04-privat.md).

## Git ist die Mappe

| Datei / Ordner | Rein | Nicht rein |
| --- | --- | --- |
| `STAND.md` | Handoff, nächster Schritt, kurzes Log | lange Transkripte |
| `ERKENNTNISSE.md` | gesicherte Synthese nach Merge | Entwürfe aus offenen PRs als Fakt |
| `regeln/` | Methode | Personenlisten |
| `evidenz/**/*.md` | ein Ereignis oder eine Person, mit Scan | Spekulation ohne Akt |
| `evidenz/scans/` | versionierte Belegbilder | Ausweise, Familienfotos Lebender |
| `archiv/` | Match-Scans, höchste öffentliche Auflösung, sprechende Namen | Hochskalierung, Nachzeichnung |
| `*-records/` | Personenakte + README + die in `.gitignore` freigegebenen JPEGs | ganze Bände «auf Vorrat» |
| `stammbaum/` | Gegenlese bisavós und älter | lebende, avós |
| `00_Arbeitsordner/` | — | alles (gitignore) |

Neue JPEG-Datei: in `.gitignore` die Ausnahme setzen (`!pfad/datei.jpg`),
sonst liegt sie nur lokal und der Cloud-Agent sieht sie nicht.

## Issue = Auftrag

Vorlage unter `.github/ISSUE_TEMPLATE/`. Kurz reicht, wenn Ziel und
«nicht tun» klar sind. Der Agent bekommt z. B.:

`Issue #N umsetzen. AGENTS.md und STAND.md zuerst.`

## PR = Rückweg

Vorlage `.github/PULL_REQUEST_TEMPLATE.md`. Ein Fund ohne PR und ohne
`STAND.md`-Zeile ist für den nächsten Lauf unsichtbar.

`master` nur nach Gegenlese mergen. Offene Draft-PRs anderer Läufe
nicht still in die Synthese kippen.

## Branch

Cloud-Branches wie bisher. Neue Regeln und neue Funde dürfen im
selben PR liegen, wenn der Fund die Regel braucht. Sonst trennen:
erst Regel, dann Suche.
