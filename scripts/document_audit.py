#!/usr/bin/env python3
"""Read-only audit for TXT/Markdown, PDF, and DOCX documents.

This tool reports metadata and possible anomalies. It does not detect AI authorship,
remove watermarks, or alter provenance/authenticity information. Its only cleanup
operation creates a separate TXT/Markdown copy with trailing line whitespace removed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import xml.etree.ElementTree as ET

MAX_FILE_BYTES = 50 * 1024 * 1024
SUPPORTED = {".txt", ".md", ".markdown", ".pdf", ".docx"}
WATERMARK_HINTS = (b"watermark", b"confidential", b"draft", b"sample")
CORE_NS = {"dc": "http://purl.org/dc/elements/1.1/", "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def inspect_text(data: bytes) -> dict[str, Any]:
    text = data.decode("utf-8-sig", errors="replace")
    unusual: Counter[str] = Counter()
    examples: list[dict[str, Any]] = []
    for pos, char in enumerate(text):
        category = __import__("unicodedata").category(char)
        if category == "Cf" or (category == "Cc" and char not in "\n\r\t") or char == "\u00a0":
            label = f"U+{ord(char):04X} ({__import__('unicodedata').name(char, 'unnamed')})"
            unusual[label] += 1
            if len(examples) < 100:
                examples.append({"character": label, "offset": pos})
    lines = text.splitlines()
    trailing = [index for index, line in enumerate(lines, 1) if line.rstrip(" \t") != line]
    return {
        "encoding": "UTF-8 (replacement characters may indicate invalid byte sequences)",
        "characters": len(text),
        "lines": len(lines),
        "invisible_or_unusual_characters": dict(unusual),
        "character_examples_first_100": examples,
        "lines_with_trailing_spaces_or_tabs": trailing,
        "cleanup_note": "Invisible characters are reported, never removed.",
    }


def inspect_docx(data: bytes) -> dict[str, Any]:
    with zipfile.ZipFile(__import__("io").BytesIO(data)) as archive:
        bad_member = archive.testzip()
        names = archive.namelist()
        result: dict[str, Any] = {
            "package_integrity": "ok" if bad_member is None else f"CRC error: {bad_member}",
            "embedded_images": [name for name in names if name.startswith("word/media/")],
            "headers_and_footers": [name for name in names if re.fullmatch(r"word/(?:header|footer)\d+\.xml", name)],
            "embedded_objects": [name for name in names if name.startswith("word/embeddings/")],
            "metadata": {},
            "formatting_findings": [],
        }
        if "docProps/core.xml" in names:
            root = ET.fromstring(archive.read("docProps/core.xml"))
            for node in root:
                value = (node.text or "").strip()
                if value:
                    result["metadata"][node.tag.rsplit("}", 1)[-1]] = value
        if "word/document.xml" in names:
            root = ET.fromstring(archive.read("word/document.xml"))
            paragraphs = root.findall(".//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p")
            result["paragraph_count"] = len(paragraphs)
            result["empty_paragraphs"] = sum(
                not "".join(node.itertext()).strip() for node in paragraphs
            )
            result["watermark_related_text_hints"] = [
                hint.decode("ascii") for hint in WATERMARK_HINTS
                if hint in archive.read("word/document.xml").lower()
            ]
        return result


def inspect_pdf(data: bytes) -> dict[str, Any]:
    if not data.startswith(b"%PDF-"):
        raise ValueError("File extension is PDF but the PDF signature is missing.")
    metadata: dict[str, str] = {}
    for key in (b"Title", b"Author", b"Subject", b"Creator", b"Producer", b"CreationDate", b"ModDate"):
        match = re.search(rb"/" + key + rb"\s*\(([^)]{0,2048})\)", data)
        if match:
            metadata[key.decode("ascii")] = match.group(1).decode("latin-1", errors="replace")
    hints = [hint.decode("ascii") for hint in WATERMARK_HINTS if hint in data.lower()]
    return {
        "metadata": metadata,
        "has_xmp_metadata_stream": b"/Metadata" in data,
        "embedded_file_indicators": data.count(b"/EmbeddedFiles"),
        "image_object_indicators": len(re.findall(rb"/Subtype\s*/Image\b", data)),
        "raw_content_watermark_text_hints": hints,
        "limitations": [
            "PDF text and visual watermark detection is heuristic without a PDF renderer/OCR.",
            "Compressed, encrypted, or object-stream metadata may not be visible to this stdlib-only scan.",
        ],
    }


def audit(path: Path) -> dict[str, Any]:
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED:
        raise ValueError(f"Unsupported format {suffix or '(no extension)'}; supported: {', '.join(sorted(SUPPORTED))}")
    data = path.read_bytes()
    if len(data) > MAX_FILE_BYTES:
        raise ValueError(f"File is larger than the {MAX_FILE_BYTES // (1024 * 1024)} MiB safety limit.")
    report: dict[str, Any] = {
        "file": str(path),
        "format": suffix.lstrip("."),
        "size_bytes": len(data),
        "sha256": sha256(data),
        "analysis": {},
        "provenance_policy": "No watermark, provenance, or authenticity marker is removed or modified.",
    }
    if suffix in {".txt", ".md", ".markdown"}:
        report["analysis"] = inspect_text(data)
    elif suffix == ".docx":
        report["analysis"] = inspect_docx(data)
    else:
        report["analysis"] = inspect_pdf(data)
    return report


def clean_text_copy(source: Path, destination: Path) -> tuple[Path, Path, dict[str, Any]]:
    if source.resolve() == destination.resolve():
        raise ValueError("Output must be a different path; the original is never overwritten.")
    if source.suffix.lower() not in {".txt", ".md", ".markdown"}:
        raise ValueError("Safe formatting cleanup is currently limited to TXT and Markdown.")
    raw = source.read_bytes()
    if len(raw) > MAX_FILE_BYTES:
        raise ValueError("Input exceeds the 50 MiB safety limit.")
    text = raw.decode("utf-8-sig")
    cleaned = "\n".join(line.rstrip(" \t") for line in text.splitlines())
    if text.endswith(("\n", "\r")):
        cleaned += "\n"
    output_data = cleaned.encode("utf-8")
    log_path = Path(str(destination) + ".audit.json")
    if destination.exists() or log_path.exists():
        raise FileExistsError("Output or audit log already exists; choose unused paths.")
    log = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source": str(source),
        "source_sha256": sha256(raw),
        "output": str(destination),
        "output_sha256": sha256(output_data),
        "changes": ["Removed trailing spaces and tabs at line ends only."],
        "preserved": ["Invisible Unicode characters", "document metadata", "watermarks", "provenance and authenticity information"],
    }
    try:
        with destination.open("xb") as stream:
            stream.write(output_data)
        with log_path.open("x", encoding="utf-8") as stream:
            json.dump(log, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    except Exception:
        destination.unlink(missing_ok=True)
        log_path.unlink(missing_ok=True)
        raise
    return destination, log_path, log


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path, help="TXT, Markdown, PDF, or DOCX file to inspect")
    parser.add_argument("--json", action="store_true", help="print a structured JSON report")
    parser.add_argument("--clean-copy", type=Path, metavar="OUTPUT", help="create a separate TXT/Markdown copy with trailing line whitespace removed, plus an audit log")
    args = parser.parse_args(argv)
    try:
        report = audit(args.file)
        if args.clean_copy:
            destination, log_path, log = clean_text_copy(args.file, args.clean_copy)
            report["cleanup"] = log
            report["cleanup"]["output"] = str(destination)
            report["cleanup"]["audit_log"] = str(log_path)
        if args.json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(f"document audit error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
