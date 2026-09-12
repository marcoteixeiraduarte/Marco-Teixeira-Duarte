# Archive und Links

Zentrale Übersicht: wo welche Linie liegt, Portale, Signaturen, Kontakt.
Scan-IDs und Einzelblätter: [`evidenz/quellenregister.md`](../evidenz/quellenregister.md).
Suchstand Roza/Manoel Pedro:
[`evidenz/linie-torre/suche-taufe-roza-manoel.md`](../evidenz/linie-torre/suche-taufe-roza-manoel.md).

---

## Linien und Archive (nicht vermischen)

Auf dem Blatt gibt es **zwei Familienarme**; archivisch liegen sie in
**zwei Clustern**, und die **Teixeira-** sowie **Duarte-**Akte teilen
sich denselben Cumeeira-Bestand:

```
Ramo paterno                         Ramo materno
Duarte / Freire Bicho                Torre / Reis / Teixeira / Guiomar / …
        │                                      │
        └──── Cumeeira-Cluster (AUC) ──────────┘
              Duarte + Teixeira + Freire
              Cabeça Redonda · Figueiras Podres · Carrasqueiras
                         │
              (Heirat / späterer Rahmen)
                         │
              Ansião-Cluster (ADLRA)
              Torre · Pragosa · Avelar · Alvorge · Lagarteira/Pião
```

- **Duarte** und **Teixeira** = dieselben Pfarreibücher `PNL01` am **AUC**
  (Cumeeira). Teixeira ist auf dem Blatt materno, archivisch aber Cumeeira
  wie Duarte — die Brücke zwischen den beiden Armen.
- **Torre / Reis / Alvorge / Avelar** = **ADLRA** Leiria.
- Linien in der Auswertung getrennt halten; nur der spätere Familienrahmen
  verbindet sie (siehe `ERKENNTNISSE.md`).

### Schnellzuordnung

| Linie / Thema | Familienarm | Archiv | Portal |
| --- | --- | --- | --- |
| **Duarte / Freire Bicho** (Cumeeira) | paterno | **AUC** `PNL01` | tombo `pnl01` |
| **Teixeira** (Cabeça Redonda / Figueiras Podres) | materno (Brücke) | **AUC** `PNL01` | tombo `pnl01` · [`teixeira-records`](../teixeira-records/README.md) |
| Zivil Penela (José Freire Bicho 1922) | paterno | **AUC** RCV `PNL` | tombo `m/pnl` |
| Torre / Reis / Narciza / Pragosa | materno | **ADLRA** `PANS08` | tombo `ans08` |
| Alvorge / Ateanha / Vale Paio | materno (Roza) | **ADLRA** `PANS01` | tombo `ans01` |
| Avelar (Gato/Simões-Kandidaten) | materno | **ADLRA** `PANS03` | DigitArq |
| Guiomar / Ascenção / Matta (Vale de Todos u. a.) | materno | **ADLRA** (Torre u. Nachbarn) | tombo `ans08` u. a. |
| Bisavós *1912–1915 Fotos | beide Arme | Conservatória Ansião | `archiv/conservatoria-ansiao/` |

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

Gemeinsames Buch für **Duarte**, **Freire Bicho** und **Teixeira**
(Weiler Cabeça Redonda, Figueiras Podres/Figueira Podra, Carrasqueiras).

| | |
| --- | --- |
| tombo | https://tombo.pt/f/pnl01 |
| Signatur | `PT/AUC/PAR/PNL01` |
| Inhalt | Batismos / Casamentos / Óbitos bis 1911 |
| Repo | `duarte-freire-records/`, `teixeira-records/`, `archiv/duarte-freire/`, `archiv/teixeira/` |

Beispiele AUC-Details:

| Thema | Linie | Link |
| --- | --- | --- |
| Taufe João Teixeira 1879 | Teixeira | https://pesquisa.auc.uc.pt/details?id=43225 |
| Taufe Manoel Duarte 1885 | Duarte | https://pesquisa.auc.uc.pt/details?id=43231 |
| Taufe Joaquina 1886 | Duarte/Freire | https://pesquisa.auc.uc.pt/details?id=48506 |
| Heirat Manuel × Joaquina 1907 | Duarte | https://pesquisa.auc.uc.pt/details?id=48550 |

Offen digital: Elternheiraten António Duarte × Thereza Freire;
António Freire Bicho × Maria Ignácia — weiter in `PNL01` Casamentos.
Custodio Teixeira × Joana de Jesus: Heirat in `PNL01` bzw. Nachbarpfarrei
noch offen (siehe `teixeira-records/README.md`).

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
