---
name: claude-humanizer
description: Improve the clarity, tone, and individuality of Claude-generated or other prose without changing its meaning or making claims about detector outcomes.
---

# Claude humanizer

This is an editorial skill for improving text, including drafts produced with Claude. It does not conceal provenance, establish authorship, or guarantee a detector result.

## Workflow

1. Identify the reader, purpose, medium, language, and requested level of formality.
2. Preserve the author's meaning, facts, uncertainty, attribution, terminology, and constraints.
3. Remove generic openings, repeated transitions, empty emphasis, redundant summaries, and phrasing that obscures the point, but only where they are actually unhelpful.
4. Use supplied examples or prior writing to match the author's voice. Do not fabricate opinions, memories, anecdotes, or imperfections.
5. Keep useful structure and technical or academic conventions. Do not vary sentence lengths mechanically.
6. Check the revision against the source for meaning drift.

Return the revised text and a concise change note. If the user asks for an audit only, report observations without rewriting. Do not optimize against AI detectors or claim the text is now human-written.
