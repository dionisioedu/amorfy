# Publicação incremental do Amorfy — leia antes de usar

## Para que serve (e para que NÃO serve)

Este script existe para as **próximas** publicações de conteúdo, não para
retroagir as que já foram.

Ele **não** conserta o histórico de commits passado. Os artigos que já estão
no site continuam commitados nos mesmos dias em que foram criados. Nenhum
script local muda isso.

## O contexto do histórico (o que descobrimos)

```
19 commits em 2025-02/2025-03   → projeto original (quiz interativo: sons,
                                   progress bar, hearts, AdSense inicial)
19 meses de silêncio             → 2025-03 até 2026-09
38 commits em 2026-09/2026-10   → reconstrução completa como portal de artigos
```

Esse intervalo, mais do que qualquer coisa no código, é o sinal mais forte de
"site reativado e inundado de conteúdo". Mas ele está no **git**, não no site.
O Google avalia o site ao vivo — e aí já corrigimos as datas, o sitemap e a
autoria.

## O que REALMENTE importa (em ordem de impacto)

1. **Datas das páginas (datePublished)** — já corrigidas. É isso que o
   Google lê e indexa. Um site com páginas datadas de mai-set/2026 lê como
   "publicando ao longo de meses". ✓
2. **lastmod no sitemap** — já corrigido, agora varia por página. ✓
3. **Tráfego real no GSC** — o que falta. Nenhum script resolve; é
   divulgação (ver DIVULGACAO.md).
4. **Histórico de commits do git** — impacto marginal. Um revisor humano do
   AdSense raramente abre o repo. Não vale reescrever histórico por isso.

## Como usar para publicações futuras

Toda vez que você gerar conteúdo novo (via `_gen/build.py`), **não** commite
tudo de uma vez. Use este script:

```bash
# ver o plano sem commitar
bash _gen/incremental_publish.sh --dry-run

# publicar um lote (um commit por execução)
bash _gen/incremental_publish.sh
```

Depois de cada lote, espere 2-4 dias antes de rodar de novo. Cada execução
publica **um** lote e para.

⚠️ Os lotes atuais referenciam arquivos que **já existem** no repo. Para
conteúdo novo, edite o array `LOTES` no script com os caminhos dos arquivos
novos antes de rodar.

## Regra de ouro para o futuro

Ao adicionar N artigos novos:
- Commite em `ceil(N/4)` lotes temáticos, não em 1 commit.
- Um por vez, com 2-4 dias de intervalo.
- Mensagem de commit descritiva (o changelog público conta como atividade
  editorial contínua).

O objetivo é que, daqui a 3 meses, o histórico mostre atividade distribuída —
não picos.
