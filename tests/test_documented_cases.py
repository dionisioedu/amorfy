import html
import json
from pathlib import Path
import re
import sys
import unittest
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_gen'))
from documented_cases import CASES

class DocumentedCasesTest(unittest.TestCase):
    def test_sources_credit_assets_and_discovery(self):
        for case in CASES:
            with self.subTest(slug=case['slug']):
                url = '/casos/' + case['slug'] + '.html'
                page = (ROOT / url.lstrip('/')).read_text(encoding='utf-8')
                schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', page, re.S)[1])
                self.assertEqual(schema['citation'], case['sources'])
                self.assertEqual(schema['@type'], 'Article')
                self.assertIn('href="https://amorfy.com.br' + url + '"', page)
                for source in case['sources']:
                    self.assertIn('href="' + html.escape(source, quote=True) + '"', page)
                for field in ('url', 'license_url'):
                    self.assertIn(html.escape(case['image_credit'][field], quote=True), page)
                self.assertNotIn('Imagem ilustrativa criada com IA', page)
                self.assertNotIn('Nomes e detalhes foram alterados', page)
                self.assertIn('História pública documentada', page)
                self.assertEqual((ROOT / case['image'].lstrip('/')).read_bytes()[8:12], b'WEBP')
                for target in ('index.html', 'casos/index.html', 'sitemap.xml'):
                    self.assertIn(url, (ROOT / target).read_text(encoding='utf-8'))
                for link in re.findall(r'href="(/[^"#]*)', page):
                    path = ROOT / link.lstrip('/')
                    self.assertTrue(path.exists(), link)
