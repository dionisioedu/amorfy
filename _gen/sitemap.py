#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera sitemap.xml a partir das páginas geradas + páginas estruturais mantidas à mão.

Para cada .html no output (recursivo) monta um <url> com loc, lastmod, changefreq
e priority. O lastmod usa a data do último commit git do arquivo no repositório,
com fallback para o mtime do arquivo se o git falhar.

As páginas estruturais (home e índices de seção artigos/, testes/, casos/) são
mantidas manualmente fora do pipeline, por isso são incluídas mesmo quando não
estão presentes no diretório de output (ex.: builds de verificação em /tmp).
"""

import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BASE_URL = "https://amorfy.com.br"

# Páginas estruturais mantidas manualmente (fora do pipeline _gen).
STRUCTURAL = ["index.html", "artigos/index.html", "testes/index.html", "casos/index.html"]

# Páginas que não devem entrar no sitemap (página de erro, etc.).
EXCLUDE = {"404.html"}

# Group rank (para ordenação) + priority + changefreq por tipo de página.
# Preserva o mapeamento do sitemap atual (sitemap.xml).
def _entry(rel):
    """Retorna (group_rank, url_path, priority, changefreq) para um .html relativo ao output."""
    rel = rel.as_posix()
    if rel == "index.html":
        return 0, "/", "1.0", "weekly"
    if "/" not in rel:
        # Páginas estáticas na raiz.
        if rel == "sobre.html":
            return 1, "/" + rel, "0.5", "monthly"
        if rel in ("privacidade.html", "termos.html"):
            return 1, "/" + rel, "0.3", "yearly"
        return 1, "/" + rel, "0.5", "monthly"
    section, name = rel.split("/", 1)
    group = {"artigos": 2, "testes": 3, "casos": 4}.get(section, 5)
    if name == "index.html":
        # Índices de seção: artigos/ e testes/ = 0.9, casos/ = 0.8 (conforme sitemap atual).
        priority = "0.9" if section != "casos" else "0.8"
        return group, f"/{section}/", priority, "weekly"
    priority = {"artigos": "0.8", "testes": "0.8", "casos": "0.7"}.get(section, "0.5")
    return group, f"/{section}/{name}", priority, "monthly"


def _lastmod(rel, output):
    """Data (YYYY-MM-DD) do último commit git do arquivo; fallback: mtime."""
    rel_str = rel.as_posix()
    try:
        r = subprocess.run(
            ["git", "-C", str(REPO), "log", "-1", "--format=%cs", "--", rel_str],
            capture_output=True, text=True,
        )
        if r.returncode == 0:
            dates = [line.strip() for line in r.stdout.splitlines() if line.strip()]
            if dates:
                return dates[0]
    except Exception:
        pass
    # Fallback: mtime do arquivo (no output se existir, senão no repositório).
    candidate = output / rel
    if not candidate.exists():
        candidate = REPO / rel
    if candidate.exists():
        return datetime.fromtimestamp(candidate.stat().st_mtime, tz=timezone.utc).strftime("%Y-%m-%d")
    # Último recurso: data de hoje (UTC).
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def write_sitemap(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)

    rels = {p.relative_to(output) for p in output.rglob("*.html")}
    rels.difference_update({Path(e) for e in EXCLUDE})
    # Garante que as páginas estruturais mantenham-se presentes.
    for s in STRUCTURAL:
        rels.add(Path(s))

    entries = []
    for rel in rels:
        group, url_path, priority, changefreq = _entry(rel)
        lastmod = _lastmod(rel, output)
        entries.append((group, url_path, priority, changefreq, lastmod))

    entries.sort(key=lambda e: (e[0], e[1]))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for _group, url_path, priority, changefreq, lastmod in entries:
        loc = BASE_URL + url_path
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append(f"    <changefreq>{changefreq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")

    path = output / "sitemap.xml"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"OK {path} ({len(entries)} URLs)")


if __name__ == "__main__":
    import sys
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO
    write_sitemap(out)
