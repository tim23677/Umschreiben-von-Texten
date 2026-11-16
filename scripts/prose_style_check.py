#!/usr/bin/env python3
"""Flag possible prose habits for human review; this is not an AI detector."""
import re
import sys
from pathlib import Path

PATTERNS = {
    "stock transition": r"\b(furthermore|moreover|additionally|in conclusion|overall)\b",
    "generic framing": r"\b(in today's (?:world|landscape)|at its core|it is important to note|it is worth noting)\b",
    "chatbot residue": r"\b(great question|I hope this helps|let me know if you need|certainly!)\b",
    "inflated phrasing": r"\b(plays a crucial role|serves as a testament|pivotal moment|groundbreaking|seamless(?:ly)?)\b",
    "decorative clause": r",\s*(?:highlighting|underscoring|showcasing|fostering)\b",
}


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} FILE", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        print(exc, file=sys.stderr)
        return 2
    found = False
    for number, line in enumerate(lines, 1):
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, line, re.IGNORECASE):
                found = True
                print(f"{number}: {label}: {match.group(0)} | {line.strip()}")
    if not found:
        print("No listed patterns found. This is not evidence of human authorship.")
    else:
        print("Review matches in context; they are style prompts, not authorship evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
