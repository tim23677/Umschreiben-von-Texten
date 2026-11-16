#!/usr/bin/env python3
"""Check a text file with a LanguageTool server and print findings.

Reports spelling, grammar and punctuation problems for German and English.
It never changes the input file. Only the Python standard library is used.

Server: set LT_URL or pass --url. Default is http://localhost:8081/v2.
Start a local server (see https://dev.languagetool.org/http-server):
    java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081

The public API (https://api.languagetool.org/v2) is rate limited and sends the
text to a third party. Use it only when the text may leave the machine.

Exit codes: 0 no findings, 1 findings, 2 server or input error.
"""
import argparse
import bisect
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_URL = "http://localhost:8081/v2"
# Masked regions become spaces, which would trigger whitespace rules.
DEFAULT_DISABLED = ["WHITESPACE_RULE"]

CATEGORY_LABELS = {
    "TYPOS": "Rechtschreibung",
    "SPELLING": "Rechtschreibung",
    "GRAMMAR": "Grammatik",
    "PUNCTUATION": "Zeichensetzung",
    "COMMA_PARENTHESIS_WHITESPACE": "Zeichensetzung",
    "CASING": "Gross-/Kleinschreibung",
    "COMPOUNDING": "Zusammen-/Getrenntschreibung",
    "CONFUSED_WORDS": "Verwechselte Wörter",
    "TYPOGRAPHY": "Typografie",
    "STYLE": "Stil",
    "REDUNDANCY": "Stil",
    "SEMANTICS": "Bedeutung",
    "MISC": "Sonstiges",
}

MASK_PATTERNS = [
    re.compile(r"\A---\n.*?\n---\n", re.S),                       # front matter
    re.compile(r"^(```|~~~)[^\n]*\n.*?^\1[^\n]*$", re.S | re.M),  # code fences
    re.compile(r"`[^`\n]+`"),                                     # inline code
    re.compile(r"(?<=\])\([^)\n]*\)"),                            # link targets
    re.compile(r"https?://[^\s)>\]]+"),                           # bare URLs
    re.compile(r"<[^>\n]+>"),                                     # HTML tags
]


def mask_markup(text):
    """Blank out code, URLs and tags with spaces; offsets stay unchanged."""
    def blank(match):
        return "".join(c if c == "\n" else " " for c in match.group())

    for pattern in MASK_PATTERNS:
        text = pattern.sub(blank, text)
    return text


def chunk_text(text, limit):
    """Split on blank lines into (offset, chunk) pairs of at most `limit` chars."""
    chunks, start, pos = [], 0, 0
    for match in re.finditer(r"\n\s*\n", text):
        end = match.end()
        if end - start > limit and pos > start:
            chunks.append((start, text[start:pos]))
            start = pos
        pos = end
    if start < len(text):
        # A single oversized paragraph is cut at line breaks as a last resort.
        rest = text[start:]
        offset = start
        while len(rest) > limit:
            cut = rest.rfind("\n", 0, limit)
            cut = cut + 1 if cut > 0 else limit
            chunks.append((offset, rest[:cut]))
            offset += cut
            rest = rest[cut:]
        chunks.append((offset, rest))
    return [(o, c) for o, c in chunks if c.strip()]


def call_server(url, chunk, args):
    fields = {
        "text": chunk,
        "language": args.lang,
        "level": args.level,
        "disabledRules": ",".join(DEFAULT_DISABLED + args.disable),
    }
    if args.lang == "auto":
        fields["preferredVariants"] = "de-DE,en-US"
    if args.enable:
        fields["enabledRules"] = ",".join(args.enable)
    data = urllib.parse.urlencode(fields).encode("utf-8")
    request = urllib.request.Request(
        url.rstrip("/") + "/check",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(request, timeout=args.timeout) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("file", help="text or Markdown file, or - for stdin")
    parser.add_argument("--lang", default="auto",
                        help="auto (default), de-DE, de-AT, de-CH, en-US, en-GB ...")
    parser.add_argument("--url", default=os.environ.get("LT_URL", DEFAULT_URL),
                        help="LanguageTool API base URL (env LT_URL)")
    parser.add_argument("--level", choices=["default", "picky"], default="default")
    parser.add_argument("--disable", action="append", default=[], metavar="RULE_ID",
                        help="rule id to switch off (repeatable)")
    parser.add_argument("--enable", action="append", default=[], metavar="RULE_ID",
                        help="rule id to switch on (repeatable)")
    parser.add_argument("--no-mask", action="store_true",
                        help="check code, URLs and tags too (default: skip them)")
    parser.add_argument("--max-chunk", type=int, default=15000,
                        help="max characters per request (public API limits to 20000)")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--json", action="store_true", help="print findings as JSON")
    args = parser.parse_args()

    try:
        raw = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"error: cannot read input: {exc}", file=sys.stderr)
        return 2

    text = raw.replace("\r\n", "\n")
    checked = text if args.no_mask else mask_markup(text)
    line_starts = [0] + [m.end() for m in re.finditer(r"\n", text)]

    findings = []
    try:
        for offset, chunk in chunk_text(checked, args.max_chunk):
            result = call_server(args.url, chunk, args)
            detected = (result.get("language", {}).get("detectedLanguage", {}) or {}).get("code") \
                or result.get("language", {}).get("code", "")
            for match in result.get("matches", []):
                start = offset + match["offset"]
                length = match["length"]
                line_no = bisect.bisect_right(line_starts, start)
                col = start - line_starts[line_no - 1] + 1
                rule = match.get("rule", {})
                category = rule.get("category", {}).get("id", "MISC")
                findings.append({
                    "line": line_no,
                    "column": col,
                    "offset": start,
                    "length": length,
                    "matched": text[start:start + length],
                    "language": detected,
                    "category": CATEGORY_LABELS.get(category, category),
                    "rule": rule.get("id", ""),
                    "message": match.get("message", ""),
                    "replacements": [r["value"] for r in match.get("replacements", [])[:5]],
                })
    except (urllib.error.URLError, OSError, ValueError) as exc:
        print(
            f"error: LanguageTool server not reachable at {args.url} ({exc}).\n"
            "Start one, for example:\n"
            "  java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081\n"
            "or set LT_URL. No check was performed.",
            file=sys.stderr,
        )
        return 2

    findings.sort(key=lambda f: f["offset"])
    if args.json:
        json.dump(findings, sys.stdout, ensure_ascii=False, indent=2)
        print()
    elif not findings:
        print("No findings.")
    else:
        for f in findings:
            suggestion = " | ".join(f["replacements"]) or "-"
            print(f"L{f['line']}:{f['column']} [{f['category']}] {f['rule']} "
                  f"«{f['matched']}» {f['message']} -> {suggestion}")
        print(f"\n{len(findings)} finding(s).")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
