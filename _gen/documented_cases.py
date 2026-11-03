"""Public historical cases, with sources and reusable photography."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = []
for path in sorted((ROOT / 'cases').glob('*.json')):
    case = json.loads(path.read_text(encoding='utf-8'))
    consulted = case.get('sources_consulted', '29 de outubro de 2026')
    image_note = ('A capa é uma ilustração conceitual criada com IA, não um registro histórico.' if case.get('illustration_caption') else 'As fotografias têm créditos e licença na legenda.')
    refs = ''.join(f'<li id="ref-{i}"><a href="{escape(r["url"], quote=True)}">{escape(r["label"])}</a> — {escape(r["supports"])}</li>' for i, r in enumerate(case.pop('references'), 1))
    case['body'] = ('<p class="home-note"><strong>História pública documentada.</strong> Texto baseado nas fontes indicadas, não em entrevista do Amorfy. As reflexões são editoriais e não avaliam clinicamente as pessoas retratadas.</p>' + case['body'] + '<h2 id="referencias">Fontes e referências</h2><ol>' + refs + f'</ol><p>Fontes consultadas em {consulted}. {image_note} A presença das pessoas nesta página não implica vínculo ou endosso ao Amorfy.</p>')
    CASES.append(case)


def write_cases_index(output):
    from home import card
    cards = ''.join(card(dict(title=c['title'], desc=c['desc'], url=f'/casos/{c["slug"]}.html', kind='caso', image=c['image'], label='Caso documentado', date=c['date'], meta=f'{c["read_min"]} min de leitura', topics=c['tag'])) for c in sorted(CASES, key=lambda c: (c["date"], c.get("publication_order", 0)), reverse=True))
    section = '<section id="documentados" class="cat-group"><h2>Histórias públicas documentadas</h2><p>Histórias com fontes verificáveis e reflexões sobre vínculos, saúde mental e cuidado. Fotografias e ilustrações são identificadas nas legendas.</p><div class="home-grid">' + cards + '</div></section>'
    template = (ROOT / 'casos_index_template.tmpl').read_text(encoding='utf-8')
    template = template.replace('</head>', '<link rel="stylesheet" href="/css/home.css">\n</head>')
    target = Path(output) / 'casos/index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(template.replace('@@documented_cases@@', section), encoding='utf-8')
