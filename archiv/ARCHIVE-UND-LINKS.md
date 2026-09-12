# Archive und Links

Zentrale Übersicht: wo welche Linie liegt, Portale, Signaturen, Kontakt.
Scan-IDs und Einzelblätter: [`evidenz/quellenregister.md`](../evidenz/quellenregister.md).
Suchstand Roza/Manoel Pedro:
[`evidenz/linie-torre/suche-taufe-roza-manoel.md`](../evidenz/linie-torre/suche-taufe-roza-manoel.md).

---

## Schnellzuordnung

| Linie / Thema | Archiv | Portal | Nicht hier |
| --- | --- | --- | --- |
| Alvorge, Ateanha, Vale Paio / Aljazede | **ADLRA** Leiria | tombo `ans01`, DigitArq | AUC, Torre do Tombo |
| Torre de Vale de Todos, Pragosa | **ADLRA** Leiria | tombo `ans08`, DigitArq | AUC, Torre do Tombo |
| Avelar (Gato/Simões-Kandidaten) | **ADLRA** Leiria | tombo `ans03` | — |
| Cumeeira / Penela (Duarte, Freire Bicho) | **AUC** Coimbra | tombo `pnl01`, pesquisa.auc | ADLRA |
| Zivil Penela ab 1911 (José Freire Bicho 1922) | **AUC** Coimbra RCV | tombo `m/pnl` | Pfarreibücher allein |
| Bisavós *1912–1915 Fotos | Conservatória Ansião | lokal unter `archiv/conservatoria-ansiao/` | — |

„Apresentação da Universidade de Coimbra“ bei Alvorge = historisches
**Präsentationsrecht**, nicht Lagerort der Bücher.

---

## 1. Nationale Portale (Zugang, keine Lagerorte)

| Name | URL | Rolle |
| --- | --- | --- |
| DigitArq / arquivos.pt | https://digitarq.arquivos.pt/ | Viewer + API der Bezirks-/Uni-Bestände |
| tombo.pt | https://tombo.pt/ | Pfarrei-Index mit Links zu ADLRA/AUC |
| DGLAB | https://www.dglab.gov.pt/ | Dachorganisation |
| Torre do Tombo (ANTT) | https://antt.dglab.gov.pt/ · https://digitarq.arquivos.pt/ | Nationalarchiv Lissabon — **nicht** primär für Alvorge/Torre-Pfarreibücher |

DigitArq-Download (Arbeitskopien):

```text
GET https://digitarq.arquivos.pt/api/rdigital/{uuid}?max=500
GET https://digitarq.arquivos.pt/rdigital/dissemination?fileId={id}
```

---

## 2. ADLRA — Arquivo Distrital de Leiria

- Web: https://adleiria.dglab.gov.pt/ (bzw. DGLAB-Seiten zu Leiria)
- DigitArq-Prefix: `PT/ADLRA/…`
- Zuständig für Ansião-Pfarreien inkl. **Alvorge**, **Torre de Vale de Todos**, **Avelar**

### 2.1 Alvorge (`PANS01`)

| | |
| --- | --- |
| tombo | https://tombo.pt/f/ans01 |
| Fonds | `PT/ADLRA/PRQ/PANS01` |
| Orago | Nossa Senhora da Conceição |
| Lokal (gitignore) | `/workspace/alvorge-records/` · README dort |

| Band | Signatur | DigitArq-UUID / Ref. | Lokal |
| --- | --- | --- | --- |
| Batismos 1808–1822 | `…/001/0003` | `2b9730bbd061439faf679c501daa4705` (Ref. 271247) | `baptismos-1808-1822/` (100 JPG) |
| Batismos 1822–1852 | `…/001/0004` | `4b820d7bb81e4910a88430792e576518` (Ref. 271248) | `baptismos-1822-1852/` (244 JPG) |
| Casamentos …–1788 | digitalisiert | bei tombo ans01 | online |
| Casamentos **1789–1859** | **Lücke** | — | Anfrage ADLRA / Lesesaal |
| Casamentos ab 1860 | jährlich | tombo ans01 | online |

Zielsuche: Taufe Roza Maria, Eltern Joaquim × Florencia Maria (~1820–1835).

### 2.2 Torre de Vale de Todos (`PANS08`)

| | |
| --- | --- |
| tombo | https://tombo.pt/f/ans08 |
| Fonds | `PT/ADLRA/PRQ/PANS08` |
| Lokal (gitignore) | `/workspace/torre-records/` · README dort |

| Band | Signatur | DigitArq-UUID | Lokal |
| --- | --- | --- | --- |
| Batismos 1810–1842 | `…/001/0003` | `6aa3bacfa07046a4b8d3fd47d1198480` | `baptismos-1810-1842/` (143 JPG) |
| Batismos 1842–1859 | `…/001/0004` | (bei Bedarf) | — |
| Casamentos 1812–1859 | `…/002/0003` | Viewer-id `6230184fe7b24d380e323ff32271ae9f` | Stichproben offen |
| Casamentos 1719–1813 | `…/002/…` | tombo ans08 | noch offen |
| Sammelband alt | `…/003/0001` (1609–1748) | — | **erst später**, keine Namenssuche |

Zielsuche: Taufe Manoel Pedro, Eltern Manoel Pedro × Joaquina Maria, Pragosa.

### 2.3 Avelar (`PANS03`)

| | |
| --- | --- |
| tombo | https://tombo.pt/f/ans03 (falls verlinkt) / DigitArq `PANS03` |
| Nutzung | Kandidaten Theodora / Simões — siehe [`avelar-kandidaten.md`](../evidenz/linie-torre/avelar-kandidaten.md) |

---

## 3. AUC — Arquivo da Universidade de Coimbra

| | |
| --- | --- |
| Katalog | https://pesquisa.auc.uc.pt/ |
| Fonds RCV | https://www.uc.pt/auc/fundos-colecoes/rcv/ |
| Anfragen | [auc-geral@auc.uc.pt](mailto:auc-geral@auc.uc.pt) |
| Kurznotiz José Freire Bicho | [`evidenz/linie-duarte/AUC-coimbra-jose-freire-bicho.md`](../evidenz/linie-duarte/AUC-coimbra-jose-freire-bicho.md) |

### 3.1 Pfarrei Cumeeira / Penela (`PNL01`)

| | |
| --- | --- |
| tombo | https://tombo.pt/f/pnl01 |
| Signatur | `PT/AUC/PAR/PNL01` |
| Inhalt | Batismos / Casamentos / Óbitos bis 1911 |

Beispiele DigitArq/AUC-Details (aus dem Repo):

| Thema | Link |
| --- | --- |
| Taufe Manoel Duarte 1885 | https://pesquisa.auc.uc.pt/details?id=43231 |
| Heirat 1907 | https://pesquisa.auc.uc.pt/details?id=48550 |
| Taufe Joaquina | https://pesquisa.auc.uc.pt/details?id=48506 |
| Taufe João Teixeira 1879 | https://pesquisa.auc.uc.pt/details?id=43225 |

Offen digital: Elternheiraten António Duarte × Thereza Freire;
António Freire Bicho × Maria Ignácia — weiter in `PNL01` Casamentos.

### 3.2 Registo Civil Penela (`RCV/PNL`)

| | |
| --- | --- |
| tombo Inventar | https://tombo.pt/m/pnl |
| Signatur | `PT/AUC/RCV/PNL` |
| Priorität 1 | **Casamentos 1922 Nr. 94** José Freire Bicho × Margarida |
| Begleitakten | Processos de casamento Cx. 7 (1921–1922), Cx. 8 (1922–1923) |

Online-Viewer für 1922 oft nicht erreichbar → Lesesaal / Reproduktion /
Certidão-Service der UC.

---

## 4. Conservatória / Zivil vor Ort

| Stelle | Wofür | Lokal im Repo |
| --- | --- | --- |
| Conservatória Ansião | bisavós *1912–1915, Fotokopien lesen | `archiv/conservatoria-ansiao/` |
| Registo Civil nach 1911 | allgemein | jeweilige Conservatória des Concelhos |

---

## 5. Was bewusst nicht zuerst

| Ort | Warum nicht |
| --- | --- |
| Torre do Tombo (ANTT) | Kein Ersatz für fehlende Alvorge-Casamentos 1789–1859 |
| AUC für Alvorge/Torre-Taufen | Bestände liegen bei ADLRA |
| ADLRA für Cumeeira-Zivil 1922 | Bestände liegen bei AUC RCV Penela |

---

## 6. Lokale Arbeitskopien auf dem Server

| Pfad | Inhalt |
| --- | --- |
| `/workspace/alvorge-records/` | Alvorge Batismos (gitignore; README versioniert) |
| `/workspace/torre-records/` | Torre Batismos 1810–1842 (gitignore; README versioniert) |
| `/workspace/evidenz/scans/` | versionierte Belegscans |
| `/workspace/archiv/` | Match-Scans zum Gegenlesen |

Nur Treffer mit Elternanschluss nach `evidenz/` übernehmen.
