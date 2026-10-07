"""Verify portable generation and index/card integrity without changing the checked-in site."""
import html
import importlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
GEN_DIR = ROOT / "_gen"

# Pages maintained by hand that are never produced by the generator.
MANUALLY_MAINTAINED = {
    "index.html",
    "testes/index.html",
    "casos/index.html",
    "404.html",
}


def _import_gen(name):
    """Import a top-level module from _gen by filename; return None if absent."""
    if not (GEN_DIR / f"{name}.py").exists():
        return None
    if str(GEN_DIR) not in sys.path:
        sys.path.insert(0, str(GEN_DIR))
    return importlib.import_module(name)


def source_slugs():
    """Map each content section to the slugs declared in the _gen source modules."""
    articles, quizzes, casos = [], [], []

    for name in ("batch1", "batch2", "batch3", "manual_batch", "temas_batch1", "temas_batch2", "temas_batch3", "livros_batch", "psicanalise_batch1", "psicanalise_batch2", "psicanalise_batch3", "infidelidade_batch"):
        mod = _import_gen(name)
        if mod is not None:
            articles.extend(entry["slug"] for entry in mod.ARTICLES)

    mod = _import_gen("borderline_artigo")
    if mod is not None:
        articles.append(mod.ARTIGO["slug"])

    mod = _import_gen("quiz_batch1")
    if mod is not None:
        quizzes.extend((mod.PERSONALIDADE["slug"], mod.LINGUAGEM["slug"]))

    mod = _import_gen("quiz_batch2")
    if mod is not None:
        quizzes.extend((mod.NARCISISTA["slug"], mod.COMPATIBILIDADE["slug"]))

    mod = _import_gen("borderline_quizzes")
    if mod is not None:
        quizzes.extend((mod.AUTO["slug"], mod.PARCEIRO["slug"]))

    mod = _import_gen("casos_batch")
    if mod is not None:
        casos.extend(entry["slug"] for entry in mod.CASOS)

    return {"artigos": articles, "testes": quizzes, "casos": casos}


class GenerationTest(unittest.TestCase):
    def test_generation_from_another_directory_preserves_published_content(self):
        with tempfile.TemporaryDirectory(prefix="amorfy-generation-") as temp:
            subprocess.run(
                [sys.executable, "-B", str(ROOT / "_gen/build.py"), "--output", temp],
                cwd=temp, check=True, capture_output=True,
            )
            generated = {p.relative_to(temp).as_posix() for p in Path(temp).rglob("*.html")}

            expected = {
                p.relative_to(ROOT).as_posix()
                for p in ROOT.rglob("*.html")
                if ".git" not in p.parts
                and p.relative_to(ROOT).as_posix() not in MANUALLY_MAINTAINED
            }

            self.assertEqual(generated, expected)

            for rel in generated:
                with self.subTest(page=rel):
                    generated_text = (Path(temp) / rel).read_text(encoding="utf-8")
                    published = (ROOT / rel).read_text(encoding="utf-8")
                    self.assertEqual(html.unescape(generated_text), html.unescape(published))
                    for block in re.findall(
                        r'<script type="application/ld\+json">(.*?)</script>', generated_text, re.S
                    ):
                        json.loads(block)
                    if rel.split("/")[0] == "casos":
                        self.assertIn('href="/casos/#conte-sua-historia"', generated_text)

    def test_every_content_page_has_a_card_in_its_index(self):
        for category, prefix in (("artigos", "/artigos/"), ("testes", "/testes/"), ("casos", "/casos/")):
            index_text = (ROOT / category / "index.html").read_text(encoding="utf-8")
            for slug in source_slugs()[category]:
                with self.subTest(category=category, slug=slug):
                    self.assertIn(
                        f'href="{prefix}{slug}.html"',
                        index_text,
                        f"{prefix}{slug}.html missing from {category}/index.html",
                    )


if __name__ == "__main__":
    unittest.main()
