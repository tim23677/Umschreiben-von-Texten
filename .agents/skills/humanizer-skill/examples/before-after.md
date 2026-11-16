# Worked rewrites

Three complete examples. The source texts are invented, and every fact in each `Final` appears in its `Source`. No rewrite adds a number, name, citation, or claim. The pattern numbers refer to `../references/patterns.md`.

Diagnosis lists are what diagnose mode returns. Rewrite mode returns only the `Final` text.

## 1. Product blog introduction

Source

"Our new export pipeline takes four seconds instead of forty. The CSV still has nine columns. The nightly job no longer reads two databases. Two customers asked for it in Q1 and it shipped on Tuesday. This isn't just a faster way to get a report, it's a testament to what this team can achieve when we embrace a data-driven mindset. In today's fast-moving landscape, speed, reliability, and clarity are essential. We are thrilled to deliver seamless reporting that empowers every user to unlock actionable insights. And that changes everything."

Diagnosis

1. Pattern 1: "This isn't just a faster way to get a report, it's a testament to..." — the second half adds no fact.
2. Pattern 2: "And that changes everything." — a standalone closer that claims significance without evidence.
3. Pattern 6: "speed, reliability, and clarity" — a triad with no measurement behind two of its items.
4. Pattern 12: "testament", "mindset", "fast-moving landscape", "seamless", "actionable insights" — stock vocabulary.
5. Pattern 16: "We are thrilled to deliver... empowers every user to unlock" — sales register.
6. Pattern 13: "a new way to think about" and "changes everything" — inflated significance for a performance fix.

Final

Exports take four seconds instead of forty. The CSV still has nine columns, and the nightly job no longer reads two databases. Two customers asked for this in Q1; it shipped on Tuesday.

Preserved

Four seconds versus forty; nine columns; two databases; two customers in Q1; shipped Tuesday. The order of the facts stayed as the source had them.

## 2. Support reply

Source

"Hi Ana, great question! Here's the thing: as you know, our ticketing system was introduced in 2019 to replace a shared inbox, and over the years we added labels, automations, and an API. Many teams ask us about data portability, and it's worth noting that exports matter a great deal when you are migrating. So, to answer your question: yes, you can export to CSV from Settings > Export > CSV, and the file includes closed tickets from the last 90 days. Hope this helps! Let me know if you need anything else."

Diagnosis

1. Pattern 24: the answer arrives after 70 words of background the customer already has.
2. Pattern 3: "Here's the thing:" stages the reply.
3. Pattern 23: "it's worth noting that exports matter a great deal" describes the importance of the topic instead of answering.
4. Pattern 22: "great question!", "Hope this helps!", "Let me know if you need anything else" are chat wrappers.
5. Pattern 9: "matter a great deal" is an unmeasured qualifier.

Final

Hi Ana,

Yes. Settings > Export > CSV includes closed tickets from the last 90 days. Many teams ask about exports when they migrate. Our ticketing system replaced the shared inbox in 2019; labels, automations, and the API came later.

Preserved

The export path; CSV; closed tickets; the 90-day window; the 2019 shared-inbox history; labels, automations, and the API; the observation that many teams ask about data portability. Background moved behind the answer rather than being discarded, because those details are facts.

## 3. Research summary

Source

"Studies have shown that teams with clear documentation are significantly more productive, underscoring the pivotal role of knowledge sharing in the modern software landscape. The survey was distributed to 40 teams in 2025, and 12 of them reported having a written deploy checklist. These teams also reported fewer rollbacks, highlighting the importance of structured process documentation. It is worth noting that this marks a fundamental shift in how the industry thinks about reliability."

Diagnosis

1. Pattern 14: "Studies have shown" names no study. The draft's own survey measured checklists and rollbacks, not productivity.
2. Pattern 12: "pivotal role", "modern software landscape", "underscoring" — stock vocabulary.
3. Pattern 15: "highlighting the importance of structured process documentation" — a trailing clause that announces a lesson.
4. Pattern 13: "marks a fundamental shift in how the industry thinks about reliability" — historical weight for one survey.
5. Pattern 3: "It is worth noting that" stages the last sentence.

Final

In a 2025 survey of 40 teams, 12 reported having a written deploy checklist. Those 12 also reported fewer rollbacks.

Preserved

2025; 40 teams; 12 teams; written deploy checklist; fewer rollbacks. The association between the checklist and the rollbacks stays an association. It does not become a cause.

Removed with a reason

"Teams with clear documentation are significantly more productive" was cut under pattern 14. No study is named in the source, so `voice-and-facts.md` calls for cutting the claim or narrowing it to what the survey measured, not for inventing a citation. In diagnose mode this removal is reported; in rewrite mode it is silent.

## What a failed rewrite looks like

- Replacing "four seconds instead of forty" with "blazing fast" loses the measurement that made the sentence worth reading.
- Turning "12 of 40 teams" into "most teams" reverses the proportion.
- Changing "reported fewer rollbacks" into "the checklist reduced rollbacks" adds a causal claim the survey did not make.
- Keeping "And that changes everything" because it sounds like a strong ending leaves the most obvious tell in place.
- Swapping every stock word for a synonym while keeping the hollow contrast produces a cleaner-sounding draft with the same problem.
