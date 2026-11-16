# AI writing patterns

24 patterns, ordered by how strongly they mark a text as generated. Sections 1 through 5 justify an edit on a single sighting. A pattern marked *weak alone* needs a companion tell in the same passage before it earns an edit, because careful writers use those forms on purpose.

Every example below is invented sample prose written for this file. The `After` lines show what a rewrite looks like when those specifics were already available in the source. When editing real text, never add a fact that is not there; see `voice-and-facts.md`.

Word habits change with every model release. Structural habits persist, so staging, rhythm by rule, and borrowed authority lead the list. A tell is stronger the less often a careful writer would produce it by choice.

## A. Posture instead of a fact (1-5)

### 1. Hollow contrast

Problem: "Not X but Y" and "isn't just X, it's Y" build weight without adding information. The second half is usually a mood, not a claim. Also appears split across two sentences.

Before: "This isn't just a faster way to export reports, it's a new way to think about what your team measures."

After: "Exports take four seconds instead of forty. The report has the same nine columns."

### 2. Dramatic one-line closer

Problem: A short standalone sentence at the end repeats the point and claims significance without evidence. Common forms: "And that changed everything.", "That's the real story.", "The rest is history."

Before: "The migration finished on Tuesday. And that changed everything."

After: "The migration finished on Tuesday, so the nightly job no longer has to read two databases."

### 3. Staged opener

Problem: A phrase announces that something important is coming instead of saying it. "Here's the thing:", "The truth is,", "Let's be clear:", "It turns out that".

Before: "Here's the thing: most teams never check the retry count."

After: "Most teams never check the retry count. Our logs show three retries per failed request."

### 4. Fake-profundity aphorism

Problem: A universal-sounding definition replaces the detail the reader needs. Often starts with "At its core", "In a world where", or "X is really about Y".

Before: "At its core, caching is really about trust."

After: "The cache holds a response for 60 seconds, so a stale price can show for up to a minute."

### 5. Arguing with a reader who is not there

Problem: Invents an objection and a group that holds it, then wins the argument. "You might think X. But." "Critics will say." "Power users know better."

Before: "You might think the free tier is enough. But serious teams know better."

After: "The free tier caps exports at 20 per month. The paid tier removes the cap."

## B. Mechanical rhythm (6-11)

### 6. Forced triad (*weak alone*)

Problem: Three parallel beats applied to a claim that only one or two facts support. Strongest when it happens in every section, or when the third item is an abstraction.

Before: "It's fast, reliable, and built for teams."

After: "Median response time is 120 ms. We had two outages this year, both under ten minutes."

### 7. Identical sentence openings (*weak alone*)

Problem: Consecutive sentences repeat the same subject or opener instead of combining the facts.

Before: "We tested it on Monday. We tested it again on Thursday. We found the same error both times."

After: "Monday's run and Thursday's run produced the same error."

### 8. Em dash as a universal connector (*weak alone*)

Problem: Dashes stand in for punctuation the writer did not choose, stacking asides inside a sentence that should have been two. Keep the writer's own dash rate; see `voice-and-facts.md`.

Before: "The build failed — again — and the logs — which nobody had read — pointed at the token — not the cache."

After: "The build failed again. Nobody had read the logs, which pointed at the expired token rather than the cache."

### 9. Stacked qualifiers

Problem: Hedges accumulate without naming what they qualify, leaving a claim that says almost nothing.

Before: "This can arguably generally be considered somewhat faster in many typical cases."

After: "In our 12 runs it was 8% faster. On files under 10 KB the difference disappeared."

### 10. Compound-adjective pileup (*weak alone*)

Problem: Hyphenated descriptors describe a mood, not a mechanism. Three or more in a row is the usual signal.

Before: "An AI-powered, end-to-end, data-driven workflow for frictionless cross-team collaboration."

After: "A shared queue assigns incoming requests to the next available reviewer."

### 11. Passive with no actor

Problem: Removes the person or system that did the thing, which is often the useful fact.

Before: "It was decided that the endpoint would be deprecated, and the change was communicated."

After: "The platform team deprecated the endpoint and emailed API customers on 3 March."

## C. Inflation and borrowed authority (12-18)

### 12. Stock AI vocabulary

Problem: Words such as testament, landscape, realm, tapestry, pivotal, robust, seamless, delve, underscore, leverage, and navigate appear when there is no specific fact to write. Check for them after the structural edits, not before.

Before: "This release is a testament to the team's commitment to navigating an ever-evolving landscape."

After: "This release fixes 14 bugs, including the duplicate invoice reported in #482."

### 13. Inflated significance

Problem: Assigns historical weight to a routine change. "Marks a turning point", "represents a fundamental shift", "changes how we think about".

Before: "The switch to weekly backups marks a turning point in how the industry thinks about durability."

After: "Backups now run weekly instead of monthly. A failure can lose up to seven days of data."

### 14. Vague attribution

Problem: "Studies show", "experts agree", "research suggests" borrow authority without naming a source. Fix by using the source that is actually present, or by narrowing the claim; do not invent a citation.

Before: "Studies show that teams with clear documentation are significantly more productive."

After: "In a 2025 survey of 40 teams, the 12 with a written deploy checklist reported fewer rollbacks."

### 15. Shallow -ing tail

Problem: A trailing clause announces a benefit or a lesson instead of stating it. "ensuring that", "highlighting the importance of", "allowing teams to".

Before: "We moved the job to 02:00, ensuring that reports are ready before standup and highlighting the value of scheduling."

After: "We moved the job to 02:00. Reports are ready before standup."

### 16. Sales register (*weak alone*)

Problem: Verbs that promise a feeling replace what the thing does. "Unlock", "empower", "effortless", "game-changing", "supercharge". May be deliberate in launch copy, so require a second tell.

Before: "Unlock effortless, game-changing insights and empower your team to win."

After: "The dashboard shows yesterday's signups by source. Export is one click."

### 17. Name-dropping

Problem: Borrowed visibility stands in for evidence. "As covered by leading outlets", "discussed across the industry", "featured by top publications".

Before: "As covered by leading outlets and discussed across the industry, the approach is gaining traction."

After: "Three customers asked for it in Q1. We shipped it in April."

### 18. Avoiding plain verbs

Problem: "Serves as", "stands as", "boasts", "plays a crucial role in" add length without adding meaning. A plain "is" or "has" is usually right.

Before: "The queue serves as the backbone of the pipeline and boasts sub-second latency."

After: "The queue holds jobs until a worker picks them up. Median wait is 300 ms."

## D. Formatting by habit (19-21)

### 19. Decorative bold

Problem: Bold on every label, or on mid-sentence phrases for emphasis that is not there. When everything is bold, nothing is. Also check bold on CLI flags and field names in docs.

Before: "**Fast setup:** one command. **Clear logs:** every request has an id. **Real support:** we answer in a day."

After: "Setup takes one command. Every request has an id in the log. Support replies within a day."

### 20. Decorative heading that restates the first line (*weak alone*)

Problem: The heading and the sentence under it say the same thing. A heading that names the fact saves a line; one that repeats it wastes one.

Before: "## Why Speed Matters" followed by "Speed matters because users wait less."

After: "## Latency" followed by "Median page load fell from 1.9 s to 0.8 s after the cache change."

### 21. Identical list shape (*weak alone*)

Problem: Every bullet is a bold label, a colon, and one sentence, eight times over, even where the items are not parallel. The shape comes from a template, not from the material.

Before: Eight bullets, each reading "**Label:** one sentence."

After: Two bullets for the two items that are genuinely parallel; the rest written as prose.

## E. Chat and drafting leftovers (22-23)

### 22. Conversational wrapper

Problem: Phrases addressed to the requester rather than the reader. "Sure!", "Here's a quick rewrite", "Hope this helps", "Let me know if you'd like anything else", knowledge-cutoff disclaimers, apologies for being an AI.

Before: "Sure! Here's the draft — hope this helps, and let me know if you want me to change anything!"

After: Cut the wrapper entirely. Keep the draft.

### 23. Writing about the document instead of the subject

Problem: Describes the reader's future experience with the text instead of giving the finding. "In this article, we will explore", "by the end you'll understand", "this section covers".

Before: "In this article, we will explore three ways to reduce churn, and by the end you will understand what worked for us."

After: "Churn fell from 6.1% to 4.8% after we added the cancellation survey. Two other changes did not move it."

## F. Written for the wrong reader (24)

### 24. Buried answer

Problem: Re-explains background the requester already supplied, then answers in the last line. Common in support replies and in chat drafts that were pasted into a document. Keep the background if it is a fact, but move the answer to the front.

Before: "As you know, our ticketing system was introduced in 2019 to replace a shared inbox, and over the years we added labels, automations, and an API. Many teams ask about data portability when they migrate, and exports matter a great deal in that situation. So, to answer your question: yes, you can export to CSV from Settings > Export > CSV, and the file includes closed tickets from the last 90 days."

After: "Yes. Settings > Export > CSV includes closed tickets from the last 90 days. Our ticketing system replaced the shared inbox in 2019; labels, automations, and the API came later."

## Five tells that survive a first rewrite

Search for these again at the end of step 3: 1 hollow contrasts, 2 dramatic closers, 6 forced triads, 8 em-dash chaining, 19 decorative bold. They tend to reappear in the summary paragraph even after the body has been fixed.
