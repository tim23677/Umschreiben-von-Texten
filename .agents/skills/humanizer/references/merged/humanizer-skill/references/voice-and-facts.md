# Voice and fact preservation

Load this file when a writing sample is supplied, or when the draft contains numbers, citations, quotations, or a sequence of events. Patterns are preferences; facts and voice are requirements.

## Reading a writing sample

A sample overrides `references/patterns.md`. Work through it in this order before editing anything.

1. Count sentence lengths. Note the shortest and longest sentence and whether short ones cluster at the ends of paragraphs.
2. Look at punctuation. Record how often the writer uses em dashes, semicolons, parentheses, colons, and fragments. Reproduce that rate; do not erase a habit that is theirs.
3. Look at paragraph openings. Some writers start with a claim, some with a date, some with a question, some with "We". Match the mix.
4. Note person and distance: I / we / you / the reader / passive. Do not introduce "we" into a writer who uses "I".
5. Collect their exact terms for recurring things. If they say "customer" and not "user", keep "customer". Do not swap in a more polished synonym.
6. Note what they do not do. A writer who never uses bold, never writes one-line paragraphs, or never opens with a question is giving a negative constraint too.
7. Check register markers: contractions, hedging, numbers in words or digits, whether they cite sources inline.
8. If the sample and the draft disagree, ask which voice the result should use. Do not average them into a third voice.

When no sample exists, keep the draft's existing person and terminology. Changing those is a rewrite of identity, not an edit of style.

## Fact-preservation checklist

Compare the final text against the source item by item. A missing or altered item is an error even when the prose reads better.

1. Names of people, teams, products, files, and places, including spelling and capitalization.
2. Every number: counts, percentages, dates, times, versions, prices, durations. Watch for rounding and for "about" becoming an exact figure.
3. Negation. "No longer", "not supported", "never" are easy to drop when a sentence is compressed.
4. Qualifiers and scope: "in our tests", "on US accounts", "as of March", "up to". Removing one turns a limited claim into a universal one.
5. Comparisons and their direction. "Faster than X" must not become "fast".
6. Citations, links, and link targets. Keep the URL and keep what the citation is said to support.
7. Quotations, word for word. Paraphrasing a quote is a fact change.
8. Sequence and simultaneity. "A then B" and "A while B" are different claims. Compressing two events into one sentence loses this most often.
9. Attribution. "The support team reported" is not the same as "we found".
10. Uncertainty. "May", "we think", "unconfirmed" must survive.

Two failure modes recur. The first is a smooth sentence that quietly promotes an estimate to a measurement. The second is a rewritten list that keeps all the items but changes their order, which matters when the order is chronological or by priority. Check both explicitly.

If a pattern fix would require a detail the source does not contain, choose one of these: ask for the detail, cut the claim, or write a shorter sentence that says less. Do not fill the gap with plausible-sounding specifics.

## Register notes

- **Academic.** Keep hedging and citations intact. Vague attribution such as "studies show" is not fixed by inventing a study; either the source names one or the claim is narrowed to what the source can support. Preserve technical terms even when they sound formal.
- **Blog and newsletter.** The opening sentence carries the piece. Cut staged openers and put the concrete finding first. A personal aside is voice, not an AI tell, so keep it unless it is a template aside.
- **Marketing copy.** Superlatives may be deliberate. Flag them as weak-alone patterns; do not flatten a launch announcement into a changelog unless the writer asks for that. Keep product names and claims exactly.
- **Email and support.** Answer in the first line. Chat wrappers at the end go. Keep every instruction and deadline. "Let me know if that helps" is optional only when the writer added it, not when the recipient needs a next step.
- **README and documentation.** Code, commands, paths, and frontmatter are out of scope. Prose around them can be tightened. Watch for decorative bold on CLI flags and for headings that restate the line below them.
- **Release notes and changelogs.** Facts dominate. Fix stock vocabulary and inflated significance, keep every version number, date, and issue reference.

## Other languages

The patterns are written from English prose, but the structural ones travel: hollow contrasts, dramatic closers, forced triads, decorative formatting, and buried answers appear in machine-generated text in many languages.

Chinese drafts have habits this list does not name. Look for `首先 / 其次 / 最后` applied to any three points, `值得注意的是`, `总的来说` as a paragraph closer, `综上所述`, stacked abstractions such as `赋能 / 抓手 / 闭环 / 底层逻辑`, three parallel four-character phrases, and a summary sentence at the end of every paragraph. Handle them the same way: restate the point, cut the staging, keep the facts. If the writer's sample uses these forms deliberately, keep them.

## When to stop and ask

- The draft contains a statistic, quote, or citation with no visible source and the rewrite would need to keep it verbatim.
- Two possible readings of a sentence lead to different facts.
- The text is legal, medical, financial, or safety guidance where a softened qualifier changes the meaning.
- The request is to make generated text appear human-authored for a submission with a disclosure rule.

In each case, return the question instead of a plausible rewrite. Silence on a fact is better than a confident invention.
