---
name: unslop
description: "Use when revising reader-facing text to remove generic or formulaic phrasing while preserving meaning, facts, and the author's voice. This is an editorial aid, not an AI detector."
tags: [human-writing, natural-language, ai-tells, editing, rewrite]
origin: ericrisco/rsc-harness
---

# unslop: revise prose for real readers

Use this skill to review or revise text intended for another person: emails, posts, documentation, messages, landing pages, and similar prose. Focus on the fit between the text, its reader, and its context. This skill does not determine who wrote a text and does not promise a detector result.

## Find the source

If the user pasted text, work on it. If they ask to revise the previous answer, use that answer. If they ask for new copy, draft it from the supplied brief. Ask for the text only when no source exists.

## Editorial pass

1. **Preserve the payload.** Keep names, facts, numbers, links, commitments, constraints, uncertainty, quotations, and necessary warnings. Never invent evidence, opinions, anecdotes, or certainty to make the prose flow.
2. **Match the context.** Use the user's language and fit the audience, relationship, and channel. Natural writing can still be formal or technical.
3. **Remove unnecessary scaffolding.** Cut throat-clearing, needless recaps, repeated conclusions, corporate filler, fake enthusiasm, and headings or bullets that do not help navigation.
4. **Use a natural cadence.** Prefer concrete verbs and direct sentences where they improve clarity. Do not manufacture slang, typos, fragments, or informality.
5. **Audit specific patterns.** Name an issue only when you can point to it in the text and explain why it hurts the intended reader.
6. **Rewrite locally.** Preserve meaning, facts, links, and intended tone. Do not replace every occurrence of a watched word mechanically.
7. **Read once more.** Check that the edit has not made the text sterile, changed a fact, or flattened the author's voice.

## Patterns worth checking in context

- Inflated importance: “pivotal moment,” “testament to,” or “plays a key role” without a concrete result.
- Decorative participial clauses such as “highlighting,” “ensuring,” or “showcasing” that add no supported claim.
- Vague attribution such as “experts believe” or “studies show” without naming a source.
- Repeated stock transitions, forced lists of three, or synonym cycling where one precise term would do.
- Filler such as “in order to,” “it is important to note,” or “at the end of the day.”
- Generic chatbot phrases such as “I hope this helps” when they add nothing.
- Repeated sentence or paragraph shapes that make the piece harder to follow.
- Unnecessary bolding, decorative emoji, or headings inconsistent with the requested format.

These are prompts to review, not a blacklist. Keep a phrase when it is accurate, useful, required by the medium, or part of the author's voice.

## Do not

- Claim that a text is AI-written or human-written based on style.
- Score or optimize text for an AI detector, or promise that it will pass one.
- Add fake personal experience, opinions, facts, sources, metrics, or anecdotes.
- Add errors or awkwardness to make prose appear human.
- Rewrite code, commands, URLs, quotations, or regulated wording unless explicitly requested.
- Flatten the writer's chosen voice or change technical meaning for stylistic variety.

## Output

For an audit-only request, report concrete patterns and locations; do not rewrite unless asked. For an edit, return the complete revised text and a concise note about material changes. Keep commentary outside the text the user may copy.
