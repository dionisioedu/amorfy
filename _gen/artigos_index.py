#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera /artigos/index.html — índice de todos os artigos agrupados por tema.

Antes deste módulo o índice era um arquivo estático editado à mão e nunca
regenerado pelo build (os artigos novos não apareciam). Agora faz parte do
pipeline: `build.py` chama `write_articles_index(articles, output)`.

Agrupa por categoria primária (article['categories'][0]); a ordem dos grupos
segue a ordem canônica de article_template.CATEGORIES.
"""
from pathlib import Path
from article_template import CATEGORIES

SITE_URL = "https://amorfy.com.br"


def _esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def _card(art):
    slug = art["slug"]
    title = _esc(art["title"])
    desc = _esc(art.get("desc", ""))
    tag = _esc(art.get("tag", "Artigo"))
    tag_color = art.get("tag_color", "rose")
    read = art.get("read_min", 8)
    chips = "".join(
        f'<a class="cat-chip cat-{c}" href="/temas/{c}.html">{CATEGORIES.get(c, (c.title(), ""))[0]}</a>'
        for c in art.get("categories", [])
    )
    return f'''<div class="card">
          <div class="card-body">
            <span class="card-tag {tag_color}">{tag}</span>
            <h3 class="card-title"><a href="/artigos/{slug}.html">{title}</a></h3>
            <p class="card-text">{desc}</p>
            <div class="card-meta"><span>📅 {read} min de leitura</span></div><div class="card-cats">{chips}</div>
          </div>
        </div>'''


def write_articles_index(articles, output):
    """Escreve output/artigos/index.html agrupado por tema."""
    # agrupa por categoria primária
    groups = {}
    for a in articles:
        cats = a.get("categories") or ["relacionamentos"]
        primary = cats[0]
        groups.setdefault(primary, []).append(a)

    # ordena grupos pela ordem canônica de CATEGORIES
    ordered_keys = [k for k in CATEGORIES if k in groups]
    # qualquer categoria desconhecida vai ao fim
    ordered_keys += [k for k in groups if k not in CATEGORIES]

    # nav de atalhos (só grupos não vazios)
    nav = "".join(
        f'\n        <a href="#{k}">{CATEGORIES.get(k, (k.title(), ""))[0]}</a>'
        for k in ordered_keys
    )

    blocks = []
    for k in ordered_keys:
        items = sorted(groups[k], key=lambda a: a.get("date", ""), reverse=True)
        label = CATEGORIES.get(k, (k.title(), ""))[0]
        cards = "\n\n".join(_card(a) for a in items)
        blocks.append(f'''      <div class="cat-group" id="{k}">
        <div class="cat-group-head"><h2>{label}</h2><span class="cat-count">{len(items)} artigo{'s' if len(items) != 1 else ''}</span></div>
        <div class="grid grid-3">

{cards}

        </div>
      </div>''')

    total = len(articles)
    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Artigos sobre Relacionamentos, Psicologia e Autoconhecimento — Amorfy</title>
  <meta name="description" content="Todos os artigos do Amorfy: relacionamentos, borderline, narcisismo, bipolaridade, psicanálise, relacionamento abusivo e dependência emocional. Conteúdo aprofundado e baseado em evidências.">
  <link rel="canonical" href="{SITE_URL}/artigos/">
  <meta property="og:title" content="Artigos — Amorfy">
  <meta property="og:description" content="Conteúdo aprofundado sobre relacionamentos, psicologia e autoconhecimento.">
  <meta property="og:type" content="website">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "CollectionPage",
    "name": "Artigos — Amorfy",
    "url": "{SITE_URL}/artigos/",
    "isPartOf": {{"@type": "WebSite", "name": "Amorfy", "url": "{SITE_URL}"}}
  }}
  </script>
</head>
<body>
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="logo"><img src="/images/logo.svg" alt="Amorfy" width="38" height="38">Amorfy</a>
      <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="site-navigation">☰</button>
      <nav><ul class="nav-links" id="site-navigation">
      <li><a href="/">Início</a></li>
      <li><a href="/testes/">Testes</a></li>
      <li><a href="/artigos/">Artigos</a></li>
      <li><a href="/casos/">Casos Reais</a></li>
      <li><a href="/perguntas-frequentes.html">FAQ</a></li>
      <li><a href="/sobre.html">Sobre</a></li>
    </ul></nav>
    </div>
  </header>

<main>
  <section class="hero" style="padding:2.5rem 0">
    <div class="container hero-content">
      <h1>📝 Artigos sobre Relacionamentos</h1>
      <p>{total} artigos sobre psicologia, comportamento e dinâmicas dos relacionamentos. Escritos com base em evidências e empatia.</p>
    </div>
  </section>

    <section class="section">
    <div class="container">

      <nav class="cat-nav" aria-label="Temas de artigos">{nav}
      </nav>

{chr(10).join(blocks)}

    </div>
    </section>
</main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <h4>Amorfy 💖</h4>
        <p>Seu guia completo sobre relacionamentos, autoconhecimento e amor próprio.</p>
      </div>
      <div class="footer-col">
        <h4>Navegue</h4>
        <ul>
          <li><a href="/testes/">Testes</a></li>
          <li><a href="/artigos/">Artigos</a></li>
          <li><a href="/casos/">Casos Reais</a></li>
          <li><a href="/perguntas-frequentes.html">FAQ</a></li>
          <li><a href="/sobre.html">Sobre</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="/privacidade.html">Política de Privacidade</a></li>
          <li><a href="/termos.html">Termos de Uso</a></li>
        </ul>
      </div>
    </div>
    <div class="container footer-bottom">
      <p>© 2026 Amorfy · Conteúdo informativo, não substitui acompanhamento profissional.</p>
      <a href="https://dionisio.dev" class="footer-made" rel="noopener" target="_blank">Dionisio Software</a>
    </div>
  </footer>
  <script src="/js/main.js"></script>
</body>
</html>
'''
    out = Path(output) / "artigos" / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"OK {out} ({total} artigos, {len(ordered_keys)} temas)")
    return out
