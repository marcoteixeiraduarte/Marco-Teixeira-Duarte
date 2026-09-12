# Erkenntnisse – Archiv und Git zusammengeführt

Stand aus `master` (PR #2–#4), Archiv/Quellenformen (PR #6),
Evidenz-Ledger (PR #7) und Avelar-Gegenlese (PR #5).
Schreibweisen bleiben quellengetreu. Linien werden nicht vermischt.

## Gewissheit

| Stufe | Bedeutung |
| --- | --- |
| sicher | am Originalscan gelesen; Datum und Personen passen |
| wahrscheinlich | mehrere Einträge zeigen dieselbe Person, ein Detail weicht ab |
| Kandidat | Namens-/Ortsnähe, Identität nicht bewiesen |
| offen | gesucht, nicht gefunden oder widersprüchlich |

## Wo was liegt

| Ort | Inhalt |
| --- | --- |
| [`archiv/`](archiv/README.md) | Match-Scans unter sprechenden Namen; Conservatória-Fotokopien |
| [`evidenz/`](evidenz/README.md) | Einzelblätter mit Transkript und Gewissheit |
| [`stammbaum/`](stammbaum/README.md) | Blattprüfung bisavós und älter |
| `*-records/` | Personenakten mit Signatur und DigitArq/AUC-Links |
| [`README.md`](README.md) | Ortsregister und Arbeitsregeln |

---

## Zwei getrennte Spuren

```
Ramo paterno (Duarte / Freire Bicho)     Ramo materno (Torre / Reis / Teixeira …)
Cumeeira · Carrasqueiras ·               Torre · Pragoza · Avelar ·
Cabeça Redonda · Figueiras Podres        Lagarteira / Pião · Alvorge
```

Die Duarte-Urgroßeltern sind **nicht** an die Torre-/Narciza-Spur
gehängt. Gemeinsam ist nur der spätere Familienrahmen auf dem Blatt.

---

## Ramo paterno – sicher

Ausgangspunkt: **Manuel Duarte × Joaquina Ignácia**, Heirat
**13.11.1907**, Cumeeira ([G2-heirat](evidenz/linie-duarte/G2-heirat-1907.md)).

| Person | Fakt | Gewissheit | Akte |
| --- | --- | --- | --- |
| Manuel Duarte | * 19.11.1885 Carrasqueiras; Taufe 2.12.1885 | sicher | [duarte](duarte-freire-records/README.md) |
| Joaquina | * 7.2.1886 Cabeça Redonda; Taufe nur `Joaquina`; Heirat `Joaquina Ignácia` | sicher | dasselbe |
| Eltern Manuel | António Duarte × Thereza Freire | sicher | Taufe + Heirat |
| Eltern Joaquina | António Freire Bicho × Maria Ignácia | sicher | Taufe + Heirat |
| Großeltern (genannt) | Manoel Duarte × Joaquina de Jesus; Manoel [Silva?] × Maria Freire; António Freire Bicho × Maria de Christo; Manuel Francisco Dias × Joaquina Maria | sicher genannt, eigene Akten offen | [G3](evidenz/linie-duarte/G3-eltern.md) |
| Margarida | * 27.6.1897 Cabeça Redonda; † 29.11.1979 (Rand); Heirat 28.10.1922 mit José Freire Bicho | sicher (Geburt/Eltern); Randvermerke für Heirat/Tod | dasselbe |
| Manuel † | **30.9.1962**, Ansião (Blatt und Averbamento); Sterbeakt ungeprüft | sicher im Datum laut Blatt/Averbamento | Heirat 1907 / Stammbaumblatt |

### Ramo paterno – offen / korrigieren

| Thema | Stand |
| --- | --- |
| José Freire Bicho ~1894, „Mesmos pais (irmãos)“ | **streichen**. Eltern über Heirat 1922 separat belegt; nicht mit Margaridas Eltern gleichsetzen. Geburt weiter offen |
| Margarida Blatt `* 24.07.1897 · Santa Eufémia` | ersetzen durch `* 27.06.1897 · Cabeça Redonda` |
| Manuel † | Blatt und Averbamento **30.09.1962 · Ansião** — frühere Lesung 1964 war Regression |
| Figueiras Podres | **ein** Ort (mit **-s**); heute Figueiras de S. João; Taufen auch `Figueira Podra` |
| Joaquina Maria / Silvéria / Ignácia (ältere Frau) | nicht zu einer Person zusammenführen |
| Lesung mütterlicher Großvater Therezas | Manoel Dias / Freire / Silva – offen |

---

## Ramo materno – sicher (bisavós-Eltern und älter)

### Narciza / Reis / Caetana

| Person | Fakt | Gewissheit | Akte |
| --- | --- | --- | --- |
| Narciza | Taufe 6.11.1856 Torre; Heirat 8.5.1878 als Narcisa da Conceição × José Pedro dos Reis | sicher | [narcisa](narcisa-records/README.md) |
| Geburt Narciza | Zeremonie 6.11.; Geburt „19. des Vormonats“ → Sept. vs. Okt. | offen (Lesung `mez passado`) | [narciza.md](evidenz/linie-torre/narciza.md) |
| Maria da Piedade | * 15.9.1878 Pragoza; Eltern José Pedro × Narciza | sicher | narcisa + [jose-maria](jose-maria-records/README.md) |
| José Pedro dos Reis | * 24.11.1854 Pragosa; Taufe 19.12.1854; Heirat 1878; † 2.10.1903 Grenze Pião/Lagarteira | sicher | [jose-pedro](evidenz/linie-torre/jose-pedro-dos-reis.md) |
| 4. Grad **paterno** | Manoel Pedro dos Reis × Roza Maria; Heirat 23.3.1851 Torre | sicher als Eltern José Pedros (Taufe 1854) | [G4-paterno-reis](evidenz/linie-torre/G4-paterno-reis.md) |
| Roza, Alvorge-Seite | Pfarrei Alvorge sicher; Vale Paio / Vallejazede / Aljazede nicht zusammenführen; Ateanha nur Suchort | Pfarrei sicher; Lugar und Joaquims Nachname offen | [alvorge-ateanha](evidenz/linie-torre/alvorge-ateanha.md) |
| Caetana Maria | Taufe 21.11.1815; Heirat 16.11.1837 × João Roiz Gato; † 14.2.1891 | sicher | narcisa / [caetana](evidenz/linie-torre/caetana-maria.md) |
| Eltern Caetana | Manoel (Joaquim) Sol × Maria Joaquina | sicher | Taufe + Heirat |
| Großeltern Maria Joaquina | Alexandre Manoel × Joaquina da Affonseca, Vila de Avelar | sicher als Großeltern; deren Heirat nur Kandidat | Avelar-Abschnitt |
| 4. Grad **materno** | João Rodrigues Gato × Caetana — nicht mit dem Reis-Paar vermischen | sicher als Narcizas Eltern | narcisa |

### Teixeira / Guiomar / Ascenção / Matta

| Person | Fakt | Gewissheit | Akte |
| --- | --- | --- | --- |
| João Teixeira | * 13.10.1879 Cabeça Redonda; Eltern Custodio Teixeira × Joana de Jesus | sicher | [teixeira](teixeira-records/README.md) |
| João (Guiomar) | * 22.4.1874 Rua d'Além; Vater Luiz Guiomar | sicher | [guiomar](guiomar-records/README.md) |
| Maria (1882) | * 25.2.1882 Valle do Pião (Lagarteira/LAR); Eltern Joaquim Rodrigues Feio × Maria Helena | sicher | guiomar |
| Joze Maria da Ascenção | * 25.4.1880 Valle de Todos (nicht Pragoza); Vater Joze Mendes Ferreira | sicher | jose-maria |
| Anna | * 15.6.1845 Valle de todos; `da Piedade` erst 1880 beim Sohn | sicher | jose-maria |
| Manuel (Matta) | * 26.7.1872 São Jorge (Kapelle in Vale de Todos); filho natural der Anna de Jesus Matta | sicher | [matta](matta-records/README.md) |

### Avelar – abgegrenzt

| Befund | Gewissheit |
| --- | --- |
| Alexandre × Joaquina Maria, Castello, wahrscheinlich 7.2.1774 (oberer Eintrag m0013) | wahrscheinlich = Caetanas Großeltern |
| Antonio Simões × Maria Joaquina, 10.2.1774 (unterer Eintrag) | **ausgeschlossen** als unsere Maria Joaquina |
| Theodora Maria *27.12.1780 / tauf 9.1.1781, Rapoula, Alexandre Manoel Furtado × Marianna da Affonseca | **nicht** Maria Joaquina Sol; Schwester nur Kandidat |

---

## Blattkorrekturen (Priorität)

Aus [`stammbaum/README.md`](stammbaum/README.md), verkürzt:

1. `José Maria … Pragosa` → `Joze Maria da Ascenção · Valle de Todos`; Vater Joze Mendes Ferreira
2. `Narcisa Rodrigues Gato` → `Narciza` / bei Heirat `Narcisa da Conceição`
3. Maria da Piedade: Taufname ohne belegtes `dos Reis`; Ort `Pragoza`
4. Maria da Piedade † `16.01.1952`: Tages-/Monatszuordnung weiterhin nicht sicher
5. Manuel Duarte † **30.09.1962 · Ansião** (Blatt = Averbamento; 1964 war Fehlregression)
6. Margarida: `* 27.06.1897`, Cabeça Redonda; nicht `24.07.1897 · Santa Eufémia`
7. José Freire Bicho: `Mesmos pais (irmãos)` streichen; Eltern über Heirat 1922 separat
8. João Teixeira: Weiler **Cabeça Redonda** (nicht nur Cumeeira); Vater `Custodio`
9. João Guiomar: `* 22.04.1874 · Rua d'Além`; Vater `Luiz Guiomar`
10. Maria 1882: Taufname **Maria**, Ort **Valle do Pião** (LAR)
11. 4.º-avós-Platzhalter Duarte/Freire durch die Großeltern der Cumeeira-Taufen ersetzen

---

## AUC Coimbra (Uni-Archiv) – wo weiter suchen

Kirchenbücher **Cumeeira** (São Sebastião, Penela) liegen schon im
[Arquivo da Universidade de Coimbra](https://pesquisa.auc.uc.pt/)
(`PT/AUC/PAR/PNL01`); Taufen/Heiraten bis 1911. Überblick:
[tombo.pt/f/pnl01](https://tombo.pt/f/pnl01).

Für **José Freire Bicho × Margarida** (Zivilakt Nr. 94 / 1922) nicht
weiter in den Pfarreibüchern suchen, sondern im **Zivilfonds Penela**
derselben Uni:

| Band / Einheit | Bestand | Hinweis |
| --- | --- | --- |
| Casamentos 1922 | `PT/AUC/RCV/PNL` | Eintrag Nr. 94 – Eltern und Geburt Josés |
| Processos de casamento Cx. 7 | 1921–1922 | Begleitakte möglich |
| Processos de casamento Cx. 8 | 1922–1923 | Begleitakte möglich |

Inventar: [tombo.pt/m/pnl](https://tombo.pt/m/pnl) · Fonds-Übersicht:
[uc.pt/auc … rcv](https://www.uc.pt/auc/fundos-colecoes/rcv/).
Kurznotiz: [`evidenz/linie-duarte/AUC-coimbra-jose-freire-bicho.md`](evidenz/linie-duarte/AUC-coimbra-jose-freire-bicho.md).
Online-Viewer für 1922 war hier nicht erreichbar; Lesesaal / Reproduktion
über [auc-geral@auc.uc.pt](mailto:auc-geral@auc.uc.pt) bzw. Certidão-Service
der UC.

Elternheiraten **António Duarte × Thereza Freire** und
**António Freire Bicho × Maria Ignácia** (vor 1885/86): weiterhin
`PNL01` Casamentos am AUC – digital wie die bekannten Taufen.

---

## Noch offen (nächste Arbeit)

| Priorität | Aufgabe |
| --- | --- |
| 1 | **AUC Coimbra – RCV Penela:** Casamentos 1922 Nr. 94 (+ Processos Cx. 7/8) |
| 2 | Conservatória Ansião: zehn Fotos in [`archiv/conservatoria-ansiao/`](archiv/conservatoria-ansiao/README.md) händisch lesen (bisavós *1912–1915) |
| 3 | Taufe Manoel Joaquim Sol in Avelar; Elternzeilen m0013 ohne Namensvorgabe |
| 4 | AUC `PNL01` Casamentos: António Duarte × Thereza Freire; António Freire Bicho × Maria Ignácia |
| 5 | Narciza-Geburt: `mez passado` zu November 1856 noch einmal vergrößert lesen |
| 6 | Alvorge: Taufe Roza Maria (Bände 1808–1822 / 1822–1852); Joaquims Nachname 1851 `Duarte` vs. 1854 `Fre…` |
| 7 | Ortsformen Vale Paio / Vallejazede / Aljazede getrennt lassen, bis Rozas Taufe sie klärt |
| 8 | Gegenlese Heiratsscan 1878 (`…0022_m0006`): `Manuel Pedro Coelho` als **frühere, inzwischen fragliche Lesung** dokumentiert halten, bis die Zeile gezielt geprüft ist; aktuelle Lesung `Manoel Pedro dos Reis` — Elternanschluss über Taufe 1854 bleibt sicher |

---

## Alter Band PANS08/003/0001 — später, von jung nach alt

Lokal geprüfte Stichprobe (16 Seiten) aus dem Sammelband:

- Casamentos 1609–1719  
- Óbitos 1609–1748  

**Kein Upload, kein Personenanschluss.** Mehrere Generationen vor dem
derzeit gesicherten Reis-Anschluss. Sofortige Namenssuche (Mendes, Dias,
Roiz …) würde Scheinsicherheit erzeugen.

Forschungsweg:

1. Manoel Pedro dos Reis und Roza Maria rückwärts über die eigenen Taufen  
2. Deren Eltern sicher bestimmen  
3. Generation für Generation bis ins frühe 18. Jahrhundert  
4. Erst wenn eine belegte Linie zeitlich an 1748 heranreicht, den Band
   systematisch erschließen  
5. Bis dahin: nur als ungesichtete Stichproben aus `PANS08/003/0001`
   vermerken — ohne Personenanschluss und außerhalb von Git  

Arbeitsprotokoll zur Taufsuche (Roza / Manoel Pedro):
[`evidenz/linie-torre/suche-taufe-roza-manoel.md`](evidenz/linie-torre/suche-taufe-roza-manoel.md).

Lokale Ablage (gitignore) für Volllese:

- `alvorge-records/` — Batismos 1808–1822 (100) + 1822–1852 (**244**)
- `torre-records/` — Batismos 1810–1842 (143)

Ateanha/Atianha ist im Alvorge-Band sichtbar (z. B. m0089/m0091), hat aber
keine eigenen tombo-Bücher. Taufanschluss Roza/Manoel Pedro noch offen.

**Blocker online:** Alvorge-Casamentos **1789–1859** fehlen (Lücke 1788→1860).

---

## Git-Herkunft dieser Zusammenführung

| Quelle | Beitrag |
| --- | --- |
| `master` PR #2 | Narciza / Caetana / Sterbefälle Torre |
| `master` PR #3 | Duarte / Freire Bicho Cumeeira; Reis-Eltern 1851 |
| `master` PR #4 | Belegstärken, José Freire Bicho, Ortsformen |
| Draft PR #5 | Avelar m0013: zwei Heiraten getrennt |
| Draft PR #6 | `archiv/`, Ortsregister, Teixeira/Guiomar/Matta/Ascenção, Stammbaumblatt |
| Draft PR #7 | `evidenz/` inkl. G4-paterno-reis, Taufe José Pedro 1854, Alvorge/Ateanha; Theodora und Simões abgegrenzt |

Lebende und avós bleiben beim Auftraggeber und stehen nicht in dieser Prüfung.
