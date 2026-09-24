# Agenten — Chat und Cloud

Dieses Repo ist das gemeinsame Gedächtnis. Ein Chat auf dem Handy
und ein Cloud-Agent sehen **nur**, was in Git auf `master` (oder im
aktuellen PR) liegt. Gespräche sind keine Ablage.

## Pflicht vor jeder Arbeit

1. [`STAND.md`](STAND.md) — wo wir stehen, was als Nächstes kommt
2. [`ERKENNTNISSE.md`](ERKENNTNISSE.md) — zusammengeführte Fakten
3. [`regeln/06-forschung.md`](regeln/06-forschung.md) — eine Frage, Herkunft, begrenzter Bereich
4. die betroffene Personenakte
5. [`evidenz/suchen.md`](evidenz/suchen.md) — schon durchsuchte Fenster

Nicht von vorn anfangen. Vorhandenes Wissen übernehmen, Herkunft nennen.
Keine Wiederholung ohne dokumentierten Anlass.

## Pflicht am Ende jeder Arbeit

Im **selben** PR / Commit:

- [`STAND.md`](STAND.md) aktualisieren (Datum, was erledigt, nächster Schritt)
- bei einer Suche: Zeile in [`evidenz/suchen.md`](evidenz/suchen.md) (Frage, Signatur, Bilder, Lesbarkeit, Ergebnis, Lücken) und den nächsten begründeten Schritt
- bei einer Regeländerung: Eintrag in [`regeln/AENDERUNGEN.md`](regeln/AENDERUNGEN.md)
- neuer Akt: Scan, Signatur, Transkript, Lesesicherheit und Identität getrennt; Herkunft jedes übernommenen Wissens

Ohne diesen Rückweg ist der Fund für den nächsten Agenten verloren.

## Wo was liegt

| Ort | Rolle |
| --- | --- |
| [`STAND.md`](STAND.md) | Handoff zwischen Chat und Cloud |
| [`regeln/`](regeln/README.md) | Arbeitsregeln, erweiterbar |
| [`ERKENNTNISSE.md`](ERKENNTNISSE.md) | gesicherter Forschungsstand auf `master` |
| [`evidenz/`](evidenz/README.md) | Einzelblätter + Suchprotokoll |
| [`archiv/`](archiv/README.md) | Match-Scans zum Gegenlesen |
| `*-records/` | Personenakten mit Signatur |
| [`stammbaum/`](stammbaum/README.md) | Blattprüfung, nur bisavós und älter |
| `00_Arbeitsordner/` | nur lokal, nicht in Git |

## Cursor Cloud

Cloud liest dieselben Dateien wie Chat, sobald sie **committed** sind.
User-Rules im Cursor-Konto gelten zusätzlich; `~/.cursor/rules` auf
einem Laptop gilt in der Cloud **nicht**.

Vor dem Branch: `git fetch origin master`, wenn der Stand auf dem
neuesten `master` aufbauen soll.

## Sprache und Umfang

Antworten auf Deutsch. Lebende und avós nicht anfassen.
Themen in [`evidenz/auftraggeber-fest.md`](evidenz/auftraggeber-fest.md)
nicht suchen und nicht anzweifeln.
Privatdokumente nicht hochladen — [`regeln/04-privat.md`](regeln/04-privat.md).
