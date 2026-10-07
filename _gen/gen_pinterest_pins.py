#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera pins verticais para Pinterest (1000×1500) a partir dos OG cards.

Pinterest favorece 2:3 vertical. Reusa exatamente o branding do
gen_og_cards.py (mesmas fontes, mesmos tokens de cor, mesmo gradiente)
e adiciona os ganchos de copy (subtítulo + lista de bullets) que
aumentam o save-rate no Pinterest.

Uso:
    python3 _gen/gen_pinterest_pins.py

Grava em /pinterest/<slug>.png. As definições vivem em PINS abaixo —
fonte única de verdade para título/subtítulo/bullets de cada pin.
"""
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "pinterest"
W, H = 1000, 1500

FONT_DIR = ROOT / "_gen" / "fonts"
FRAUNCES = str(FONT_DIR / "fraunces-v38-latin-700.ttf")
LORA = str(FONT_DIR / "lora-v37-latin-500.ttf")
INTER = str(FONT_DIR / "inter-v20-latin-600.ttf")
_FALLBACK_SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
_FALLBACK_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

# Tokens da marca (idênticos a css/style.css e gen_og_cards.py)
BG = (250, 246, 241)
TEXT = (51, 34, 43)
ROSE = (193, 58, 88)
ROSE_DARK = (160, 37, 69)
PURPLE = (123, 79, 181)
GOLD = (217, 142, 43)
MUTED = (150, 130, 138)

# ---- Definições dos 10 pins -------------------------------------------------
# (slug, eyebrow, cor, título, subtítulo, [bullets], url_curta)
PINS = [
    ("linguagens-do-amor", "GUIA COMPLETO", ROSE,
     "As 5 Linguagens do Amor",
     "Descubra como você ama e como quer ser amado",
     ["Palavras de afirmação", "Tempo de qualidade", "Presentes", "Atos de serviço", "Toque físico"],
     "amorfy.com.br"),

    ("relacionamento-narcisista", "TESTE GRATUITO", PURPLE,
     "Você Está em um Relacionamento Narcisista?",
     "7 sinais que a maioria demora anos para perceber",
     ["Você duvida da sua memória", "A culpa sempre sobra pra você", "Ele nunca pede desculpas de verdade", "Você se isolou sem perceber"],
     "amorfy.com.br"),

    ("estilos-de-apego", "PSICOLOGIA DO AMOR", ROSE,
     "Estilos de Apego no Amor",
     "Por que você reage assim quando ama",
     ["Ansioso", "Evitativo", "Seguro", "Desorganizado"],
     "amorfy.com.br"),

    ("luto-do-termino", "SUPERAÇÃO", GOLD,
     "O Luto do Término",
     "Por que dói tanto perder um amor",
     ["Perder um amor é um luto real", "As fases não são lineares", "Dói no corpo, não só na alma", "Como atravessar sem se perder"],
     "amorfy.com.br"),

    ("dependencia-emocional", "PSICANÁLISE", PURPLE,
     "Dependência Emocional",
     "O amor que vicia — e como se libertar",
     ["Por que você não consegue ir embora", "O que a psicanálise diz", "Autonomia sem perder o vínculo", "Passos práticos"],
     "amorfy.com.br"),

    ("red-flags-precoces", "TESTE DE SINAIS", ROSE,
     "Red Flags no Início do Relacionamento",
     "Os sinais que a gente ignora e depois se arrepende",
     ["Pressa excessiva para compromisso", "Ciúme disfarçado de cuidado", "Desprezo disfarçado de piada", "Isolamento gradual"],
     "amorfy.com.br"),

    ("ciume", "AUTOCONHECIMENTO", PURPLE,
     "Ciúme",
     "O que ele revela sobre você e sua história",
     ["O ciúme fala mais de você que do outro", "Raiz na autoestima, não no outro", "Como sair do ciclo", "Quando vira controle"],
     "amorfy.com.br"),

    ("borderline-relacionamentos", "GUIA COM EMPATIA", ROSE,
     "Borderline e Relacionamentos",
     "Sustentar um vínculo sem se perder no cuidado",
     ["Entenda o medo do abandono", "Como reagir a uma crise", "Limites sem abandonar", "Quando buscar ajuda profissional"],
     "amorfy.com.br"),

    ("repeticao-no-amor", "RUMO CERTO", PURPLE,
     "Por Que Repetimos o Mesmo Tipo de Relacionamento?",
     "A compulsão à repetição explicada",
     ["Por que escolhemos o mesmo perfil", "O que a psicanálise revela", "Como identificar seu padrão", "Como quebrar o ciclo"],
     "amorfy.com.br"),

    ("amor-proprio", "AMOR-PRÓPRIO", GOLD,
     "Amor-Próprio Não É Egoísmo",
     "Narcisismo saudável e a capacidade de amar",
     ["A base de todo relacionamento maduro", "Diferença entre egoísmo e autoestima", "Como desenvolver", "Sem culpa"],
     "amorfy.com.br"),
]


def _font(path, size, fallback):
    import os
    return ImageFont.truetype(path if os.path.exists(path) else fallback, size)


def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
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


def pin(title, subtitle, bullets, eyebrow, accent, url):
    img = Image.new("RGB", (W, H), BG)

    # gradiente suave rose → purple (blur, blend leve) — assinatura da marca
    glow = Image.new("RGB", (W, H), BG)
    gd = ImageDraw.Draw(glow)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        gd.line([(i, 0), (i, H)], fill=(r, g, b))
    glow = glow.filter(ImageFilter.GaussianBlur(90))
    img = Image.blend(img, glow, 0.14)

    d = ImageDraw.Draw(img)

    # moldura sutil
    d.rectangle([28, 28, W - 28, H - 28], outline=(232, 222, 226), width=2)

    # ---- topo: coração + wordmark + eyebrow ----
    draw_heart(d, 104, 108, 24, ROSE)
    f_word = _font(FRAUNCES, 54, _FALLBACK_SERIF)
    d.text((148, 76), "Amorfy", font=f_word, fill=ROSE)

    f_eye = _font(INTER, 26, _FALLBACK_SANS)
    eye_w = d.textlength(eyebrow, font=f_eye)
    d.text((W - 104 - eye_w, 88), eyebrow, font=f_eye, fill=accent)

    # divisória
    d.line([(104, 200), (W - 104, 200)], fill=(226, 214, 219), width=2)

    # ---------------------------------------------------------------
    # Medição prévia: calcula a altura de todo o bloco (título + sub +
    # bullets) e centraliza verticalmente entre a divisória (y=200) e
    # o rodapé (H-130). Evita o "buraco" de espaço vazio embaixo.
    # ---------------------------------------------------------------
    max_w = W - 208

    title_size = 48
    for ts in (88, 78, 70, 62, 54, 48):
        f_t = _font(FRAUNCES, ts, _FALLBACK_SERIF)
        if len(wrap(d, title, f_t, max_w)) <= 5:
            title_size = ts
            break
    f_title = _font(FRAUNCES, title_size, _FALLBACK_SERIF)
    title_lines = wrap(d, title, f_title, max_w)
    title_block_h = int(title_size * 1.16) * len(title_lines)

    f_sub = _font(LORA, 42, _FALLBACK_SERIF)
    sub_lines = wrap(d, subtitle, f_sub, max_w)[:3]
    sub_block_h = 54 * len(sub_lines)

    f_b = _font(INTER, 34, _FALLBACK_SANS)
    bullet_boxes = []
    for b in bullets[:5]:
        blines = wrap(d, b, f_b, max_w - 88)
        bullet_boxes.append((blines, 30 + 48 * len(blines)))
    bullets_h = sum(h + 16 for _, h in bullet_boxes)

    gap_sub = 18
    gap_bullets = 34
    total_h = title_block_h + gap_sub + sub_block_h + gap_bullets + bullets_h

    top = 200
    bottom = H - 130
    y = top + max(0, int(((bottom - top) - total_h) / 2))

    # ---- título ----
    line_h = int(title_size * 1.16)
    for ln in title_lines:
        d.text((104, y), ln, font=f_title, fill=TEXT)
        y += line_h

    y += gap_sub

    # ---- subtítulo ----
    for ln in sub_lines:
        d.text((104, y), ln, font=f_sub, fill=MUTED)
        y += 54

    y += gap_bullets

    # ---- bullets em pill boxes ----
    for blines, box_h in bullet_boxes:
        d.rounded_rectangle([104, y, W - 104, y + box_h], radius=14,
                            fill=(255, 255, 255), outline=(233, 222, 227), width=2)
        d.ellipse([132, y + 26, 158, y + 52], fill=accent)
        ty = y + 16
        for ln in blines:
            d.text((182, ty), ln, font=f_b, fill=TEXT)
            ty += 48
        y += box_h + 16

    # ---- rodapé: barra de acento + url ----
    bar = Image.new("RGB", (W, 18))
    bd = ImageDraw.Draw(bar)
    for i in range(W):
        t = i / W
        r = int(ROSE[0] + (PURPLE[0] - ROSE[0]) * t)
        g = int(ROSE[1] + (PURPLE[1] - ROSE[1]) * t)
        b = int(ROSE[2] + (PURPLE[2] - ROSE[2]) * t)
        bd.line([(i, 0), (i, 18)], fill=(r, g, b))
    img.paste(bar, (0, H - 18))

    f_url = _font(INTER, 32, _FALLBACK_SANS)
    url_w = d.textlength(url, font=f_url)
    d.text(((W - url_w) / 2, H - 92), url, font=f_url, fill=ROSE)

    return img


def gen_all():
    OUT.mkdir(parents=True, exist_ok=True)
    for slug, eyebrow, accent, title, subtitle, bullets, url in PINS:
        img = pin(title, subtitle, bullets, eyebrow, accent, url)
        out = OUT / f"{slug}.png"
        img.save(out, "PNG", optimize=True)
        print(f"OK {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
    print(f"\n{len(PINS)} pins gerados em {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    gen_all()
