"""Publication integrity for the clinical reading series."""
import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent

class TechnicalPostsTest(unittest.TestCase):
    def test_series_order_and_published_links(self):
        posts = sorted((json.loads(p.read_text(encoding="utf-8")) for p in (ROOT / "_gen/technical").glob("*.json")), key=lambda a: a["publication_order"])
        self.assertTrue(posts)
        self.assertLessEqual(len(posts), 9)
        self.assertEqual([a["publication_order"] for a in posts], list(range(1, len(posts)+1)))
        for i, a in enumerate(posts):
            self.assertEqual(a["categories"], [["borderline", "narcisismo", "autoestima"][i % 3]])
            page = (ROOT / "artigos" / (a["slug"] + ".html")).read_text(encoding="utf-8")
            ids = set(re.findall(r'id="([^"]+)"', page))
            for href in re.findall(r'href="([^"]+)"', page):
                if href.startswith("#"):
                    self.assertIn(href[1:], ids)
                elif href.startswith("/"):
                    path = ROOT / href.split("#")[0].split("?")[0].lstrip("/")
                    self.assertTrue(path.exists(), str(path))
            schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)[1])
            self.assertEqual(schema["@type"], "Article")
            self.assertEqual(schema["citation"], [r["url"] for r in a["references"]])
            self.assertEqual(schema["inLanguage"], "pt-BR")
            self.assertIn("audience", schema)
            self.assertIn('content="image/png"', page)
            for field in ("image", "social_image"):
                self.assertTrue((ROOT / a[field].lstrip("/")).exists())
            self.assertIn(a["slug"], (ROOT / "sitemap.xml").read_text())

    def test_home_preserves_same_day_publication_order(self):
        page = (ROOT / "index.html").read_text(encoding="utf-8")
        items = json.loads(re.search(r'<script id="home-catalog" type="application/json">(.*?)</script>', page, re.S)[1])
        series = [a for a in items if a.get("publication_order", 0)]
        orders = [a["publication_order"] for a in series]
        self.assertTrue(orders)
        self.assertEqual(orders, sorted(orders, reverse=True))
