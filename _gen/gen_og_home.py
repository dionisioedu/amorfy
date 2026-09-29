#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera o card de marca da home (og.png, 1200×630) — fraunces + inter.

Substitui o og.png genérico antigo. Home (index.html) e 404 usam este card.
"""
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og.png"
W, H = 1200, 630

BG = (250, 246, 241)
TEXT = (51, 34, 43)
ROSE = (193, 58, 88)
PURPLE = (123, 79, 181)
GOLD = (217, 142, 43)
MUTED = (150, 130, 138)

FONT_DIR = ROOT / "_gen" / "fonts"
FRAUNCES = str(FONT_DIR / "fraunces-v38-latin-700.ttf")
INTER = str(FONT_DIR / "inter-v20-latin-600.ttf")
INTER_REG = str(FONT_DIR / "inter-v20-latin-600.ttf")


def font(path, size, fallback):
    return ImageFont.truetype(path if os.path.exists(path) else fallback, size)


F_SERIF_FB = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SANS_FB = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def draw_heart(d, cx, cy, s, color):
    r = s
    d.ellipse([cx - r, cy - r, cx, cy], fill=color)
    d.ellipse([cx, cy - r, cx + r, cy], fill=color)
    d.polygon([(cx - r, cy - r * 0.42), (cx + r, cy - r * 0.42), (cx, cy + r)], fill=color)


def main():
    img = Image.new("RGB", (W, H), BG)

    # glow suave rose → purple
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        gd.line([(i, 0), (i, H)], fill=(r, g, b))
    glow = glow.filter(ImageFilter.GaussianBlur(80))
    img = Image.blend(img, glow, 0.18)

    d = ImageDraw.Draw(img)

    # barra inferior
    bar = Image.new("RGB", (W, 16))
    bd = ImageDraw.Draw(bar)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        bd.line([(i, 0), (i, 16)], fill=(r, g, b))
    img.paste(bar, (0, H - 16))

    # coração grande com glow
    hx, hy, hs = 600, 185, 88
    glow_heart = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ghd = ImageDraw.Draw(glow_heart)
    draw_heart(ghd, hx, hy, hs, (*ROSE, 120))
    glow_heart = glow_heart.filter(ImageFilter.GaussianBlur(28))
    img = Image.alpha_composite(img.convert("RGBA"), glow_heart).convert("RGB")
    d = ImageDraw.Draw(img)
    draw_heart(d, hx, hy, hs, ROSE)

    # wordmark
    f_word = font(FRAUNCES, 150, F_SERIF_FB)
    w = d.textlength("Amorfy", font=f_word)
    d.text(((W - w) / 2, 255), "Amorfy", font=f_word, fill=TEXT)

    # tagline
    f_tag = font(INTER, 32, F_SANS_FB)
    t1 = "Testes, artigos e histórias reais"
    t2 = "sobre relacionamentos e autoconhecimento"
    w1 = d.textlength(t1, font=f_tag)
    w2 = d.textlength(t2, font=f_tag)
    d.text(((W - w1) / 2, 440), t1, font=f_tag, fill=ROSE)
    d.text(((W - w2) / 2, 490), t2, font=f_tag, fill=MUTED)

    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"saved {OUT}")


if __name__ == "__main__":
    main()
