# Erkenntnisse – Archiv und Git zusammengeführt

Stand aus `master` (PR #2–#4), Archiv/Quellenformen (PR #6),
Evidenz-Ledger (PR #7) und Avelar-Gegenlese (PR #5).
Integrationsweg 22.09.2026: [integration-2026-09-22](evidenz/integration-2026-09-22.md).
Schreibweisen bleiben quellengetreu. Linien werden nicht vermischt.

Scans durchforsten: [`archiv/NAMEN.md`](archiv/NAMEN.md) — jeder Name
seinen Ordner.

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
| [`akten/`](akten/README.md) | Personenakten mit Signatur und DigitArq/AUC-Links |
| [`evidenz/`](evidenz/README.md) | Einzelblätter mit Transkript und Gewissheit |
| [`stammbaum/`](stammbaum/README.md) | Blattprüfung bisavós und älter |
| [`suche/`](suche/README.md) | Rohbande, nicht versioniert |
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
| Manuel Duarte | * 19.11.1885 Carrasqueiras; Taufe 2.12.1885 | sicher | [duarte](akten/duarte-freire/README.md) |
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
| Figueiras Podres | **ein** Ort; **so schreiben**; heute Figueiras de S. João |
| Carrasqueiras der Paten João 1879 | Pfarrei **Chão de Couce**; nicht mit Duarte `* 1885 Carrasqueiras` gleichsetzen |
| Joaquina Maria / Silvéria / Ignácia (ältere Frau) | nicht zu einer Person zusammenführen |
| Lesung mütterlicher Großvater Therezas | Manoel Dias / Freire / Silva – offen |

---

## Ramo materno – sicher (bisavós-Eltern und älter)

### Narciza / Reis / Caetana

| Person | Fakt | Gewissheit | Akte |
| --- | --- | --- | --- |
| Narciza | Taufe 6.11.1856 Torre; Heirat 8.5.1878 als Narcisa da Conceição × José Pedro dos Reis | sicher | [narcisa](akten/narcisa/README.md) |
| Geburt Narciza | Zeremonie 6.11.; Geburt „19. des Vormonats“ → Sept. vs. Okt. | offen (Lesung `mez passado`) | [narciza.md](evidenz/linie-torre/narciza.md) |
| Maria da Piedade | * 15.9.1878 Pragoza; Eltern José Pedro × Narciza | sicher | narcisa + [jose-maria](akten/jose-maria/README.md) |
| José Pedro dos Reis | * 24.11.1854 Pragosa; Taufe 19.12.1854; Heirat 1878; † 2.10.1903 Grenze Pião/Lagarteira | sicher | [jose-pedro](evidenz/linie-torre/jose-pedro-dos-reis.md) |
| 4. Grad **paterno** | Manoel Pedro dos Reis × Roza Maria; Heirat 23.3.1851 Torre | sicher als Eltern José Pedros (Taufe 1854) | [G4-paterno-reis](evidenz/linie-torre/G4-paterno-reis.md) |
| Zwei Reis-Häuser Pragoza | **Brüder:** Manoel Pedro dos Reis (Haus B) und **José dos Reis** (Haus A, × Maria Ramalha). Gemeinsame Eltern Manoel Pedro × Joaquina Maria. Beleg Sebastião * 7.05.1871 | sicher (Taufe 1871) | [zwei-reis-haeuser](evidenz/linie-torre/zwei-reis-haeuser-pragoza.md) |
| Roza, Alvorge-Seite | Pfarrei Alvorge sicher; Vale Paio / Vallejazede / Aljazede nicht zusammenführen; Ateanha nur Suchort | Pfarrei sicher; Lugar und Joaquims Nachname offen | [alvorge-ateanha](evidenz/linie-torre/alvorge-ateanha.md) |
| Caetana Maria | Taufe 21.11.1815; Heirat 16.11.1837 × João Roiz Gato; † 14.2.1891 | sicher | narcisa / [caetana](evidenz/linie-torre/caetana-maria.md) |
| Eltern Caetana | Manoel (Joaquim) Sol × Maria Joaquina | sicher | Taufe + Heirat |
| Großeltern Maria Joaquina | Alexandre Manoel × Joaquina da Affonseca, Vila de Avelar | sicher als Großeltern; deren Heirat nur Kandidat | Avelar-Abschnitt |
| 4. Grad **materno** | João Rodrigues Gato × Caetana — nicht mit dem Reis-Paar vermischen | sicher als Narcizas Eltern | narcisa |

### Teixeira / Guiomar / Ascenção / Matta

| Person | Fakt | Gewissheit | Akte |
| --- | --- | --- | --- |
| João Teixeira (Forte) | * 13.10.1879 Cabeça Redonda; Taufname João; Forte = Großmutter Maria Forte; Eltern Custodio Teixeira (Figueiras Podres, wohnhaft Cabeça Redonda) × Joana de Jesus (Cabeça Redonda); Paten Carrasqueiras / Chão de Couce | sicher | [teixeira](akten/teixeira/README.md) |
| Maria José dos Santos | ~1884, freguesia Ansião; Frau Joãos; Eltern **Francisco José dos Santos** × **Maria Thereza** (Akt 1913); Taufe **1876–1894** und Heirat **1895–1913** offen — Ring plus [suche-erweitert](evidenz/suche-erweitert.md) | sicher als Eltern 1913; Taufe/Heirat offen | [maria-jose](evidenz/linie-teixeira/maria-jose-dos-santos.md) |
| João (Guiomar) | * 22.4.1874 Rua d'Além; Eltern **Luiz Guiomar × Delfina Maria** (haben wir). Pass-António 1901 = **Bruder**, nicht avô. Avós 1874 **Antonio Dias Guiomar × Joaquina Maria** | sicher (Taufe); Pass **wahrscheinlich** | [guiomar](akten/guiomar/README.md) · [passe-1901](evidenz/linie-torre/passe-antonio-guiomar-1901.md) · [avós](evidenz/linie-torre/antonio-dias-guiomar-joaquina.md) |
| Maria (1882) | * 25.2.1882 Valle do Pião (Lagarteira/LAR); Eltern Joaquim Rodrigues Feio × Maria Helena; **sie** geht zu João Guiomar nach Vale de Todos — nicht die Feio- oder Contente-Sippe. Blatt `Maria Helena Feio Rodrigues`: Taufname Maria, Sippe Rodrigues Feio | sicher | guiomar |
| Joaquim Rodrigues Feio | * 3.4.1853 Pragoza, Taufe 27.4.1853 Torre; Eltern Nicolao Rodrigues Feio × Maria de Jesus; avós Belchior Roiz Feio × **Agueda Maria** (Carvalhal) — Blatt `Rosa Maria` daneben; avós maternos Manoel Lourenço Lobo × Josefa Maria (Castello). Schicht darüber: **Antonio Rodrigues Feio × Maria Mendes**, Carvalhinho; Fenster **1720–1767** | sicher 1853/1775; Taufen der avós-Kinder offen | [feio-contente](evidenz/linie-guiomar/feio-contente.md) · [antonio-feio](evidenz/linie-guiomar/antonio-feio-carvalhinho.md) |
| Joze Maria da Ascenção | * 25.4.1880 Valle de Todos (nicht Pragoza); Vater Joze Mendes Ferreira. Pass 1902, 22, wohnhaft Pragosa, Eltern Ferreiro / Ana da Piedade — **wahrscheinlich** dieselbe Person | sicher Taufe; Pass wahrscheinlich | jose-maria · [passe-1901](evidenz/linie-torre/passe-antonio-guiomar-1901.md) |
| Anna | * 15.6.1845 Valle de todos; `da Piedade` erst 1880 beim Sohn | sicher | jose-maria |
| Manuel (Matta) | * 26.7.1872 São Jorge (Kapelle in Vale de Todos); filho natural der Anna de Jesus Matta; 1912 wohnhaft Pragoza × Joaquina Reis | sicher | [matta](akten/matta/README.md) |
| Joaquina Reis | * **15.06.1873** Pragosa (**Blatt**); Heirat **21.08.1896** × Manuel Matta; Eltern dort José dos Reis × Maria Ramalha (**Akttext**; Identität Blatt/1912 Gegenlese). Avós Ramalho × Angelica; Leal-Eltern **Castello 1829**. Maria Thereza Leal × Freire **Alvorge 1846**. Ateanha Herkunft **Kandidat** | Geburt Blatt; 1896/1871 sicher als Akt; 1838 Kandidat | [Erkenntnisse Ramalha](evidenz/linie-torre/erkenntnisse-ramalha-reis-ateanha.md) · [joaquina-reis-leal](evidenz/linie-torre/joaquina-reis-leal.md) |
| Palmira Reis | * 24.4.1912 Pragoza; Heirat 19.4.1937 × José Mendes — **viel später** als die erste **Palmyra * 8.6.1897** (primeira filha, Pragoza) | sicher beide Akte; 1897-Tod Kandidat | joaquina-reis-leal / [matta](akten/matta/README.md) |

### Ramalha / Reis / Ateanha

Stand, Gewissheit und was sich nicht vermengt:
[erkenntnisse-ramalha-reis-ateanha](evidenz/linie-torre/erkenntnisse-ramalha-reis-ateanha.md).
Prüfseite nur Scans: [ramalha-pruefung](evidenz/linie-torre/ramalha-pruefung.md).

Wer blieb wo, Zuzug über Mann oder Frau: [wer-blieb](evidenz/wer-blieb.md).
**Auftraggeber: das stimmt.** Guiomar: Luiz aus Bemposta; neben ihm
die Frau **Maria** aus Pião, nicht Contente/Feio als Linie.
Mendes aus **Ateanha**, nicht aus Aljazede (Aljazede = Roza).
Feio-Blatt 1853: Joaquim * 3.4.1853 **passt**; Belchior × Agueda,
nicht Blatt-Rosa. 1700–1800: [Inventar](evidenz/1700-1800.md).
Weiler und Gärten (Lagoa, Cancela, Castello, Barreira, **Freixo**,
**Lindos**, **Caralinho**/Carvalhinho …) sind die Namen im Gedächtnis
— deshalb schreibt Torre sie in die Akten. Lindos ≠ Lindoso. Freixo
≠ Rua do Freixo Pousaflores.

### Avelar – abgegrenzt

| Befund | Gewissheit |
| --- | --- |
| Alexandre × Joaquina Maria, Castello, wahrscheinlich 7.2.1774 (oberer Eintrag m0013) | wahrscheinlich = Caetanas Großeltern; Castello = **Avelar**, nicht Vale de Todos |
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
8. João Teixeira **(Forte)**: Weiler **Cabeça Redonda**; Taufname João; Vater `Custodio`, natürlich **Figueiras Podres**, wohnhaft Cabeça Redonda; Joana natürlich Cabeça Redonda; Paten **Carrasqueiras / Chão de Couce**
8a. `Pais de Maria José por confirmar` → **Francisco José dos Santos** × **Maria Thereza**; Heirat João × Maria José offen — Kirche unbekannt (Torre / Lagarteira / Ansião / Chão de Couce / Cumeeira / **Avelar** / **Alvorge**)
8b. Joaquina * **15.06.1873** Pragosa (**Blatt, haben wir**). Zivil **Reis**, Pragoza; Heirat **21.08.1896** als **Joaquina Ramalha** × Manuel Matta; Eltern dort **José dos Reis** × **Maria Ramalha** (Akttext; Identität Blatt/1912 Gegenlese). Erste Tochter **Palmyra * 8.06.1897**; Blatt-Palmira * 24.04.1912 **viel später**. Blatt Ramalho × Leal = **avós maternos** (Sebastião 1871, primeiro deste nome), nicht die Eltern. José dos Reis **Bruder** des Manoel Pedro dos Reis. [Erkenntnisse](evidenz/linie-torre/erkenntnisse-ramalha-reis-ateanha.md)
9. João Guiomar: `* 22.04.1874 · Rua d'Além`; Eltern **Luiz Guiomar × Delfina Maria** (haben wir); † 08.01.1958 **passt**. Pass-António 1901 = Bruder, nicht avô. Nächste Schicht: avós **Antonio Dias Guiomar × Joaquina Maria**
10. Maria 1882: Taufname **Maria**, Ort **Valle do Pião** (LAR); Blatt `Maria Helena Feio Rodrigues` — Sippe **Rodrigues Feio**, nicht in den Taufnamen
10a. Joaquim Rodrigues Feio * **3.04.1853** Pragoza **passt**. Belchior × **Agueda Maria** (Carvalhal); Blatt `Rosa Maria` daneben. Avós maternos Manoel Lourenço Lobo × Josefa Maria (Castello). Schicht **Antonio Rodrigues Feio × Maria Mendes**, Carvalhinho; `001/0001` **1720–1767**
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
| 2 | Conservatória Ansião: `01` `03` `04` `06` `07` `08` gelesen; Geburt José Mendes N.º 320/1914 hier kein Foto |
| 2a | Ramalha/Reis: [Erkenntnisse](evidenz/linie-torre/erkenntnisse-ramalha-reis-ateanha.md). Joaquina * **15.06.1873** Blatt — **haben wir**. Eltern-Heirat **16.11.1863**. Geschwister haben wir. Palmira jetzt nicht. Ältere Ramalho Lagarteira/Carraçal **offen** |
| 2b | Heirat João Teixeira (Forte) × Maria José **1895–1913**; Taufe Maria José **1876–1894** — [suche-erweitert](evidenz/suche-erweitert.md) |
| 2c | **Geburt Melchior * 15.05.1775** Val de Todos. Avós 1824 = **Antonia Maria**. DigitArq `002/0001`=`003/0001`, `002/0002`=`001/0002`=`003/0002` — keine Online-Casamentos 1609–1811. Heirat Melchior × Rozaria **vor ~1810**; Kinder avô Feio `001/0001` **1720–1767** plus `001/0002` ab 19.06.1767. [antonio-feio-carvalhinho](evidenz/linie-guiomar/antonio-feio-carvalhinho.md) |
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

Kurz: dem Faden vom Licht zurück in die Tiefe folgen, nicht im Nebel
bekannte Namen suchen.

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
