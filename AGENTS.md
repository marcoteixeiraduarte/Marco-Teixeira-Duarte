# Agenten — Desktop, App und Cloud

Dieses Repo ist das gemeinsame Gedächtnis. Desktop (Cursor am
Rechner), App (Handy) und Cloud-Agent sehen **nur**, was in Git
auf `master` (oder im aktuellen PR) liegt — außer der Lauf
läuft auf dem Rechner (Remote Control oder My Machines).
Gespräche sind keine Ablage.

## Pflicht vor jeder Arbeit

1. [`STAND.md`](STAND.md) — wo wir stehen, was als Nächstes kommt
2. [`ERKENNTNISSE.md`](ERKENNTNISSE.md) — zusammengeführte Fakten
3. [`regeln/`](regeln/README.md) — Methode, die wir anpassen können
4. [`evidenz/suchen.md`](evidenz/suchen.md) — schon durchsuchte Fenster

Nicht von vorn anfangen. Bekannte Fakten nicht neu suchen.

## Pflicht am Ende jeder Arbeit

Im **selben** PR / Commit:

- [`STAND.md`](STAND.md) aktualisieren (Datum, was erledigt, nächster Schritt)
- bei einer Suche: Zeile in [`evidenz/suchen.md`](evidenz/suchen.md)
- bei einer Regeländerung: Eintrag in [`regeln/AENDERUNGEN.md`](regeln/AENDERUNGEN.md)
- neuer Fakt nur mit Scan, Signatur, Transkript, Gewissheit

Ohne diesen Rückweg ist der Fund für den nächsten Agenten verloren.

## Wo was liegt

| Ort | Rolle |
| --- | --- |
| [`STAND.md`](STAND.md) | Handoff zwischen Desktop, App und Cloud |
| [`regeln/`](regeln/README.md) | Arbeitsregeln, erweiterbar |
| [`ERKENNTNISSE.md`](ERKENNTNISSE.md) | gesicherter Forschungsstand auf `master` |
| [`evidenz/`](evidenz/README.md) | Einzelblätter + Suchprotokoll |
| [`archiv/`](archiv/README.md) | Match-Scans zum Gegenlesen |
| `*-records/` | Personenakten mit Signatur |
| [`stammbaum/`](stammbaum/README.md) | Blattprüfung, nur bisavós und älter |
| `00_Arbeitsordner/` | nur lokal, nicht in Git |

## Desktop und App

**Standard: Desktop.** Neue Arbeit auf dem Rechner, nicht in der
Cloud. Kein Geräte-Pairing. Dieselbe Cursor-Anmeldung, dieses Repo.

- **App:** beim Start **My Machines**, Worker mit Remote dieses Repos.
- **Desktop:** Agents Window, dieses Repo offen; Remote Control an,
  dann `/remote-control`, wenn das Handy steuern soll.
- **Cloud nur** wenn der Mac aus ist oder ausdrücklich verlangt.
- Eine schon laufende Cloud-Sitzung hängt nicht nachträglich
  an den Rechner. Nicht in der Cloud weitermachen.

Schritte: [`regeln/06-geraete.md`](regeln/06-geraete.md).

## Cursor Cloud

Cloud liest dieselben Dateien wie die App, sobald sie **committed**
sind. User-Rules im Cursor-Konto gelten zusätzlich; `~/.cursor/rules`
auf einem Laptop gilt in der Cloud **nicht**.

Vor dem Branch: `git fetch origin master`, wenn der Stand auf dem
neuesten `master` aufbauen soll.

## Sprache und Umfang

Antworten auf Deutsch. Lebende und avós nicht anfassen.
Privatdokumente nicht hochladen — [`regeln/04-privat.md`](regeln/04-privat.md).
