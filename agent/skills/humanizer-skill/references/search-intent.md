# Search demand behind the trigger wording

Recorded on 2026-11-14. Source: one `keyword_ideas` call with `mode=suggestions`, `gl=us`, `hl=en`, `limit=50`, from the gefei keyword snapshot. Cost 8 credits. The call returned 50 suggestions; the snapshot reports 791 related terms for the seed set.

These are long-tail and autocomplete-style suggestions from a keyword snapshot, not a live scrape of Google's dropdown. Volume, 12-month trend, CPC, KD, and intent are the snapshot's own fields. Direct requests to Google's suggest endpoints from this machine return `http=000`, so no live dropdown data is claimed here.

## Head term

`humanize ai text` — 33,100 searches/month, KD 69, 12-month trend flat at -19%, intent informational. A broad head term with high difficulty. It belongs in the description as a phrase, but it does not describe a single job.

## Rows removed by hand

`online tools to humanize ai text` is labeled 18,100/month, but its monthly series runs 201,000 in 2025-11, drops to 10-20 afterwards, and reaches 0 in 2026-10. `humanize ai text converter` (-87%) and `free unlimited` show the same discontinuity. Treat these as stale or mis-attributed snapshot rows. Do not build copy or triggers on them.

## Four clusters

### 1. Free and word-count tools (largest, mostly falling)

`humanize ai text free` 6,600; `free humanize ai text` 4,400 (-31%); `humanize ai text free 1 000 words` 1,900 (+32%); `humanize ai text free 1000 words` 1,900 (same intent, different spelling); `free 5000 words` 480; `free unlimited` 390; `for free` 260 (-42%); `free online` 140 (-87%).

Intent: a hosted paste-in box with a paywall or word cap. A skill cannot serve the searcher's immediate need, so these words stay out of the `description`. The README explains the difference instead.

### 2. Method and how-to (growing)

`how to humanize ai text` 1,900 (-30%); `how to humanize ai generated text` 210 (+424%); `how to humanize ai-generated text` 210 (same intent); `how do you humanize ai generated text` 90 (+208%); `how to humanize ai text for free` 140 (+117%); `how can i humanize ai text` 140; `humanize ai-generated text` 260 (+51%).

Intent: the caller wants the actual edits, not a button. Core coverage. These phrasings feed the `description` and the workflow.

### 3. Reusable prompts (lowest difficulty)

`prompts to humanize ai text` 480 (KD 9); `prompt to humanize ai text` 480 (KD 9); `best prompt to humanize ai text` 140 (KD 3); `best prompts to humanize ai text` 140; `prompt to humanize ai text for academic writing` 90 (+52%).

Intent: a portable instruction set for the caller's own agent. This is exactly what an Agent Skill is, so it is the strongest fit in the sample. KD 3-9 is the lowest band here.

### 4. Tool comparison

`best tool to humanize ai text` 140 (+177%, CPC 18.66, KD 13); `best tools to humanize ai text` 140 (+177%); `apps to humanize ai text` 90 (+177%); `what is the best humanize ai text` 90 (+136%); `grammarly humanize ai text` 260 (+68%); `can grammarly humanize ai text` 140 (KD 5).

Intent: comparison with existing products. The README answers the Grammarly question directly. The skill does not claim to be a replacement for a grammar checker.

### Excluded: detector evasion

`humanize ai text undetectable` 590 (-86%); `humanize ai text and bypass ai detection` 210 (-87%); `ai detector humanize text` 110 (+192%, small base).

Demand is collapsing on the two main phrases. Independent of the numbers, the skill is for readers and must not be used to hide required disclosure of generated content. Do not add these phrases to `description`, README headings, install examples, or issue templates as goals.

## Normalization

Several rows are the same question with different punctuation or word order. Normalize them into one job before using them: the two `1000 words` spellings, the `ai generated` / `ai-generated` pair, singular/plural `prompt(s)`, and `best tool(s)`. One job gets one explanation in the README and one set of trigger phrases in the `description`. Do not create a pattern, mode, or FAQ entry per search string.

When these terms are used to plan web pages rather than a skill, they are a candidate pool, not a build list. Keyword-to-page rules belong to the site's own SEO specification and are out of scope here.

## Trigger phrases used

`humanize AI text`, `make AI writing sound human`, `remove AI tells`, `signs of AI writing`, `rewrite ChatGPT-sounding prose`, `rewrite Claude-sounding prose`, `prompts to humanize AI text`, `how to humanize AI-generated text`, `without changing the meaning`, `in my voice`.

Deliberately absent: `free`, `online`, `converter`, `unlimited`, `1000 words`, `5000 words`, `undetectable`, `bypass AI detection`.
