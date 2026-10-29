"""Technical reading series, ordered independently from filename sorting."""
import json
import math
import re
from html import escape, unescape
from pathlib import Path
ROOT = Path(__file__).resolve().parent
ARTICLES = sorted([json.loads(p.read_text(encoding='utf-8')) for p in (ROOT / 'technical').glob('*.json')], key=lambda a: a['publication_order'])
for article in ARTICLES:
    body = article['body']
    headings = []
    def heading(match):
        ident = 'secao-' + str(len(headings) + 1)
        headings.append((ident, match[1]))
        return f'<h2 id="{ident}">{match[1]}</h2>'
    body = re.sub(r'<h2>(.*?)</h2>', heading, body)
    refs = '<h2 id="referencias">Referências comentadas</h2><ol>' + ''.join(f'<li id="ref-{i}"><a href="{escape(r["url"], quote=True)}">{escape(r["label"])}</a>. {escape(r["note"])}</li>' for i,r in enumerate(article['references'],1)) + '</ol>'
    series = '<nav class="study-series" aria-label="Série de estudos clínicos"><h2>Série: personalidade e autoestima</h2><p>Percurso alternado: borderline → narcisismo → autoestima. Leituras já publicadas:</p><ol>' + ''.join(f'<li><a href="/artigos/{a["slug"]}.html"' + (' aria-current="page"' if a['slug']==article['slug'] else '') + f'>{escape(a["title"])}</a></li>' for a in ARTICLES) + '</ol></nav>'
    note = '<p class="home-note"><strong>Leitura técnica para estudantes e profissionais.</strong> Síntese narrativa de fontes selecionadas, consultadas em 29/10/2026; não é revisão sistemática nem protocolo individual de atendimento. Exemplos didáticos são fictícios. O uso clínico exige formação, supervisão e avaliação contextual.</p>'
    article['sources'] = [r['url'] for r in article['references']]
    article['read_min'] = str(max(1, math.ceil(len(unescape(re.sub('<[^>]+>', ' ', body)).split()) / 180)))
    article['body'] = note + body + refs + series
