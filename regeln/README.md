# Regeln — erweiterbar

Hier steht die **Methode**. Fakten stehen in `ERKENNTNISSE.md` und
`evidenz/`. Eine Regel ändert, *wie* der nächste Agent arbeitet.

Chat und Cloud lesen diese Dateien, sobald sie auf dem Branch bzw.
auf `master` committed sind.

## Dateien

| Datei | Inhalt |
| --- | --- |
| [01-quellen.md](01-quellen.md) | Gewissheit, Lesungen, kein Merge ohne Beleg |
| [02-evidenz.md](02-evidenz.md) | Was auf ein Blatt gehört |
| [03-ablage.md](03-ablage.md) | Wohin Dateien kommen |
| [04-privat.md](04-privat.md) | Was nie nach GitHub / Geni / MyHeritage |
| [05-suche.md](05-suche.md) | Suchen protokollieren, nicht doppelt |
| [06-geraete.md](06-geraete.md) | Desktop, App, Cloud; Remote Control / My Machines |
| [AENDERUNGEN.md](AENDERUNGEN.md) | Jede Regeländerung, älteste unten |

## Eine Regel anpassen

Nicht still im Chat «ab jetzt anders» sagen. Sonst kennt es der
nächste Agent nicht.

1. GitHub-Issue mit Vorlage **Regel** (oder kurz: Datei + neuer Wortlaut).
2. Datei ändern oder `06-….md` anlegen, wenn es ein neues Thema ist.
3. Zeile in `AENDERUNGEN.md` (Datum, Datei, was sich ändert).
4. PR. Nach dem Merge gilt die neue Fassung für Chat und Cloud.

Alte Regel nicht löschen, wenn sie schon Funde geprägt hat. Stattdessen
oben in der Datei: `Ersetzt durch 0N-….md am JJJJ-MM-TT` und den alten
Text darunter lassen.

## Was eine Regel darf

- knapper Imperativ («nicht zusammenführen», «Scan zuerst»)
- Verweis auf ein Beispielblatt, nicht den ganzen Forschungsstand kopieren

## Was eine Regel nicht darf

- neue Personen oder Orte festsetzen
- eine unsichere Lesung zur einzigen Wahrheit machen
- Privatdokumente oder Lebende ins Repo holen
