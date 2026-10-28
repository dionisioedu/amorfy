# Rede de profissionais — análise e operação

Análise do código e do conteúdo em 28/10/2026. Não houve acesso a métricas de tráfego ou conversão; os pontos abaixo são observações do percurso disponível, não estimativas de pacientes ou receita.

## Oportunidade identificada

- A home já oferece busca e conteúdo recente; artigos sobre convivência, limites e autoconhecimento dão contexto para um convite discreto à busca por atendimento.
- O percurso encerrava na leitura, em um teste ou em links de publicidade. Faltavam perfis profissionais e contato de atendimento.
- A autoria atual identifica Eduardo Dionisio como engenheiro de software e pesquisador de conteúdo. Essa identificação não comprova uma formação clínica. Não alterar a biografia editorial nem atribuir habilitações sem os dados corretos.
- Os quizzes são de reflexão/entretenimento, alguns incluem linguagem de saúde mental. Não usar pontuação, respostas ou rótulos de resultados para direcionar pacientes ou anunciar necessidade de tratamento.
- As imagens ilustrativas, relatos do site e conteúdo editorial não constituem depoimentos de pacientes dos profissionais. Não reutilizá-los como prova de eficácia.

## Percurso implementado

Home/artigo → /profissionais/ → perfil individual → WhatsApp ou e-mail autorizado.

A página de rede reúne orientações, critérios de apresentação e um canal para profissionais solicitarem inclusão. O perfil mostra nome, título, formação, registro quando aplicável, público, modalidade, localização e contato. O vínculo com o site é público. A ordem é alfabética, sem pontuação ou ranking de qualidade.

O responsável informou atuação em Psicanálise e atendimento exclusivamente remoto por videochamada para Eduardo e Alice. Os perfis usam esses dados declarados; formação específica e público atendido permanecem explicitamente não informados. Não há selo de verificação de credenciais nem declaração de especialidades. Eduardo usa o nome já presente na autoria do site. Atualizar os detalhes quando forem fornecidos.

## Ativar um perfil

Editar `_gen/professionals/profiles.json`. Os campos de texto são escapados pelo gerador; não usar HTML.

1. Registrar nome profissional, título declarado, formação, público, modalidade e localização. Se formação específica ou público ainda não tiverem sido fornecidos, indicar explicitamente essa ausência no perfil e orientar o leitor a consultar o profissional; nunca inventar uma qualificação.
2. Para Psicologia, confirmar o CRP e a identificação profissional no cadastro oficial. Para outras práticas, descrever a formação específica sem equiparar automaticamente a Psicologia ou Medicina. A validação de formato no código não verifica a validade de registro.
3. Confirmar autorização de divulgação dos dados públicos e da fotografia. Não armazenar documentos comprobatórios, diplomas completos ou dados de pacientes no repositório.
4. Usar `kind`: `psicologia`, `psicanalise` ou `terapia`; `modes`: `Online` e/ou `Presencial`; `relationship`: `owner` (responsável pelo site) ou `partner`.
5. `contact_url` deve ser HTTPS sem parâmetros. Para WhatsApp: `https://wa.me/55DDDNUMERO`. O e-mail tem seu campo próprio. Não incluir sintomas, respostas de teste ou mensagens pré-preenchidas nos links.
6. Preencher `reviewed_on` com a data real da conferência editorial, `consent_publication: true` e somente então `published: true`.
7. Rodar `python -B _gen/build.py` e `python -B -m unittest discover -s tests -p 'test_*.py'`. Conferir página, contato e identificação antes de publicar o commit.

O avatar provisório é uma silhueta identificada como “Foto em breve”, não uma fotografia de terceiro.

## Privacidade e operação

Não há banco de leads, formulário clínico, pixel publicitário ou envio de respostas dos testes no diretório. O cabeçalho de referência é suprimido na navegação externa das páginas profissionais. A hospedagem e os serviços de contato podem manter seus registros técnicos; não prometer anonimato absoluto.

O contato é direto: agenda, honorários, atendimento e política de cancelamento pertencem ao profissional. Não há comissão por paciente implementada, cobrança ou promessa de resultado. Qualquer futuro modelo comercial deve ter condições e vínculos claramente informados e revisão das regras aplicáveis antes de entrar em operação.

Para avaliar a captação inicialmente, cada profissional pode registrar, de forma agregada e sem relatos clínicos, quantos contatos espontaneamente mencionam o Amorfy e quantos se tornam agendamentos. Isso não está automatizado. Não atribuir conversão a dados do navegador sem uma política e implementação específicas.

Para retirar um perfil já publicado: marcar como inativo, regenerar o site e remover apenas seu HTML público antigo em um commit revisado. O build não apaga arquivos antigos automaticamente.

## Fontes de referência

- CRP: publicidade profissional, identificação e títulos: https://transparencia.cfp.org.br/crp10/pergunta-frequente/publicidade-profissional/
- Cadastro Nacional de Psicólogas e Psicólogos: https://cadastro.cfp.org.br/
- ANPD, dados pessoais sensíveis: https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/glossario-anpd

Não foram implementados depoimentos clínicos, promoções de preço, promessas de cura ou declarações de “melhor profissional”.
