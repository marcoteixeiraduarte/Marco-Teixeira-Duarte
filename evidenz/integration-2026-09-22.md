# Integrationsstand 22.09.2026

Dieser Zweig `cursor/integration-korrektur-0e2e` ist der **eine**
Abschlussweg. Nach dem normalen Merge nach `master` werden die neun
offenen Draft-PRs mit Verweis auf den Merge-Commit geschlossen.
Die Variante, #14 als Nachfolger weiterzuführen, entfällt.

Basis ist #17 einschließlich der beiden späteren Commits
`6cf5cfe` (Prüfseite) und `2980f52` (Leal 1829 / Freire 1846 /
José 1841). Der ältere Integrationsbericht, der #17 nur bis
`887ebae` kannte, ist damit überholt.

## Was dieser Stand aufnimmt

| Quelle | Was bleibt |
| --- | --- |
| #17 | Torre-Kinder, Ateanha/Leal-Prüfseite, Aktenreorganisation |
| #16 | GEDCOM; Narciza-Septemberlesung **neben** der Oktoberlesung |
| #14 | Katalog-JSONs Manoel 1886 und António 1901 — #14 ist kein vollständig überholter Vorläufer |

#14 und #17 haben nach dem gemeinsamen Stand je eigene Commits.
Die Kataloge fehlen in #17; die Passübersicht arbeitete dort mit
der Blogtranskription. Katalog schlägt Blog, sobald ein Feld in
beiden steht. Carrasqueiras-Chão de Couce bleibt von Duarte
Carrasqueiras/Cumeeira getrennt, solange kein Akt sie verbindet.

## Korrekturen gegenüber dem Paket

1. **Wiederherstellungsnachweis.** `stammbaum/validate.py` schreibt
   `repo_head` und `repo_tree` (`HEAD` / `HEAD^{tree}`), dazu
   Arbeitsbaumstatus und `validator_version`. Der zweite Lauf
   (`--pass wiederherstellung`) trägt den SHA-256 der
   Belegerhalt-Datei. Zwei bytegleiche JSON-Dateien allein belegen
   keinen zweiten Lauf am importierten Stand.
2. **F47 bleibt aus dem bestätigten Export.** Die Heirat 1896 nennt
   die Eltern José dos Reis × Maria Ramalha — das ist Akttext. Die
   Identitätskette Blatt *15.06.1873 — Braut 1896 — Mutter Palmiras
   1912 (Zivilfoto 08) ist ein eigener offener Punkt. F18 wird nicht
   als Eltern Joaquinas wiederhergestellt.
3. **GEDCOM.** `geneaologische` → `genealogische`. Eigene Notizen mit
   echten Zeichen. Historische Namensformen (`Jose Rodrigues Gatto`)
   unverändert. CRLF bleibt: in GEDCOM 5.5.1 bei UTF-8 zulässig.

## Lesefehler der Gegenlese

| Fundstelle | Korrektur |
| --- | --- |
| Sebastião 1871 | `filho legitimo e primeiro deste nome` — nicht Erstgeburt, kein Geschwisterwiderspruch. Betrifft auch REIS-01. |
| Casimiro 1898 | * 06.12.1898, 16 Uhr; ~ 26.12.1898. Nottaufe ohne eigenes Datum. |
| Heirat Ramalho × Angelica | 21.02 („Vinte e hum“) und 22.02 („Vinte dois“) nebeneinander; Datum nicht sicher. Identität Kandidat. |
| Alvorge Juni 1873 | „in diesen Bildern kein passender Eintrag gefunden“, kein Ortsausschluss. |
| Dias | Blattlesung erhalten; fehlende Namensbestandteile in anderen Akten getrennt; keine unbelegte Ursache. |

Relative Verweise in den fünf Linienübersichten unter `akten/*/README.md`
zeigen wieder nach `../../evidenz/` und `../../archiv/`.

## Was offen bleibt und einen Merge nicht blockiert

Diese Punkte bleiben ausdrücklich offen und erzeugen keine bestätigte
Exportkante:

- Antonio N.º 9: März/April, Nazareth oder Benedita — dieselbe Quelle,
  zwei Lesungen. Keine weitere Modelllesung.
- Zivilfoto 01: Francisco José oder Manuel dos Santos — dasselbe.
- Zivilfoto 08 (Palmira 1912) in diesem Lauf nicht erneut visuell geprüft.
- Narciza-Monat: September und Oktober nebeneinander.
- Feio: Identitäten und Frauenlesungen bleiben auf dem Detailblatt;
  die Stammbaumzusammenfassung stuft sie nicht hoch.
- Joaquina-Kirchenakt um den 15.06.1873; Marias eigene Taufe;
  Leal-Heirat vor 1812.

Luiz × Delfina **haben wir**. Lebende und avós bleiben beim
Auftraggeber.

## Schliessreihenfolge

1. Diesen Zweig per normalem Merge nach `master` übernehmen.
2. Danach #9, #10, #11, #12, #13, #14, #15, #16, #17 mit Verweis auf
   den Merge-Commit schließen.
3. Kein zweiter Weg über #14.

Prüfen: `python3 stammbaum/validate.py --pass belegerhalt` und
danach `--pass wiederherstellung` im ausgecheckten Stand.
