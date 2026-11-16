---
name: vale-ci
description: "Bindet Vale in GitHub Actions, pre-commit oder einen anderen Runner ein (advisory oder blockierend). Trigger: 'add vale to CI', 'Vale auf PRs ausführen', 'pre-commit hook für Vale'."
license: MIT
origin: vale-cli/agent-tools
---

# Put Vale in the pipeline

> **Abgrenzung im Repo:** Vale ist der Stil- und Syntax-Linter für Markdown-Texte (Stilpakete sind überwiegend englisch). Rechtschreibung und Grammatik auf Deutsch und Englisch prüft `proofread-audit`, korrigiert `proofread-fix` (LanguageTool). KI-Muster prüft `ai-text-pattern-review`, Umschreiben macht `humanizer`.
> Herkunft: vale-cli/agent-tools (MIT), hier als eigenständiger Skill mit Präfix `vale-` übernommen; Hook und MCP-Server des Plugins sind nicht installiert.

## When to use this

Vale runs locally and should now run automatically.

## Prerequisites

1. `vale ls-config` resolves, and a plain `vale <path>` run works locally. Do
   not wire up CI for a config that does not resolve — the failure will look
   like a CI problem.
2. The user has said whether the job should block. Ask if not.

## Advisory or blocking

**Only `error` sets a non-zero exit code.** Warnings and suggestions exit 0, so
a job wired up naively passes no matter how much it reports.

- **Advisory** — Vale reports, the job stays green. The right way to adopt Vale
  on a corpus that has never had it.
- **Blocking** — the rules the team cares about are set to `error` in the
  config, and the job fails on those.

Say which one you are setting up, in those words. "It runs in CI" tells nobody
whether it can stop a merge.

## GitHub Actions

```yaml
- uses: vale-cli/vale-action@reviewdog
  with:
    files: docs
```

Alerts arrive as review comments on the pull request, which is where a writer
will see them.

## pre-commit

```yaml
repos:
  - repo: https://github.com/vale-cli/vale
    rev: v3.17.0
    hooks:
      - id: vale
```

Pin `rev` to a release. Hooks that float break at the worst time.

## Any other runner

```bash
vale --no-global --output=line docs/
```

`--output=line` gives `path:line:col:rule:message`, which most CI systems can
turn into annotations. `--no-global` keeps a config on the machine from
changing the result.

If the runner has no cached `StylesPath`, `vale sync` has to run first — and
that means a style updating upstream can fail a build nobody changed. Pin
`Packages` to a release URL rather than a moving reference.

## Do not

- **Do not add `--no-exit` to make a failing job pass.** If those alerts should
  not block, change the levels in the config, where the decision is visible to
  the team.
- **Do not raise `MinAlertLevel` in CI only.** A config that reports different
  things locally and in CI is how people stop trusting the tool.
