---
name: ai-text-pattern-review
description: Review a supplied draft for observable language and structure patterns sometimes associated with generated prose. Never infer authorship or provide a detector score.
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
