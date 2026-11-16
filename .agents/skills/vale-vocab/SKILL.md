---
name: vale-vocab
description: "Trägt Projektbegriffe in ein Vale-Vokabular ein, damit Vale.Spelling sie akzeptiert. Trigger: 'Vale kennt unseren Produktnamen nicht', 'stop flagging this word in Vale'. Nicht für Rechtschreibprüfung allgemein (dafür proofread-audit)."
license: MIT
origin: vale-cli/agent-tools
---

# Teach Vale a project's own words

> **Abgrenzung im Repo:** Vale ist der Stil- und Syntax-Linter für Markdown-Texte (Stilpakete sind überwiegend englisch). Rechtschreibung und Grammatik auf Deutsch und Englisch prüft `proofread-audit`, korrigiert `proofread-fix` (LanguageTool). KI-Muster prüft `ai-text-pattern-review`, Umschreiben macht `humanizer`.
> Herkunft: vale-cli/agent-tools (MIT), hier als eigenständiger Skill mit Präfix `vale-` übernommen; Hook und MCP-Server des Plugins sind nicht installiert.

## When to use this

`Vale.Spelling` is flagging terms that are spelled correctly for this
project — product names, APIs, jargon.

The alternative someone will otherwise reach for is disabling spell check
entirely, which stops checking every other word in the repository over one
proper noun.

## Prerequisites

1. `vale ls-config` resolves and shows a `StylesPath`.
2. The flagged terms really are the project's spelling. Check the docs or the
   product itself — the vocabulary becomes the reference everyone else follows.

## Workflow

**1. Collect the terms Vale is actually flagging**, rather than guessing:

```bash
vale --output=JSON <path> | jq -r '.[][] | select(.Check == "Vale.Spelling") | .Match' | sort | uniq -c | sort -rn
```

**2. Create the vocabulary.** It lives inside `StylesPath` but is the one part
of it that is yours and survives `vale sync`:

```
styles/config/vocabularies/<Project>/accept.txt
styles/config/vocabularies/<Project>/reject.txt
```

**3. Name it in `.vale.ini`:**

```ini
Vocab = <Project>
```

**4. Add one term per line** to `accept.txt`. Entries are case-sensitive
regular expressions, so `Kubernetes` accepts that spelling and not
`kubernetes` — usually what a project wants, because the casing is part of the
name.

**5. Use `reject.txt`** for terms the project has banned: an old product name,
a deprecated spelling. Rejected terms are flagged wherever they appear.

**6. Re-run** and report what is left.

**7. Commit the vocabulary.** Unlike the rest of `StylesPath`, it is source.

## Do not

- **Do not disable `Vale.Spelling`.** One unknown product name is not a reason
  to stop checking the repository.
- **Do not add a misspelling to `accept.txt`** to clear an alert. If the term is
  wrong, fix the prose.
- **Do not bulk-add every flagged token.** Read the list first; some of them
  are genuine typos, and that is the point of the rule.
