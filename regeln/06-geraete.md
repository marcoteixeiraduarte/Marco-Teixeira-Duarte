# 06 — Desktop, App und Cloud

Damit Handy und Rechner dieselbe Mappe sehen. Kein Geräte-Pairing.
Dieselbe Cursor-Anmeldung, dieses GitHub-Repo.

**Standard: Desktop.** Neue Arbeit läuft auf dem Rechner.
Cloud nur, wenn der Mac aus ist oder der Auftraggeber Cloud
ausdrücklich will. Eine Cloud-Sitzung nicht still fortsetzen.

Offizielle Schritte: [Cursor for iOS](https://cursor.com/docs/cloud-agent/mobile),
[My Machines](https://cursor.com/docs/cloud-agent/self-hosted/my-machines).

## Was jeder sieht

| Oberfläche | Sieht |
| --- | --- |
| Cloud-Agent (App wählt Cloud) | nur Git auf `master` / PR. Kein `~/.cursor/`, kein `00_Arbeitsordner/` |
| App-Inbox / cursor.com/agents / Desktop Agents Window | dieselben Agenten, dasselbe Konto |
| Rechner (Remote Control oder My Machines) | Git **und** lokale Dateien dieses Checkouts |

`~/.cursor/rules` auf dem Laptop gilt in der Cloud **nicht**.
Gemeinsame Regeln nur hier und in `.cursor/rules/`.

## Einstellen (Checkliste)

Cloud kann Desktop **nicht** für dich umschalten. Eine laufende
Cloud-Sitzung hängt **nicht** nachträglich an den Mac. Nächsten
Agenten neu starten und dort den Rechner wählen.

### A — My Machines (App / cursor.com/agents)

1. Am Mac, im Git-Checkout **dieses** Repos, Worker starten und
   laufen lassen:

```bash
agent login
agent worker start --name genealogie
```

2. Optional prüfen: `agent worker debug` (Konto, Remote, Sichtbarkeit).
3. In der App / auf cursor.com/agents: neues Agenten-Gespräch.
4. Bei der Umgebung **My Machines** → Worker **`genealogie`**
   (oder der Eintrag, der **dieses** Repo zeigt). Nicht Cloud.
5. Aufgabe senden.

Zählt nur der Worker, dessen Git-Remote **dieses** Repo ist.
Ein zweiter Worker ohne Repo-Eintrag taugt nicht — den nicht wählen.
Rechnerpfade und Maschinennamen nicht ins Git schreiben.

### B — Remote Control (Desktop Agents Window)

Nur Cursor **3.9.8+**, nur Agents Window:

1. Settings → Agents → Remote Control an.
2. Keep this computer awake an (Rechner wach und online).
3. Repo auf dem Mac öffnen.
4. Im Agent-Eingabefeld `/remote-control`, dann eine Nachricht.
5. Sitzung erscheint in der App-Inbox.

Zwei Wege nicht vermischen.

`00_Arbeitsordner/` bleibt lokal. Wer ihn braucht, muss den
Rechner wählen — nicht Cloud.

## Wenn es nicht geht

| Symptom | Was tun |
| --- | --- |
| Nur Cloud wählbar | Worker-Prozess am Mac noch aktiv? Gleiches Cursor-Konto in App und CLI? |
| Maschine fehlt im Menü | `agent worker debug`; Checkout hat Remote dieses Repos; Worker neu starten |
| Falscher Ordner | Nur Worker mit Repo-Label dieses Repos; anderen Worker stoppen oder ignorieren |
| Cloud-Chat soll «Desktop» werden | Geht nicht. Neuen Agenten auf My Machines / Remote Control starten |
| Name `genealogie` fehlt | Worker mit `--name genealogie` neu starten; alten unbenannten Worker nicht wählen |

## Öffentliches Repo, privater Rechner

GitHub ist öffentlich. Der Server wird dadurch nicht öffentlich.
Cloud sieht nur den Clone. Desktop sieht den Checkout **und**
benachbarte lokale Dateien.

Push macht Dateien weltweit sichtbar. Lokal lesen ≠ veröffentlichen.
Pfade und Rechnernamen nicht ins Repo schreiben.
[`04-privat.md`](04-privat.md).

## Move to Cloud

Nimmt die Unterhaltung, nicht uncommittete Dateien. Zuerst
committen oder stashen.
