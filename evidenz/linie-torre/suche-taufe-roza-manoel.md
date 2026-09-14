# Suche rückwärts: Taufen Roza Maria und Manoel Pedro dos Reis

Arbeitsstand nach Merge von PR #8. Dem Faden vom gesicherten Paar
**Manoel Pedro dos Reis × Roza Maria** (Heirat 23.3.1851) zurückfolgen —
nicht den Sammelband 1609–1748 **an den Stammbaum** anschließen.
Quellenlesen dieses Bandes: nur über das Prüfregister
[`fruehe-register-1609-1748.md`](fruehe-register-1609-1748.md) (kein Personen-Merge).

**Methode ab 2026-09-12:** benötigte Bände lokal ablegen (DigitArq
`/api/rdigital/{uuid}` + `/rdigital/dissemination?fileId=`), dann lesen.
Arbeitskopien unter `alvorge-records/` und `torre-records/` (gitignore).
Siehe dortige README. Viewer-Stichproben allein gelten nicht als Volllese.

## Ausgangspunkt (sicher)

| Person | Was sicher ist | Quelle |
| --- | --- | --- |
| Manoel Pedro dos Reis | Eltern **Manoel Pedro × Joaquina Maria**, Pragosa, Torre | Heirat 1851; Taufe Sohn 1854 |
| Roza Maria | Eltern **Joaquim […] × Florencia Maria**, Pfarrei Alvorge | Heirat 1851 |
| Joaquims Nachname | 1851 Lesung `Duarte`; 1854 beim Sohn beginnend `Fre…` | offen bis Alvorge-Taufe |
| Rozas Lugar | Vale Paio / Vallejazede / Aljazede — getrennt lassen | Ateanha nur Suchort |

Blätter: [G4-paterno-reis](G4-paterno-reis.md), [alvorge-ateanha](alvorge-ateanha.md).

## A — Roza Maria (Alvorge)

### Bücher

| Band | Signatur | DigitArq-Ref. | Bilder |
| --- | --- | --- | --- |
| Batismos 1808–1822 | `PT/ADLRA/PRQ/PANS01/001/0003` | 271247 | 100 |
| Batismos 1822–1852 | `PT/ADLRA/PRQ/PANS01/001/0004` | 271248 | 244 |

Portal: [tombo.pt/f/ans01](https://tombo.pt/f/ans01).
DigitArq-UUIDs: `2b9730bbd061439faf679c501daa4705` (0003),
`4b820d7bb81e4910a88430792e576518` (0004).

Lokal abgelegt:

- `alvorge-records/baptismos-1808-1822/` — **100/100** JPG
- `alvorge-records/baptismos-1822-1852/` — **244/244** JPG

### Suchfenster

Taufe **ca. 1820–1835** (Heirat 1851, typisches Brautalte).
Nur Treffer mit Eltern **Joaquim × Florencia/Florência**.

### Bereits ausgeschlossen

| Kind | Datum | Lugar | Eltern | Warum nicht |
| --- | --- | --- | --- | --- |
| Roza | * 14.1.1826, tauf 22.1.1826 | Vale Galego | Francisco José Giraldes × Thereza Maria | falsche Eltern |

### Sichtbarkeit Ateanha

Ateanha/Atianha ist **kein** eigenes tombo-Fonds, steht aber im Alvorge-Band
als Lugar (z. B. `…0004_m0089`, `…0004_m0091`, Schreibweise `Atianha`).
Ohne lokale JPG war das im PR nicht sichtbar.

### Treffer: Elternpaar Joaquim Duarte × Florencia Maria (sicher)

| Feld | Lesung | Gewissheit |
| --- | --- | --- |
| Kind | **Manoel** | sicher |
| Taufe / Geburt | **9.7.1829** / **29.6.1829** | sicher |
| Vater | **Joaquim Duarte** | sicher |
| Mutter | **Florencia Maria** | sicher |
| Lugar | Aljorde / Alvorge (Rand+Text) | wahrscheinlich |
| Avós pat. | Manoel Duarte × Maria Jozefa | sicher |
| Avós mat. | Antonio Ramos × Angelica Maria, Athianha/Ateanha | wahrscheinlich |
| Quelle | `…0004_m0059` (rechte Seite); Schreiber Jozé Ferreira | — |

Crops: [`evidenz/scans/alvorge-joaquim-florencia/`](../scans/alvorge-joaquim-florencia/).
Passt namensmäßig zur Heirat 1851 (`Joaquim Duarte × Florencia Maria`).
Lugar 1829 (Aljorde/Alvorge) vs. 1851 (**Valle paio**) noch klären (Umzug/Schreibform).

**Roza als Kind dieses Paares:** **Treffer** in Band **0003 m0098-R**.

| Feld | Lesung | Gewissheit |
| --- | --- | --- |
| Kind | **Roza** | sicher |
| Taufe / Geburt | **28.4.1822** / *22. oder 26.4.1822 | sicher / wahrscheinlich |
| Vater | **Joaquim Duarte** | sicher |
| Mutter | **Florencia Maria** | sicher |
| Lugar | Aljaride / Algarida (Aljazede-Variante) | wahrscheinlich |
| Avós pat. | Manoel Duarte × Jozefa Maria | sicher |
| Avós mat. | Antonio Ramos × Angelica Maria, **Atianha** | sicher |
| Quelle | `…0003_m0098` rechte Seite, Mitte | — |

Crops: `HOLD-ROZA-1822-04-28_*` in [`evidenz/scans/alvorge-joaquim-florencia/`](../scans/alvorge-joaquim-florencia/).
Geschwister: **Joaquina** 21.2.1820 (m0084-R); **Manoel** 9.7.1829 (0004 m0059-R).

### Homonym — nicht Rozas Eltern (sicher getrennt)

| Kind | Datum | Eltern | Avós | Lugar | Quelle |
| --- | --- | --- | --- | --- | --- |
| Antonio | tauf 10.11.1834 | Joaquim **Jozé** × Florencia Maria | Joze Sebastiao×Maria Joaquina; Joze Caetano×Angelina Rosa (Granja) | Castello Ventoso | m0097-R / m0098-L |
| Manoel | 6.11.1833 | Theodoro Lopes × Florencia Maria | Simões Vinagre / Izabel dos Anjos | Oiteiro | m0090 |
| Adrianno | 25.8.1833 | Jozé Luis × Florencia Maria | Grillo / Joaquina Maria | Outeiro | m0088 |
| Maria | 9.9.1829 | Theodoro Lopes × Florencia Maria | — | Oiteiro | m0061 |

### Durchsicht 1822–1852 (Stand, lokal)

| Seite | Jahr (ca.) | Ergebnis |
| --- | --- | --- |
| m0020 | ~1824 | Parish Alvorge; kein Joaquim×Florencia |
| m0030 | 1826 | Vale-Galego-Roza ausgeschlossen |
| m0040–m0058 | ~1827–1829 | Duarte-Fingerprint / Roza: Negativ (Bänder) |
| **m0059-R** | **1829** | **Treffer:** Manoel, Joaquim Duarte × Florencia Maria |
| m0060–m0090 | ~1829–1833 | kein weiteres Duarte×Florencia-Kind; viele Roza-Homonyme |
| m0089–m0091 | 1833–1834 | Atianha; Florencia × Theodoro Lopes — anderes Paar |
| m0097–m0098 | 1834 | Antonio = Joaquim Jozé × Florencia — **Homonym**, nicht 1851 |
| m0102–m0140 | Stichprobe | kein Duarte-Fingerprint |

OCR (Tesseract por) auf m0020–m0120 nur als Hinweisgeber; Handschrift zu unsicher
für alleinige Entscheidung.

**Erledigt:** Roza-Taufe mit Duarte-Fingerprint — Band 0003 m0098-R (28.4.1822).
Noch offen: Geburtstag 22 vs 26 Gegenlese; Joaquims `Fre…` (1854) gegen `Duarte` halten;
Lugar Aljaride 1822 vs Valle paio 1851.

### Elternheirat Joaquim × Florencia (Alvorge)

Bei [tombo ans01](https://tombo.pt/f/ans01) enden die digitalisierten Casamentos
**1725–1788**; danach erst wieder **ab 1860**. Die Lücke **1789–1859** deckt
das gesuchte Fenster (~1815–1835) vollständig ab — **online nicht suchbar**.
Nächster Schritt nur über ADLRA vor Ort / Anfrage, nicht über DigitArq.

Roza-Taufe mit Duarte-Fingerprint gesichert (0003 m0098-R). Paläografie:
Geburtstag 22 vs 26 und Lugar-Schreibform noch gegenlesen.

## B — Manoel Pedro dos Reis (Torre / Pragosa)

### Ziel

Taufe in **Torre de Vale de Todos** (`PANS08`), Lugar **Pragosa/Fragosa**,
Eltern **Manoel Pedro × Joaquina Maria**. Fenster ca. **1820–1835**.

### Bücher

| Band | Signatur | DigitArq / Portal |
| --- | --- | --- |
| Batismos 1810–1842 | `PT/ADLRA/PRQ/PANS08/001/0003` | [tombo ans08](https://tombo.pt/f/ans08); UUID `6aa3bacfa07046a4b8d3fd47d1198480` (**143** Bilder) |
| Batismos 1842–1859 | `PT/ADLRA/PRQ/PANS08/001/0004` | nur falls Fenster zu spät |

Lokal abgelegt: `torre-records/baptismos-1810-1842/` — **143/143** JPG.
Anker: Caetana *1815* auf `…0003_m0020.jpg` (fol. 19).

### Durchsicht 1810–1842 (Stand)

Frühere Viewer-Stichproben m0040–m0105 ohne klaren Treffer. Mit lokalem Band
ist Vollzeilen-Lesung möglich — **noch nicht abgeschlossen**.

### Elternheirat Manoel Pedro × Joaquina Maria (Torre)

| Band | Signatur | Stand |
| --- | --- | --- |
| Casamentos 1812–1859 | `PT/ADLRA/PRQ/PANS08/002/0003` (83 Bilder; Viewer-id `6230184fe7b24d380e323ff32271ae9f`) | Stichproben / Durchsicht Seiten ~3–45 (~1812–1830er): **kein** klarer Treffer; ab ~60 oft „Páginas manchadas“ |
| Casamentos 1719–1813 | `PANS08/002/…` bei [tombo ans08](https://tombo.pt/f/ans08) | für ~1805–1813 **noch offen** |

Sohnesheirat 1851 im selben Band 0003 (Nachtrag ~m0080) nicht mit dem Vater verwechseln.

Kein sicherer Tauf- oder Elternheiratsanschluss bisher.

## Regel

1. Scan/Signatur und Bildnummer notieren.
2. Nur mit passenden Eltern übernehmen.
3. Ortsformen nicht harmonisieren.
4. Negativbereiche mit Datum und Bildbereich protokollieren.
5. Alten Sammelband `PANS08/003/0001` (1609–1748) erst **an den Stammbaum**
   anschließen, wenn diese Linie zeitlich heranreicht. Quellen erfassen:
   [`fruehe-register-1609-1748.md`](fruehe-register-1609-1748.md).
