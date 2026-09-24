# 06 — Desktop, App und Cloud

Damit Handy und Rechner dieselbe Mappe sehen. Kein Geräte-Pairing.
Dieselbe Cursor-Anmeldung, dieses GitHub-Repo.

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

## App startet Cloud, solange kein Rechner gewählt ist

Eine schon laufende Cloud-Sitzung hängt **nicht** nachträglich
an den Mac. Nächsten Agenten neu starten.

In der App beim Start **My Machines** wählen — nur den Worker,
dessen Git-Remote **dieses** Repo ist. Ein Worker in einem
anderen Ordner (ohne dieses Remote) zählt nicht.

## Rechner von der App steuern

Zwei getrennte Wege. Nicht vermischen.

### Remote Control

Nur im **Agents Window** am Desktop, Cursor **3.9.8+**.

1. Settings → Agents → Remote Control an.
2. Rechner wach und online lassen (Keep this computer awake).
3. Im Agent-Eingabefeld `/remote-control`, dann eine Nachricht.
4. Sitzung erscheint in der App-Inbox.

### My Machines

Im Git-Checkout **dieses** Repos:

```bash
agent worker start --name genealogie
```

Prozess laufen lassen. Nächster Agent in der App: diese Maschine
wählen, nicht Cloud.

`00_Arbeitsordner/` bleibt lokal. Wer ihn braucht, muss den
Rechner wählen — nicht Cloud.

## Move to Cloud

Nimmt die Unterhaltung, nicht uncommittete Dateien. Zuerst
committen oder stashen.
