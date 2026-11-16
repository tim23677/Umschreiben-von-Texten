# Humanizer Skill

An [Agent Skill](https://agentskills.io/specification) that rewrites AI-sounding prose so it reads like the person who asked for it, without changing any of its facts. One `SKILL.md` file, no build step, no account, no upload.

It works in Claude Code, Claude.ai, Claude Desktop, WorkBuddy, Codex, Gemini CLI, GitHub Copilot, Cursor, Windsurf, and any other agent that reads a `SKILL.md` from a skills directory.

## What it does

Give it a draft that sounds like a chatbot and ask for a rewrite. It finds 24 specific habits, redrafts the prose around its actual meaning, then checks that no name, number, date, quote, or sequence of events changed. It can also diagnose a draft without rewriting it, edit a single file in place, or write fresh prose that avoids the habits from the start.

The habits are grouped in six families in [`references/patterns.md`](references/patterns.md): staged importance instead of facts, mechanical rhythm, inflated claims and stock vocabulary, decorative formatting, chat leftovers, and prose written for the wrong reader. Each one has a short explanation and a before/after pair. Voice matching and the fact-by-fact check are documented in [`references/voice-and-facts.md`](references/voice-and-facts.md).

## Who this is for

The wording in the skill's `description` comes from a 2026-11-14 snapshot of English search demand in the US. See [`references/search-intent.md`](references/search-intent.md) for the numbers. Four groups of requests showed up:

1. People who want the method: "how to humanize AI text", "how to humanize AI-generated text", "how can I humanize AI text". This group grew in the snapshot, with `how to humanize ai generated text` up 424% over 12 months.
2. People who want a reusable prompt: "prompts to humanize AI text", "best prompt to humanize AI text", "prompt to humanize AI text for academic writing". These had the lowest keyword difficulty in the sample, between 3 and 9.
3. People with a specific genre: essays, academic writing, blog posts, marketing copy, emails, README files, support replies, and documentation.
4. People comparing tools: "best tool to humanize AI text", "Grammarly humanize AI text", "can Grammarly humanize AI text".

A skill is a good fit for the first three. It is a poor fit for someone searching for a paste-in web box with a word counter, and it is not built for "bypass AI detection" requests. Those two cases are explained below.

## How this differs from a web humanizer

Web humanizers take pasted text, apply one transformation, and return it. Most have a free tier with a word cap; the snapshot contains searches such as `humanize ai text free 1000 words` (1,900/month) and `free 5000 words` (480/month). If that is the job, use one of those sites.

This skill runs inside the agent that is already editing the files. There is no word limit and no third-party service sees the text. It reads a writing sample if one is supplied, keeps the rest of the file untouched, and can be applied to the same project repeatedly. It also works on structured files: `edit in place` mode changes only prose, leaving code, data, frontmatter, and link targets alone.

Grammarly and similar tools check grammar, tone, and correctness. This skill checks for generated-prose habits. They solve different problems and can be used together.

## Install

Pick the agent in use. The repository root is the skill directory, so the `SKILL.md` stays at the top level in every case.

1. **Claude Code, via marketplace**

   ```
   /plugin marketplace add rockyandtom/humanizer-skill
   /plugin install humanizer-skill@humanizer-skill
   ```

2. **Claude Code, manually**: clone or copy this directory into `~/.claude/skills/humanizer-skill/`.

3. **Claude.ai and Claude Desktop**: zip this directory and upload it under Settings → Skills, or use the Skills API.

4. **WorkBuddy**: copy this directory into `~/.workbuddy/skills/humanizer-skill/`. The `agent_created: true` frontmatter field lets WorkBuddy manage the skill. Other agents ignore unknown frontmatter fields.

5. **Any agent supported by the `skills` CLI**: `npx skills add rockyandtom/humanizer-skill --agent '*'`. To list what it detects first, run `npx skills add rockyandtom/humanizer-skill --list`.

6. **Anything else**: copy `SKILL.md` plus the `references/` and `examples/` directories into that agent's skills folder. There are no platform-specific scripts or paths.

7. **OpenAI-compatible agents**: `agents/openai.yaml` supplies a display name and a default prompt. Codex and similar tools can read it or ignore it.

The plugin manifests under `.claude-plugin/` and `.cursor-plugin/`, and `package.json`, exist only so those loaders can find the root `SKILL.md`. They contain no instructions.

## Use

Ask in plain English. The `description` field is what triggers the skill, so phrases like "humanize this", "make this sound human", "remove the AI tells", "rewrite this ChatGPT draft", or "prompts to humanize AI text" all point at it.

1. Rewrite: `Humanize this introduction. Keep the three figures and the customer quote.`

2. Diagnose only: `List the AI tells in this draft. Do not rewrite it.`

3. Match a voice: `Here is a sample of my writing: <sample>. Rewrite the attached post in that voice.`

4. Edit a file: `Humanize the prose in docs/onboarding.md. Leave the code blocks and frontmatter unchanged.`

5. Write fresh: `Write a 200-word release note for the 1.4.2 fix, avoiding stock AI phrasing.`

The default output is the finished prose with no commentary. Diagnose mode returns a numbered list of pattern numbers, short quotes, and one-line reasons. Full examples with what was preserved are in [`examples/before-after.md`](examples/before-after.md).

## What it fixes

- "This isn't just a faster export, it's a new way to think about measurement" becomes the actual timing and the actual columns.
- "Fast, reliable, and built for teams" becomes the latency and the outage count.
- "A testament to navigating an ever-evolving landscape" becomes the 14 bugs that were fixed.
- "Here's the thing" and "Hope this helps" disappear.
- A reply that spends 200 words on background before answering "yes" starts with the answer.

## What it will not do

- It will not add facts, statistics, quotes, or citations that are not in the source. When a rewrite needs one, it asks or writes a simpler sentence.
- It will not help pass AI-detection tools. Searches for `humanize ai text undetectable` fell 86% and `humanize ai text and bypass ai detection` fell 87% in the same snapshot. The skill is for readers, and it should not be used where disclosure of generated content is required.
- It will not optimize keyword density, insert search terms, or write link anchors. Those are separate tasks with separate rules.
- It will not change code, data, frontmatter, link targets, citations, proper names, or quoted speech.
- It will not flatten a writer's voice. A supplied sample overrides the pattern list, including its use of dashes and short paragraphs.

## Compatibility

The skill follows the [Agent Skills standard](https://agentskills.io/specification): `SKILL.md` with `name` and `description` in YAML frontmatter, optional `license` and `metadata`, and progressive loading of `references/`. It uses no tool calls, no scripts, and no absolute paths. `name` matches the directory name `humanizer-skill`, which is what strict loaders check.

Version `1.0.0` lives in `metadata.version` and is repeated in the plugin manifests. `package.json` deliberately has no `version` field because pi-style installers read from git.

## Repository layout

1. `SKILL.md` — the prompt. Guardrails, the four-step workflow, output modes, and pointers to the references.
2. `references/patterns.md` — the 24 numbered tells, strongest first, with problem, before, and after.
3. `references/voice-and-facts.md` — reading a writing sample, the fact-preservation checklist, and register notes by genre.
4. `references/search-intent.md` — the search-demand snapshot behind the trigger wording and the intents deliberately excluded.
5. `examples/before-after.md` — three complete rewrites with diagnosis and preservation notes.
6. `.claude-plugin/`, `.cursor-plugin/`, `agents/openai.yaml`, `package.json` — thin discovery metadata for loaders.
7. `LICENSE`, `CHANGELOG.md` — MIT license and release notes.

## FAQ

**Is this an AI text humanizer?** It is an instruction set for an agent, not a hosted service. It does the same editing job, but it runs locally and has no word cap.

**Does it change the meaning of the content?** It is written not to. Step 3 of the workflow is a fact-by-fact comparison against the source, and dropping a claim is treated as an error.

**Should the output still be edited?** Yes, by the person who owns the text. The skill cannot know whether a claim is true; it can only keep the one that was there.

**Is using it good for SEO?** Search engines judge the published page, not which editor produced it. Removing filler and putting the answer earlier tends to help readers. This skill does not do keyword work.

**Does it work with Claude, or only with one agent?** The same folder works across agents. It was checked against the Agent Skills specification and the loader manifests in this repository; there is no Claude-specific code.

**Is there a word limit?** No. Very long documents are best handled section by section so the fact check stays reliable.

**Where do the trigger phrases come from?** A keyword snapshot, not live Google autocomplete. The method, prompt, and volume figures are recorded in `references/search-intent.md` with the dirty rows called out.

## Contributing

Open an issue with a before/after pair and the pattern number it belongs to. New patterns need a reason the existing 24 do not already cover them. Keep `SKILL.md` and `README.md` in sync when a pattern is added, renumbered, or removed, and add a `CHANGELOG.md` line for any behavior change. Keep install instructions neutral across agents.

## Credits and license

MIT. See [`LICENSE`](LICENSE).

The pattern-family idea owes a debt to [blader/humanizer](https://github.com/blader/humanizer) (MIT), which showed that a single skill file can serve many agents. The patterns, examples, workflow, and demand analysis in this repository were written independently for this project.

This is an independent community project. It is not affiliated with Anthropic, OpenAI, Google, Microsoft, or any other agent vendor. Product names above refer to compatibility only.
