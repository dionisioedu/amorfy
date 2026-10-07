#!/usr/bin/env python3
"""Regenera as páginas do pipeline (artigos, testes, casos, temas, estáticas) e o sitemap.

Home e índices de seção (artigos/, testes/, casos/) são mantidos manualmente fora do pipeline.
"""
import argparse
from pathlib import Path

from article_template import write_article
from article_extras import apply_extras
from sponsors import inject_sponsored
from quiz_related import apply_related
from quiz_template import write_quiz
from batch1 import ARTICLES as BATCH1
from batch2 import ARTICLES as BATCH2
from batch3 import ARTICLES as BATCH3
from manual_batch import ARTICLES as MANUAL
from borderline_artigo import ARTIGO
from temas_batch1 import ARTICLES as TEMAS1
from temas_batch2 import ARTICLES as TEMAS2
from temas_batch3 import ARTICLES as TEMAS3
from livros_batch import ARTICLES as LIVROS
from psicanalise_batch1 import ARTICLES as PSI1
from psicanalise_batch2 import ARTICLES as PSI2
from psicanalise_batch3 import ARTICLES as PSI3
from infidelidade_batch import ARTICLES as INFID
from abusivo_batch1 import ARTICLES as ABUS1
from abusivo_batch2 import ARTICLES as ABUS2
from dependencia_batch1 import ARTICLES as DEP1
from dependencia_batch2 import ARTICLES as DEP2
from quiz_batch1 import PERSONALIDADE, LINGUAGEM
from quiz_batch2 import NARCISISTA, COMPATIBILIDADE
from quiz_batch3 import MEU_NARCISISMO, PARCEIRO_PRONTO, AFASTO_PESSOAS, AUTOSSABOTAGEM, CIUME_INVEJA, RED_FLAGS
from borderline_quizzes import AUTO, PARCEIRO
from quiz_landing import enrich as enrich_quiz
from casos_batch import CASOS, write_caso
from static_pages import PAGES, write_page
import faq_page
from temas import write_temas
from artigos_index import write_articles_index
from sitemap import write_sitemap


def build(output):
    articles = []
    for raw in [*BATCH1, *BATCH2, *BATCH3, *MANUAL, ARTIGO, *TEMAS1, *TEMAS2, *TEMAS3, *LIVROS, *PSI1, *PSI2, *PSI3, *INFID, *ABUS1, *ABUS2, *DEP1, *DEP2]:
        article = apply_related(inject_sponsored(apply_extras(raw)))
        articles.append(article)
        write_article(article, output / "artigos")

    for quiz in [PERSONALIDADE, LINGUAGEM, NARCISISTA, COMPATIBILIDADE, AUTO, PARCEIRO,
                 MEU_NARCISISMO, PARCEIRO_PRONTO, AFASTO_PESSOAS, AUTOSSABOTAGEM, CIUME_INVEJA, RED_FLAGS]:
        write_quiz(enrich_quiz(quiz), output / "testes")
    for story in CASOS:
        write_caso(story, output / "casos")
    for page in PAGES:
        write_page(page, output)
    faq_page.build(output)

    write_temas(articles, output)
    write_articles_index(articles, output)
    write_sitemap(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Output directory (default: repository root)")
    args = parser.parse_args()
    build(args.output.resolve())
