#!/usr/bin/env python3
"""Links patrocinados/afiliados de livros.

Para cada livro patrocinado, liste os slugs dos artigos onde o CTA "leitura
recomendada" deve aparecer. build.py injeta o bloco no final do body (antes do
highlight-box de cross-links) automaticamente — não edite os bodies dos batches.
"""
SPONSORED_BOOKS = [
    {
        "book": "Sexo no Cativeiro",
        "author": "Esther Perel",
        "url": "https://meli.la/2ZhYqit",
        "tagline": "a referência sobre desejo, intimidade e os paradoxos do amor a longo prazo",
        "slugs": [
            "sexualidade",
            "libidos-diferentes-no-casal",
            "fantasia-e-desejo-no-casal",
            "capacidade-de-ficar-so",
        ],
    },
    {
        "book": "Mentes que Amam Demais",
        "author": "Ana Beatriz Barbosa Silva",
        "url": "https://meli.la/1hUkCJp",
        "tagline": "um guia essencial para entender o Transtorno de Personalidade Borderline (TPB) e conviver com quem o tem",
        "slugs": [
            "borderline",
            "relacionamento-borderline",
            "borderline-na-familia",
            "tenho-borderline-e-quero-amar",
            "desregulacao-emocional-no-casal",
        ],
    },
    {
        "book": "Casos e Casos",
        "author": "Esther Perel",
        "url": "https://meli.la/2nndt4K",
        "tagline": "a referência para repensar a infidelidade e entender o que os casos revelam sobre nós",
        "slugs": [
            "por-que-as-pessoas-traem",
            "descobri-uma-traicao-e-agora",
            "reconstruir-a-confianca-depois-da-traicao",
            "confianca",
        ],
    },
]


def _cta(book, author, url, tagline):
    return (
        '<div class="highlight-box" style="border-color:var(--gold-light);background:var(--gold-bg)">\n'
        '  <h3>&#128214; Leitura recomendada</h3>\n'
        f'  <p>Para ir além deste artigo, o livro <strong>{book}</strong>, de {author}, é {tagline}:</p>\n'
        f'  <p><a class="btn btn-primary" href="{url}" target="_blank" rel="sponsored nofollow noopener">Comprar o livro</a></p>\n'
        '  <p style="font-size:.78rem;color:var(--text-muted);margin-top:.6rem">Link patrocinado: o Amorfy pode receber uma comissão pela compra, sem custo extra para você.</p>\n'
        '</div>'
    )


def inject_sponsored(article):
    """Insere o CTA patrocinado no body, se o slug estiver mapeado."""
    slug = article.get("slug")
    for sp in SPONSORED_BOOKS:
        if slug in sp["slugs"]:
            cta = _cta(sp["book"], sp["author"], sp["url"], sp["tagline"])
            body = article["body"]
            idx = body.rfind('<div class="highlight-box">')
            if idx != -1:
                article["body"] = body[:idx] + cta + "\n\n" + body[idx:]
            else:
                article["body"] = body + "\n\n" + cta
            break
    return article
