#!/usr/bin/env bash
# Publicação incremental do Amorfy — evita o padrão "tudo no mesmo dia".
#
# Por que existe:
#   O Google/AdSense penaliza sites cujo histórico de git/histórico de
#   publicação mostra dezenas de páginas subindo em um único commit. O sinal
#   que procuram é "curadoria e manutenção contínuas" — ou seja, atividade
#   distribuída no tempo.
#
# O que faz:
#   Reenvia em lotes (grupos de páginas afins), com espaçamento de dias entre
#   cada commit. Cada commit tem uma mensagem de changelog real (não "update"),
#   porque o Google lê a página /commits do repo público como sinal de atividade
#   editorial.
#
# Como usar:
#   1. Revise os lotes abaixo (ordem e conteúdo).
#   2. Rode:  bash _gen/incremental_publish.sh --dry-run
#      para ver o plano sem commitar nada.
#   3. Rode:  bash _gen/incremental_publish.sh
#      O script faz um commit por lote e para. Agende as execuções
#      (cron / manualmente) com 2-4 dias de intervalo.
#
# IMPORTANTE: o script NÃO usa 'git add -A' — ele adiciona apenas os arquivos
# do lote corrente. Isso garante que cada commit seja limpo e coeso.

set -euo pipefail
cd "$(dirname "$0")/.."

DRY_RUN=0
[ "${1:-}" = "--dry-run" ] && DRY_RUN=1

# ---------------------------------------------------------------------------
# Lotes de publicação. Cada lote = uma linha "titulo|lote_idx|arquivo1 arquivo2 ..."
# Os arquivos são relativos à raiz do repo.
#
# A estratégia: começar pelos TEMAS (que agregam os artigos, ficam com
# interlink forte) e quizzes de maior apelo, depois soltar os artigos em
# lotes temáticos menores a cada 2-3 dias.
# ---------------------------------------------------------------------------
LOTES=(
  # --- Lote 1: pilares (temas + hubs) ---
  "Pilares temáticos: hubs de narcisismo, borderline, bipolaridade, psicanálise e relacionamentos|temas/*.html"

  # --- Lote 2: quizzes de maior apelo ---
  "Testes de autoconhecimento: linguagens do amor, narcisista, red flags, traços narcisistas|testes/linguagem-do-amor.html testes/narcisista.html testes/red-flags-precoces.html testes/meus-tracos-narcisistas.html"

  # --- Lote 3: cluster narcisismo ---
  "Cluster narcisismo: identificar, sair, filhos, co-parentalidade, amor-próprio|artigos/narcisismo.html artigos/como-sair-de-relacao-com-narcisista.html artigos/filhos-de-pais-narcisistas.html artigos/coparentalidade-com-narcisista.html artigos/amor-proprio-narcisismo-saudavel.html"

  # --- Lote 4: cluster apego/psicanálise ---
  "Psicanálise do amor: apego, repetição, transferência, dependência emocional|artigos/estilos-de-apego-no-amor.html artigos/repeticao-compulsiva-no-amor.html artigos/dependencia-emocional-psicanalise.html artigos/arte-de-amar-erich-fromm.html artigos/medo-de-amar-contraintimidade.html"

  # --- Lote 5: infidelidade/confiança ---
  "Confiança e infidelidade: motivações, descoberta e reconstrução|artigos/por-que-as-pessoas-traem.html artigos/descobri-uma-traicao-e-agora.html artigos/reconstruir-a-confianca-depois-da-traicao.html artigos/casos-e-casos-repensando-a-infidelidade.html artigos/confianca.html"

  # --- Lote 6: cluster borderline/bipolaridade ---
  "Saúde mental no vínculo: borderline e bipolaridade na família e no casal|artigos/relacionamento-borderline.html artigos/borderline.html artigos/borderline-na-familia.html artigos/tenho-borderline-e-quero-amar.html artigos/amando-alguem-com-bipolaridade.html artigos/bipolaridade-em-casa-guia-familia.html"

  # --- Lote 7: sexualidade e conexão ---
  "Sexualidade e conexão: desejo, libido, fantasia e intimidade|artigos/sexualidade.html artigos/sexualidade-alem-da-norma-lgbtqia.html artigos/libidos-diferentes-no-casal.html artigos/fantasia-e-desejo-no-casal.html artigos/sexo-no-cativeiro.html artigos/sexualidade-e-conexao.html"

  # --- Lote 8: habilidades relacionais ---
  "Habilidades: comunicação, conflitos, ciúme, inteligência emocional|artigos/comunicacao.html artigos/conflitos.html artigos/ciume-o-que-ele-revela.html artigos/inteligencia-emocional.html artigos/desregulacao-emocional-no-casal.html"

  # --- Lote 9: autoconhecimento e ciclo de vida ---
  "Autoconhecimento e ciclo do amor: fases, luto, ficar só, autoconhecimento|artigos/autoconhecimento.html artigos/fases-relacionamento.html artigos/luto-do-termino.html artigos/capacidade-de-ficar-so.html artigos/mitos-amor.html"

  # --- Lote 10: casos reais ---
  "Casos reais: histórias de recuperação e reconstrução|casos/*.html"
)

echo "=========================================="
echo " Publicação incremental do Amorfy"
echo " Modo: $([ $DRY_RUN -eq 1 ] && echo 'DRY-RUN (nada será commitado)' || echo 'EXECUÇÃO REAL')"
echo " Lotes definidos: ${#LOTES[@]}"
echo "=========================================="
echo

for i in "${!LOTES[@]}"; do
  entry="${LOTES[$i]}"
  msg="${entry%%|*}"
  files="${entry#*|}"
  n=$(($i + 1))

  echo "--- Lote $n/${#LOTES[@]} ---"
  echo "  Mensagem : $msg"
  echo "  Arquivos : $files"

  if [ $DRY_RUN -eq 1 ]; then
    # shellcheck disable=SC2086
    matched=$(ls -1 $files 2>/dev/null | wc -l | tr -d ' ')
    echo "  Encontrados: $matched arquivo(s)"
    echo
    continue
  fi

  # shellcheck disable=SC2086
  git add $files

  if git diff --cached --quiet; then
    echo "  (nada novo para commitar neste lote — pulando)"
    echo
    continue
  fi

  git commit -q -m "$msg"
  echo "  ✓ commit criado: $(git log -1 --format=%h)"
  echo
  echo "  → Próximo lote deve ser publicado em 2-4 dias."
  echo "    Rode novamente para publicar o lote $((n + 1))."
  echo
  echo "=========================================="
  echo " Um lote por execução. Encerrando."
  echo "=========================================="
  exit 0
done

echo "Todos os lotes já foram publicados (ou nada pendente)."
