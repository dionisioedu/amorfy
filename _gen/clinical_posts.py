"""Technical articles beyond the original nine-part reading series."""
import json
import math
import re
from html import escape
from pathlib import Path
ARTICLES = []
for path in sorted(Path(__file__).with_name('studies').glob('*.json')):
    article = json.loads(path.read_text(encoding='utf-8'))
    article['sources'] = [r['url'] for r in article['references']]
    article['read_min'] = str(max(1, math.ceil(len(re.sub('<[^>]+>', ' ', article['body']).split()) / 180)))
    refs = '<h2 id="referencias">Referências comentadas</h2><ol>' + ''.join(f'<li id="ref-{i}"><a href="{escape(r["url"], quote=True)}">{escape(r["label"])}</a>. {escape(r["note"])}</li>' for i, r in enumerate(article['references'], 1)) + '</ol>'
    note = '<p class="home-note"><strong>Leitura técnica com linguagem acessível.</strong> Síntese narrativa para estudantes e profissionais, com fontes consultadas em 03/11/2026. Não é revisão sistemática nem protocolo individual. Exemplos didáticos são fictícios.</p>'
    article['body'] = note + article['body'] + refs
    ARTICLES.append(article)
