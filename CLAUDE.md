# Text-Werkzeugkasten: Skills und Workflow

Dieses Repo bündelt Skills zum Prüfen, Korrigieren, Umschreiben und Kürzen von Texten (Deutsch und Englisch). Die Skills liegen in `.agents/skills/`, `.claude/skills/` verlinkt sie für Claude Code. `_archive/` enthält nur Verpackungs-Metadaten und wird nicht gelesen.

## Pipeline (Reihenfolge für perfekte Texte)

```
Entwurf -> Grammatik/Syntax-Check -> KI-Audit -> Humanize -> Kürzen -> Schluss-Check
```

| Schritt | Aufgabe | Skill | Ändert den Text? |
|---|---|---|---|
| 0 | Entwurf, Gliederung | `skeleton`, `persona-write`, `write` (technische Doku) | ja, neuer Text |
| 1a | Rechtschreibung, Grammatik, Zeichensetzung prüfen (DE/EN) | `proofread-audit` | nein |
| 1b | Eindeutige Fehler minimal korrigieren | `proofread-fix` | ja, nur Fehler |
| 1c | Stil und Syntax von Markdown mit Linter | `vale-fix`, `vale-triage`, `vale-vocab` (Einrichtung: `vale-setup`, `vale-ci`) | `vale-fix` ja, die anderen nein |
| 2 | KI-Muster prüfen | `ai-text-pattern-review` | nein |
| 3 | Umschreiben, damit der Text nicht nach KI klingt | `humanizer` (allgemein) oder `humanizer-for-paper-writing` (wissenschaftlich) | ja |
| 4 | Kürzen und Straffen | `kuerzen` (DE), `shorten` und `tighten` (EN), `abrege` (FR), `abrevia` (ES), `abbrevia` (IT), `escurca` (CA), `sokrati` (RU) | ja |
| 5 | Schluss-Check, weil Schritt 3 und 4 neue Fehler einführen können | `proofread-audit`, dann bei Bedarf `proofread-fix` | nein / ja |

Nur Feedback ohne Änderung: `critique`. Klarheit und Lesbarkeit messen: `clarity`.

## Prüfen oder Ändern? (strikte Trennung)

- **Nur prüfen:** `proofread-audit`, `ai-text-pattern-review`, `critique`, `vale-triage`
- **Nur Fehler beheben, Wortlaut bleibt:** `proofread-fix`, `vale-fix`
- **Aktiv umschreiben oder kürzen:** `humanizer`, `humanizer-for-paper-writing`, `kuerzen`, `shorten`, `tighten` und die Sprachvarianten

## Allgemein oder wissenschaftlich?

- Allgemeine und redaktionelle Texte: `humanizer`
- Paper, Experimentberichte, Design-Dokumente: `humanizer-for-paper-writing`
- Gliederung, Zitation, Reviewer-Antworten: `academic-writing`; Paper lesen: `paper-companion`

## Werkzeuge einrichten

**LanguageTool** (für `proofread-audit` und `proofread-fix`). Ein lokaler Server muss laufen:

```bash
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

Das Skript `scripts/lt_check.py` nutzt `LT_URL` (Standard `http://localhost:8081/v2`). Die öffentliche API `https://api.languagetool.org/v2` sendet Text an einen Dritten und ist begrenzt. Sie wird nur mit ausdrücklicher Erlaubnis genutzt. Ist kein Server erreichbar, sagen die Skills das offen und prüfen nicht heimlich anders.

**Unsichtbare Zeichen** prüft `python3 -I scripts/hygiene_check.py DATEI` (nur lesend, Exit 1 bei Funden).

**Vale** (für `vale-*`). Das Programm `vale` muss installiert sein, Einrichtung über `vale-setup`. Hook und kostenpflichtiger MCP-Server aus `vale-cli/agent-tools` sind bewusst nicht installiert.

## Regeln für alle Skills

- Fakten, Zahlen, Namen, Zitate und Quellen nie ändern.
- Keine Optimierung gegen KI-Detektoren, kein Urteil über Autorschaft, keine erfundenen Details.
- Originale nicht überschreiben: im Git-Repo arbeiten, damit `git diff` jede Änderung zeigt.

## Pflege

- Neue Skills nach `.agents/skills/<name>/` legen und in `.claude/skills/` verlinken (`ln -s ../../.agents/skills/<name> .claude/skills/<name>`).
- Beim Anlegen oder Ändern einer Beschreibung prüfen, dass kein anderer Skill denselben Trigger hat. Beschreibungen bleiben unter 1024 Zeichen.
- Die zusammengeführten Humanizer-Regeln stehen unter `.agents/skills/humanizer/references/merged/`.
- `skills-lock.json` hält die Quellen der installierten Skills. Lokal angepasste Beschreibungen (zum Beispiel bei `humanizer`, `tighten`, `shorten`, `kuerzen`, `critique`, `academic-writing`) nicht per `skills update` überschreiben lassen.

- Welche externen Werkzeuge eingebaut sind und welche nicht (mit Begründung): `docs/WERKZEUGE.md`.
