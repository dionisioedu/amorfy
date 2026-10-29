import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '_gen'))
import home

class HomeRecencyTest(unittest.TestCase):
    def test_new_article_overtakes_news_and_cases_without_image(self):
        common = dict(desc='Descrição', read_min=3, categories=[])
        articles = [dict(common, slug='old-news', title='Notícia antiga', date='2026-10-22', news=True),
                    dict(common, slug='new', title='Artigo novo', date='2026-10-30')]
        cases = [dict(common, slug='case', title='Caso', date='2026-10-29', image='/images/case.webp', tag='Caso')]
        with patch.object(home, 'CASES', cases), tempfile.TemporaryDirectory() as temp:
            items = home.catalog(articles, [])
            self.assertEqual([a['title'] for a in items], ['Artigo novo', 'Caso', 'Notícia antiga'])
            home.write_home(articles, [], temp)
            page = (Path(temp) / 'index.html').read_text(encoding='utf-8')
            hero = re.search(r'<article class="home-feature .*?</article>', page, re.S)[0]
            self.assertIn('Artigo novo', hero)
            self.assertIn('30/10/2026', hero)
            self.assertNotIn('src=""', hero)

    def test_published_highlights_follow_catalog_without_duplicates(self):
        page = (ROOT / 'index.html').read_text(encoding='utf-8')
        items = json.loads(re.search(r'<script id="home-catalog" type="application/json">(.*?)</script>', page, re.S)[1])
        dated = [a for a in items if a['date']]
        self.assertEqual([a['date'] for a in dated], sorted([a['date'] for a in dated], reverse=True))
        highlights = page.split('<div class="home-highlights">')[1].split('<section id="explorar"')[0]
        recent = page.split('<section id="recentes"')[1].split('</section>')[0]
        links = re.findall(r'href="([^"#]+\.html)"', highlights + recent)
        self.assertEqual(links, [a['url'] for a in dated[:9]])
        self.assertEqual(len(links), len(set(links)))
