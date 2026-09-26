#!/usr/bin/env python3
"""Regenerate pipeline pages (artigos, testes, casos, static pages) and the sitemap.

Home and section indexes are maintained manually outside this pipeline.
"""
import argparse
from pathlib import Path

from article_template import write_article
from quiz_template import write_quiz
from batch1 import ARTICLES as BATCH1
from batch2 import ARTICLES as BATCH2
from batch3 import ARTICLES as BATCH3
from manual_batch import ARTICLES as MANUAL
from borderline_artigo import ARTIGO
from quiz_batch1 import PERSONALIDADE, LINGUAGEM
from quiz_batch2 import NARCISISTA, COMPATIBILIDADE
from borderline_quizzes import AUTO, PARCEIRO
from casos_batch import CASOS, write_caso
from static_pages import PAGES, write_page
from sitemap import write_sitemap


def build(output):
    for article in [*BATCH1, *BATCH2, *BATCH3, *MANUAL, ARTIGO]:
        write_article(article, output / "artigos")
    for quiz in [PERSONALIDADE, LINGUAGEM, NARCISISTA, COMPATIBILIDADE, AUTO, PARCEIRO]:
        write_quiz(quiz, output / "testes")
    for story in CASOS:
        write_caso(story, output / "casos")
    for page in PAGES:
        write_page(page, output)
    write_sitemap(output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parent.parent,
                        help="Output directory (default: repository root)")
    args = parser.parse_args()
    build(args.output.resolve())
