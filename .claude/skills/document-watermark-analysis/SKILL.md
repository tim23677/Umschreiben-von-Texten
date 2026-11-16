---
name: document-watermark-analysis
description: Inspect user-owned TXT, Markdown, PDF, and DOCX documents for metadata, unusual Unicode, embedded items, and basic formatting issues; offer only non-destructive, provenance-preserving cleanup.
---

# Document watermark and metadata analysis

Use `python scripts/document_audit.py <file> --json` to produce a local structured report for a TXT, Markdown, PDF, or DOCX file. The script uses only the Python standard library and does not upload document contents.

## Safety boundaries

- Inspect only files the user owns or is authorized to process.
- This project provides **analysis**, not watermark/provenance removal. Never remove, alter, obscure, or advise bypassing AI provenance, C2PA/content credentials, signatures, authenticity labels, or authorship evidence.
- Never overwrite the source. Never claim that a negative heuristic result proves a document is watermark-free or human-authored.
- Report metadata; do not strip it. Metadata may be relevant provenance or evidence.
- Explain that visible-watermark detection is limited: there is no OCR or PDF renderer in this standard-library tool. DOCX embedded images and header/footer parts are inventoried, not interpreted visually.

## Available checks

- TXT/Markdown: unusual/invisible Unicode code points, trailing line whitespace, encoding and file hash.
- DOCX: ZIP integrity, core properties, paragraph counts, embedded image/object paths, headers/footers, and basic watermark-related text hints.
- PDF: readable Info dictionary fields, XMP/embedded-file/image indicators, and raw watermark-related text hints. Compressed/encrypted streams may not be fully inspectable.
- All findings are heuristic and should be presented as leads for human review, not definitive watermark detection.

## Optional safe cleanup

Offer cleanup only when the user confirms that a TXT/Markdown file is theirs and wants trailing spaces/tabs removed:

```bash
python scripts/document_audit.py draft.md --clean-copy draft.cleaned.md --json
```

This creates a separate output and `draft.cleaned.md.audit.json` log containing source/output SHA-256 hashes and the exact operation. It changes trailing line whitespace only. Invisible Unicode, metadata, watermarks, and provenance/authenticity information are preserved. DOCX and PDF cleanup is intentionally not implemented.

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```
