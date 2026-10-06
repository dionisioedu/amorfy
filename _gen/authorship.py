#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Autoria e E-E-A-T do Amorfy — fonte única de verdade.

O Google exige autoria humana identificável para conteúdo YMYL (saúde mental /
psicologia). Aqui ficam o autor, o revisor técnico e os trechos de HTML/JSON-LD
usados por todos os geradores.
"""

import json

AUTHOR_NAME = "Eduardo Dionisio"
AUTHOR_URL = "https://amorfy.com.br/sobre.html"
AUTHOR_ROLE = "Engenheiro de software e pesquisador de conteúdo"

# Revisor técnico (CRP = registro profissional de psicólogo no Brasil).
# IMPORTANTE: confirmar que a pessoa é psicóloga registrada e autorizou o uso
# do nome e do CRP antes de publicar. Enquanto não confirmado, o default
# permanece None e o site cai no fallback "Revisão editorial pela equipe Amorfy".
REVIEWER_NAME = None
REVIEWER_CRP = None

PUBLISHER_NAME = "Amorfy"
PUBLISHER_URL = "https://amorfy.com.br"


def reviewer_display():
    """Nome do revisor com CRP, ou a equipe Amorfy quando não houver revisor."""
    if REVIEWER_NAME and REVIEWER_CRP:
        return f"{REVIEWER_NAME} (CRP {REVIEWER_CRP})"
    return "Equipe Amorfy"


def author_json_block():
    """Bloco JSON-LD (dict) de autoria para Article/Quiz."""
    return {
        "@type": "Person",
        "name": AUTHOR_NAME,
        "url": AUTHOR_URL,
    }


def publisher_json_block():
    return {
        "@type": "Organization",
        "name": PUBLISHER_NAME,
        "url": PUBLISHER_URL,
        "logo": {"@type": "ImageObject", "url": f"{PUBLISHER_URL}/favicon.svg"},
    }


def reviewed_json_block():
    """Bloco reviewedBy: Person se houver revisor nomeado, senão Organization."""
    if REVIEWER_NAME and REVIEWER_CRP:
        return {
            "@type": "Person",
            "name": REVIEWER_NAME,
            "jobTitle": "Psicóloga(o)",
            "identifier": REVIEWER_CRP,
        }
    return {"@type": "Organization", "name": f"{PUBLISHER_NAME} — Equipe editorial"}


def _json(obj):
    return json.dumps(obj, ensure_ascii=False)


# ---- Trechos prontos para os templates -------------------------------------

def article_schema_fields():
    """Linhas JSON-LD adicionais para o <script> do Article (indentadas)."""
    return (
        f'    "author": {_json(author_json_block())},\n'
        f'    "reviewedBy": {_json(reviewed_json_block())},\n'
        f'    "publisher": {_json(publisher_json_block())},'
    )


def quiz_schema_fields():
    """Linhas JSON-LD de autoria para o <script> do Quiz (indentadas)."""
    return (
        f'    "author": {_json(author_json_block())},\n'
        f'    "publisher": {_json(publisher_json_block())}'
    )



def byline_html():
    """Byline visível em páginas de conteúdo."""
    return (
        f'<span>&#9997;&#65039; Por <a href="/sobre.html">{AUTHOR_NAME}</a></span>'
        f'<span>&#128203; Revis&atilde;o: {reviewer_display()}</span>'
    )
