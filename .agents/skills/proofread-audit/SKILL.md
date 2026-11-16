---
name: proofread-audit
description: "Prüft Rechtschreibung, Grammatik und Zeichensetzung (Deutsch und Englisch) mit LanguageTool und berichtet nur, ohne den Text zu verändern. Trigger: 'Rechtschreibung prüfen', 'Grammatik prüfen', 'Kommafehler suchen', 'Tippfehler finden', 'spellcheck', 'check grammar', 'proofread this (report only)'. Zum Korrigieren stattdessen proofread-fix; Stil-/Syntax-Lint von Markdown macht vale-fix; KI-Muster prüft ai-text-pattern-review; Umschreiben macht humanizer."
license: MIT
---

# Rechtschreibung und Grammatik prüfen (nur Bericht)

Dieser Skill markiert Fehler und ändert **nie** den Text. Er ist der Prüfschritt vor und nach dem Umschreiben.

## Abgrenzung

| Aufgabe | Skill |
|---|---|
| Fehler finden, nichts ändern (Deutsch, Englisch) | **proofread-audit** (dieser) |
| Eindeutige Fehler minimal korrigieren | `proofread-fix` |
| Markdown-Stil und -Syntax mit Linter | `vale-fix`, `vale-triage` |
| KI-typische Muster markieren | `ai-text-pattern-review` |
| Text umschreiben oder kürzen | `humanizer`, `kuerzen`, `shorten`, `tighten` |

## Ablauf

1. **Eingabe klären.** Datei oder eingefügter Text. Sprache nur angeben, wenn sie nicht erkennbar ist (`de-DE`, `de-AT`, `de-CH`, `en-US`, `en-GB`). Gemischte Dokumente funktionieren mit `auto`.
2. **LanguageTool befragen.** Eingefügten Text zuerst in eine temporäre Datei schreiben, dann:

   ```bash
   python3 -I scripts/lt_check.py DATEI --lang auto
   ```

   Optionen: `--level picky` (strenger), `--disable REGEL_ID` (Regel abschalten), `--json` (maschinenlesbar), `--no-mask` (Code und URLs mitprüfen). Standardmäßig überspringt das Skript Front Matter, Codeblöcke, Inline-Code, URLs, Link-Ziele und HTML-Tags.
3. **Server.** Das Skript nutzt `LT_URL`, sonst `http://localhost:8081/v2`. Lokal starten:

   ```bash
   java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
   ```

   Die öffentliche API (`https://api.languagetool.org/v2`) sendet den Text an einen Dritten und ist begrenzt. Nur nutzen, wenn der Nutzer das für diesen Text ausdrücklich erlaubt.
4. **Exit-Code 2 heißt: keine Prüfung gelaufen.** Das offen sagen. Nicht so tun, als wäre geprüft worden. Nur wenn der Nutzer es möchte, eine manuelle Durchsicht anbieten und sie klar als "ohne LanguageTool" kennzeichnen.
5. **Bericht schreiben.** Nach Schwere gruppieren, nicht nach Reihenfolge der Regel-IDs:
   - Rechtschreibung (Tippfehler, falsche Wörter)
   - Grammatik (Kongruenz, Fall, Zeit)
   - Zeichensetzung (Komma, Anführungszeichen)
   - Sonstiges (Typografie, Stil-Hinweise von LanguageTool)

   Je Fund: `Zeile:Spalte`, markierte Stelle, kurze Erklärung, Korrekturvorschlag. Am Ende die Zahlen und eine Zeile, ob `proofread-fix` sinnvoll ist.

## Beurteilen, nicht nur weiterreichen

LanguageTool irrt sich. Vor dem Bericht jeden Fund prüfen und als **wahrscheinlich Fehler**, **unsicher** oder **vermutlich Fehlalarm** einstufen. Typische Fehlalarme:

- Eigennamen, Produktnamen, Fachbegriffe, Abkürzungen
- bewusste Mundart, Zitate, Beispielsätze mit Fehlern, Lyrik
- Anglizismen und Denglisch in Fachtexten
- Regeln, die Stil statt Fehler betreffen

Fehlalarme nicht verschweigen, sondern kennzeichnen und anbieten, die Regel mit `--disable` abzuschalten.

## Nicht tun

- Keine Datei verändern, auch keine "kleinen" Korrekturen.
- Keine Fakten, Zahlen oder Zitate bewerten. Es geht nur um Sprache.
- Kein Urteil über Autorschaft oder KI-Herkunft des Textes.
- Keine Funde erfinden, wenn das Skript nichts liefert. Dann: "Keine Funde."
