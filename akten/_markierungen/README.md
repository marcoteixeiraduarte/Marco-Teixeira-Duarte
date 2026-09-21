# Markierungen auf den Scans

Wie bei FamilySearch: **durchsichtige Flächen** auf den Textstellen,
die schon als Fund gelten. Nicht die ganze Seite einfärben.

Die Originalscans bleiben daneben (ohne Farbe), für die Gegenlese der
Handschrift. Die Koordinaten stehen in `felder.py` — nach der
Gegenlese dürfen die Kästen verschoben werden, nicht die Lesung.

| Farbe | Was |
| --- | --- |
| Gelb | Name in diesem Akt |
| Orange | Datum |
| Blau | Ort / Naturalidade |
| Grün | Eltern |
| Violett | Avós |
| Rosa | späterer Randvermerk |
| Petrol | Paten — **nicht** Elternort |
| Grau | Hinweis (anderer Eintrag auf derselben Seite) |

Neu erzeugen: `python3 render.py` (nur JPEG neben den bestehenden
Scans, Signatur unverändert).
