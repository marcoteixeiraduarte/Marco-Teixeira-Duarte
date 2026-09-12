#!/usr/bin/env python3
"""Generate archiv/karten/ place cards, orte.md, orte.geojson, README.md."""
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent

KEEP_NAMES = {"_generate.py"}  # do not delete this script during wipe


def osm(lat, lon, z=14):
    return f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map={z}/{lat}/{lon}"


def gmaps(lat, lon):
    return f"https://www.google.com/maps?q={lat},{lon}"


cards = []


def add(**kw):
    cards.append(kw)


# ========== ANSIÃO / ADLRA ==========
add(
    slug="torre-vale-todos",
    title="Torre de Vale de Todos",
    aliases=[
        "Torre",
        "Torre de Valle de Todos",
        "Valle de Todos",
        "Vale de Todos",
        "freguesia da Torre",
    ],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS08",
    tombo="https://tombo.pt/f/ans08",
    linha="Materno (Torre / Reis / Narciza / Guiomar / Matta)",
    status="gesichert (Wohn-/Heiratsort mehrerer Generationen)",
    notes=(
        "Zentrale Pfarrei Nossa Senhora da Graça da Torre. Digitale Batismos u. a. 1810–1842, 1843–1859; "
        "Casamentos 1830–1859. Lugares u. a. Pragoza, São Jorge (Kapelle in Vale de Todos), Rua d'Além. "
        "Nicht verwechseln: Pião/Lagarteira ist eigene Pfarrei (PANS05)."
    ),
    lat=39.95897,
    lon=-8.43017,
    related=["pragoza", "sao-jorge-torre", "rua-dalem", "ansiao", "lagarteira", "alvorge"],
    sources=["README.md (Ortsregister)", "evidenz/linie-torre/", "torre-records/"],
)

add(
    slug="pragoza",
    title="Pragoza / Pragosa",
    aliases=["Pragoza", "Pragosa", "Fragosa", "Lugar da Pragosa", "Lugar da Fragosa"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Torre)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS08",
    tombo="https://tombo.pt/f/ans08",
    linha="Materno Reis (José Pedro; Manoel Pedro-Herkunftsangabe)",
    status="gesichert als Weiler; Taufe Manoel Pedro (~1820–35) noch offen",
    notes=(
        "Quellenform mit z (Pragoza) auf dem Blatt belassen, wenn die Quelle so schreibt. "
        "José Pedro dos Reis *1854 Pragoza. Manoel Pedro dos Reis 1851: Eltern Manoel Pedro × Joaquina Maria, "
        "Lugar Pragosa/Fragosa — in Torre-Batismos 1810–1842 noch kein sicherer Taufanschluss. "
        "Kein eigener sicherer OSM-Knoten; Pin genähert bei Torre."
    ),
    lat=39.95897,
    lon=-8.43017,
    related=["torre-vale-todos"],
    sources=["README.md", "evidenz/linie-torre/suche-taufe-roza-manoel.md"],
)

add(
    slug="sao-jorge-torre",
    title="São Jorge (Kapelle / lugar in Vale de Todos)",
    aliases=["São Jorge", "S. Jorge", "logar de São Jorge"],
    tipo="Lugar / Kapelle",
    municipio="Ansião (Pfarrei Torre)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS08",
    tombo="https://tombo.pt/f/ans08",
    linha="Materno Torre",
    status="gesichert (lugar derselben Pfarrei Torre)",
    notes=(
        "Kleine Kapelle im Weiler Vale de Todos — kein ferner Weiler und keine fremde Pfarrei. "
        "Nicht Capela/Rua/Mata de São Jorge in Chão de Couce und nicht São Jorge in Porto de Mós."
    ),
    lat=39.95897,
    lon=-8.43017,
    related=["torre-vale-todos", "chao-de-couce"],
    sources=["README.md (VALLE DE TODOS / São Jorge)"],
)

add(
    slug="rua-dalem",
    title="Rua d'Além",
    aliases=["Rua d'Além", "Rua d'Allem"],
    tipo="Lugar / Weiler",
    municipio="Ansião (Pfarrei Torre)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS08",
    tombo="https://tombo.pt/f/ans08",
    linha="Materno Guiomar / Matta",
    status="gesichert (Taufe João Guiomar 1874)",
    notes="Weiler der Pfarrei Torre. João *22.4.1874 Rua d'Além; Paten Manuel 1872 ebenfalls.",
    lat=39.95897,
    lon=-8.43017,
    related=["torre-vale-todos", "bemposta"],
    sources=["guiomar-records/", "README.md"],
)

add(
    slug="lagarteira",
    title="Lagarteira (São Domingos)",
    aliases=["Lagarteira", "São Domingos da Lagarteira", "LAR"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS05",
    tombo="https://tombo.pt/f/ans05",
    linha="Materno (Guiomar-Umfeld; Grenze zu Reis †1903)",
    status="gesichert als eigene Pfarrei (nicht Torre)",
    notes=(
        "Pfarrei São Domingos da Lagarteira (DigitArq PANS05; Auftraggeber LAR). "
        "Pião / Valle do Pião gehört hierher, nicht zur Torre. "
        "Sterbeeintrag José Pedro dos Reis 2.10.1903: linha divisoria Torre ↔ Lagarteira."
    ),
    lat=39.95354,
    lon=-8.40614,
    related=["piao", "torre-vale-todos"],
    sources=["README.md (VALLE DO PIÃO / LAGARTEIRA)", "narcisa-records/"],
)

add(
    slug="piao",
    title="Pião / Valle do Pião",
    aliases=["Pião", "Valle do Pião", "Pião desta freguezia"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Lagarteira)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS05",
    tombo="https://tombo.pt/f/ans05",
    linha="Materno (Maria 1882 Lagarteira)",
    status="gesichert — Pfarrei Lagarteira, nicht Torre",
    notes=(
        "Weiler der Pfarrei Lagarteira. Taufe Maria 5.3.1882 in PANS05. "
        "Grenze zu Torre am Weiler (linha divisoria)."
    ),
    lat=39.95354,
    lon=-8.40614,
    related=["lagarteira", "torre-vale-todos"],
    sources=["README.md", "guiomar-records/"],
)

add(
    slug="alvorge",
    title="Alvorge",
    aliases=["Alvorge", "freguesia do Alvorge"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno Reis (Herkunft Roza Maria)",
    status="gesichert (Heiratsherkunft Roza Maria 1851)",
    notes=(
        "Roza Maria „natural e baptizada na freguesia do Alvorge“. "
        "Batismos 1808–1822 / 1822–1852 lokal unter alvorge-records/. "
        "Casamentos 1789–1859 fehlen online → nur ADLRA. "
        "Lugares: Ateanha, Vale Paio, Aljazede/Vallejazede, Bemposta, Vila Nova — getrennt lassen."
    ),
    lat=39.9788,
    lon=-8.4507,
    related=[
        "ateanha",
        "vale-paio",
        "aljazede",
        "bemposta",
        "vila-nova-alvorge",
        "torre-vale-todos",
    ],
    sources=["evidenz/linie-torre/suche-taufe-roza-manoel.md", "alvorge-records/"],
)

add(
    slug="ateanha",
    title="Ateanha / Atianha",
    aliases=["Ateanha", "Atianha", "Attianha", "Atanha"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01 (kein eigenes Fonds)",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno (Prüfhypothese Roza — als Herkunft ausgeschlossen)",
    status="Ort gesichert als Lugar; als Roza-Herkunft ausgeschlossen",
    notes=(
        "Einträge in Alvorge-Büchern (z. B. m0089/m0091). Kein separates DigitArq-Fonds. "
        "Nicht mit Rozas belegter Herkunft „Alvorge“ gleichsetzen. Atanha = Quellenform Joze Mendes Ferreiras 1880."
    ),
    lat=39.9794,
    lon=-8.4200,
    related=["alvorge"],
    sources=["evidenz/linie-torre/alvorge-ateanha.md", "README.md"],
)

add(
    slug="vale-paio",
    title="Vale Paio",
    aliases=["Vale Paio", "Valle paio", "Vale do Paio"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno Reis (Roza — Quellenform)",
    status="genannt in Heirat 1851; nicht mit Aljazede zusammenführen",
    notes=(
        "Lugar der Pfarrei Alvorge, nicht Cumeeira. "
        "Vale Paio / Vallejazede / Aljazede / Ateanha getrennt lassen, bis Rozas Taufe klärt."
    ),
    lat=39.9788,
    lon=-8.4507,
    related=["alvorge", "aljazede", "ateanha"],
    sources=["evidenz/linie-torre/alvorge-ateanha.md", "ERKENNTNISSE.md"],
)

add(
    slug="aljazede",
    title="Aljazede / Vallejazede",
    aliases=["Aljazede", "Vallejazede", "Aljazéde"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno Reis (Roza-Umfeld)",
    status="sicher genannt in Sohnesheirat/-tod; Lage genähert",
    notes=(
        "Quellenformen in Einträgen zu Rozas Nachkommen. Pfarrei Alvorge. "
        "Nicht mit Vale Paio oder Ateanha zu einem Ort zusammenziehen."
    ),
    lat=39.9788,
    lon=-8.4450,
    related=["alvorge", "vale-paio", "ateanha"],
    sources=["evidenz/linie-torre/alvorge-ateanha.md", "narcisa-records/"],
)

add(
    slug="bemposta",
    title="Bemposta (Alvorge)",
    aliases=["Bemposta"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno Guiomar (Herkunft Luiz Guiomar)",
    status="gesichert (Taufe João 1874)",
    notes="Herkunft Luiz Guiomars, Vater von João (*1874 Rua d'Além, Torre).",
    lat=39.97565,
    lon=-8.43118,
    related=["alvorge", "rua-dalem", "torre-vale-todos"],
    sources=["guiomar-records/", "README.md"],
)

add(
    slug="vila-nova-alvorge",
    title="Vila Nova (Alvorge)",
    aliases=["Vila Nova", "Vila Nova de Alvorge"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno (Kontext Alvorge-Bücher)",
    status="belegt im Bandrand / Patin 1854",
    notes="Lugar im Alvorge-Band; Patin Maria Joaquina (Witwe) 1854 am Taufeintrag des Sohnes.",
    lat=39.98256,
    lon=-8.44228,
    related=["alvorge"],
    sources=["alvorge-records/", "evidenz/linie-torre/alvorge-ateanha.md"],
)

add(
    slug="vale-galego",
    title="Vale Galego",
    aliases=["Vale Galego", "Vale do Galego"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Alvorge)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS01",
    tombo="https://tombo.pt/f/ans01",
    linha="Materno (Negativkontrolle Roza)",
    status="Ort belegt; Roza-Kandidatin ausgeschlossen",
    notes=(
        "Roza *14.1./tauf 22.1.1826 (Francisco José Giraldes × Thereza Maria) — "
        "falsche Eltern für unsere Roza Maria."
    ),
    lat=39.9780,
    lon=-8.4480,
    related=["alvorge"],
    sources=["evidenz/linie-torre/suche-taufe-roza-manoel.md"],
)

add(
    slug="avelar",
    title="Avelar",
    aliases=["Avelar"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS03",
    tombo="https://tombo.pt/f/ans03",
    linha="Materno (Gato/Simões-Kandidaten; Rapoula)",
    status="Kontextpfarrei",
    notes="Nachbarfreguesia; Rapoula liegt hier. Theodora-Kandidaten gegenlesen.",
    lat=39.9145,
    lon=-8.3599,
    related=["rapoula", "ansiao"],
    sources=["ERKENNTNISSE.md"],
)

add(
    slug="rapoula",
    title="Rapoula (bei Avelar)",
    aliases=["Rapoula", "Rapolla"],
    tipo="Lugar",
    municipio="Ansião (Pfarrei Avelar)",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA PANS03",
    tombo="https://tombo.pt/f/ans03",
    linha="Materno (Theodora-Kandidaten)",
    status="belegt für Theodora Maria 1781; nicht Maria Joaquina Sol",
    notes=(
        "Theodora Maria *27.12.1780 / tauf 9.1.1781, Rapoula "
        "(Alexandre Manoel Furtado × Marianna da Affonseca)."
    ),
    lat=39.93124,
    lon=-8.35768,
    related=["avelar"],
    sources=["evidenz/linie-torre/theodora-maria-1781.md"],
)

add(
    slug="ansiao",
    title="Ansião",
    aliases=["Ansião", "Anciao", "Anciāo", "concelho d'Anciao"],
    tipo="Kreisstadt (Concelho)",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA; Conservatória do Registo Civil",
    tombo="https://tombo.pt/",
    linha="Verwaltung + Conservatória (*1912–1915 Fotos)",
    status="gesichert",
    notes=(
        "Concelho für Torre, Alvorge, Avelar, Lagarteira u. a. "
        "Quellenform Anciao in Taufen 1878/1880 belassen. "
        "Conservatória-Fotokopien: archiv/conservatoria-ansiao/."
    ),
    lat=39.9122,
    lon=-8.4344,
    related=["torre-vale-todos", "alvorge", "avelar", "lagarteira", "sarzedela"],
    sources=["README.md", "archiv/conservatoria-ansiao/"],
)

add(
    slug="sarzedela",
    title="Sarzedela",
    aliases=["Sarzedela", "Cervedela (alt)"],
    tipo="Lugar",
    municipio="Ansião",
    distrito="Leiria",
    cluster="ansiao-adlra",
    archiv="ADLRA (Pfarrei Ansião PANS02)",
    tombo="https://tombo.pt/f/ans02",
    linha="nur Kandidat zu Lesung Sarrazina / São Cosme",
    status="Lage plausibel; nicht als gelesener Patenort setzen",
    notes=(
        "Nachbar von Figueiras de S. João. 1879 Pfarrei Ansião (N.S. da Conceição), nicht São Cosme. "
        "Gleichsetzung mit Sarrazina hängt an der Handschrift — unsicher."
    ),
    lat=39.92753,
    lon=-8.44387,
    related=["ansiao", "figueiras-podres", "cabeca-redonda"],
    sources=["README.md (SARRAZINA / SÃO COSME)", "teixeira-records/"],
)

# ========== CUMEEIRA / AUC ==========
add(
    slug="cumeeira",
    title="Cumeeira",
    aliases=["Cumeeira", "Cumieira", "Cumeira", "São Sebastião da Cumeeira"],
    tipo="Freguesia",
    municipio="Penela",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01",
    tombo="https://tombo.pt/f/pnl01",
    linha="Paterno Duarte + Teixeira (archivische Brücke)",
    status="gesichert",
    notes=(
        "Gemeinsames Pfarreibuch-Fonds für Duarte/Freire Bicho und Teixeira. "
        "Quellenform der geprüften Taufen und Heirat 1907: Cumeeira. "
        "Nicht ADLRA. Zivilheirat Penela 1922 Nr. 94 ebenfalls AUC."
    ),
    lat=39.94357,
    lon=-8.38060,
    related=[
        "cabeca-redonda",
        "figueiras-podres",
        "carrasqueiras",
        "ferraria-sao-joao",
        "penela",
    ],
    sources=["evidenz/linie-duarte/", "teixeira-records/", "ERKENNTNISSE.md"],
)

add(
    slug="cabeca-redonda",
    title="Cabeça Redonda",
    aliases=["Cabeça Redonda", "Cabeca Redonda"],
    tipo="Lugar",
    municipio="Penela (Pfarrei Cumeeira)",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01",
    tombo="https://tombo.pt/f/pnl01",
    linha="Paterno Duarte / Teixeira",
    status="gesichert",
    notes=(
        "Taufen Joaquina 1886, Margarida 1897; João Teixeira 1879 hier geboren "
        "(nicht nur „in Cumeeira“)."
    ),
    lat=39.93205,
    lon=-8.40327,
    related=["cumeeira", "figueiras-podres", "carrasqueiras"],
    sources=["README.md", "duarte-freire-records/"],
)

add(
    slug="figueiras-podres",
    title="Figueiras Podres / Figueiras de S. João",
    aliases=[
        "Figueiras Podres",
        "Figueira Podres",
        "Figueira Podra",
        "Figueiras de S. João",
        "Figueiras de São João",
    ],
    tipo="Lugar",
    municipio="Ansião / Grenze Cumeeira (Penela)",
    distrito="Leiria / Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01 (Ereignisse) / Lage Ansião",
    tombo="https://tombo.pt/f/pnl01",
    linha="Paterno Duarte / Teixeira",
    status="gesichert — ein Ort (historisch Podres, heute de S. João)",
    notes=(
        "Ein Ort, keine zwei Siedlungen. Am Ereignis Figueiras Podres (mit -s) belassen; "
        "Taufen auch Figueira Podra. Heute INE/OSM Figueiras de São João. "
        "Nachbar Cabeça Redonda, Grenze Cumeeira/Ansião. "
        "Nicht Ferraria de S. João und nicht Venda das Figueiras."
    ),
    lat=39.93711,
    lon=-8.40637,
    related=["cabeca-redonda", "cumeeira", "ferraria-sao-joao", "venda-das-figueiras"],
    sources=["README.md (FIGUEIRA PODRA)", "teixeira-records/"],
)

add(
    slug="carrasqueiras",
    title="Carrasqueiras",
    aliases=["Carrasqueiras"],
    tipo="Lugar",
    municipio="Penela / Grenzlage Ansião (Pfarrei Cumeeira)",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01",
    tombo="https://tombo.pt/f/pnl01",
    linha="Paterno Duarte",
    status="gesichert (Taufe Manuel Duarte 1885)",
    notes="Geburtsort Manuel Duarte *19.11.1885 / Taufe 2.12.1885.",
    lat=39.93167,
    lon=-8.40912,
    related=["cumeeira", "cabeca-redonda"],
    sources=["README.md", "duarte-freire-records/"],
)

add(
    slug="ferraria-sao-joao",
    title="Ferraria de São João",
    aliases=["Ferraria de S. João", "Ferraria de São João"],
    tipo="Lugar",
    municipio="Penela (Pfarrei Cumeeira)",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01",
    tombo="https://tombo.pt/f/pnl01",
    linha="Abgrenzung zu Figueiras Podres",
    status="anderer Ort — nicht zusammenwerfen",
    notes="Weiler der Pfarrei Cumeeira. Anderer Ort als Figueiras de S. João / Figueiras Podres.",
    lat=39.97389,
    lon=-8.32333,
    related=["cumeeira", "figueiras-podres"],
    sources=["README.md"],
)

add(
    slug="venda-das-figueiras",
    title="Venda das Figueiras",
    aliases=["Venda das Figueiras"],
    tipo="Lugar",
    municipio="Penela (Pfarrei Cumeeira)",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC PNL01",
    tombo="https://tombo.pt/f/pnl01",
    linha="Abgrenzung zu Figueiras Podres",
    status="anderer Ort — nicht zusammenwerfen",
    notes=(
        "Ebenfalls Cumeeira; nicht mit Figueiras Podres / Figueiras de S. João gleichsetzen. "
        "Pin genähert bei Cumeeira."
    ),
    lat=39.94357,
    lon=-8.38060,
    related=["cumeeira", "figueiras-podres"],
    sources=["README.md"],
)

add(
    slug="penela",
    title="Penela",
    aliases=["Penela"],
    tipo="Kreisstadt (Concelho)",
    municipio="Penela",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC — RCV Penela + PNL01",
    tombo="https://tombo.pt/m/pnl",
    linha="Paterno Duarte / Teixeira",
    status="gesichert",
    notes=(
        "Zivilheirat José Freire Bicho × Maria da Conceição Duarte 1922 Nr. 94. "
        "Cumeeira gehört zu Penela."
    ),
    lat=40.0320,
    lon=-8.3899,
    related=["cumeeira", "espinhal", "podentes", "coimbra"],
    sources=["evidenz/linie-duarte/AUC-coimbra-jose-freire-bicho.md"],
)

add(
    slug="espinhal",
    title="Espinhal",
    aliases=["Espinhal"],
    tipo="Freguesia",
    municipio="Penela",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC",
    tombo="https://tombo.pt/",
    linha="Paterno-Umfeld Penela",
    status="Nachbarfreguesia",
    notes="Freguesia im Concelho Penela; Kontext zu Cumeeira.",
    lat=40.0200,
    lon=-8.3500,
    related=["penela", "cumeeira"],
    sources=[],
)

add(
    slug="podentes",
    title="Podentes",
    aliases=["Podentes"],
    tipo="Freguesia",
    municipio="Penela",
    distrito="Coimbra",
    cluster="cumeeira-auc",
    archiv="AUC",
    tombo="https://tombo.pt/",
    linha="Paterno-Umfeld Penela",
    status="Nachbarfreguesia",
    notes="Freguesia im Concelho Penela.",
    lat=40.0100,
    lon=-8.4000,
    related=["penela", "cumeeira"],
    sources=[],
)

# ========== ABGRENZUNG ==========
add(
    slug="chao-de-couce",
    title="Chão de Couce",
    aliases=["Chão de Couce"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="abgrenzung",
    archiv="ADLRA",
    tombo="https://tombo.pt/f/ans04",
    linha="Abgrenzung São Jorge",
    status="Nachbarpfarrei — nicht São Jorge der Torre",
    notes=(
        "Andere Pfarrei mit eigener Capela/Rua/Mata de São Jorge. "
        "Nicht mit São Jorge in Vale de Todos zusammenwerfen."
    ),
    lat=39.89240,
    lon=-8.36965,
    related=["sao-jorge-torre", "ansiao"],
    sources=["README.md"],
)

add(
    slug="orada",
    title="Orada (Senhora da Orada)",
    aliases=["Orada", "Senhora da Orada"],
    tipo="Freguesia / Ort",
    municipio="Ansião",
    distrito="Leiria",
    cluster="abgrenzung",
    archiv="ADLRA",
    tombo="https://tombo.pt/",
    linha="Diözesenliste Coimbra 1879 (Kontext)",
    status="Nachbar — nicht Kernlinie",
    notes="In der historischen Diözesenliste Ansião/Penela 1879 genannt (kein São Cosme dort).",
    lat=39.95970,
    lon=-8.46611,
    related=["ansiao", "santiago-da-guarda"],
    sources=["README.md"],
)

add(
    slug="pousaflores",
    title="Pousaflores",
    aliases=["Pousaflores"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="abgrenzung",
    archiv="ADLRA",
    tombo="https://tombo.pt/",
    linha="Diözesenliste Coimbra 1879 (Kontext)",
    status="Nachbar — nicht Kernlinie",
    notes="In der historischen Diözesenliste Ansião/Penela 1879 genannt.",
    lat=39.86683,
    lon=-8.39548,
    related=["ansiao"],
    sources=["README.md"],
)

add(
    slug="santiago-da-guarda",
    title="Santiago da Guarda",
    aliases=["Santiago da Guarda"],
    tipo="Freguesia",
    municipio="Ansião",
    distrito="Leiria",
    cluster="abgrenzung",
    archiv="ADLRA",
    tombo="https://tombo.pt/",
    linha="Diözesenliste Coimbra 1879 (Kontext)",
    status="Nachbar — nicht Kernlinie",
    notes="In der historischen Diözesenliste Ansião/Penela 1879 genannt.",
    lat=39.94729,
    lon=-8.48073,
    related=["ansiao", "orada"],
    sources=["README.md"],
)

add(
    slug="pombalinho",
    title="Pombalinho",
    aliases=["Pombalinho"],
    tipo="Freguesia / Ort",
    municipio="Soure",
    distrito="Coimbra",
    cluster="abgrenzung",
    archiv="ggf. AD Coimbra",
    tombo="https://tombo.pt/f/sre09",
    linha="erwähnt in Alvorge-Einträgen (Großeltern-Herkunft)",
    status="Kontext / Herkunftsangabe",
    notes="In Alvorge-Einträgen als Herkunft von Großeltern erwähnt — nicht Kernpfarrei der Linien.",
    lat=40.01219,
    lon=-8.47115,
    related=["alvorge"],
    sources=[],
)

# ========== ARCHIV / KONTEXT ==========
add(
    slug="leiria",
    title="Leiria",
    aliases=["Leiria"],
    tipo="Distrikthauptstadt / Archivort",
    municipio="Leiria",
    distrito="Leiria",
    cluster="archiv",
    archiv="ADLRA — Arquivo Distrital de Leiria",
    tombo="",
    linha="Materno — Archivstandort",
    status="gesichert (Archiv)",
    notes="Lagerort PANS01/03/05/08. Alvorge-Casamentos-Lücke 1789–1859 nur hier schließbar.",
    lat=39.7436,
    lon=-8.8071,
    related=["ansiao", "torre-vale-todos", "alvorge"],
    sources=["archiv/ARCHIVE-UND-LINKS.md"],
)

add(
    slug="coimbra",
    title="Coimbra",
    aliases=["Coimbra"],
    tipo="Distrikthauptstadt / Archivort",
    municipio="Coimbra",
    distrito="Coimbra",
    cluster="archiv",
    archiv="AUC — Arquivo da Universidade de Coimbra",
    tombo="",
    linha="Paterno — Archivstandort",
    status="gesichert (Archiv)",
    notes=(
        "Lagerort PNL01 Cumeeira und RCV Penela. Nicht mit ADLRA Leiria verwechseln. "
        "„Apresentação da Universidade de Coimbra“ bei Alvorge = Präsentationsrecht, nicht Lagerort."
    ),
    lat=40.2115,
    lon=-8.4292,
    related=["penela", "cumeeira"],
    sources=["archiv/ARCHIVE-UND-LINKS.md"],
)

add(
    slug="lisboa",
    title="Lisboa",
    aliases=["Lisboa", "Lisbon", "Torre do Tombo"],
    tipo="Hauptstadt / Nationalarchiv / Portal",
    municipio="Lisboa",
    distrito="Lisboa",
    cluster="archiv",
    archiv="ANTT; digitarq.arquivos.pt",
    tombo="",
    linha="Querschnitt — Portal",
    status="Portal / Nationalarchiv",
    notes=(
        "DigitArq hostet viele Distriktarchive digital. "
        "Primäre Pfarreibücher dieser Linien liegen fachlich bei ADLRA bzw. AUC."
    ),
    lat=38.7078,
    lon=-9.1366,
    related=[],
    sources=["archiv/ARCHIVE-UND-LINKS.md"],
)

add(
    slug="pombal",
    title="Pombal",
    aliases=["Pombal"],
    tipo="Kreisstadt",
    municipio="Pombal",
    distrito="Leiria",
    cluster="kontext",
    archiv="ADLRA / Regional",
    tombo="",
    linha="Regionaler Bezugspunkt",
    status="Kontext",
    notes="Nachbarstadt; nicht Kernpfarrei der Linien.",
    lat=39.9172,
    lon=-8.6323,
    related=["ansiao", "leiria"],
    sources=[],
)

add(
    slug="chaves",
    title="Chaves",
    aliases=["Chaves"],
    tipo="Stadt",
    municipio="Chaves",
    distrito="Vila Real",
    cluster="kontext",
    archiv="außerhalb ADLRA/AUC-Kern",
    tombo="",
    linha="Lebensstation (moderne Generation)",
    status="Kontext",
    notes="Lebensort in der Familiengeschichte; kein Pfarreibuch-Kern Torre/Cumeeira.",
    lat=41.7403,
    lon=-7.4686,
    related=[],
    sources=[],
)

add(
    slug="porto",
    title="Porto",
    aliases=["Porto", "Oporto"],
    tipo="Stadt",
    municipio="Porto",
    distrito="Porto",
    cluster="kontext",
    archiv="außerhalb ADLRA/AUC-Kern",
    tombo="",
    linha="Lebensstation / Kontext",
    status="Kontext",
    notes="Lebens-/Migrationskontext; nicht Kernarchivort der historischen Pfarreilinie.",
    lat=41.1495,
    lon=-8.6110,
    related=[],
    sources=[],
)


def main():
    # wipe previous generated files (keep generator)
    for p in BASE.iterdir():
        if p.name in KEEP_NAMES:
            continue
        if p.is_file():
            p.unlink()

    features = []
    for c in cards:
        lat, lon = c["lat"], c["lon"]
        aliases = ", ".join(f"`{a}`" for a in c["aliases"])
        related_md = "\n".join(f"- [{r}]({r}.md)" for r in c["related"]) or "_—"
        sources_md = "\n".join(f"- `{s}`" for s in c["sources"]) or "_siehe Index_"
        tombo_cell = c["tombo"] if c.get("tombo") else "—"
        body = f"""# {c['title']}

| Feld | Inhalt |
|------|--------|
| **ID** | `{c['slug']}` |
| **Typ** | {c['tipo']} |
| **Município / Kontext** | {c['municipio']} |
| **Distrito** | {c['distrito']} |
| **Cluster** | `{c['cluster']}` |
| **Familienlinie** | {c['linha']} |
| **Archiv** | {c['archiv']} |
| **tombo.pt** | {tombo_cell} |
| **Status** | {c['status']} |
| **Koordinaten (WGS84)** | {lat:.5f}, {lon:.5f} _(genähert)_ |

## Schreibvarianten (Quellenformen)

{aliases}

## Kurznotiz

{c['notes']}

## Karten

- [OpenStreetMap]({osm(lat, lon)})
- [Google Maps]({gmaps(lat, lon)})

## Verwandte Orte

{related_md}

## Quellen / Doku im Repo

{sources_md}

---
← [Kartenarchiv-Index](README.md) · [Ortsliste](orte.md)
"""
        (BASE / f"{c['slug']}.md").write_text(body, encoding="utf-8")
        features.append(
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
                "properties": {
                    "id": c["slug"],
                    "name": c["title"],
                    "tipo": c["tipo"],
                    "municipio": c["municipio"],
                    "distrito": c["distrito"],
                    "cluster": c["cluster"],
                    "linha": c["linha"],
                    "archiv": c["archiv"],
                    "status": c["status"],
                },
            }
        )

    by_cluster = {
        "ansiao-adlra": "Ansião-Cluster (ADLRA) — materno",
        "cumeeira-auc": "Cumeeira-Cluster (AUC) — paterno + Teixeira-Bücher",
        "abgrenzung": "Abgrenzung / Nachbarpfarreien",
        "archiv": "Archiv- und Portalorte",
        "kontext": "Weiterer Lebens-/Regionalkontext",
    }

    readme = f"""# Kartenarchiv — Orte der Familiengeschichte

Geografisches Gegenstück zu [`../ARCHIVE-UND-LINKS.md`](../ARCHIVE-UND-LINKS.md)
und zum Ortsregister in [`../../README.md`](../../README.md):
**alle relevanten Orte** mit Kartenlinks, Archivzuordnung und Status.

## Schnellzugriff

| Datei | Inhalt |
|-------|--------|
| [orte.md](orte.md) | Tabellarische Gesamtliste |
| [orte.geojson](orte.geojson) | Punkte für [geojson.io](https://geojson.io) / QGIS |
| Einzelblätter `*.md` | Ein Ort = eine Datei |
| [`_generate.py`](_generate.py) | Generator (bei Erweiterung neu laufen lassen) |

## Zwei Forschungskerne

```
ADLRA Leiria (materno)                    AUC Coimbra (paterno + Teixeira)
─────────────────────                    ────────────────────────────────
Ansião                                   Penela
├─ Torre de Vale de Todos                └─ Cumeeira
│  ├─ Pragoza / Pragosa                     ├─ Cabeça Redonda
│  ├─ São Jorge (Kapelle Vale de Todos)     ├─ Figueiras Podres (= de S. João)
│  └─ Rua d'Além                            ├─ Carrasqueiras
├─ Lagarteira (eigene Pfarrei PANS05)       └─ Ferraria de S. João (Abgrenzung)
│  └─ Pião / Valle do Pião
├─ Alvorge
│  ├─ Ateanha / Atianha
│  ├─ Vale Paio · Aljazede/Vallejazede
│  ├─ Bemposta · Vila Nova
│  └─ Vale Galego (Negativkontrolle)
└─ Avelar · Rapoula
```

## Regeln

- **Quellenformen** der Ortsnamen nicht „korrigieren“ (`Pragoza`/`Pragosa`, `Cumeeira`/`Cumeira`, …).
- **Ein Ort vs. zwei:** Figueiras Podres = Figueiras de S. João; Vale Paio ≠ Aljazede ≠ Ateanha.
- **Pfarreigrenze:** Pião gehört zu **Lagarteira** (PANS05), nicht zu Torre (PANS08).
- Koordinaten sind **genähert** (Nominatim / Schätzung) — Belege stehen in den Akten.
- Privatadressen und Ausweisdaten gehören **nicht** hierher.

## Index nach Cluster

"""
    for cluster_id, label in by_cluster.items():
        subset = [c for c in cards if c["cluster"] == cluster_id]
        readme += f"\n### {label}\n\n"
        for c in subset:
            readme += f"- [{c['title']}]({c['slug']}.md) — {c['tipo']}\n"

    readme += f"\n---\n\nAnzahl Ortsblätter: **{len(cards)}**\n"
    (BASE / "README.md").write_text(readme, encoding="utf-8")

    lines = [
        "# Ortsliste (vollständig)\n\n",
        f"Stand: {len(cards)} Orte. GeoJSON: [orte.geojson](orte.geojson).\n\n",
        "| Ort | Typ | Cluster | Município | Archiv | Status | Karte |\n",
        "|-----|-----|---------|-----------|--------|--------|-------|\n",
    ]
    for c in sorted(cards, key=lambda x: x["title"].casefold()):
        st = c["status"] if len(c["status"]) <= 42 else c["status"][:40] + "…"
        ar = c["archiv"] if len(c["archiv"]) <= 28 else c["archiv"][:26] + "…"
        lines.append(
            f"| [{c['title']}]({c['slug']}.md) | {c['tipo']} | `{c['cluster']}` | {c['municipio']} | "
            f"{ar} | {st} | [OSM]({osm(c['lat'], c['lon'], 13)}) |\n"
        )
    (BASE / "orte.md").write_text("".join(lines), encoding="utf-8")

    gj = {
        "type": "FeatureCollection",
        "name": "Marco-Teixeira-Duarte-Orte",
        "features": features,
    }
    (BASE / "orte.geojson").write_text(
        json.dumps(gj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    print(f"OK: {len(cards)} cards")
    for c in sorted(cards, key=lambda x: x["slug"]):
        print(f"  {c['cluster']:16} {c['slug']}")


if __name__ == "__main__":
    main()
