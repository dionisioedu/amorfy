#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera um card de compartilhamento (OG, 1200×630) único por página.

Lê o <title> de cada .html publicado, aplica o branding warm editorial do
Amorfy e grava /og/<chave>.png. O caminho da imagem por página é derivado do
path (ex.: artigos/narcisismo.html → /og/artigos-narcisismo.png), então os
templates só precisam referenciar esse path determinístico.

Home (index.html na raiz) e 404 mantêm o og.png genérico de marca.
"""
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og"
W, H = 1200, 630

FONT_DIR = ROOT / "_gen" / "fonts"
FRAUNCES = str(FONT_DIR / "fraunces-v38-latin-700.ttf")   # display serif (marca)
LORA = str(FONT_DIR / "lora-v37-latin-500.ttf")           # serif (corpo)
INTER = str(FONT_DIR / "inter-v20-latin-600.ttf")         # sans (labels)
# fallbacks (se as fontes da marca não estiverem presentes)
_FALLBACK_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
_FALLBACK_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def _font(path, size, fallback):
    import os
    return ImageFont.truetype(path if os.path.exists(path) else fallback, size)

# Tokens da marca (css/style.css)
BG = (250, 246, 241)      # --bg warm paper
TEXT = (51, 34, 43)       # --text
ROSE = (193, 58, 88)      # --rose
ROSE_DARK = (160, 37, 69)
PURPLE = (123, 79, 181)   # --purple
PURPLE_DARK = (93, 58, 145)
GOLD = (217, 142, 43)     # --gold
MUTED = (150, 130, 138)   # texto secundário

EMOJI_RE = re.compile(r'[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u200D\u2B00-\u2BFF]')


def clean_title(t):
    t = re.sub(r'\s*[—|–-]\s*Amorfy.*$', '', t or '')
    t = EMOJI_RE.sub('', t)
    return re.sub(r'\s+', ' ', t).strip()


def detect(path):
    p = path.replace('\\', '/')
    if p.startswith('artigos/'):
        return 'ARTIGO', ROSE
    if p.startswith('testes/'):
        return 'TESTE', PURPLE
    if p.startswith('casos/'):
        return 'CASO REAL', GOLD
    if p.startswith('temas/'):
        return 'TEMA', ROSE
    if p == 'perguntas-frequentes.html':
        return 'FAQ', PURPLE
    if p == 'sobre.html':
        return 'SOBRE', ROSE
    return 'AMORFY', ROSE


def key_of(path):
    p = path.replace('\\', '/')
    if p.endswith('.html'):
        p = p[:-5]
    return p.replace('/', '-')


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        trial = (cur + ' ' + w).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_heart(d, cx, cy, s, color):
    r = s
    d.ellipse([cx - r, cy - r, cx, cy], fill=color)
    d.ellipse([cx, cy - r, cx + r, cy], fill=color)
    d.polygon([(cx - r, cy - r * 0.42), (cx + r, cy - r * 0.42), (cx, cy + r)], fill=color)


def card(title, eyebrow, accent):
    img = Image.new('RGB', (W, H), BG)

    # gradiente suave (rose → purple) no topo-direita
    glow = Image.new('RGB', (W, H), BG)
    gd = ImageDraw.Draw(glow)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        gd.line([(i, 0), (i, H)], fill=(r, g, b))
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    img = Image.blend(img, glow, 0.16)

    d = ImageDraw.Draw(img)

    # barra de acento inferior (gradiente rose → purple)
    bar = Image.new('RGB', (W, 16))
    bd = ImageDraw.Draw(bar)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        bd.line([(i, 0), (i, 16)], fill=(r, g, b))
    img.paste(bar, (0, H - 16))

    # ---- topo: coração + wordmark (esquerda) / eyebrow (direita) ----
    draw_heart(d, 96, 92, 20, ROSE)
    f_word = _font(FRAUNCES, 46, _FALLBACK_SERIF)
    d.text((132, 64), 'Amorfy', font=f_word, fill=ROSE)

    f_eyebrow = _font(INTER, 26, _FALLBACK_SANS)
    eb_w = d.textlength(eyebrow, font=f_eyebrow)
    d.text((W - 88 - eb_w, 76), eyebrow, font=f_eyebrow, fill=accent)

    # ---- título grande, serif, até 3 linhas ----
    max_w = W - 176
    for size in (76, 68, 60, 52, 46):
        f_title = _font(FRAUNCES, size, _FALLBACK_SERIF)
        lines = wrap(d, title, f_title, max_w)
        if len(lines) <= 3:
            break

    line_h = int(size * 1.18)
    total_h = line_h * len(lines)
    # centraliza verticalmente o bloco de título no espaço útil
    y0 = (H - 16 - total_h) / 2 + 20
    for i, ln in enumerate(lines):
        d.text((88, y0 + i * line_h), ln, font=f_title, fill=TEXT)

    return img


def gen_all():
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for f in sorted(ROOT.rglob('*.html')):
        rel = f.relative_to(ROOT).as_posix()
        if rel.startswith('_gen/'):
            continue
        if rel in ('index.html', '404.html'):
            continue
        html = f.read_text(encoding='utf-8')
        m = re.search(r'<title>(.*?)</title>', html, re.S)
        if not m:
            continue
        title = clean_title(m.group(1))
        if not title:
            continue
        eyebrow, accent = detect(rel)
        img = card(title, eyebrow, accent)
        out = OUT / f'{key_of(rel)}.png'
        img.save(out, 'PNG', optimize=True)
        count += 1
    print(f'{count} OG cards gerados em {OUT}')


if __name__ == '__main__':
    gen_all()
