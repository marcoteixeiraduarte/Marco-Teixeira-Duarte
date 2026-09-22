"""Fundstellen auf den Akten-Scans. Koordinaten relativ (x, y, w, h) 0–1.

kind: name | date | place | parents | avos | rand | paten | entry | hinweis
"""

# Jeder Eintrag: Signature-Teil des Dateinamens → Liste von Feldern.
# Mehrere Kopien derselben Pixel (Elternordner) bekommen dieselbe Markierung.

FELDER = {
    # João Guiomar 1874 — linke Seite, unterer Eintrag N.º 15
    "PANS08-001-0019_m0007": [
        {"kind": "entry", "label": "Taufe N.º 15", "box": [0.03, 0.48, 0.50, 0.48]},
        {"kind": "name", "label": "João", "box": [0.055, 0.545, 0.08, 0.045]},
        {"kind": "place", "label": "Rua d'Além", "box": [0.04, 0.58, 0.12, 0.05]},
        {"kind": "date", "label": "~ 10.05.1874", "box": [0.16, 0.50, 0.36, 0.07]},
        {"kind": "name", "label": "dei o nome de João", "box": [0.155, 0.635, 0.12, 0.04]},
        {"kind": "place", "label": "Rua d'Além", "box": [0.28, 0.64, 0.22, 0.04]},
        {"kind": "date", "label": "* 22.04.1874", "box": [0.16, 0.675, 0.35, 0.05]},
        {"kind": "parents", "label": "Luiz Guiomar", "box": [0.32, 0.72, 0.18, 0.04]},
        {"kind": "place", "label": "Bemposta / Alvorge", "box": [0.16, 0.75, 0.36, 0.055]},
        {"kind": "parents", "label": "Delfina Maria", "box": [0.155, 0.80, 0.20, 0.04]},
        {"kind": "avos", "label": "Antonio Dias Guiomar × Joaquina Maria", "box": [0.16, 0.855, 0.36, 0.04]},
        {"kind": "avos", "label": "José Gregorio × Nazareth Maria", "box": [0.16, 0.89, 0.36, 0.035]},
        {"kind": "rand", "label": "casou Maria Helena", "box": [0.03, 0.62, 0.125, 0.14]},
        {"kind": "rand", "label": "† 08.01.1958", "box": [0.03, 0.80, 0.125, 0.12]},
    ],
    # João Teixeira 1879 — Beginn N.º 42, rechte Seite ganz unten (nicht N.º 41 darüber)
    "PNL01-002-0024_m0015": [
        {"kind": "entry", "label": "N.º 42 beginnt", "box": [0.47, 0.845, 0.52, 0.155]},
        {"kind": "place", "label": "Cabeça Redonda", "box": [0.82, 0.85, 0.17, 0.055]},
        {"kind": "name", "label": "N.º 42 João", "box": [0.82, 0.90, 0.17, 0.09]},
        {"kind": "date", "label": "22.10.1879", "box": [0.48, 0.85, 0.33, 0.07]},
    ],
    # João Teixeira 1879 — Fortsetzung: Eltern, avós, Paten Carrasqueiras
    "PNL01-002-0024_m0016": [
        {"kind": "entry", "label": "Schluss N.º 42", "box": [0.10, 0.02, 0.55, 0.52]},
        {"kind": "name", "label": "João", "box": [0.22, 0.06, 0.40, 0.05]},
        {"kind": "place", "label": "Cabeça Redonda", "box": [0.28, 0.10, 0.35, 0.045]},
        {"kind": "date", "label": "* 13.10.1879, 18 Uhr", "box": [0.20, 0.14, 0.42, 0.05]},
        {"kind": "parents", "label": "Custodio Teixeira", "box": [0.20, 0.19, 0.42, 0.05]},
        {"kind": "parents", "label": "Joana de Jesus", "box": [0.20, 0.24, 0.42, 0.045]},
        {"kind": "place", "label": "Figueiras Podres / Cabeça Redonda", "box": [0.20, 0.28, 0.42, 0.05]},
        {"kind": "avos", "label": "Jozé Simão Teixeira × Maria Forte", "box": [0.20, 0.33, 0.42, 0.055]},
        {"kind": "avos", "label": "Joaquim Carvalho × Maria de Jesus", "box": [0.20, 0.385, 0.42, 0.05]},
        {"kind": "paten", "label": "Paten Carrasqueiras / Chão de Couce", "box": [0.20, 0.43, 0.42, 0.08]},
    ],
    # Maria Pião 1882 Lagarteira N.º 3 — rechte Seite
    "PANS05-001-0027_m0003": [
        {"kind": "entry", "label": "Taufe N.º 3", "box": [0.50, 0.20, 0.48, 0.58]},
        {"kind": "name", "label": "Maria", "box": [0.86, 0.26, 0.12, 0.06]},
        {"kind": "place", "label": "Valle do Pião", "box": [0.86, 0.32, 0.12, 0.08]},
        {"kind": "date", "label": "~ 05.03.1882", "box": [0.51, 0.24, 0.34, 0.06]},
        {"kind": "date", "label": "* 25.02.1882", "box": [0.51, 0.36, 0.34, 0.05]},
        {"kind": "parents", "label": "Joaquim Rodrigues Feio", "box": [0.51, 0.41, 0.34, 0.05]},
        {"kind": "place", "label": "Estrada da Pragoza", "box": [0.51, 0.46, 0.34, 0.04]},
        {"kind": "parents", "label": "Maria Helena", "box": [0.51, 0.50, 0.34, 0.045]},
        {"kind": "avos", "label": "Nicolau Feio × Maria de Jesus", "box": [0.51, 0.55, 0.34, 0.05]},
        {"kind": "avos", "label": "Jozé Contente × Helena Maria", "box": [0.51, 0.60, 0.34, 0.05]},
        {"kind": "rand", "label": "casou João Guiomar (Datum nicht einzige Form)", "box": [0.86, 0.40, 0.12, 0.18]},
    ],
    # Joaquim Feio 1853 — rechte Seite
    "PANS08-001-0004_m0050": [
        {"kind": "entry", "label": "Taufe Joaquim", "box": [0.50, 0.38, 0.48, 0.42]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.38, 0.10, 0.08]},
        {"kind": "date", "label": "~ 27.04.1853  * 03.04.", "box": [0.60, 0.40, 0.37, 0.10]},
        {"kind": "parents", "label": "Nicolao Rodrigues Feio × Maria de Jesus", "box": [0.58, 0.52, 0.39, 0.08]},
        {"kind": "avos", "label": "Belchior Roiz Feio × Agueda Maria, Carvalhinho", "box": [0.58, 0.60, 0.39, 0.08]},
        {"kind": "avos", "label": "Manoel Lourenço Lobo × Josefa Maria, Castello", "box": [0.58, 0.68, 0.39, 0.07]},
        {"kind": "rand", "label": "† 25.04.1940 wahrsch.", "box": [0.50, 0.48, 0.10, 0.22]},
    ],
    # Melchior 1775 — rechte Buchseite
    "PANS08-001-0002_m0070": [
        {"kind": "entry", "label": "Taufe Melchior", "box": [0.50, 0.02, 0.48, 0.96]},
        {"kind": "name", "label": "Melchior / Val de Todos", "box": [0.50, 0.02, 0.18, 0.12]},
        {"kind": "date", "label": "* 15.05.1775  ~ 20.05.", "box": [0.68, 0.08, 0.28, 0.10]},
        {"kind": "parents", "label": "Manoel João Neto × Antonia Maria Caetana", "box": [0.52, 0.22, 0.44, 0.12]},
        {"kind": "avos", "label": "Antonio Rodrigues Feio × Maria Mendes, Carvalhinho", "box": [0.52, 0.40, 0.44, 0.12]},
    ],
    # Theresa 1824 — linke Seite oben
    "PANS08-001-0003_m0061": [
        {"kind": "entry", "label": "Thereza / Carvalhinho", "box": [0.00, 0.00, 0.52, 0.60]},
        {"kind": "date", "label": "* 19.08.1824  ~ 25.08.", "box": [0.18, 0.08, 0.32, 0.10]},
        {"kind": "parents", "label": "Melchior Rodrigues Feio × Rozaria Maria", "box": [0.18, 0.22, 0.32, 0.12]},
        {"kind": "avos", "label": "Manoel João Neto × Antonia Maria", "box": [0.18, 0.36, 0.32, 0.10]},
    ],
    # Anna 1845 — linke Seite
    "PANS08-001-0004_m0019": [
        {"kind": "entry", "label": "Taufe Anna", "box": [0.02, 0.05, 0.48, 0.70]},
        {"kind": "name", "label": "Anna", "box": [0.03, 0.08, 0.10, 0.08]},
        {"kind": "place", "label": "Valle de todos", "box": [0.03, 0.16, 0.12, 0.08]},
        {"kind": "date", "label": "* 15.06.1845  ~ 14.07.", "box": [0.16, 0.10, 0.32, 0.10]},
        {"kind": "parents", "label": "Manoel Dias Barbeiro × Joaquina Maria", "box": [0.16, 0.28, 0.32, 0.12]},
        {"kind": "avos", "label": "João Dias Barbeiro × Maria Thereza, Pragoza", "box": [0.16, 0.42, 0.32, 0.10]},
        {"kind": "avos", "label": "João Dias da Quelha × Maria Joaquina", "box": [0.16, 0.52, 0.32, 0.10]},
    ],
    # Joze Maria 1880 N.º 5 — linke Seite oben (rechte Seite ist anderes Haus)
    "PANS08-001-0025_m0004": [
        {"kind": "entry", "label": "N.º 5 Joze Maria da Ascenção", "box": [0.02, 0.04, 0.48, 0.48]},
        {"kind": "name", "label": "Joze Maria da Ascenção", "box": [0.03, 0.10, 0.12, 0.10]},
        {"kind": "place", "label": "Valle de Todos (nicht Pragoza)", "box": [0.16, 0.14, 0.32, 0.07]},
        {"kind": "date", "label": "* 25.04.1880  ~ 06.05.", "box": [0.16, 0.06, 0.32, 0.07]},
        {"kind": "parents", "label": "Joze Mendes Ferreira, Atanha", "box": [0.16, 0.22, 0.32, 0.08]},
        {"kind": "parents", "label": "Anna da Piedade", "box": [0.16, 0.30, 0.32, 0.06]},
        {"kind": "avos", "label": "João Mendes Ferreira × Maria Ramos", "box": [0.16, 0.36, 0.32, 0.06]},
        {"kind": "avos", "label": "Manoel Dias Barbeiro × Joaquina Maria Neta", "box": [0.16, 0.42, 0.32, 0.07]},
        {"kind": "hinweis", "label": "rechte Seite = andere Taufen, nicht diese Person", "box": [0.52, 0.20, 0.46, 0.40]},
    ],
    # Sebastião 1871 — rechte Seite
    "PANS08-001-0016_m0005": [
        {"kind": "entry", "label": "Sebastião, primeiro deste nome", "box": [0.48, 0.08, 0.51, 0.64]},
        {"kind": "place", "label": "Pragoza", "box": [0.48, 0.10, 0.12, 0.08]},
        {"kind": "date", "label": "* 07.05.1871  ~ 21.05.", "box": [0.60, 0.12, 0.37, 0.08]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha", "box": [0.60, 0.28, 0.37, 0.10]},
        {"kind": "avos", "label": "Manuel Pedro dos Reis × Joaquina Maria", "box": [0.60, 0.40, 0.37, 0.08]},
        {"kind": "avos", "label": "Manuel Ramalho × Angelica Maria", "box": [0.60, 0.48, 0.37, 0.08]},
    ],
    # Manuel Matta 1872 — rechte Seite N.º 14
    "PANS08-001-0017_m0007": [
        {"kind": "entry", "label": "Manuel, N.º 14", "box": [0.48, 0.15, 0.50, 0.80]},
        {"kind": "place", "label": "São Jorge", "box": [0.48, 0.18, 0.12, 0.10]},
        {"kind": "date", "label": "* 26.07.1872  ~ 01.08.", "box": [0.60, 0.20, 0.36, 0.10]},
        {"kind": "parents", "label": "Anna de Jesus Matta (pai incógnito)", "box": [0.60, 0.40, 0.36, 0.12]},
        {"kind": "avos", "label": "Antonio Rodrigues Avelheiro × Thereza de Jesus", "box": [0.60, 0.54, 0.36, 0.10]},
    ],
    "PANS08-001-0017_m0008": [
        {"kind": "entry", "label": "Schluss Taufe Manuel", "box": [0.02, 0.00, 0.50, 0.18]},
        {"kind": "rand", "label": "Rand: Heirat Joaquina / Tod", "box": [0.02, 0.00, 0.16, 0.18]},
    ],
    # Heirat Matta × Ramalha 1896 N.º 2 — linke Seite
    "PANS08-002-0038_m0003": [
        {"kind": "entry", "label": "N.º 2, 21.08.1896", "box": [0.02, 0.20, 0.50, 0.78]},
        {"kind": "date", "label": "21.08.1896", "box": [0.20, 0.26, 0.30, 0.06]},
        {"kind": "name", "label": "Manuel Matta × Joaquina Ramalha", "box": [0.04, 0.24, 0.14, 0.10]},
        {"kind": "parents", "label": "Anna de Jesus Matta", "box": [0.20, 0.48, 0.30, 0.07]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha", "box": [0.20, 0.62, 0.30, 0.08]},
        {"kind": "place", "label": "São Jorge / Pragoza", "box": [0.20, 0.40, 0.30, 0.07]},
        {"kind": "hinweis", "label": "Leal steht in diesem Akt nicht", "box": [0.20, 0.72, 0.30, 0.06]},
    ],
    # Palmyra 1897 — rechte Seite, erste Tochter (nicht Palmira 1912)
    "PANS08-001-0042_m0005": [
        {"kind": "entry", "label": "Palmyra * 08.06.1897 — nicht 1912", "box": [0.50, 0.02, 0.48, 0.96]},
        {"kind": "name", "label": "Palmyra", "box": [0.50, 0.08, 0.14, 0.08]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.16, 0.14, 0.06]},
        {"kind": "date", "label": "* 08.06.1897  ~ 23.06.", "box": [0.64, 0.10, 0.32, 0.08]},
        {"kind": "parents", "label": "Manuel Matta × Joaquina Ramalha dos Reis", "box": [0.64, 0.28, 0.32, 0.10]},
    ],
    # Narciza 1856 — page_0070 hat den Eintrag; m0070 ist Folio 63
    "PANS08-001-0004_page_0070": [
        {"kind": "entry", "label": "Nottaufe / Eltern (Fortsetzung)", "box": [0.50, 0.02, 0.48, 0.38]},
        {"kind": "parents", "label": "João Rodrigues Gatto × Caetana Maria", "box": [0.52, 0.08, 0.44, 0.10]},
        {"kind": "place", "label": "São Jorge / Torre", "box": [0.52, 0.18, 0.44, 0.07]},
        {"kind": "avos", "label": "Manoel Joaquim Sol × Maria Joaquina", "box": [0.52, 0.26, 0.44, 0.08]},
        {"kind": "name", "label": "Narciza — Ceremonien 06.11.", "box": [0.03, 0.72, 0.46, 0.24]},
        {"kind": "date", "label": "* am 19. (Monat Gegenlese)", "box": [0.16, 0.78, 0.32, 0.08]},
    ],
    "PANS08-001-0004_m0070": [
        {"kind": "hinweis", "label": "Folio 63 — nicht Narcizas Taufe (die steht in page_0070)", "box": [0.20, 0.02, 0.60, 0.10]},
    ],
    # Heirat Narciza × José Pedro 1878
    "PANS08_002_0022_m0006": [
        {"kind": "entry", "label": "N.º 9, 08.05.1878", "box": [0.02, 0.15, 0.96, 0.70]},
        {"kind": "name", "label": "José Pedro dos Reis × Narcisa da Conceição", "box": [0.20, 0.22, 0.55, 0.08]},
        {"kind": "place", "label": "Pragoza / Torre", "box": [0.20, 0.32, 0.40, 0.06]},
        {"kind": "parents", "label": "Manoel Pedro dos Reis × Roza Maria", "box": [0.20, 0.42, 0.55, 0.08]},
        {"kind": "parents", "label": "João Rodrigues Gato × Caetana Maria", "box": [0.20, 0.52, 0.55, 0.08]},
    ],
    # Maria da Piedade 1878 N.º 6
    "PANS08-001-0023_m0004": [
        {"kind": "entry", "label": "N.º 6 Maria da Piedade", "box": [0.02, 0.05, 0.96, 0.70]},
        {"kind": "name", "label": "Maria da Piedade", "box": [0.03, 0.08, 0.20, 0.08]},
        {"kind": "place", "label": "Pragoza", "box": [0.03, 0.16, 0.18, 0.07]},
        {"kind": "date", "label": "* 15.09.1878  ~ 09.10.", "box": [0.25, 0.10, 0.50, 0.08]},
        {"kind": "parents", "label": "Joze Pedro dos Reis × Narciza da Conceição", "box": [0.25, 0.28, 0.55, 0.10]},
        {"kind": "rand", "label": "Rand: Tod Joze Maria, Alvorge Mai 1948", "box": [0.03, 0.50, 0.22, 0.20]},
    ],
    # Caetana 1815 — rechte Seite
    "PANS08-001-0003_m0020": [
        {"kind": "entry", "label": "Taufe Caetana", "box": [0.48, 0.05, 0.50, 0.70]},
        {"kind": "name", "label": "Caetana", "box": [0.48, 0.08, 0.14, 0.08]},
        {"kind": "date", "label": "~ 21.11.1815, 8 Tage alt", "box": [0.62, 0.10, 0.34, 0.08]},
        {"kind": "parents", "label": "Manoel Sol × Maria Joaquina", "box": [0.62, 0.28, 0.34, 0.10]},
        {"kind": "avos", "label": "Alexandre Manoel × Joaquina da Affonseca, Avelar", "box": [0.62, 0.42, 0.34, 0.10]},
    ],
    # Heirat Gato × Caetana 1837
    "PANS08-002-0003_m0053": [
        {"kind": "entry", "label": "16.11.1837 João Roiz Gato × Caetana Maria", "box": [0.02, 0.20, 0.50, 0.55]},
        {"kind": "name", "label": "João Roiz Gato × Caetana Maria", "box": [0.05, 0.28, 0.42, 0.08]},
        {"kind": "place", "label": "São Jorge / Torre", "box": [0.05, 0.38, 0.42, 0.06]},
        {"kind": "parents", "label": "Manoel Joaquim Sol × Maria Joaquina", "box": [0.05, 0.48, 0.42, 0.08]},
    ],
    # Caetana óbito 1891
    "PANS08_003_0035_m0002": [
        {"kind": "entry", "label": "óbito N.º 2 beginnt", "box": [0.02, 0.40, 0.96, 0.55]},
        {"kind": "name", "label": "Caetana Maria", "box": [0.15, 0.48, 0.50, 0.08]},
    ],
    "PANS08_003_0035_m0003": [
        {"kind": "entry", "label": "óbito N.º 2 Schluss", "box": [0.02, 0.02, 0.96, 0.45]},
        {"kind": "date", "label": "† 14.02.1891, 3 Uhr, Torre", "box": [0.15, 0.08, 0.55, 0.08]},
        {"kind": "parents", "label": "Manoel Joaquim × Maria Joaquina", "box": [0.15, 0.20, 0.55, 0.08]},
        {"kind": "rand", "label": "Witwe des João Rodrigues Gatto", "box": [0.15, 0.30, 0.55, 0.08]},
    ],
    # José Kind 1896
    "PANS08_003_0040_m0005": [
        {"kind": "entry", "label": "óbito N.º 12, Kind José", "box": [0.02, 0.15, 0.96, 0.55]},
        {"kind": "name", "label": "José, 3 Monate", "box": [0.15, 0.22, 0.40, 0.08]},
        {"kind": "place", "label": "Pragoza", "box": [0.15, 0.32, 0.30, 0.06]},
        {"kind": "date", "label": "† 05.11.1896", "box": [0.15, 0.40, 0.40, 0.06]},
        {"kind": "parents", "label": "José Pedro dos Reis × Narciza da Conceição", "box": [0.15, 0.48, 0.55, 0.08]},
    ],
    # Heirat Manoel Pedro × Roza 1851 Nachtrag
    "PANS08-002-0003_m0080": [
        {"kind": "entry", "label": "Nachtrag 23.03.1851 (gehörte auf fl. 70)", "box": [0.48, 0.38, 0.50, 0.58]},
        {"kind": "name", "label": "Manoel Pedro dos Reis × Roza Maria", "box": [0.50, 0.42, 0.46, 0.10]},
        {"kind": "place", "label": "Pragosa / Alvorge (Vale Paio)", "box": [0.50, 0.54, 0.46, 0.08]},
        {"kind": "avos", "label": "Manoel Pedro × Joaquina Maria", "box": [0.50, 0.64, 0.46, 0.08]},
    ],
    # José Pedro Taufe 1854
    "PANS08-001-0004_page_0056": [
        {"kind": "entry", "label": "Taufe beginnt (19.12.1854)", "box": [0.48, 0.70, 0.50, 0.28]},
        {"kind": "name", "label": "José / Pragoza", "box": [0.50, 0.74, 0.20, 0.12]},
    ],
    "PANS08-001-0004_page_0057": [
        {"kind": "entry", "label": "Taufe José Pedro", "box": [0.02, 0.02, 0.50, 0.40]},
        {"kind": "date", "label": "* 24.11.1854", "box": [0.16, 0.06, 0.32, 0.08]},
        {"kind": "parents", "label": "Manoel Pedro dos Reis × Roza Maria", "box": [0.16, 0.16, 0.32, 0.10]},
    ],
    # José Pedro óbito 1903
    "PANS08-003-0047_m0007": [
        {"kind": "entry", "label": "óbito N.º 10", "box": [0.02, 0.10, 0.96, 0.80]},
        {"kind": "name", "label": "José Pedro dos Reis", "box": [0.15, 0.16, 0.55, 0.08]},
        {"kind": "date", "label": "† 02.10.1903, 8 Uhr", "box": [0.15, 0.26, 0.55, 0.07]},
        {"kind": "place", "label": "Grenze Pião / Lagarteira", "box": [0.15, 0.34, 0.55, 0.08]},
        {"kind": "parents", "label": "Manuel Pedro dos Reis × Rosa Maria, Aljazede", "box": [0.15, 0.50, 0.60, 0.10]},
        {"kind": "rand", "label": "verheiratet mit Narcisa da Conceição", "box": [0.15, 0.42, 0.55, 0.07]},
    ],
    # Avelar 1774 — abgrenzen, oberer Eintrag
    "PANS03-002-0003_m0013": [
        {"kind": "entry", "label": "oben: Alexandre × Joaquina Maria (Kandidat, nicht Sol)", "box": [0.50, 0.05, 0.48, 0.38]},
        {"kind": "hinweis", "label": "unten: anderes Paar (Antonio Simões) — nicht vermengen", "box": [0.50, 0.48, 0.48, 0.40]},
    ],
    # Manuel Duarte 1885 N.º 40 — linke Seite (nicht die Signatur des Eintrags darüber)
    "PNL01-002-0030_m0017": [
        {"kind": "entry", "label": "N.º 40 Manoel", "box": [0.02, 0.34, 0.50, 0.54]},
        {"kind": "place", "label": "Carrasqueiras (Cumeeira-Buch)", "box": [0.03, 0.36, 0.14, 0.10]},
        {"kind": "date", "label": "* 19.11.1885  ~ 02.12.", "box": [0.18, 0.36, 0.32, 0.08]},
        {"kind": "parents", "label": "António Duarte × Thereza Freire", "box": [0.18, 0.48, 0.32, 0.10]},
        {"kind": "avos", "label": "Manoel Duarte × Joaquina de Jesus", "box": [0.18, 0.58, 0.32, 0.07]},
        {"kind": "avos", "label": "Manoel Silva × Maria Freire", "box": [0.18, 0.65, 0.32, 0.07]},
        {"kind": "paten", "label": "Paten Carrasqueiras (nicht Chão de Couce)", "box": [0.18, 0.72, 0.32, 0.08]},
    ],
    # Joaquina Ignácia 1886 N.º 9
    "PNL01-002-0031_m0009": [
        {"kind": "entry", "label": "N.º 9 Joaquina", "box": [0.16, 0.03, 0.82, 0.44]},
        {"kind": "place", "label": "Cabeça Redonda", "box": [0.78, 0.04, 0.18, 0.06]},
        {"kind": "name", "label": "N.º 9 Joaquina", "box": [0.78, 0.10, 0.18, 0.08]},
        {"kind": "date", "label": "* 07.02.1886, 18 Uhr  ~ 18.02.", "box": [0.20, 0.08, 0.55, 0.08]},
        {"kind": "parents", "label": "António Freire Bicho × Maria Ignácia", "box": [0.20, 0.18, 0.55, 0.07]},
        {"kind": "avos", "label": "António Freire Bicho × Maria de Christo", "box": [0.20, 0.26, 0.55, 0.06]},
        {"kind": "avos", "label": "Manuel Francisco Dias × Joaquina Maria", "box": [0.20, 0.32, 0.55, 0.06]},
        {"kind": "paten", "label": "Paten: Manuel Francisco Dias × Joaquina Silvéria", "box": [0.20, 0.38, 0.55, 0.06]},
        {"kind": "hinweis", "label": "N.º 10 darunter = anderes Kind", "box": [0.20, 0.50, 0.55, 0.08]},
    ],
    # Heirat 1907 N.º 9
    "PNL01-003-0051_m0015": [
        {"kind": "entry", "label": "N.º 9 beginnt, 13.11.1907", "box": [0.16, 0.50, 0.80, 0.48]},
        {"kind": "name", "label": "Manuel Duarte × Joaquina Ignácia", "box": [0.18, 0.54, 0.22, 0.10]},
        {"kind": "date", "label": "13.11.1907", "box": [0.42, 0.52, 0.45, 0.07]},
        {"kind": "place", "label": "Carrasqueiras / Cabeça Redonda", "box": [0.42, 0.78, 0.50, 0.08]},
        {"kind": "parents", "label": "António Duarte × Thereza Freire", "box": [0.42, 0.86, 0.50, 0.07]},
        {"kind": "hinweis", "label": "Eintrag darüber = andere Heirat", "box": [0.20, 0.08, 0.70, 0.18]},
    ],
    "PNL01-003-0051_m0016": [
        {"kind": "entry", "label": "N.º 9 Schluss", "box": [0.12, 0.04, 0.72, 0.62]},
        {"kind": "parents", "label": "António Freire Bicho × Maria Ignácia", "box": [0.28, 0.08, 0.50, 0.10]},
        {"kind": "place", "label": "Cabeça Redonda", "box": [0.28, 0.04, 0.50, 0.05]},
        {"kind": "paten", "label": "Zeuge José dos Santos, Carrasqueiras, Pfarrei Ansião", "box": [0.22, 0.32, 0.55, 0.10]},
        {"kind": "hinweis", "label": "N.º 10 = andere Heirat", "box": [0.14, 0.70, 0.70, 0.12]},
    ],
    # Heirat José dos Reis × Maria Ramalha 16.11.1863 — linke Seite N.º 5
    "PANS08-002-0007_m0004": [
        {"kind": "entry", "label": "N.º 5, 16.11.1863", "box": [0.02, 0.32, 0.46, 0.60]},
        {"kind": "name", "label": "José dos Reis × Maria Ramalha", "box": [0.03, 0.38, 0.12, 0.12]},
        {"kind": "date", "label": "16.11.1863", "box": [0.16, 0.34, 0.30, 0.08]},
        {"kind": "parents", "label": "Manoel Pedro dos Reis × Joaquina Maria", "box": [0.16, 0.48, 0.30, 0.08]},
        {"kind": "parents", "label": "Manoel Ramalho × Angelica Maria", "box": [0.16, 0.58, 0.30, 0.08]},
        {"kind": "place", "label": "Pragoza / Castello", "box": [0.16, 0.42, 0.30, 0.06]},
        {"kind": "hinweis", "label": "rechte Seite = späterer Vermerk, nicht diese Heirat", "box": [0.52, 0.08, 0.44, 0.30]},
    ],
    # José primeiro 1866 — rechte Seite, mittlerer Eintrag N.º 2
    "PANS08-001-0011_m0002": [
        {"kind": "entry", "label": "N.º 2 José, primeiro deste nome", "box": [0.50, 0.32, 0.48, 0.30]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.33, 0.12, 0.08]},
        {"kind": "date", "label": "~ 06.02.1866", "box": [0.62, 0.34, 0.34, 0.08]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha", "box": [0.62, 0.46, 0.34, 0.08]},
        {"kind": "hinweis", "label": "N.º 1 darüber / N.º 3 darunter = andere Häuser", "box": [0.50, 0.04, 0.48, 0.26]},
    ],
    # 1867 rechte Seite: oben Maria N.º 8 (Reis), unten Antonio N.º 9 (Guiomar)
    "PANS08-001-0012_m0003": [
        {"kind": "entry", "label": "N.º 8 Maria — Haus Reis × Ramalha", "box": [0.50, 0.04, 0.48, 0.42]},
        {"kind": "name", "label": "Maria", "box": [0.50, 0.06, 0.12, 0.08]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.14, 0.12, 0.06]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha", "box": [0.62, 0.22, 0.34, 0.10]},
        {"kind": "entry", "label": "N.º 9 Antonio — Haus Luiz × Delfina", "box": [0.50, 0.48, 0.48, 0.50]},
        {"kind": "name", "label": "Antonio, primeiro deste nome", "box": [0.50, 0.50, 0.14, 0.10]},
        {"kind": "place", "label": "Lindeo", "box": [0.50, 0.60, 0.14, 0.08]},
        {"kind": "date", "label": "* 20.04.1867  ~ 22.04.", "box": [0.64, 0.52, 0.32, 0.10]},
        {"kind": "parents", "label": "Luiz Guiomar × Delfina Maria", "box": [0.64, 0.68, 0.32, 0.10]},
    ],
    # Antonio 1867 Avós — linke Seite oben
    "PANS08-001-0012_m0004": [
        {"kind": "entry", "label": "Schluss N.º 9 Antonio", "box": [0.02, 0.02, 0.48, 0.22]},
        {"kind": "avos", "label": "Antonio Dias Guiomar × Joaquina Maria, Bemposta", "box": [0.14, 0.04, 0.34, 0.08]},
        {"kind": "avos", "label": "José Gregorio defunto × Benedita Maria, Lindeo", "box": [0.14, 0.12, 0.34, 0.08]},
        {"kind": "hinweis", "label": "rechte Seite = andere Taufen", "box": [0.52, 0.10, 0.44, 0.30]},
    ],
    # Anna 1869 — linke Seite unten, São Jorge
    "PANS08-001-0014_m0004": [
        {"kind": "entry", "label": "N.º 11 Anna, primeira deste nome", "box": [0.02, 0.52, 0.46, 0.46]},
        {"kind": "place", "label": "São Jorge", "box": [0.03, 0.54, 0.12, 0.08]},
        {"kind": "date", "label": "~ 08.08.1869", "box": [0.16, 0.56, 0.30, 0.08]},
        {"kind": "parents", "label": "Luiz Guiomar × Delfina Maria", "box": [0.16, 0.70, 0.30, 0.08]},
        {"kind": "avos", "label": "Antonio Dias × Joaquina; José Gregorio × Benedita", "box": [0.16, 0.80, 0.30, 0.10]},
        {"kind": "hinweis", "label": "Eintrag darüber = anderes Haus", "box": [0.02, 0.08, 0.46, 0.38]},
    ],
    # José segundo 1875 — rechte Seite N.º 13
    "PANS08-001-0020_m0007": [
        {"kind": "entry", "label": "N.º 13 José, segundo deste nome", "box": [0.50, 0.12, 0.48, 0.52]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.14, 0.12, 0.08]},
        {"kind": "date", "label": "* 18.09.1875  ~ 31.11. (so der Priester)", "box": [0.62, 0.16, 0.34, 0.10]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha, nat. Castello", "box": [0.62, 0.32, 0.34, 0.10]},
        {"kind": "avos", "label": "Manuel Pedro dos Reis × Joaquina Maria", "box": [0.62, 0.44, 0.34, 0.08]},
        {"kind": "hinweis", "label": "N.º 14 darunter = anderes Kind", "box": [0.50, 0.68, 0.48, 0.28]},
    ],
    # Maria da Graça 1864 — rechte Seite unten N.º 14
    "PANS08-001-0009_m0004": [
        {"kind": "entry", "label": "N.º 14 Maria da Graça, primeira do nome", "box": [0.50, 0.52, 0.48, 0.46]},
        {"kind": "place", "label": "Pragoza", "box": [0.50, 0.54, 0.12, 0.08]},
        {"kind": "date", "label": "* 30.05.1864  ~ 10.07.", "box": [0.62, 0.56, 0.34, 0.08]},
        {"kind": "parents", "label": "José dos Reis × Maria Ramalha", "box": [0.62, 0.70, 0.34, 0.10]},
        {"kind": "hinweis", "label": "Einträge darüber = andere Häuser (Lindos / Santo Romão)", "box": [0.50, 0.04, 0.48, 0.44]},
    ],
    # Consent + Heirat Joaquina Maria Leal × Jose Dias, Jan 1829 — links unten / rechts
    "PANS08-002-0003_m0033": [
        {"kind": "entry", "label": "Jan 1829 Consent: Manoel Leal × Thereza, Castello", "box": [0.02, 0.50, 0.46, 0.48]},
        {"kind": "parents", "label": "Manoel Leal × Thereza Maria, Castello", "box": [0.14, 0.58, 0.32, 0.10]},
        {"kind": "name", "label": "Joaquina Maria × Jose Dias", "box": [0.14, 0.70, 0.32, 0.08]},
        {"kind": "entry", "label": "14.01.1829 Heirat (rechte Seite)", "box": [0.50, 0.18, 0.48, 0.78]},
        {"kind": "place", "label": "Castello", "box": [0.50, 0.20, 0.10, 0.10]},
        {"kind": "hinweis", "label": "links oben durchgestrichen = nicht dieser Akt", "box": [0.02, 0.04, 0.46, 0.40]},
    ],
    # Maria Thereza Leal × Antonio Levante Freire Alvorge 02.06.1846 — links oben
    "PANS08-002-0003_m0066": [
        {"kind": "entry", "label": "02.06.1846 Maria Thereza Leal × Freire Alvorge", "box": [0.02, 0.02, 0.48, 0.42]},
        {"kind": "date", "label": "02.06.1846", "box": [0.14, 0.04, 0.34, 0.07]},
        {"kind": "name", "label": "Antonio Levante Freire × Maria Thereza", "box": [0.14, 0.14, 0.34, 0.08]},
        {"kind": "parents", "label": "Manoel Leal × Thereza Maria", "box": [0.14, 0.22, 0.34, 0.07]},
        {"kind": "place", "label": "Alvorge / Vale de Todos", "box": [0.14, 0.30, 0.34, 0.08]},
        {"kind": "hinweis", "label": "Eintrag darunter = anderes Paar", "box": [0.02, 0.48, 0.46, 0.30]},
    ],
    # José primeiro * 15.08.1841 / ~ 01.09.1841 — links unten, weiter rechts oben
    "PANS08-001-0003_m0138": [
        {"kind": "entry", "label": "José * 15.08.1841 beginnt", "box": [0.02, 0.68, 0.46, 0.30]},
        {"kind": "place", "label": "Rua da Alom", "box": [0.02, 0.70, 0.10, 0.08]},
        {"kind": "name", "label": "José", "box": [0.02, 0.78, 0.10, 0.08]},
        {"kind": "date", "label": "* 15.08.1841  ~ 01.09.", "box": [0.14, 0.72, 0.32, 0.08]},
        {"kind": "entry", "label": "Schluss: Eltern + avós Leal", "box": [0.50, 0.00, 0.48, 0.42]},
        {"kind": "parents", "label": "Manoel Thomaz × Angelica Maria", "box": [0.52, 0.02, 0.44, 0.08]},
        {"kind": "avos", "label": "Manoel Leal × Thereza Maria, Castello", "box": [0.52, 0.14, 0.44, 0.08]},
        {"kind": "hinweis", "label": "Eintrag 09.09. darunter = Ramos, nicht Ramalho", "box": [0.50, 0.44, 0.48, 0.20]},
    ],
    # Heirat Manoel Ramalho × Angelica Maria Feb. 1838 — rechte Seite unten
    "PANS08-002-0003_m0054": [
        {"kind": "entry", "label": "Feb. 1838 Manoel Ramalho × Angelica M.", "box": [0.50, 0.48, 0.48, 0.50]},
        {"kind": "name", "label": "M.el Ramalho / Angelica M.", "box": [0.50, 0.50, 0.10, 0.14]},
        {"kind": "date", "label": "21. oder 22.02.1838", "box": [0.58, 0.50, 0.38, 0.08]},
        {"kind": "parents", "label": "Braut: Manoel Leal × Thereza M.", "box": [0.58, 0.68, 0.38, 0.07]},
        {"kind": "place", "label": "Pregoza / Castello", "box": [0.58, 0.74, 0.38, 0.07]},
        {"kind": "hinweis", "label": "Dias steht nicht. Zweitname Gegenlese", "box": [0.58, 0.60, 0.38, 0.07]},
        {"kind": "hinweis", "label": "linke / obere Heirat = anderes Paar", "box": [0.02, 0.08, 0.46, 0.40]},
    ],
    # José * 02.06.1843 — Kandidat Sohn / Bruder Maria; linke Seite oben
    "PANS08-001-0004_m0009": [
        {"kind": "entry", "label": "José * 02.06.1843 Rua da Alom (Kandidat)", "box": [0.08, 0.04, 0.40, 0.42]},
        {"kind": "place", "label": "Rua da Alom", "box": [0.02, 0.04, 0.10, 0.08]},
        {"kind": "name", "label": "José", "box": [0.02, 0.12, 0.08, 0.07]},
        {"kind": "date", "label": "* 02.06.1843", "box": [0.12, 0.06, 0.34, 0.07]},
        {"kind": "parents", "label": "Manoel Thomaz Ramalho × Angelica Maria", "box": [0.12, 0.16, 0.34, 0.08]},
        {"kind": "avos", "label": "Manoel Leal × Thereza Maria", "box": [0.12, 0.28, 0.34, 0.07]},
        {"kind": "hinweis", "label": "Kandidat Bruder Maria. Dias steht nicht", "box": [0.12, 0.36, 0.34, 0.08]},
        {"kind": "hinweis", "label": "restliche Seite = andere Taufen", "box": [0.50, 0.08, 0.46, 0.40]},
    ],
    # Manoel Ramalho Pate Ateanha 10.06.1841 — linke Seite oben (Kind = Mendes, nicht Ramalho)
    "PANS01-001-0004_m0146": [
        {"kind": "entry", "label": "10.06.1841 Ateanha — Pate Manoel Ramalho", "box": [0.10, 0.04, 0.38, 0.40]},
        {"kind": "date", "label": "10.06.1841", "box": [0.12, 0.05, 0.34, 0.08]},
        {"kind": "place", "label": "Atianha", "box": [0.12, 0.18, 0.28, 0.07]},
        {"kind": "paten", "label": "Padrinho Manoel Ramalho", "box": [0.12, 0.30, 0.34, 0.08]},
        {"kind": "hinweis", "label": "Kind = Mendes-Haus, nicht unsere Maria", "box": [0.10, 0.44, 0.38, 0.12]},
    ],
    # Casimiro 1898 — linke Seite N.º 23
    "PANS08-001-0043_m0019": [
        {"kind": "entry", "label": "N.º 23 Casimiro", "box": [0.02, 0.16, 0.50, 0.78]},
        {"kind": "name", "label": "Casimiro", "box": [0.03, 0.22, 0.12, 0.07]},
        {"kind": "place", "label": "Pragoza", "box": [0.03, 0.29, 0.12, 0.05]},
        {"kind": "date", "label": "* 06.12.1898  ~ 26.12.1898", "box": [0.16, 0.18, 0.34, 0.10]},
        {"kind": "parents", "label": "Manuel Matta × Joaquina Ramalha", "box": [0.16, 0.48, 0.34, 0.10]},
        {"kind": "avos", "label": "Anna Matta; José Reis × Maria Ramalha", "box": [0.16, 0.60, 0.34, 0.10]},
        {"kind": "hinweis", "label": "rechte Seite = anderer Eintrag", "box": [0.52, 0.10, 0.44, 0.30]},
    ],
    # Margarida 1897 N.º 21
    "PNL01-002-0042_m0019": [
        {"kind": "entry", "label": "N.º 21 Margarida", "box": [0.18, 0.22, 0.78, 0.50]},
        {"kind": "place", "label": "Cabeça Redonda", "box": [0.20, 0.26, 0.16, 0.06]},
        {"kind": "name", "label": "Margarida", "box": [0.20, 0.32, 0.16, 0.06]},
        {"kind": "date", "label": "* 27.06.1897, Taufe selben Tag", "box": [0.38, 0.24, 0.55, 0.07]},
        {"kind": "parents", "label": "Joaquim Freire Bicho × Genoveva de Jesus", "box": [0.38, 0.38, 0.55, 0.08]},
        {"kind": "avos", "label": "António Freire Bicho × Maria Christo", "box": [0.38, 0.48, 0.55, 0.06]},
        {"kind": "rand", "label": "∞ 28.10.1922  † 29.11.1979", "box": [0.20, 0.40, 0.16, 0.28]},
        {"kind": "hinweis", "label": "N.º 22 darunter = anderes Kind", "box": [0.20, 0.76, 0.70, 0.10]},
    ],
}

KIND_FARBE = {
    "name": (244, 208, 63),
    "date": (230, 126, 34),
    "place": (93, 173, 226),
    "parents": (88, 214, 141),
    "avos": (175, 122, 197),
    "rand": (241, 148, 138),
    "paten": (26, 188, 156),
    "entry": (255, 235, 59),
    "hinweis": (133, 146, 158),
}

KIND_ALPHA = {
    "entry": 38,
    "hinweis": 70,
    "name": 95,
    "date": 85,
    "place": 80,
    "parents": 80,
    "avos": 78,
    "rand": 78,
    "paten": 80,
}
