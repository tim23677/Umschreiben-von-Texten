---
name: ai-text-pattern-review
description: "Prüft einen Text rein lesend auf beobachtbare Sprach- und Strukturmuster, die oft in generierter Prosa auftreten (Deutsch und Englisch). Ändert nichts, vergibt keinen Detektor-Score und urteilt nicht über Autorschaft. Trigger: 'KI-Muster prüfen', 'klingt das nach KI', 'AI audit', 'check for AI tells (report only)'. Zum Umschreiben: humanizer (allgemeine Texte) oder humanizer-for-paper-writing (wissenschaftliche Texte). Rechtschreibung und Grammatik: proofread-audit."
---

# AI text pattern review

Use this skill when someone asks whether a text has formulaic or generic writing patterns. This is a qualitative editorial review, not an authorship detector. A pattern can occur in human writing; its absence does not prove human authorship.

## Procedure

1. Read the full text and identify its language, genre, intended audience, and length.
2. Note concrete, contextual examples of repetition, stock transitions, generic claims, over-regular structure, vague attribution, or unsupported specificity.
3. Distinguish observations from interpretation. Quote only enough to locate each pattern and explain a possible reader impact.
4. Include features that are specific or effective, and note when genre conventions explain a repeated form.
5. State limitations: style alone cannot establish whether Claude or another model wrote the text. Do not assign a probability, score, or binary verdict.
6. Offer an ordinary clarity/voice edit if wanted; do not optimize for detector results.

## Output

Give a short overview, then a table with `Passage`, `Observable pattern`, and `Editorial note`. End with limitations. If no meaningful pattern is evident, say so without calling the text human-written.

## Abgrenzung (Repo-Pipeline)

Dieser Skill ist der **Prüfschritt für KI-Muster** und ändert nie den Text. Er ersetzt den früheren Audit-Modus von `no-ai-slop`, `humanize` und `claude-humanizer`.

| Aufgabe | Skill |
|---|---|
| Rechtschreibung, Grammatik, Zeichensetzung | `proofread-audit`, `proofread-fix` |
| Umschreiben allgemeiner Texte | `humanizer` |
| Umschreiben wissenschaftlicher Texte | `humanizer-for-paper-writing` |
| Kürzen | `kuerzen`, `shorten`, `tighten` |

## Musterquellen

Zum Benennen von Mustern bei Bedarf nachschlagen, nicht vollständig laden:

- `../humanizer/references/patterns.md`: 55 Muster mit Auslösern und Beispielen
- `../humanizer/references/merged/humanize/references/ai-slop-tells.md` und `editing-checklists.md`
- `../humanizer/references/merged/humanize-writing/references/ai-tells.md`
- `../humanizer/references/merged/unslop/RULES.md`: Kontextprüfung statt Phrasenliste

Für diesen Skill gilt nur der Prüfteil. Die Fix-Hinweise in diesen Quellen als Vorschlag formulieren, nicht ausführen. Keinen Score vergeben, auch wenn eine Quelle einen vorsieht.

## Deutsche Auffälligkeiten (Heuristik, keine Beweise)

Diese Formen fallen in deutschen Texten oft auf. Jede kann in Menschentexten vorkommen und zählt nur in Häufung oder ohne Funktion:

- Stehende Einstiege und Schlüsse: "In der heutigen schnelllebigen Welt", "Es ist wichtig zu beachten", "Zusammenfassend lässt sich sagen"
- Reihung von drei Gliedern, durchgehend gleich gebaute Absätze und Listen
- "nicht nur ..., sondern auch ..." und "Es geht nicht um X, sondern um Y" als Dauerform
- Aufgeblasene Bedeutung: "spielt eine entscheidende Rolle", "ein Zeugnis von", "wegweisend", "nahtlos"
- Partizipialanhänge ohne Inhalt: ", wodurch ... unterstrichen wird", ", was ... verdeutlicht"
- Vage Quellen: "Studien zeigen", "Experten sind sich einig" ohne Beleg
- Auffällig viele Gedankenstriche, Doppelpunkte vor Aufzählungen und fett gesetzte Schlagwörter
- Chatbot-Reste: "Gerne!", "Ich hoffe, das hilft", "Hier ist eine überarbeitete Version"
