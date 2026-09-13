# Suchmodell — wie wir rückwärts suchen

Arbeitsmodell aus den bisherigen Fehlern und Erfolgen.
Ziel: weniger Schein-Negativ, weniger Linienvermischung, klarere Anschlüsse.

Lebende Liste der Fäden: [`OFFENE-FAEDEN.md`](OFFENE-FAEDEN.md).

## Kernsatz

**Nur verbinden, was Eltern + Ort + Zeitfenster gemeinsam tragen.**
Viewer-Stichprobe ist Orientierung, keine Volllese.

---

## 1. Suchkarte (vor jeder Suche)

Jede offene Person bekommt **eine** Karte (Abschnitt in `suche-*.md`) mit:

| Feld | Pflicht |
| --- | --- |
| Zielperson | Name in Quellenform |
| Gesicherter Anker | Eintrag, der die Suche begründet (Heirat/Taufe des Kindes) |
| Pflicht-Eltern | genau dieses Paar — sonst kein Treffer |
| Pfarrei / Lugar | Quellenformen getrennt auflisten |
| Zeitfenster | z. B. Taufe ~1820–1835 |
| Bücher (Signatur + UUID) | Batismos / Casamentos / Óbitos |
| Lokalpfad | `*-records/…` oder „noch nicht geladen“ |
| Status | `offen` / `in Lesung` / `Negativbereich` / `Kandidat` / `sicher` / `Blocker` |
| Nächster Schritt | ein Satz, ausführbar |
| Nicht tun | typische Fehlanschlüsse |

---

## 2. Ablauf (immer gleich)

```
Anker sichern
  → Archiv wählen (AUC ≠ ADLRA ≠ Conservatória)
    → Bandliste + Online-Lücken prüfen
      → lokal laden, wenn Band digital ist
        → Volllese im Fenster (Bildbereich protokollieren)
          → nur bei Eltern-Match → Personenblatt
            → erst dann Stammbaum / ERKENNTNISSE anfassen
```

### Regeln

1. **Download first** — „nicht gefunden“ nur nach lokaler Volllese oder dokumentiertem Blocker.
2. **OCR nur Hinweis** — Tesseract/Viewer-Text entscheidet keine Identität.
3. **Negativ = Bildbereich** — z. B. `0004 m0030–m0060, ~1826–1829, kein Joaquim×Florencia`.
4. **Homonyme aussortieren** — gleiche Vornamen, andere Eltern → Negativtabelle.
5. **Ortsformen nicht mergen** — Vale Paio ≠ Aljazede ≠ Ateanha, bis ein Akt sie verbindet.
6. **Eine Generation zurück** — Sammelband 17./frühes 18. Jh. erst, wenn die Linie zeitlich anliegt.
7. **Linien nicht kreuzen** — Duarte/Cumeeira und Torre/Reis getrennt; Teixeira archivisch Cumeeira, familiär materno.

---

## 3. Was „gefunden“ heißt

| Stufe | Bedingung |
| --- | --- |
| sicher | Scan gelesen; Eltern, Ort, Datum passen zum Anker |
| wahrscheinlich | dieselben Personen über ≥2 Einträge; ein Detail weicht ab |
| Kandidat | Name/Ort/Zeit passen; Eltern oder Lugar unklar |
| offen | Fenster gelesen oder Blocker; kein Anschluss |
| ausgeschlossen | klar andere Eltern/Pfarrei (Negativtabelle) |

**Kein** Anschluss über: ähnlichen Nachnamen, gleichen Lugar allein, „Mesmos pais“, Patenort-Vermutung.

---

## 4. Archiv-Router (kurz)

| Frage | Wohin |
| --- | --- |
| Cumeeira / Cabeça Redonda / Figueiras Podres / Carrasqueiras | **AUC** `PNL01` |
| Zivil Penela (z. B. 1922) | **AUC** RCV Penela |
| Torre, Alvorge, Avelar, Lagarteira | **ADLRA** `PANS08` / `PANS01` / `PANS03` / `PANS05` |
| Bisavós *1912–1915 Fotos | Conservatória Ansião → lokal lesen |
| Alvorge-Casamentos 1789–1859 | **nur ADLRA vor Ort** (Online-Lücke) |
| DigitArq / Torre do Tombo | Zugang, nicht Lagerort der Ansião-Bücher |

Details: [`archiv/ARCHIVE-UND-LINKS.md`](../archiv/ARCHIVE-UND-LINKS.md).
Orte: [`archiv/karten/`](../archiv/karten/README.md).

---

## 5. DigitArq-Volllese (Muster)

```text
1) UUID des Bandes aus tombo/DigitArq
2) API-Liste der fileIds (max groß genug für den Band)
3) dissemination?fileId=… → JPG lokal
4) README im Ordner: Band, UUID, Anzahl, Download-Datum
5) Leselog: Bild → Jahr → Treffer/Negativ
```

Arbeitskopien bleiben **gitignore**; versioniert wird nur das Protokoll.

---

## 6. Anti-Muster (aus diesem Projekt)

| Anti-Muster | Stattdessen |
| --- | --- |
| Viewer-Stichprobe als „Band gelesen“ | lokal laden, Fenster durchlesen |
| Erste Roza Maria übernehmen | Elternzeile prüfen |
| Ateanha = Rozas Herkunft | nur belegte Pfarrei Alvorge |
| Pião zu Torre schlagen | Lagarteira `PANS05` |
| Figueiras Podres ≠ de S. João | ein Ort, zwei Namen |
| Duarte-Eltern an Narciza hängen | Arme getrennt |
| OCR-Konflikte in den Baum | händisch lesen |
| Sammelband 1609–1748 namensmatchen | Generation für Generation |
| „Apresentação da Universidade de Coimbra“ = Lagerort | Präsentationsrecht; Bücher bei ADLRA |

---

## 7. Qualitätscheck vor dem Commit

- [ ] Suchkarte aktualisiert (Status + Bildbereiche)?
- [ ] Negativsuche mit Signatur/Bild notiert?
- [ ] Kein neuer Baum-Eintrag ohne Eltern-Match?
- [ ] Ortsformen quellengetreu?
- [ ] Richtiger Archiv-Cluster (AUC vs ADLRA)?
- [ ] [`OFFENE-FAEDEN.md`](OFFENE-FAEDEN.md) / `ERKENNTNISSE.md` angepasst?

---

## 8. Später (wenn die Volllese skaliert)

1. Leselog-Tabelle pro Band (`bild,jahr,namen,eltern,ort,status`)
2. Download-Skript DigitArq (UUID → Ordner), idempotent
3. GeoJSON-Status `sicher` / `genähert` / `Kandidat`

Solange die Fenster klein sind: Markdown + lokale JPG reichen.
