import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
class ClinicalPostsTest(unittest.TestCase):
    def test_new_posts_have_sources_assets_and_valid_links(self):
        files = list((ROOT / '_gen/studies').glob('*.json')) + [p for p in (ROOT / '_gen/cases').glob('*.json') if json.loads(p.read_text(encoding='utf-8'))['date'] == '2026-11-03']
        for path in files:
            a = json.loads(path.read_text(encoding='utf-8'))
            section = 'casos' if a.get('documented') else 'artigos'
            page = (ROOT / section / (a['slug']+'.html')).read_text(encoding='utf-8')
            schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)[1])
            self.assertEqual(schema['citation'], a['sources'])
            self.assertIn('content="image/webp"', page)
            self.assertIn('criada com IA', page)
            self.assertEqual((ROOT / a['image'].lstrip('/')).read_bytes()[8:12], b'WEBP')
            ids = set(re.findall(r'id="([^"]+)"', page))
            for link in re.findall(r'href="([^"]+)"', page):
                if link.startswith('#'): self.assertIn(link[1:], ids)
                elif link.startswith('/'):
                    self.assertTrue((ROOT / link.split('#')[0].lstrip('/')).exists(), link)
            for target in ('index.html', 'sitemap.xml'):
                self.assertIn(a['slug'], (ROOT / target).read_text(encoding='utf-8'))
