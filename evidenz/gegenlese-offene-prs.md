# Gegenlese offene PRs — erster Durchgang (Agent)

Stand: 2026-09-24, nach Merge von #21 (`master` `ba743b7`).
Zweiter Durchgang: Auftraggeber. **Kein Merge in diesem Lauf.**

Urteil nur: was nach `master` darf. Funde in Drafts sind kein Fakt.

| PR | Urteil | Warum |
| --- | --- | --- |
| [#18](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/18) | **nicht mergen** | Konflikt mit #21 (`.gitignore`, README, ERKENNTNISSE, evidenz/README). Würde Ablage und Privat-Ignore überschreiben. GEDCOM enthält trotzdem Lebende- und avós-INDI. Will #9–#17 schließen, enthält aber weder #9 noch den aktuellen #16-Stand. 530 Dateien. |
| [#17](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/17) | **nicht mergen** | Steckt laut #18 darin; allein 522 Dateien. Ateanha/Leal braucht deine Gegenlese der Scans. |
| [#16](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/16) | **nicht mergen** | Git-sauber, aber GEDCOM hat Lebende- und avós-INDI und wieder `F47` (Elternkante, die #18 draußen halten wollte). Verstößt gegen `regeln/04-privat.md`. |
| [#15](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/15) | **nicht mergen** | Hängt an #12, nicht an `master`. Passkataloge später in #14/#18. |
| [#14](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/14) | **nicht mergen** | 409 Dateien, Konflikt, eigener Text «nicht mergen». `akten/` soll nur über einen bereinigten #18-Weg. |
| [#13](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/13) | **einzeln, nach deiner Gegenlese** | Klein, richtungsgleich mit master (Sarrazina ≠ Sarzedela). Nur die Zusatzsätze (CartTop, 3,5 km, Wortbruch `Sarra-`/`zina`). |
| [#12](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/12) | **nicht mergen** | Body: «Nicht mergen.» Lindos/Pass-Luis noch offen. |
| [#11](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/11) | **nicht mergen** | Francisco José am Scan 1913 — Taufe und Heirat der Mutter offen. Bleibt Draft. |
| [#10](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/10) | **nicht mergen** | Konflikt. Body: kein sicherer Taufanschluss; spätere Commits ziehen Roza 1822 nach, ohne den Body zu halten. |
| [#9](https://github.com/marcoteixeiraduarte/Marco-Teixeira-Duarte/pull/9) | **später** | Regel «kein Personenanschluss» ist schon auf master. Band erst, wenn eine belegte Linie an 1748 heranreicht. |

## Reihenfolge, wenn du mergen willst

1. Deine Gegenlese dieser Tabelle (dieser Datei).
2. Nur wenn du zustimmst: **#13** allein, nach Lesen der zwei Dateien.
3. **#18 nicht** mergen, bevor er auf #21 rebased ist, Lebende/avós aus der GEDCOM sind, Privat-Ignore aus #21 bleibt, und #9/#16 nicht still geschlossen werden.
4. **#16 nicht**, bevor die GEDCOM keine Lebenden und keine avós mehr hat und `F47` geklärt ist.

Alles andere bleibt Draft. Nicht als Fakt auf `master` übernehmen.
