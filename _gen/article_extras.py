#!/usr/bin/env python3
"""Metadados extras (categorias + imagem hero) aplicados a todos os artigos por slug.

Centraliza o retag de artigos antigos e o mapeamento de imagens, sem editar os
dicts originais dos batches. build.py aplica EXTRAS[slug] sobre cada artigo.
"""
EXTRAS = {
    # --- antigos (relacionamentos) ---
    "linguagens-do-amor": {"categories": ["relacionamentos"]},
    "fases-relacionamento": {"categories": ["relacionamentos"]},
    "sexualidade": {"categories": ["relacionamentos"]},
    "inteligencia-emocional": {"categories": ["relacionamentos"]},
    "comunicacao": {"categories": ["relacionamentos"]},
    "autoconhecimento": {"categories": ["relacionamentos"]},
    "traumas": {"categories": ["relacionamentos"]},
    "conflitos": {"categories": ["relacionamentos"]},
    "tracos-carater": {"categories": ["relacionamentos"]},
    "mitos-amor": {"categories": ["relacionamentos"]},
    "confianca": {"categories": ["relacionamentos"]},
    "temperamentos": {"categories": ["relacionamentos"]},
    # --- antigos (temas específicos) ---
    "borderline": {"categories": ["borderline"]},
    "relacionamento-borderline": {"categories": ["borderline", "relacionamentos"]},
    "narcisismo": {"categories": ["narcisismo"]},
    # --- novos (narcisismo) ---
    "coparentalidade-com-narcisista": {"categories": ["narcisismo"]},
    "filhos-de-pais-narcisistas": {"categories": ["narcisismo"]},
    "como-sair-de-relacao-com-narcisista": {"categories": ["narcisismo"]},
    # --- novos (borderline) ---
    "borderline-na-familia": {"categories": ["borderline"]},
    "tenho-borderline-e-quero-amar": {"categories": ["borderline"]},
    "desregulacao-emocional-no-casal": {"categories": ["borderline"]},
    # --- novos (bipolaridade) ---
    "amando-alguem-com-bipolaridade": {"categories": ["bipolaridade"]},
    "vivendo-e-amando-com-bipolaridade": {"categories": ["bipolaridade"]},
    "bipolaridade-em-casa-guia-familia": {"categories": ["bipolaridade"]},
    # --- novos (relacionamentos) ---
    "libidos-diferentes-no-casal": {"categories": ["relacionamentos"]},
    "sexualidade-alem-da-norma-lgbtqia": {"categories": ["relacionamentos"]},
    "estilos-de-apego-no-amor": {"categories": ["relacionamentos"]},
}


def apply_extras(article):
    """Retorna uma cópia do artigo com categorias + imagem hero injetadas."""
    slug = article["slug"]
    extra = EXTRAS.get(slug, {})
    merged = dict(article)
    merged.update(extra)
    if "image" not in merged:
        merged["image"] = f"/images/{slug}.svg"
    return merged
