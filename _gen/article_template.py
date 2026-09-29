#!/usr/bin/env python3
"""Shared template for Amorfy article generation."""

import html
import json
from pathlib import Path

# Categorias/temas canônicos (chips clicáveis → /temas/<slug>.html).
CATEGORIES = {
    "relacionamentos": ("Relacionamentos", "cat-relacionamentos"),
    "borderline": ("Borderline", "cat-borderline"),
    "narcisismo": ("Narcisismo", "cat-narcisismo"),
    "bipolaridade": ("Bipolaridade", "cat-bipolaridade"),
    "psicanalise": ("Psicanálise", "cat-psicanalise"),
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
  <link rel="canonical" href="https://amorfy.com.br/artigos/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://amorfy.com.br/artigos/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:image" content="https://amorfy.com.br/og/artigos-{slug}.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Amorfy — testes, artigos e histórias reais sobre relacionamentos">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://amorfy.com.br/og/artigos-{slug}.png">
  <meta name="twitter:image:alt" content="Amorfy">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": {title_json},
    "description": {desc_json},
    "author": {{"@type": "Organization", "name": "Amorfy"}},
    "publisher": {{"@type": "Organization", "name": "Amorfy", "logo": {{"@type": "ImageObject", "url": "https://amorfy.com.br/favicon.svg"}}}},
    "datePublished": "{date}",
    "dateModified": "{date_modified}"
  }}
  </script>
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
      <li><a href="/perguntas-frequentes.html">FAQ</a></li>
    </ul></nav>
  </div>
</header>

<main>
  <nav class="container" aria-label="Breadcrumb">
    <ol class="breadcrumbs">
      <li><a href="/">In&iacute;cio</a></li>
      <li><a href="/artigos/">Artigos</a></li>
      <li>{breadcrumb}</li>
    </ol>
  </nav>

  <article>
    {hero_html}
    <header class="article-header">
      <span class="card-tag {tag_color}" style="margin-bottom:1rem;display:inline-block">{tag}</span>
      {categories_block}
      <h1>{title}</h1>
      <div class="article-meta">
        <span>&#9997;&#65039; Equipe Amorfy</span>
        <span>&#128197; {date_human}</span>
        <span>&#128214; {read_min} min de leitura</span>
      </div>
    </header>
{related_quiz_html}    <div class="ad-container ad-article-top">
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6858130394830057" data-ad-slot="auto" data-ad-format="auto"></ins>
    </div>
    <div class="ad-label">Publicidade</div>

    <div class="article-body">
{body}
    </div>
  </article>

</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col"><h4>Amorfy &#128150;</h4><p style="color:var(--text-secondary);font-size:.9rem">Seu guia completo sobre relacionamentos, autoconhecimento e amor pr&oacute;prio.</p></div>
    <div class="footer-col"><h4>Navegue</h4><ul><li><a href="/testes/">Testes</a></li><li><a href="/artigos/">Artigos</a></li><li><a href="/casos/">Casos Reais</a></li><li><a href="/perguntas-frequentes.html">FAQ</a></li><li><a href="/sobre.html">Sobre</a></li></ul></div>
    <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacidade.html">Pol&iacute;tica de Privacidade</a></li><li><a href="/termos.html">Termos de Uso</a></li></ul></div>
  </div>
  <div class="footer-bottom">&copy; 2026 Amorfy. Desenvolvido por <a href="https://dionisio.dev">Dionisio Software</a>.</div>
</footer>

<script src="/js/main.js"></script>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</body>
</html>
"""


def _categories_html(cats):
    parts = []
    for c in cats or []:
        label, cls = CATEGORIES.get(c, (c, "cat-relacionamentos"))
        parts.append(f'<a class="cat-chip {cls}" href="/temas/{c}.html">{label}</a>')
    return "".join(parts)


def _hero_html(meta):
    img = meta.get("image")
    if not img:
        return ""
    alt = html.escape(meta.get("image_alt") or meta["title"], quote=True)
    return (
        f'<figure class="article-hero">'
        f'<img src="{img}" alt="{alt}" width="1200" height="600" loading="eager" decoding="async">'
        f'</figure>'
    )


def _related_quiz_html(meta):
    rq = meta.get("related_quiz")
    if not rq:
        return ""
    emoji = rq.get("emoji", "🎯")
    title = html.escape(rq["title"], quote=True)
    tagline = html.escape(rq.get("tagline", ""), quote=True)
    slug = rq["slug"]
    strip = (
        f'<aside class="quiz-cta">'
        f'<span class="quiz-cta-emoji">{emoji}</span>'
        f'<div class="quiz-cta-body">'
        f'<span class="quiz-cta-label">Teste relacionado</span>'
        f'<h3><a href="/testes/{slug}.html">{title}</a></h3>'
        f'<p>{tagline}</p>'
        f'</div>'
        f'<a class="btn btn-primary" href="/testes/{slug}.html">Fazer teste &#8594;</a>'
        f'</aside>'
    )
    return f"\n    {strip}\n"


def render_article(meta):
    values = dict(meta)
    for key in ("title", "desc"):
        values[key] = html.escape(meta[key], quote=True)
        values[key + "_json"] = json.dumps(meta[key], ensure_ascii=False).replace("<", "\\u003c")
    values["date_modified"] = meta.get("date_modified", meta["date"])
    cats = _categories_html(meta.get("categories"))
    values["categories_block"] = f'<div class="article-cats">{cats}</div>' if cats else ""
    values["hero_html"] = _hero_html(meta)
    values["related_quiz_html"] = _related_quiz_html(meta)
    return TEMPLATE.format(**values)


def write_article(meta, out_dir=None):
    out_dir = Path(out_dir) if out_dir is not None else Path(__file__).resolve().parent.parent / "artigos"
    out_dir.mkdir(parents=True, exist_ok=True)
    html = render_article(meta)
    path = f"{out_dir}/{meta['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {path} ({len(html)} bytes)")
