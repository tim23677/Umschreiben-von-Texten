#!/usr/bin/env python3
"""Descriptive prose diagnostics. No composite score and no authorship verdict."""
import json, re, statistics, sys

WATCH = {
    "stock phrases": ["in today's", "at its core", "it is important to note", "in conclusion", "great question", "i hope this helps"],
    "watched vocabulary": ["delve", "tapestry", "underscore", "showcase", "leverage", "foster", "utilize", "facilitate", "groundbreaking"],
}
TRANSITIONS = {"moreover", "furthermore", "additionally", "consequently", "therefore", "overall", "ultimately"}
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")
SENT = re.compile(r'[^.!?]*[.!?]+["\')\]]?|\S[^.!?]*$', re.S)

def analyze(text):
    sents = [m.group().strip() for m in SENT.finditer(text) if m.group().strip()]
    words = WORD.findall(text)
    lengths = [len(WORD.findall(s)) for s in sents]
    hits = {name: [p for p in phrases if p in text.lower()] for name, phrases in WATCH.items()}
    openers = [s for s in sents if (WORD.findall(s) and WORD.findall(s)[0].lower() in TRANSITIONS)]
    return {"words": len(words), "sentences": len(sents), "paragraphs": len([p for p in re.split(r"\n\s*\n", text) if p.strip()]),
            "mean_sentence_words": round(statistics.mean(lengths), 1) if lengths else 0,
            "sentence_length_cv": round(statistics.pstdev(lengths) / statistics.mean(lengths), 3) if len(lengths)>1 and statistics.mean(lengths) else 0,
            "transition_openers": openers, "watchlist_matches": hits,
            "limitations": "Descriptive prompts only. Matches are not defects and cannot establish authorship."}

def main():
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        print("Usage: prose_stats.py FILE [--json]", file=sys.stderr); return 2
    text = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    data = analyze(text)
    if "--json" in sys.argv[1:]: print(json.dumps(data, indent=2))
    else:
        for key, value in data.items(): print(f"{key}: {value}")
        print("Review each item in context. No score or AI-authorship conclusion is produced.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
