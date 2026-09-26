"""Verify portable generation without changing the checked-in site."""
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent


class GenerationTest(unittest.TestCase):
    def test_generation_from_another_directory_preserves_published_content(self):
        with tempfile.TemporaryDirectory(prefix="amorfy-generation-") as temp:
            subprocess.run(
                [sys.executable, "-B", str(ROOT / "_gen/build.py"), "--output", temp],
                cwd=temp, check=True, capture_output=True,
            )
            pages = list(Path(temp).rglob("*.html"))
            self.assertEqual(len(pages), 25)
            for page in pages:
                relative = page.relative_to(temp)
                with self.subTest(page=str(relative)):
                    generated = page.read_text(encoding="utf-8")
                    published = (ROOT / relative).read_text(encoding="utf-8")
                    self.assertEqual(html.unescape(generated), html.unescape(published))
                    for block in re.findall(
                        r'<script type="application/ld\+json">(.*?)</script>', generated, re.S
                    ):
                        json.loads(block)
                    if relative.parts[0] == "casos":
                        self.assertIn('href="/casos/#conte-sua-historia"', generated)


if __name__ == "__main__":
    unittest.main()
