import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.document_audit import audit, clean_text_copy, inspect_text


class DocumentAuditTests(unittest.TestCase):
    def test_text_flags_but_preserves_invisible_characters(self):
        original = "hello\u200b world  \n".encode("utf-8")
        report = inspect_text(original)
        self.assertIn("U+200B", " ".join(report["invisible_or_unusual_characters"]))
        self.assertEqual(report["lines_with_trailing_spaces_or_tabs"], [1])

    def test_txt_audit_reports_hash_and_format(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "note.txt"
            path.write_text("hello\n", encoding="utf-8")
            report = audit(path)
            self.assertEqual(report["format"], "txt")
            self.assertEqual(len(report["sha256"]), 64)

    def test_docx_reports_metadata_and_images_without_modification(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "note.docx"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("docProps/core.xml", '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:creator>Example</dc:creator></cp:coreProperties>')
                archive.writestr("word/document.xml", '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>draft</w:t></w:r></w:p></w:body></w:document>')
                archive.writestr("word/media/image1.png", b"image")
            before = path.read_bytes()
            result = audit(path)["analysis"]
            self.assertEqual(result["metadata"]["creator"], "Example")
            self.assertEqual(len(result["embedded_images"]), 1)
            self.assertEqual(path.read_bytes(), before)

    def test_pdf_metadata_and_signature(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.pdf"
            path.write_bytes(b"%PDF-1.4\n1 0 obj << /Title (Sample) /Subtype /Image >> endobj")
            report = audit(path)["analysis"]
            self.assertEqual(report["metadata"]["Title"], "Sample")
            self.assertEqual(report["image_object_indicators"], 1)

    def test_cleanup_creates_copy_and_log_leaving_original_unchanged(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.md"
            output = Path(directory) / "cleaned.md"
            source.write_text("keep\u200b me  \n", encoding="utf-8")
            original = source.read_bytes()
            _, log_path, _ = clean_text_copy(source, output)
            self.assertEqual(source.read_bytes(), original)
            self.assertIn("\u200b", output.read_text(encoding="utf-8"))
            self.assertEqual(output.read_text(encoding="utf-8"), "keep\u200b me\n")
            log = json.loads(log_path.read_text(encoding="utf-8"))
            self.assertIn("provenance and authenticity information", log["preserved"])

    def test_cleanup_refuses_overwrite_and_non_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.txt"
            source.write_text("text  \n", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                clean_text_copy(source, source)
            docx = root / "file.docx"
            docx.write_bytes(b"not opened")
            with self.assertRaises(ValueError):
                clean_text_copy(docx, root / "out.docx")


if __name__ == "__main__":
    unittest.main()
