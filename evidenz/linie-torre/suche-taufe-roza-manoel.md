# Suche rückwärts: Taufen Roza Maria und Manoel Pedro dos Reis

Arbeitsstand nach Merge von PR #8. Dem Faden vom gesicherten Paar
**Manoel Pedro dos Reis × Roza Maria** (Heirat 23.3.1851) zurückfolgen —
nicht den Sammelband 1609–1748 öffnen.

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

### Durchsicht 1822–1852 (Stand, lokal)

| Seite | Jahr (ca.) | Ergebnis |
| --- | --- | --- |
| m0020 | ~1824 | Parish Alvorge; kein Joaquim×Florencia |
| m0030 | 1826 | Vale-Galego-Roza ausgeschlossen |
| m0050 | 1828 | kein Treffer |
| m0068 | 1830 | Joaquim als Kindname; kein Elternpaar |
| m0089–m0091 | 1833–1834 | **Atianha**/Alvorge im Text; Florencia Maria × Theodoro Lopes (Kind Manoel) — **anderes** Paar; keine Roza×Joaquim×Florencia |

OCR (Tesseract por) auf m0020–m0120 nur als Hinweisgeber; Handschrift zu unsicher
für alleinige Entscheidung.

**Noch offen:** Vollzeilen m0001–m0244 und Band 0003 systematisch.

### Elternheirat Joaquim × Florencia (Alvorge)

Bei [tombo ans01](https://tombo.pt/f/ans01) enden die digitalisierten Casamentos
**1725–1788**; danach erst wieder **ab 1860**. Die Lücke **1789–1859** deckt
das gesuchte Fenster (~1815–1835) vollständig ab — **online nicht suchbar**.
Nächster Schritt nur über ADLRA vor Ort / Anfrage, nicht über DigitArq.

Kein sicherer Taufanschluss bisher. Paläografie im Viewer oft zu unsicher
für Namensfeststellung; Negativsuche gilt nur für *klare* Treffer.

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
5. Alten Sammelband `PANS08/003/0001` (1609–1748) erst anfassen, wenn
   diese Linie zeitlich heranreicht.
