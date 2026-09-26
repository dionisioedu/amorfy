# Amorfy 💖

Portal estático sobre relacionamentos, autoconhecimento e psicologia do amor.
O site é servido via GitHub Pages no domínio **amorfy.com.br** e combina
conteúdo educativo (artigos, testes interativos e casos reais) com uma
pipeline de geração de páginas em Python (somente biblioteca padrão).

## Estrutura

```
.
├── artigos/               # 15 artigos (gerados pela pipeline)
├── testes/                # 6 testes interativos (gerados pela pipeline)
├── casos/                 # 4 histórias reais (geradas pela pipeline)
├── css/style.css          # estilos do site
├── js/                    # main.js (menu/navegação) e quiz.js (lógica dos testes)
├── _gen/                  # pipeline de geração (Python stdlib-only)
│   ├── build.py           # orquestra a geração de todas as páginas
│   ├── article_template.py
│   ├── quiz_template.py
│   ├── static_pages.py    # sobre, privacidade e termos
│   └── batch1..3.py, borderline_artigo.py, manual_batch.py,
│       quiz_batch1..2.py, borderline_quizzes.py, casos_batch.py  # fontes de conteúdo
├── tests/                 # testes (node --test + unittest)
├── index.html             # página inicial (mantida manualmente)
├── sobre.html, privacidade.html, termos.html, 404.html
├── .github/workflows/test.yml   # CI (testes em push e pull_request)
└── package.json           # scripts de teste
```

### Páginas mantidas manualmente

Estas páginas **não** são geradas pela pipeline e são editadas à mão:

- `index.html`
- `artigos/index.html`
- `testes/index.html`
- `casos/index.html`
- `404.html`

Todo o restante (artigos, testes, casos e as páginas estáticas
sobre/privacidade/termos) é gerado a partir dos módulos em `_gen/`.

## Como gerar conteúdo

O conteúdo vive nos módulos de `_gen/` e as páginas HTML são produzidas por:

```bash
cd _gen && python3 build.py
```

Isso regenera artigos, testes, casos e páginas estáticas diretamente na raiz
do repositório. Para gerar em outro diretório (útil para validação, sem tocar
no site publicado):

```bash
python3 _gen/build.py --output /tmp/amorfy-out
```

Requer apenas Python 3 (biblioteca padrão — sem dependências externas).

## Como rodar os testes

```bash
npm test
# ou diretamente:
node --test tests/*.test.cjs
python3 -m unittest tests.test_generation -v
```

Os testes cobrem:

- navegação e menu (`navigation.test.cjs`);
- lógica dos quizzes (`quiz.test.cjs`);
- integridade da geração: as páginas geradas em um diretório temporário devem
  bater exatamente com o conteúdo publicado, com JSON-LD válido
  (`test_generation.py`);
- anti-drift de cards: todo artigo/quiz/caso deve ter um card com link no seu
  índice (`artigos/index.html`, `testes/index.html`, `casos/index.html`).

## Deploy

O deploy é automático: qualquer `push` na branch `main` publica o site via
GitHub Pages. O workflow de CI (`.github/workflows/test.yml`) roda os testes
em todo `push` e `pull_request` para garantir que a geração está íntegra antes
de publicar.
