# 04 — Privat, nicht online

Dieses GitHub-Repo ist **öffentlich**. Commit, Issue und PR
sieht jeder im Netz. Der Server-Rechner ist das nicht.
Lokal bleibt lokal, bis jemand pusht.

## Nie nach GitHub, Geni, MyHeritage oder sonst wohin

- Cartão de Cidadão, Bilhete de Identidade, Pass, Führerschein
- Dokumentnummer, NIF, NISS, Utente
- Adresse, Telefon, E-Mail lebender Personen
- Ausweis-Fotos, Familienfotos Lebender
- Scans, auf denen so etwas mit drauf ist (abdecken oder lokal lassen)

Nur offline:

`00_Arbeitsordner/data/Privat_Identidade_Offline/`

Der Ordner ist in `.gitignore`. Nicht «ausnahmsweise» committen.

## In Git / GEDCOM / Online-Stammbaum

Nur genealogische Fakten: Name, Datum, Filiação, Naturalidade.
Quellenform der maßgeblichen Urkunde.

## Lebende und avós

Bleiben beim Auftraggeber. In diesem Repo: **bisavós und älter**,
plus die schon liegenden Torre-Scans. Conservatória-Fotos der
Geburten 1912–1915: gegenlesen ja, erst nach festgelesener Zeile
ins Blatt — ohne Dokumentnummern.

## Schweiz

Wohnort, Zivilstand und Papiere der in der Schweiz lebenden Familie
gehören nicht in dieses Repo. Die Verbindung nach Portugal ist die
Filiação der älteren Generationen, nicht die aktuelle Adresse.

## Öffentlich und Server

| Ort | Wer sieht es |
| --- | --- |
| GitHub (`master`, Branches, Issues, PRs) | jeder |
| `00_Arbeitsordner/`, Ausweise, `~/.cursor/` | nur der Rechner |
| Cursor-Chat / Agentenlauf | das Konto, nicht GitHub |

Nicht committen: Rechnername, lokale Pfade, Worker-IDs,
Cursor-E-Mail, Adressen, Ausweise.

Ein Agent auf dem Desktop **kann** lokale Dateien sehen und
versehentlich pushen. `.gitignore` halten. Privatordner nie
«ausnahmsweise» freigeben.

Der öffentliche Clone gibt Fremden **keinen** Zugang zum
Server. My Machines öffnet keine eingehenden Ports.
