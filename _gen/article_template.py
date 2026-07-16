#!/usr/bin/env python3
"""Shared template for Amorfy article generation."""

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://amorfy.com.br/artigos/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://amorfy.com.br/artigos/{slug}.html">
  <meta property="og:type" content="article">
  <meta property="og:locale" content="pt_BR">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc}",
    "author": {{"@type": "Organization", "name": "Amorfy"}},
    "publisher": {{"@type": "Organization", "name": "Amorfy", "logo": {{"@type": "ImageObject", "url": "https://amorfy.com.br/favicon.svg"}}}},
    "datePublished": "{date}",
    "dateModified": "{date}"
  }}
  </script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="/" class="logo"><img src="/favicon.svg" alt="" width="38" height="38">Amorfy</a>
    <button class="nav-toggle" aria-label="Abrir menu">&#9776;</button>
    <nav><ul class="nav-links">
      <li><a href="/">In&iacute;cio</a></li>
      <li><a href="/testes/">Testes</a></li>
      <li><a href="/artigos/">Artigos</a></li>
      <li><a href="/casos/">Casos Reais</a></li>
      <li><a href="/sobre.html">Sobre</a></li>
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
    <header class="article-header">
      <span class="card-tag {tag_color}" style="margin-bottom:1rem;display:inline-block">{tag}</span>
      <h1>{title}</h1>
      <div class="article-meta">
        <span>&#9997;&#65039; Equipe Amorfy</span>
        <span>&#128197; {date_human}</span>
        <span>&#128214; {read_min} min de leitura</span>
      </div>
    </header>

    <div class="ad-container ad-article-top">
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6858130394830057" data-ad-slot="auto" data-ad-format="auto"></ins>
    </div>
    <div class="ad-label">Publicidade</div>

    <div class="article-body">
{body}
    </div>
  </article>

  <section class="container" style="margin-bottom:3rem">
    <div class="newsletter">
      <h3>&#128140; Gostou deste artigo?</h3>
      <p>Receba mais conte&uacute;dos exclusivos sobre relacionamentos toda semana.</p>
      <form class="newsletter-form" action="#" method="post">
        <input type="email" placeholder="Seu melhor e-mail" required>
        <button type="submit" class="btn btn-primary">Inscrever</button>
      </form>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col"><h4>Amorfy &#128150;</h4><p style="color:var(--text-secondary);font-size:.9rem">Seu guia completo sobre relacionamentos, autoconhecimento e amor pr&oacute;prio.</p></div>
    <div class="footer-col"><h4>Navegue</h4><ul><li><a href="/testes/">Testes</a></li><li><a href="/artigos/">Artigos</a></li><li><a href="/casos/">Casos Reais</a></li><li><a href="/sobre.html">Sobre</a></li></ul></div>
    <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacidade.html">Pol&iacute;tica de Privacidade</a></li><li><a href="/termos.html">Termos de Uso</a></li></ul></div>
  </div>
  <div class="footer-bottom">&copy; 2025 Amorfy. Desenvolvido por <a href="https://dionisio.dev">Dionisio Software</a>.</div>
</footer>

<script src="/js/main.js"></script>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</body>
</html>
"""


def write_article(meta, out_dir="/home/eduardo/projects/amorfy/artigos"):
    html = TEMPLATE.format(**meta)
    path = f"{out_dir}/{meta['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {path} ({len(html)} bytes)")
