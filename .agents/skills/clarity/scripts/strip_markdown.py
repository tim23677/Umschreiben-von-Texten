#!/usr/bin/env python3
"""Reduce Markdown to reader-facing prose for descriptive diagnostics."""
import re
import sys

def strip(text):
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^```.*?^```|^~~~.*?^~~~", "", text, flags=re.S | re.M)
    text = re.sub(r"^(?: {4}|\t).*$", "", text, flags=re.M)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^\s*\|.*$", "", text, flags=re.M)
    text = re.sub(r"^\s{0,3}#{1,6}\s+|^\s{0,3}>\s?|^\s{0,3}(?:[-*+] |\d+\. )", "", text, flags=re.M)
    text = re.sub(r"[*_~`]+", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

if __name__ == "__main__":
    raw = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 and sys.argv[1] != "-" else sys.stdin.read()
    sys.stdout.write(strip(raw))
