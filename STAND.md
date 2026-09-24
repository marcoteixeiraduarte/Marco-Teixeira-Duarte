# Stand — Handoff Chat ↔ Cloud

Letzte Aktualisierung: 2026-09-24 (#21-Korrektur: Gegenlese ≠ Suchschleife).
Basis: `master` bei `ba743b7` (#21 gemergt).

Jeder Agent **liest** diese Datei zuerst und **schreibt** sie am Ende
derselben Arbeit fort. Ältere Zeilen nicht löschen, oben ergänzen.

## Jetzt tun

| Prio | Aufgabe | Nicht tun |
| --- | --- | --- |
| 1 | AUC Coimbra, RCV Penela: Casamentos 1922 Nr. 94 (+ Processos Cx. 7/8) | nicht in den Pfarreibüchern Cumeeira nach dieser Heirat suchen |
| 2 | Conservatória Ansião: zehn Fotos in `archiv/conservatoria-ansiao/` händisch lesen | keine OCR-Namen ins Blatt übernehmen |
| 3 | Taufe Manoel Joaquim Sol, Avelar; Elternzeilen m0013 ohne Namensvorgabe | Antonio Simões × Maria Joaquina 1774 nicht als unsere Maria Joaquina |
| 4 | AUC `PNL01` Casamentos: António Duarte × Thereza Freire; António Freire Bicho × Maria Ignácia | nicht an Torre/Narciza hängen |
| 5 | Alvorge: Taufe Roza Maria (1808–1822 / 1822–1852); Joaquim 1851 `Duarte` vs. 1854 `Fre…` | Vale Paio / Vallejazede / Aljazede nicht zusammenführen |

Offene Liste ausführlich: [`ERKENNTNISSE.md`](ERKENNTNISSE.md) Abschnitt
«Noch offen». Durchsuchte Fenster: [`evidenz/suchen.md`](evidenz/suchen.md).

## Fest — nicht blind neu suchen

Gegenlese gegen die Primärquelle bleibt erlaubt, wenn die Zuordnung
unsicher ist oder neue Evidenz da ist. Anlass festhalten. Ohne Anlass
nicht dasselbe Fenster noch einmal.

- Duarte-G2: Manuel × Joaquina Ignácia, Heirat 13.11.1907 Cumeeira
- Manuel † 30.09.1962 Ansião (Blatt/Averbamento; 1964 war Regression)
- José Freire Bicho: `Mesmos pais (irmãos)` gestrichen; Eltern über Heirat 1922 separat
- José Pedro dos Reis * 24.11.1854; Eltern Manoel Pedro dos Reis × Roza Maria
- Narciza Taufe 6.11.1856; Heirat 8.5.1878 als Narcisa da Conceição
- Joze Maria da Ascenção * 25.04.1880 Valle de Todos (nicht Pragoza)
- Figueiras Podres = ein Ort (heute Figueiras de S. João)
- São Jorge = Kapelle/lugar in Vale de Todos, Pfarrei Torre
- Pião / Valle do Pião = Lagarteira (LAR), nicht Torre
- Avelar m0013 unterer Eintrag (Antonio Simões) ausgeschlossen
- Theodora Maria 1781 ist nicht Maria Joaquina Sol
- Sarrazina / São Cosme: Pfarrei unidentifiziert; Sarzedela nicht als gelesen setzen
- PANS08/003/0001 (1609–1748): kein Personenanschluss

## Offene PRs (nicht `master`)

**Nicht mergen**, bis du [`evidenz/gegenlese-offene-prs.md`](evidenz/gegenlese-offene-prs.md)
gegenlesen hast. Einziger späterer Einzelkandidat: #13.

| PR | Thema | Erster Durchgang |
| --- | --- | --- |
| [#18](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/18) | Integrationsstand | nicht mergen (Konflikt #21, Lebende in GEDCOM) |
| [#17](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/17) | Torre-Kinder / Leal | nicht mergen |
| [#16](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/16) | GEDCOM | nicht mergen (Lebende/avós, F47) |
| [#15](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/15) | Guiomar-Pässe | nicht mergen |
| [#13](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/13) | Sarrazina ≠ Sarzedela | einzeln nach deiner Gegenlese |
| #9–#12, #14 | diverse Drafts | nicht mergen / später |

## Log

| Datum | Was | Wo |
| --- | --- | --- |
| 2026-09-24 | #21-Korrektur: «nicht neu suchen» = keine Schleife, nicht «nicht mehr prüfen». Kette Quelle → Aussage → Person/Ort → Gewissheit. | dieser Branch |
| 2026-09-24 | Forschungsauftrag als `regeln/06-forschung.md`: Herkunft, eine Frage, begrenzter Bereich, kein Blind-Wiederholen. | dieser Branch |
| 2026-09-24 | Lebende-Formel; Barreira/avós/Lebende in `auftraggeber-fest.md`. Offene PRs #9–#18: nicht mergen, erster Durchgang in `gegenlese-offene-prs.md`. | dieser Branch |
| 2026-09-24 | Ablage übernommen: PR #21 nicht mehr Draft, mergebar. Issues #19/#20 schließen sich mit dem Merge. | #21 |
| 2026-09-24 | Gemeinsame Ablage: `AGENTS.md`, `STAND.md`, `regeln/`, Issue-/PR-Vorlagen, Suchprotokoll | dieser Branch |
