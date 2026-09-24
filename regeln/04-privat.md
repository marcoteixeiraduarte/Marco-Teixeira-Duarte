# 04 — Privat, nicht online

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

Nur genealogische Fakten **Verstorbener, bisavós und älter**:
Name, Datum, Filiação, Naturalidade. Quellenform der maßgeblichen
Urkunde.

Keine `INDI` für noch Lebende, auch nicht mit `RESN privacy` oder
NOTE «Lebende Person». Avós nicht in der versionierten GEDCOM.
Liste der festgehaltenen Themen ohne Akt:
[`evidenz/auftraggeber-fest.md`](../evidenz/auftraggeber-fest.md).

## Lebende — Formel

Für **jede noch lebende Person** gilt derselbe Satz, ohne Namen
und ohne Akt in diesem Repo:

> Lebende: beim Auftraggeber fest, Akt nicht in diesem Repo.

Agenten: nicht suchen, nicht anzweifeln, nicht aufs Blatt, nicht
in die GEDCOM, nicht «zur Vollständigkeit» anlegen.

Avós bleiben ebenfalls beim Auftraggeber, auch wenn sie nicht mehr
leben. In diesem Repo: **bisavós und älter**, plus die schon
liegenden Torre-Scans. Conservatória-Fotos der Geburten 1912–1915:
gegenlesen ja, erst nach festgelesener Zeile ins Blatt — ohne
Dokumentnummern, ohne Lebende daneben.

## Schweiz

Wohnort, Zivilstand und Papiere der in der Schweiz lebenden Familie
gehören nicht in dieses Repo. Die Verbindung nach Portugal ist die
Filiação der älteren Generationen, nicht die aktuelle Adresse.
