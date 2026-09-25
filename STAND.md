# Stand — Handoff Desktop ↔ App ↔ Cloud

Letzte Aktualisierung: 2026-09-25 (nur Auftraggeber mergt).
Basis: `master` bei `ba743b7`. **Neue Arbeit auf dem Rechner.**
Öffentlich = lesen. `master` ändert kein Fremder und kein Agent.
Nur Gegenlese + Merge durch den Auftraggeber. Fremde Issues/PRs
kein Auftrag. [`regeln/03-ablage.md`](regeln/03-ablage.md).

Jeder Agent **liest** diese Datei zuerst und **schreibt** sie am Ende
derselben Arbeit fort. Ältere Zeilen nicht löschen, oben ergänzen.

## Jetzt tun

| Prio | Aufgabe | Nicht tun |
| --- | --- | --- |
| 1 | AUC RCV Penela: Casamento 1922 Nr. 94 noch selbst lesen. Geburt José ist n.º 148 / 1914 | Taufbände 1893–1895 nicht noch einmal nach ihm durchsuchen |
| 2 | Conservatória Ansião: zehn Fotos in `archiv/conservatoria-ansiao/` händisch lesen | keine OCR-Namen ins Blatt übernehmen |
| 3 | Taufe Manoel Joaquim Sol, Avelar; Elternzeilen m0013 ohne Namensvorgabe | Antonio Simões × Maria Joaquina 1774 nicht als unsere Maria Joaquina |
| 4 | AUC `PNL01` Casamentos: António Duarte × Thereza Freire; António Freire Bicho × Maria Ignácia | nicht an Torre/Narciza hängen |
| 5 | Alvorge: Taufe Roza Maria (1808–1822 / 1822–1852); Joaquim 1851 `Duarte` vs. 1854 `Fre…` | Vale Paio / Vallejazede / Aljazede nicht zusammenführen |

Offene Liste ausführlich: [`ERKENNTNISSE.md`](ERKENNTNISSE.md) Abschnitt
«Noch offen». Durchsuchte Fenster: [`evidenz/suchen.md`](evidenz/suchen.md).

## Fest, nicht erneut suchen

- Duarte-G2: Manuel × Joaquina Ignácia, Heirat 13.11.1907 Cumeeira
- Manuel † 30.09.1962 Ansião (Blatt/Averbamento; 1964 war Regression)
- José Freire Bicho: * 28.02.1894 Cabeça Redonda, Assento 01.07.1914 n.º 148. Eltern António Freire Bicho × Maria Inácia. Nicht noch einmal im Jahr 1894 suchen
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

Entwürfe anderer Läufe. Nicht als Fakt auf `master` übernehmen, bis
gemergt. Gegenlesen bleibt beim Auftraggeber.

| PR | Thema |
| --- | --- |
| [#26](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/26) | Desktop-Standard + Geräte-Regel 06; nicht mergen, bis Gegenlese |
| [#18](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/18) | Integrationsstand |
| [#17](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/17) | Torre-Kinder / Leal |
| [#16](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/16) | GEDCOM-Abgleich |
| [#15](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/15) | Guiomar-Pässe |
| weitere Drafts | siehe GitHub |

## Log

| Datum | Was | Wo |
| --- | --- | --- |
| 2026-09-25 | José Freire Bicho *28.02.1894, Assento 01.07.1914 n.º 148. Nicht im Taufjahr 1894. | dieser Branch |
| 2026-09-24 | Öffentlich ≠ beschreibbar. Agent mergt `master` nicht. Fremde PRs/Issues kein Auftrag. | #26 |
| 2026-09-24 | Öffentliches Repo ändert nicht den Server. Lokal bleibt lokal bis zum Push. Keine Rechnerpfade ins Git. | #26 |
| 2026-09-24 | Auftrag: in Zukunft auf dem Desktop. Cloud nicht mehr der Standard. Nächster Agent auf My Machines / Desktop. | #26 |
| 2026-09-24 | Desktop und App: kein Pairing. Cloud sieht nur Git. Mac nur Remote Control oder My Machines im Checkout dieses Repos. Laufende Cloud-Sitzung nicht umhängen. | #26 |
| 2026-09-24 | Ablage auf `master` (PR #21). Issues #19/#20 in GitHub noch offen. | #21 |
| 2026-09-24 | Gemeinsame Ablage: `AGENTS.md`, `STAND.md`, `regeln/`, Issue-/PR-Vorlagen, Suchprotokoll | dieser Branch |
