#!/usr/bin/env python3
"""Gera as imagens hero (SVG) dos artigos — paleta warm editorial do Amorfy."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

# Paletas por tema (cor primária, cor secundária, tom de texto/linha)
THEMES = {
    "narcisismo":     ("#7b4fb5", "#c13a58", "#5d3a91"),
    "borderline":     ("#d4548f", "#7b4fb5", "#a02460"),
    "bipolaridade":   ("#d98e2b", "#7b4fb5", "#96601a"),
    "relacionamentos":("#c13a58", "#d98e2b", "#a02545"),
    "psicanalise":    ("#7a5c8f", "#c13a58", "#5a4270"),
    "relacionamento-abusivo":  ("#8e2b3a", "#c13a58", "#6d1f2c"),
    "dependencia-emocional":   ("#2f6d6a", "#7a5c8f", "#245552"),
}

# slug -> tema (27 artigos)
ARTICLES = {
    # antigos (relacionamentos)
    "linguagens-do-amor": "relacionamentos",
    "fases-relacionamento": "relacionamentos",
    "sexualidade": "relacionamentos",
    "inteligencia-emocional": "relacionamentos",
    "comunicacao": "relacionamentos",
    "autoconhecimento": "relacionamentos",
    "traumas": "relacionamentos",
    "conflitos": "relacionamentos",
    "tracos-carater": "relacionamentos",
    "mitos-amor": "relacionamentos",
    "confianca": "relacionamentos",
    "temperamentos": "relacionamentos",
    # antigos (temas específicos)
    "borderline": "borderline",
    "relacionamento-borderline": "borderline",
    "narcisismo": "narcisismo",
    # novos
    "coparentalidade-com-narcisista": "narcisismo",
    "filhos-de-pais-narcisistas": "narcisismo",
    "como-sair-de-relacao-com-narcisista": "narcisismo",
    "borderline-na-familia": "borderline",
    "tenho-borderline-e-quero-amar": "borderline",
    "desregulacao-emocional-no-casal": "borderline",
    "amando-alguem-com-bipolaridade": "bipolaridade",
    "vivendo-e-amando-com-bipolaridade": "bipolaridade",
    "bipolaridade-em-casa-guia-familia": "bipolaridade",
    "libidos-diferentes-no-casal": "relacionamentos",
    "sexualidade-alem-da-norma-lgbtqia": "relacionamentos",
    "estilos-de-apego-no-amor": "relacionamentos",
    "sexo-no-cativeiro": "relacionamentos",
    "repeticao-compulsiva-no-amor": "psicanalise",
    "amor-e-odio-ambivalencia": "psicanalise",
    "dependencia-emocional-psicanalise": "psicanalise",
    "transferencia-por-que-nos-apaixonamos": "psicanalise",
    "arte-de-amar-erich-fromm": "psicanalise",
    "ciume-o-que-ele-revela": "psicanalise",
    "medo-de-amar-contraintimidade": "psicanalise",
    "luto-do-termino": "psicanalise",
    "amor-proprio-narcisismo-saudavel": "psicanalise",
    "fantasia-e-desejo-no-casal": "psicanalise",
    "capacidade-de-ficar-so": "psicanalise",
    "amor-na-era-dos-aplicativos": "psicanalise",
    "casos-e-casos-repensando-a-infidelidade": "relacionamentos",
    "por-que-as-pessoas-traem": "relacionamentos",
    "descobri-uma-traicao-e-agora": "relacionamentos",
    "reconstruir-a-confianca-depois-da-traicao": "relacionamentos",
    # relacionamento abusivo
    "relacionamento-abusivo-sinais": "relacionamento-abusivo",
    "gaslighting-o-que-e": "relacionamento-abusivo",
    "como-sair-de-relacionamento-abusivo": "relacionamento-abusivo",
    "isolamento-no-abuso": "relacionamento-abusivo",
    "violencia-patrimonial": "relacionamento-abusivo",
    "violencia-psicologica-rotina": "relacionamento-abusivo",
    # dependência emocional
    "dependencia-emocional-o-que-e": "dependencia-emocional",
    "amor-ou-necessidade": "dependencia-emocional",
    "codependencia-no-casal": "dependencia-emocional",
    "dependencia-emocional-sinais": "dependencia-emocional",
    "como-superar-dependencia-emocional": "dependencia-emocional",
    "autonomia-afetiva": "dependencia-emocional",
    "dependencia-emocional-teoria-do-apego": "dependencia-emocional",
}


def _gradient(slug, c1, c2):
    return f'''<defs>
    <radialGradient id="bg" cx="35%" cy="28%" r="90%">
      <stop offset="0%" stop-color="{c1}" stop-opacity="0.16"/>
      <stop offset="55%" stop-color="{c1}" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="#faf6f1" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
    <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="42"/></filter>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="14"/></filter>
    <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/><feComponentTransfer><feFuncA type="linear" slope="0.05"/></feComponentTransfer></filter>
  </defs>'''


def _blobs(c1, c2, v):
    # 3 blobs orgânicos, posições variando com o seed v
    x1 = 180 + (v * 37) % 200
    y1 = 120 + (v * 29) % 160
    x2 = 980 - (v * 53) % 260
    y2 = 420 + (v * 41) % 120
    return f'''<circle cx="{x1}" cy="{y1}" r="150" fill="{c1}" opacity="0.14" filter="url(#blur)"/>
    <circle cx="{x2}" cy="{y2}" r="190" fill="{c2}" opacity="0.12" filter="url(#blur)"/>
    <circle cx="{600 + (v*23)%160 - 80}" cy="{300 - (v*19)%120 + 60}" r="90" fill="{c2}" opacity="0.10" filter="url(#blur)"/>'''


def _motif(theme, c1, c2, line, v):
    stroke = f'stroke="{line}" fill="none" stroke-width="4" stroke-linecap="round"'
    if theme == "relacionamentos":
        # dois círculos sobrepostos + coração no encontro
        return f'''<g {stroke} opacity="0.85">
      <circle cx="520" cy="300" r="120"/>
      <circle cx="680" cy="300" r="120"/>
    </g>
    <path d="M600 322 c-8 -10 -30 -16 -30 -32 c0 -13 10 -22 22 -22 c7 0 13 3 8 0 c-5 3 1 0 8 0 c12 0 22 9 22 22 c0 16 -22 22 -30 32 z" fill="{c1}" opacity="0.9"/>
    <circle cx="470" cy="250" r="8" fill="{c2}" opacity="0.7"/>
    <circle cx="730" cy="350" r="6" fill="{c2}" opacity="0.7"/>'''
    if theme == "borderline":
        # ondas / turbulência emocional
        waves = []
        base = 250 + (v % 3) * 20
        for i in range(4):
            y = base + i * 55
            waves.append(f'<path d="M150 {y} C 320 {y-55}, 420 {y+55}, 620 {y} S 920 {y-55}, 1050 {y}" {stroke} opacity="{0.8 - i*0.15}"/>')
        return "\n    ".join(waves) + f'\n    <circle cx="{180+(v*30)%160}" cy="150" r="10" fill="{c1}" opacity="0.6"/>'
    if theme == "narcisismo":
        # anéis concêntricos com um rompido (espelho quebrado)
        rings = []
        for i, r in enumerate([180, 130, 85]):
            op = 0.85 - i * 0.2
            if i == 1:
                rings.append(f'<path d="M {600+r} 300 A {r} {r} 0 1 0 {600-r*0.5} {300 - r*0.866} L {600-r*0.3} {300 - r*0.8}" {stroke} opacity="{op}"/>')
            else:
                rings.append(f'<circle cx="600" cy="300" r="{r}" {stroke} opacity="{op}"/>')
        return "\n    ".join(rings) + f'\n    <circle cx="600" cy="300" r="14" fill="{c1}" opacity="0.85"/>'
    if theme == "bipolaridade":
        # sol/lua — círculo dividido + crescente
        return f'''<circle cx="600" cy="300" r="130" fill="url(#accent)" opacity="0.9"/>
    <path d="M600 170 A130 130 0 0 0 600 430 A100 100 0 0 1 600 170 z" fill="#faf6f1"/>
    <circle cx="600" cy="300" r="130" {stroke} opacity="0.8"/>
    <circle cx="545" cy="245" r="8" fill="{c2}" opacity="0.7"/>
    <circle cx="660" cy="360" r="6" fill="{c2}" opacity="0.7"/>'''
    if theme == "psicanalise":
        # iceberg: consciente (topo) / inconsciente (submerso) — o modelo freudiano
        return f'''<path d="M110 400 C 310 380, 510 425, 700 400 S 990 378, 1090 400" {stroke} opacity="0.7"/>
    <path d="M478 400 L 600 248 L 722 400 Z" {stroke} opacity="0.9"/>
    <path d="M424 404 L 600 556 L 776 404 Z" {stroke} opacity="0.45"/>
    <path d="M520 404 L 600 486 L 680 404 Z" {stroke} opacity="0.35"/>
    <circle cx="600" cy="208" r="7" fill="{c1}" opacity="0.7"/>'''
    if theme == "relacionamento-abusivo":
        # corrente rompida + grade/barras (controle) ao fundo
        bars = []
        for i in range(6):
            x = 250 + i * 130
            bars.append(f'<line x1="{x}" y1="180" x2="{x}" y2="420" {stroke} opacity="0.25"/>')
        links = []
        for i in range(4):
            cx = 400 + i * 130
            links.append(f'<circle cx="{cx}" cy="300" r="46" {stroke} opacity="0.7"/>')
        # elo central rompido
        links[0] = f'<path d="M354 300 a46 46 0 1 1 92 0" {stroke} opacity="0.7"/>'
        links.append(f'<path d="M812 300 a46 46 0 1 0 -92 0" {stroke} opacity="0.7"/>')
        return "\\n    ".join(bars) + "\\n    " + "\\n    ".join(links) + f'\\n    <line x1="600" y1="278" x2="640" y2="250" {stroke} opacity="0.9"/>\\n    <line x1="600" y1="322" x2="640" y2="350" {stroke} opacity="0.9"/>'
    if theme == "dependencia-emocional":
        # dois círculos em que um orbita/sustenta o outro + fio que liga (vínculo que prende)
        return f'''<circle cx="600" cy="300" r="150" {stroke} opacity="0.35"/>
    <circle cx="600" cy="300" r="105" {stroke} opacity="0.55"/>
    <circle cx="470" cy="300" r="58" {stroke} opacity="0.9"/>
    <circle cx="470" cy="300" r="26" fill="{c1}" opacity="0.85"/>
    <path d="M528 300 C 580 236, 700 236, 742 300" {stroke} opacity="0.8"/>
    <circle cx="770" cy="316" r="34" {stroke} opacity="0.6"/>
    <circle cx="770" cy="316" r="13" fill="{c2}" opacity="0.75"/>'''
    return ""


def svg(slug, theme, v):
    c1, c2, line = THEMES[theme]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 600" width="1200" height="600" role="img">
  {_gradient(slug, c1, c2)}
  <rect width="1200" height="600" fill="#faf6f1"/>
  <rect width="1200" height="600" fill="url(#bg)"/>
  {_blobs(c1, c2, v)}
  {_motif(theme, c1, c2, line, v)}
  <rect width="1200" height="600" filter="url(#grain)" opacity="1"/>
</svg>
'''


# variação determinística por slug (hash) para diferenciar artigos do mesmo tema
def seed(slug):
    return sum(ord(ch) for ch in slug)


for i, (slug, theme) in enumerate(ARTICLES.items()):
    v = seed(slug)
    (OUT / f"{slug}.svg").write_text(svg(slug, theme, v), encoding="utf-8")
    print(f"OK images/{slug}.svg ({theme})")

print(f"\n{len(ARTICLES)} imagens geradas em {OUT}")
