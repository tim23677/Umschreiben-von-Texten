---
name: proofread-fix
description: "Korrigiert eindeutige Rechtschreib-, Grammatik- und Zeichensetzungsfehler (Deutsch und Englisch) minimal und lässt Wortlaut, Stil und Markup unangetastet. Nutzt LanguageTool. Trigger: 'Rechtschreibfehler korrigieren', 'Fehler beheben ohne umzuschreiben', 'Kommas korrigieren', 'korrigiere nur die Fehler', 'fix the typos', 'correct grammar without rewriting'. Nur Berichten ohne Änderung: proofread-audit. Umformulieren oder Kürzen: humanizer, kuerzen, shorten, tighten. Vale-Fehler: vale-fix."
license: MIT
---

# Rechtschreibung und Grammatik korrigieren (minimal)

Dieser Skill behebt **nur Fehler**. Er formuliert nichts um. Wer den Text verbessern, straffen oder natürlicher machen will, braucht einen anderen Skill (siehe unten).

## Abgrenzung

| Aufgabe | Skill |
|---|---|
| Fehler finden, nichts ändern | `proofread-audit` |
| Eindeutige Fehler korrigieren, Wortlaut bleibt | **proofread-fix** (dieser) |
| Markdown-Linter-Fehler beheben | `vale-fix` |
| Umschreiben, Stil, KI-Muster entfernen | `humanizer` |
| Kürzen und Straffen | `kuerzen`, `shorten`, `tighten` |

## Ablauf

1. **Arbeitskopie.** Hochgeladene Dateien nie im Original ändern, sondern eine Kopie bearbeiten. Im Git-Repo direkt am Text arbeiten, damit `git diff` die Änderungen zeigt.
2. **Prüfen.** Wie in `proofread-audit`, aber maschinenlesbar:

   ```bash
   python3 -I scripts/lt_check.py DATEI --lang auto --json
   ```

   Exit-Code 2 heißt: kein LanguageTool erreichbar. Dann abbrechen und das sagen. Ohne Prüfergebnis nichts "aus dem Gefühl" ändern.
3. **Sortieren.** Jeden Fund einer von drei Gruppen zuordnen:

   | Gruppe | Bedingung | Aktion |
   |---|---|---|
   | **Anwenden** | Kategorie Rechtschreibung, Grammatik, Zeichensetzung, Groß-/Kleinschreibung oder Zusammen-/Getrenntschreibung **und** genau ein plausibler Vorschlag **und** kein Eigenname, Zitat oder Fachbegriff | korrigieren |
   | **Offen lassen** | mehrere mögliche Vorschläge, Bedeutung könnte kippen, Stil- oder Typografie-Hinweis | im Bericht auflisten, nicht ändern |
   | **Fehlalarm** | Eigenname, Produktname, Zitat, Absicht erkennbar | nicht ändern, auf Wörterbuch oder `--disable` hinweisen |

4. **Anwenden.** Von hinten nach vorn arbeiten (größter `offset` zuerst), damit die Positionen der übrigen Funde stimmen. Vor jeder Änderung prüfen, dass an der Stelle wirklich `matched` steht. Nur die betroffenen Zeichen ändern. Zeilenumbrüche, Einrückung, Listen, Links, Code und Satzzeichen außerhalb des Fundes bleiben.
5. **Gegenprobe.** `lt_check.py` erneut laufen lassen. Es dürfen keine neuen Funde durch die Korrektur entstanden sein. Verbleibende Funde gehören in die Gruppen "Offen" oder "Fehlalarm".
6. **Bericht.** Kurz und konkret:

   ```
   Korrigiert: 7   Offen: 3   Fehlalarme: 2
   Zeile 7 — "ein Bruch" → "einen Bruch" — OBJECT_AGREEMENT
   Zeile 7 — "ware" → "wäre" — GERMAN_SPELLER_RULE
   Offen: Zeile 12 — "das/dass" (zwei Lesarten), bitte entscheiden
   ```

## Harte Grenzen

- **Kein Umformulieren.** Kein Wort austauschen, nur weil es besser klingt. Keine Sätze zusammenlegen oder trennen.
- **Keine Fakten, Zahlen, Namen, Zitate oder Quellenangaben ändern.** Auch nicht, wenn sie falsch aussehen. Das melden, nicht beheben.
- **Zitate und wörtliche Rede bleiben, wie sie sind**, außer der Nutzer sagt ausdrücklich etwas anderes.
- **Variante beibehalten.** Deutsch in der Schweiz, Österreich oder Deutschland und britisches oder amerikanisches Englisch nicht vermischen.
- **Keine Regel abschalten**, nur damit eine Prüfung sauber aussieht.
- Wenn mehr als etwa jeder zehnte Satz betroffen ist, vor dem Anwenden nachfragen. Das ist dann eher ein Umschreibauftrag.
