#!/usr/bin/env python3
"""Gera as páginas de tema (/temas/<slug>.html) listando os artigos da categoria."""
import re
from pathlib import Path

from article_template import CATEGORIES

BASE_URL = "https://amorfy.com.br"

# Metadados SEO por tema.
META = {
    "relacionamentos": {
        "desc": "Artigos sobre relacionamentos: apego, desejo, sexualidade, comunicação e dinâmicas do amor. Guias práticos escritos com rigor e empatia.",
        "intro": "Entenda as dinâmicas que aproximam ou afastam os casais — do apego ao desejo, da comunicação à confiança.",
    },
    "borderline": {
        "desc": "Artigos sobre Transtorno de Personalidade Borderline (TPB): sinais, relacionamentos, família e autocuidado. Conteúdo acolhedor e informativo.",
        "intro": "Um acervo acolhedor sobre o TPB — para quem convive com o diagnóstico e para quem ama alguém que o tem.",
    },
    "narcisismo": {
        "desc": "Artigos sobre narcisismo nos relacionamentos: como identificar, proteger-se, co-parentalidade e o caminho da cura. Guias práticos e empáticos.",
        "intro": "Reconheça os padrões do abuso narcisista e reconstrua sua vida com segurança, limites e autoestima.",
    },
    "bipolaridade": {
        "desc": "Artigos sobre Transtorno Bipolar: ciclos, relacionamentos, família e tratamento. Entenda e cuide de quem você ama — ou de si mesmo.",
        "intro": "Compreenda os ciclos do transtorno bipolar e aprenda a construir vínculos estáveis entre a crise e a calmaria.",
    },
}

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6858130394830057">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://amorfy.com.br/temas/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://amorfy.com.br/temas/{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:image" content="https://amorfy.com.br/og.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Amorfy — {label}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://amorfy.com.br/og.png">
  <meta name="twitter:image:alt" content="Amorfy — {label}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="/" class="logo"><img src="/favicon.svg" alt="" width="38" height="38">Amorfy</a>
    <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="site-navigation">&#9776;</button>
    <nav><ul class="nav-links" id="site-navigation">
      <li><a href="/">In&iacute;cio</a></li>
      <li><a href="/testes/">Testes</a></li>
      <li><a href="/artigos/">Artigos</a></li>
      <li><a href="/casos/">Casos Reais</a></li>
      <li><a href="/sobre.html">Sobre</a></li>
    </ul></nav>
  </div>
</header>

<main>
  <section class="hero tema-hero">
    <div class="container hero-content">
      <h1>{emoji} Artigos sobre {label}</h1>
      <p>{intro}</p>
      <div class="card-cats" style="justify-content:center">{nav_chips}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="grid grid-3">
        {cards}
      </div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col"><h4>Amorfy &#128150;</h4><p style="color:var(--text-secondary);font-size:.9rem">Seu guia completo sobre relacionamentos, autoconhecimento e amor pr&oacute;prio.</p></div>
    <div class="footer-col"><h4>Navegue</h4><ul><li><a href="/testes/">Testes</a></li><li><a href="/artigos/">Artigos</a></li><li><a href="/casos/">Casos Reais</a></li><li><a href="/sobre.html">Sobre</a></li></ul></div>
    <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacidade.html">Pol&iacute;tica de Privacidade</a></li><li><a href="/termos.html">Termos de Uso</a></li></ul></div>
  </div>
  <div class="footer-bottom">&copy; 2026 Amorfy. Desenvolvido por <a href="https://dionisio.dev">Dionisio Software</a>.</div>
</footer>

<script src="/js/main.js"></script>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</body>
</html>
"""

EMOJI = {"relacionamentos": "💞", "borderline": "🌊", "narcisismo": "🪞", "bipolaridade": "🌗"}


def short_title(title):
    return re.split(r"\s*[—:]\s*", title)[0].strip()


def _chip(slug, active=False):
    label, cls = CATEGORIES[slug]
    cls = cls if not active else f"{cls} active"
    return f'<a class="cat-chip {cls}" href="/temas/{slug}.html">{label}</a>'


def _card(article):
    slug = article["slug"]
    title = short_title(article["title"])
    desc = article.get("desc", "")
    read_min = article.get("read_min", "")
    tag = article.get("tag", "")
    tag_color = article.get("tag_color", "rose")
    chips = "".join(_chip(c) for c in article.get("categories", []))
    return (
        f'<div class="card"><div class="card-body">\n'
        f'  <span class="card-tag {tag_color}">{tag}</span>\n'
        f'  <h3 class="card-title"><a href="/artigos/{slug}.html">{title}</a></h3>\n'
        f'  <p class="card-text">{desc}</p>\n'
        f'  <div class="card-meta"><span>&#128197; {read_min} min de leitura</span></div>\n'
        f'  <div class="card-cats">{chips}</div>\n'
        f'</div></div>'
    )


def _nav_chips(active):
    return "".join(_chip(c, active=(c == active)) for c in CATEGORIES)


def write_temas(articles, output):
    output = Path(output)
    temas_dir = output / "temas"
    temas_dir.mkdir(parents=True, exist_ok=True)

    by_cat = {c: [] for c in CATEGORIES}
    for article in articles:
        for c in article.get("categories", []):
            if c in by_cat:
                by_cat[c].append(article)

    for slug, (label, _cls) in CATEGORIES.items():
        meta = META[slug]
        cards = "\n        ".join(_card(a) for a in sorted(by_cat[slug], key=lambda a: a["slug"]))
        html = TEMPLATE.format(
            title=f"Artigos sobre {label} &mdash; Amorfy",
            desc=meta["desc"],
            slug=slug,
            label=label,
            intro=meta["intro"],
            emoji=EMOJI[slug],
            nav_chips=_nav_chips(slug),
            cards=cards,
        )
        path = temas_dir / f"{slug}.html"
        path.write_text(html, encoding="utf-8")
        print(f"OK {path} ({len(by_cat[slug])} artigos)")
