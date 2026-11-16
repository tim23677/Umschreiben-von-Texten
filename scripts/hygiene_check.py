#!/usr/bin/env python3
"""Report invisible and unusual Unicode characters in text files. Read-only.

Finds zero-width characters, bidi controls, soft hyphens, exotic spaces and
BOMs. It never changes a file and makes no statement about who wrote the text:
such characters come from copy-paste, word processors and web pages as often
as from anything else.

Usage: hygiene_check.py FILE [FILE ...]   (use - for stdin)
Exit codes: 0 nothing found, 1 findings, 2 input error.
"""
import sys
import unicodedata

# Characters that carry meaning in some scripts (ZWNJ/ZWJ in Persian, Hindi, emoji).
CONTEXTUAL = {0x200C, 0x200D}
SUSPECT_SPACES = {0x00A0, 0x2007, 0x202F, 0x3000} | set(range(0x2000, 0x200B))


def classify(cp):
    ch = chr(cp)
    cat = unicodedata.category(ch)
    if cp == 0xFEFF:
        return "BOM/ZWNBSP"
    if cp == 0x00AD:
        return "weicher Trennstrich"
    if cp in CONTEXTUAL:
        return "ZWNJ/ZWJ (kann in Emoji/Schrift nötig sein)"
    if cp in (0x200B, 0x2060):
        return "Zero-Width-Zeichen"
    if 0x202A <= cp <= 0x202E or 0x2066 <= cp <= 0x2069 or cp in (0x200E, 0x200F):
        return "Bidi-Steuerzeichen"
    if cp in SUSPECT_SPACES:
        return "ungewöhnliches Leerzeichen"
    if cat == "Cf":
        return "Format-Steuerzeichen"
    if cat == "Cc" and ch not in "\n\r\t":
        return "Steuerzeichen"
    return None


def scan(name, text):
    n = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        for col, ch in enumerate(line, 1):
            label = classify(ord(ch))
            if label:
                n += 1
                print(f"{name}:{lineno}:{col}: U+{ord(ch):04X} {label}")
    return n


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    total = 0
    for path in argv:
        try:
            text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError) as exc:
            print(f"{path}: {exc}", file=sys.stderr)
            return 2
        total += scan("stdin" if path == "-" else path, text)
    print(f"{total} Fund(e)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
