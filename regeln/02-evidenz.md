# 02 — Evidenzblatt

Issue #19 (`evidenz`) und der bestehende Ledger. Ein Fakt existiert
für Chat und Cloud erst, wenn er auf einem Blatt mit Scan steht.

## Was Portugal und die Schweiz verbindet

Die Familie: Wurzeln in Ansião / Penela / Torre de Vale de Todos,
Auftraggeber und avós in der Schweiz. **In diesem Repo** liegt nur die
portugiesische Belegarbeit (Kirchenbuch, Conservatória, AUC). Die
Schweizer Seite (Lebende, Großeltern, Ausweise, Adressen) bleibt beim
Auftraggeber und kommt nicht nach GitHub.

GEDCOM / Geni / MyHeritage: nur Name, Datum, Filiação, Naturalidade.
Keine Dokumentnummer, kein NIF, NISS, Utente, keine Ausweis-Fotos.

## Was auf jedes neue Blatt gehört

Vorlage: [`evidenz/VORLAGE.md`](../evidenz/VORLAGE.md).
Beispiel: [`evidenz/linie-duarte/G2-heirat-1907.md`](../evidenz/linie-duarte/G2-heirat-1907.md).

1. Scan-Pfad und Archivsignatur (DigitArq / AUC / Conservatória)
2. Kurzes Transkript der Namens- und Datumszeilen (Quellenform)
3. Gewissheit je Feld (`sicher` / `wahrscheinlich` / `Kandidat` / `offen`)
4. Erst danach Personenanschluss oder Blattkorrektur
5. Widersprüche stehen lassen

Ohne Schritt 1–3 kein Eintrag in `ERKENNTNISSE.md` und keine
Blattänderung.

## Wo das Blatt hingehört

| Linie | Ordner |
| --- | --- |
| Duarte / Freire Bicho, Cumeeira | `evidenz/linie-duarte/` |
| Torre / Reis / Gato / Narciza | `evidenz/linie-torre/` |
| neuer, belegter Strang | neuer Unterordner, in `evidenz/README.md` eintragen |

Scan zusätzlich ins Quellenregister
[`evidenz/quellenregister.md`](../evidenz/quellenregister.md) und, zum
Gegenlesen, unter sprechendem Namen nach [`archiv/`](../archiv/README.md).

## Was kein Evidenzblatt ist

- eine Chat-Zusammenfassung ohne Datei
- ein Index-Treffer ohne gelesene Seite
- eine mündliche Zuordnung ohne Akt
- OCR über die Conservatória-Fotos
