#!/usr/bin/env python3
"""Shared template for Amorfy quiz pages."""

from pathlib import Path

TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6858130394830057">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://amorfy.com.br/testes/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://amorfy.com.br/testes/{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:image" content="https://amorfy.com.br/og.png">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Amorfy — testes, artigos e histórias reais sobre relacionamentos">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="https://amorfy.com.br/og.png">
  <meta name="twitter:image:alt" content="Amorfy">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap" rel="stylesheet">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Quiz",
    "name": "{title}",
    "description": "{desc}",
    "publisher": {{"@type": "Organization", "name": "Amorfy"}}
  }}
  </script>{ld_faq}
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
      <li><a href="/testes/">Testes</a></li>
      <li>{breadcrumb}</li>
    </ol>
  </nav>

  <section class="hero" style="padding:2rem 0 1rem">
    <div class="container hero-content">
      <h1>{h1}</h1>
      <p>{intro}</p>
    </div>
  </section>

  <div class="quiz-container">
    <div id="quiz"></div>
    {disclaimer}
  </div>

  <div class="container" style="max-width:650px">
    <div class="ad-label">Publicidade</div>
    <div class="ad-container mb-3">
      <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-6858130394830057" data-ad-slot="auto" data-ad-format="auto"></ins>
    </div>
  </div>

{landing_html}

  <section class="container" style="max-width:650px;margin-bottom:3rem">
    <div class="card"><div class="card-body">
      <h3 class="card-title">&#128218; Leitura recomendada</h3>
      <p class="card-text">{related_text}</p>
      <a href="{related_link}" class="btn btn-secondary" style="margin-top:.5rem">{related_label}</a>
    </div></div>
  </section>
</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col"><h4>Amorfy &#128150;</h4><p style="color:var(--text-secondary);font-size:.9rem">Seu guia completo sobre relacionamentos, autoconhecimento e amor pr&oacute;prio.</p></div>
    <div class="footer-col"><h4>Navegue</h4><ul><li><a href="/testes/">Testes</a></li><li><a href="/artigos/">Artigos</a></li><li><a href="/casos/">Casos Reais</a></li><li><a href="/perguntas-frequentes.html">FAQ</a></li><li><a href="/sobre.html">Sobre</a></li></ul></div>
    <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacidade.html">Pol&iacute;tica de Privacidade</a></li><li><a href="/termos.html">Termos de Uso</a></li></ul></div>
  </div>
  <div class="footer-bottom">&copy; 2026 Amorfy. Desenvolvido por <a href="https://dionisio.dev">Dionisio Software</a>.</div>
</footer>

<script>
window.QUIZ_DATA = {quiz_data};
</script>
<script src="/js/main.js"></script>
<script src="/js/quiz.js"></script>
<script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
</body>
</html>
"""

DISCLAIMER = """<p style="text-align:center;color:var(--text-secondary);font-size:.85rem;margin-top:1rem">&#9878;&#65039; Este teste tem car&aacute;ter informativo e educacional. N&atilde;o substitui avalia&ccedil;&atilde;o, diagn&oacute;stico ou tratamento por profissional de sa&uacute;de mental.</p>"""


def render_landing(sections, faq):
    """Render the rich SEO landing content + FAQ accordion below the quiz.

    sections: list of {"type": "text"|"dimensions", "heading", "html", "items"}
    faq: list of {"q", "a"} -> rendered as a <details> accordion
    """
    import json

    parts = []
    for sec in sections or []:
        heading = sec.get("heading", "")
        if sec.get("type") == "dimensions":
            cards = []
            for it in sec["items"]:
                cards.append(
                    '<div class="dimension-card"><h3>{h}</h3>{p}</div>'.format(
                        h=it["title"], p=it["body"]))
            body = "".join(cards)
        else:
            body = sec.get("html", "")
        parts.append(
            '<section class="landing-section">'
            '<h2>{h}</h2>{b}'
            '</section>'.format(h=heading, b=body))

    faq_html = ""
    ld_faq = ""
    if faq:
        items = []
        for q in faq:
            items.append(
                '<details class="accordion-item">'
                '<summary>{q}</summary>'
                '<div class="accordion-body">{a}</div>'
                '</details>'.format(q=q["q"], a=q["a"]))
        faq_html = (
            '<section class="landing-section">'
            '<h2>Perguntas frequentes</h2>'
            '<div class="accordion">' + "".join(items) + '</div>'
            '</section>')
        ld = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q["q"],
                 "acceptedAnswer": {"@type": "Answer", "text": _strip(q["a"])}}
                for q in faq
            ],
        }
        ld_faq = '\n  <script type="application/ld+json">\n  ' + json.dumps(ld, ensure_ascii=False) + '\n  </script>'

    return parts and "".join(parts) + faq_html or "", ld_faq


def _strip(html_str):
    import re
    return re.sub(r"<[^>]+>", "", html_str).strip()


def write_quiz(meta, out_dir=None):
    import os, json
    out_dir = Path(out_dir) if out_dir is not None else Path(__file__).resolve().parent.parent / "testes"
    os.makedirs(out_dir, exist_ok=True)
    meta = dict(meta)
    meta["quiz_data"] = json.dumps(meta["quiz_data"], ensure_ascii=False, indent=2)
    meta["disclaimer"] = DISCLAIMER if meta.get("show_disclaimer") else ""
    meta.pop("show_disclaimer", None)
    landing, ld_faq = render_landing(meta.pop("landing_sections", None), meta.pop("faq", None))
    meta["landing_html"] = landing
    meta["ld_faq"] = ld_faq
    html = TEMPLATE.format(**meta)
    path = f"{out_dir}/{meta['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {path} ({len(html)} bytes)")
