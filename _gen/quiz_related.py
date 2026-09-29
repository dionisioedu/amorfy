#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mapeia cada artigo a um teste relacionado (faixa "Teste relacionado" no topo).

Aplicado via apply_related() no build.py, logo após apply_extras(). Mantém os
dicts dos artigos focados no texto e centraliza a curadoria de cross-sell
artigo → teste aqui.
"""

# Título + gancho + emoji de cada teste (para a faixa de sugestão).
QUIZZES = {
    "personalidade-amorosa": {"title": "Teste de Personalidade Amorosa", "emoji": "🎭", "tagline": "Descubra seu temperamento no amor em 10 perguntas."},
    "linguagem-do-amor": {"title": "Qual é a sua Linguagem do Amor?", "emoji": "💬", "tagline": "Saiba como você dá e recebe amor."},
    "narcisista": {"title": "Você Está em um Relacionamento Narcisista?", "emoji": "🚩", "tagline": "Identifique sinais de abuso narcisista."},
    "compatibilidade": {"title": "Teste de Compatibilidade Amorosa", "emoji": "💞", "tagline": "Meça a compatibilidade real do seu casal."},
    "borderline": {"title": "Você Tem Traços de Borderline?", "emoji": "🎢", "tagline": "Autoavaliação informativa sobre o TPB."},
    "parceiro-borderline": {"title": "Seu Parceiro Tem Traços de Borderline?", "emoji": "🌊", "tagline": "Entenda as oscilações de quem você ama."},
    "meus-tracos-narcisistas": {"title": "Você Tem Traços Narcisistas?", "emoji": "🪞", "tagline": "Olhe para o próprio padrão com honestidade."},
    "parceiro-pronto-relacionamento": {"title": "Seu Parceiro Está Pronto para um Relacionamento?", "emoji": "⏳", "tagline": "Avalie a disponibilidade emocional dele(a)."},
    "por-que-afasto-pessoas": {"title": "Por Que Eu Afasto as Pessoas?", "emoji": "🚪", "tagline": "Nomeie o padrão que sabota suas relações."},
    "autossabotagem-amorosa": {"title": "Você Sabota Seus Relacionamentos?", "emoji": "🧨", "tagline": "Descubra se você boicota o próprio amor."},
    "ciume-inveja-relacionamento": {"title": "Ciúme ou Inveja no Relacionamento?", "emoji": "💚💔", "tagline": "Entenda o que move suas emoções."},
    "red-flags-precoces": {"title": "Red Flags no Início do Relacionamento", "emoji": "⚠️", "tagline": "Veja os sinais de alerta dos primeiros encontros."},
}

# artigo → teste
RELATE = {
    # relacionamentos
    "linguagens-do-amor": "linguagem-do-amor",
    "fases-relacionamento": "compatibilidade",
    "sexualidade": "compatibilidade",
    "inteligencia-emocional": "personalidade-amorosa",
    "comunicacao": "compatibilidade",
    "autoconhecimento": "personalidade-amorosa",
    "traumas": "por-que-afasto-pessoas",
    "conflitos": "compatibilidade",
    "tracos-carater": "por-que-afasto-pessoas",
    "mitos-amor": "compatibilidade",
    "confianca": "ciume-inveja-relacionamento",
    "temperamentos": "personalidade-amorosa",
    "libidos-diferentes-no-casal": "compatibilidade",
    "sexualidade-alem-da-norma-lgbtqia": "compatibilidade",
    "estilos-de-apego-no-amor": "por-que-afasto-pessoas",
    "por-que-as-pessoas-traem": "ciume-inveja-relacionamento",
    "descobri-uma-traicao-e-agora": "ciume-inveja-relacionamento",
    "reconstruir-a-confianca-depois-da-traicao": "ciume-inveja-relacionamento",
    "sexo-no-cativeiro": "compatibilidade",
    "casos-e-casos-repensando-a-infidelidade": "ciume-inveja-relacionamento",
    # borderline
    "borderline": "borderline",
    "relacionamento-borderline": "parceiro-borderline",
    "borderline-na-familia": "parceiro-borderline",
    "tenho-borderline-e-quero-amar": "borderline",
    "desregulacao-emocional-no-casal": "borderline",
    # narcisismo
    "narcisismo": "narcisista",
    "coparentalidade-com-narcisista": "narcisista",
    "filhos-de-pais-narcisistas": "meus-tracos-narcisistas",
    "como-sair-de-relacao-com-narcisista": "red-flags-precoces",
    # bipolaridade
    "amando-alguem-com-bipolaridade": "compatibilidade",
    "vivendo-e-amando-com-bipolaridade": "compatibilidade",
    "bipolaridade-em-casa-guia-familia": "compatibilidade",
    # psicanalise
    "amor-proprio-narcisismo-saudavel": "meus-tracos-narcisistas",
    "fantasia-e-desejo-no-casal": "compatibilidade",
    "capacidade-de-ficar-so": "personalidade-amorosa",
    "amor-na-era-dos-aplicativos": "red-flags-precoces",
    "repeticao-compulsiva-no-amor": "autossabotagem-amorosa",
    "amor-e-odio-ambivalencia": "compatibilidade",
    "dependencia-emocional-psicanalise": "parceiro-pronto-relacionamento",
    "transferencia-por-que-nos-apaixonamos": "personalidade-amorosa",
    "arte-de-amar-erich-fromm": "compatibilidade",
    "ciume-o-que-ele-revela": "ciume-inveja-relacionamento",
    "medo-de-amar-contraintimidade": "por-que-afasto-pessoas",
    "luto-do-termino": "personalidade-amorosa",
}


def apply_related(article):
    """Anexa `related_quiz` (dict com slug/title/tagline/emoji) ao artigo."""
    slug = article.get("slug")
    quiz_slug = RELATE.get(slug)
    if quiz_slug and quiz_slug in QUIZZES:
        merged = dict(article)
        merged["related_quiz"] = {"slug": quiz_slug, **QUIZZES[quiz_slug]}
        return merged
    return article
