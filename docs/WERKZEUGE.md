# Werkzeug-Register

Stand der zwölf Werkzeuge, die für dieses Repo vorgesehen waren. Spalte „Status" sagt, was im Repo liegt und was nur lokal installiert wird.

| Nr. | Werkzeug | Lizenz | Status | Wo / wie |
|---|---|---|---|---|
| 1 | Matt-Komiske/humanizer | keine im Repo angegeben | nicht eingebaut | Lokale Web-App mit rund 15 GB Modellen und eingebauten KI-Detektoren. Ohne Lizenz darf der Code nicht kopiert werden. Zweck (Detektor-Scores) widerspricht den Repo-Regeln. |
| 2 | TextHumanize | unbekannt | nicht eingebaut | Der Link `github.com/TextHumanize` führt auf kein Repo (nur ein Name, keine Projekt-URL). Bitte konkrete `owner/repo`-URL nennen. |
| 3 | lynote-ai/humanize-text | MIT | nicht eingebaut | Übersetzungsketten (ZH→JA→FI→EN) und Detektor-Rückkopplung. Das verändert Inhalte und optimiert gegen Detektoren, beides verbietet `CLAUDE.md`. |
| 4 | hannsxpeter/humanizer | MIT | **eingebaut** | `.agents/skills/humanizer/references/merged/hannsxpeter-humanizer/`, in der Tabelle von `humanizer/SKILL.md` verlinkt. Eigener Skill wäre ein doppelter Trigger. |
| 5 | Meta TextSeal | – | nicht eingebaut | `facebookresearch/seal` ist ein anderes Projekt (Suchmaschine mit autoregressiven Sprachmodellen, archiviert, CC-BY-NC). Die korrekte TextSeal-URL fehlt. |
| 6 | AI Watermark Detector | unbekannt | nicht eingebaut | Link war nur `github.com/`. Konkrete URL nötig. Erkennen von Wasserzeichen wäre mit den Repo-Regeln vereinbar. |
| 7 | dewatermark | MIT (PyPI) | nicht eingebaut | Das Paket entfernt Herkunftsmarken aus Text und testet das Entfernen statistischer Wasserzeichen. Das widerspricht den Regeln. Ersatz: `scripts/hygiene_check.py` meldet nur unsichtbare Zeichen und ändert nichts. |
| 8 | LanguageTool | LGPL-2.1 | vorhanden | `scripts/lt_check.py`, Skills `proofread-audit` und `proofread-fix`. Server siehe `CLAUDE.md`. |
| 9 | Harper (Automattic) | Apache-2.0 | Anleitung | Nur Englisch, läuft offline. Nicht installiert, weil in der Sitzung nicht getestet. Installation: `cargo install harper-cli`, Aufruf: `harper-cli lint DATEI`. Für Deutsch bleibt LanguageTool. |
| 10 | LangCheck | MIT (PyPI) | Anleitung | Link war nur `github.com/`. Gemeint ist vermutlich das PyPI-Paket `langcheck` (Metriken für EN, JA, DE, ZH). Es dient der Bewertung von LLM-Ausgaben, nicht der Textprüfung für Menschen. Nicht eingebaut. |
| 11 | Vale | MIT | vorhanden | Skills `vale-setup`, `vale-fix`, `vale-triage`, `vale-vocab`, `vale-ci`. |
| 12 | WritingTools | GPL-3.0 | nicht eingebaut | Desktop-App mit Hotkeys, keine Kommandozeile. Ersetzt durch die Skills `humanizer`, `proofread-*`, `tighten`. GPL-Code wird nicht ins Repo kopiert. |

## Neu in diesem Stand

- `scripts/hygiene_check.py`: listet Zero-Width-Zeichen, Bidi-Steuerzeichen, weiche Trennstriche und ungewöhnliche Leerzeichen mit Zeile und Spalte. Nur lesend, kein Urteil über Autorschaft. Schritt 1 der Pipeline.
- Humanizer-Regeln von hannsxpeter als Regelquelle.

## Offene Fragen

Für 2, 5, 6 und 10 fehlen vollständige Repo-URLs. Mit ihnen lässt sich prüfen, ob Lizenz und Zweck zu den Repo-Regeln passen.
