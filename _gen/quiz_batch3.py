#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quizzes batch 3: traços narcisistas (eu), prontidão do parceiro,
por que afasto as pessoas, autossabotagem amorosa, ciúme e inveja,
red flags precoces."""
from quiz_template import write_quiz

# ─────────────────────────────────────────────────────────────────────────
# 1. TRAÇOS NARCISISTAS EM VOCÊ (sum: maior = mais traços)
# ─────────────────────────────────────────────────────────────────────────
MEU_NARCISISMO = {
"slug": "meus-tracos-narcisistas",
"title": "Você Tem Traços Narcisistas? — Teste de Autoconhecimento",
"desc": "Teste honesto de 12 perguntas para identificar traços narcisistas em você mesmo: necessidade de admiração, dificuldade de empatia, reação a críticas. Grátis.",
"breadcrumb": "Traços Narcisistas em Mim",
"h1": "🪞 Você Tem Traços Narcisistas?",
"intro": "Todos temos um pouco de narcisismo. Ele só vira problema quando impede conexões reais. Responda com honestidade brutal — ninguém está vendo.",
"related_text": "Narcisismo não é só sobre o outro: entenda o espectro, a diferença entre traços saudáveis e patológicos, e como trabalhar esses padrões.",
"related_link": "/artigos/narcisismo.html",
"related_label": "Ler: Tudo Sobre Narcisismo",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de traços narcisistas do Amorfy. O resultado me pegou de surpresa:",
  "questions": [
    {"q": "Como você reage a uma crítica, mesmo construtiva?", "options": [
      {"text": "Agradeço e penso se faz sentido", "value": 0},
      {"text": "Fico incomodado(a) mas reflito depois", "value": 1},
      {"text": "Respondo na hora defendendo meu ponto com firmeza", "value": 2},
      {"text": "Sinto como ataque pessoal e não esqueço", "value": 3}
    ]},
    {"q": "Quando alguém te conta um problema, sua primeira reação é...", "options": [
      {"text": "Escutar, perguntar e validar o que a pessoa sente", "value": 0},
      {"text": "Tentar ajudar sugerindo soluções", "value": 1},
      {"text": "Falar de um caso parecido que vivi, maior ainda", "value": 2},
      {"text": "Achar que a pessoa está exagerando ou se vitimizando", "value": 3}
    ]},
    {"q": "Quanto você precisa que as pessoas reconheçam o que você faz?", "options": [
      {"text": "Quase nada — sei o que valho", "value": 0},
      {"text": "Gosto de um elogio, como qualquer um", "value": 1},
      {"text": "Preciso. Se ninguém nota, fico incomodado(a)", "value": 2},
      {"text": "É combustível: sem admiração me sinto vazio(a)", "value": 3}
    ]},
    {"q": "Você já distorceu uma história para parecer o(a) herói dela?", "options": [
      {"text": "Nunca. Conto o que aconteceu", "value": 0},
      {"text": "Dei uma 'ajustada' no tom, sem mentir", "value": 1},
      {"text": "Algumas vezes omiti partes que me desfavoreciam", "value": 2},
      {"text": "Com frequência reescrevo os fatos a meu favor", "value": 3}
    ]},
    {"q": "Como você lida com o sucesso de alguém próximo?", "options": [
      {"text": "Fico genuinamente feliz", "value": 0},
      {"text": "Alegro-me, com um leve aperto no peito", "value": 1},
      {"text": "Comparo com o que ainda não conquistei", "value": 2},
      {"text": "Sinto inveja e procuro o defeito por trás da conquista", "value": 3}
    ]},
    {"q": "Você consegue pedir desculpas de verdade?", "options": [
      {"text": "Sim, sem rodeios, quando errei", "value": 0},
      {"text": "Sim, mas às vezes preciso de tempo", "value": 1},
      {"text": "Prefiro 'me desculpar' com presentes ou gestos", "value": 2},
      {"text": "Raramente. Sempre há um motivo justificável para o que fiz", "value": 3}
    ]},
    {"q": "As pessoas te descrevem como...", "options": [
      {"text": "Acolhedor(a) e fácil de conversar", "value": 0},
      {"text": "Confiante e direto(a)", "value": 1},
      {"text": "Intenso(a), imponente", "value": 2},
      {"text": "Arrogante, competitivo(a) ou difícil de agradar", "value": 3}
    ]},
    {"q": "Quando um relacionamento termina, a culpa costuma ser...", "options": [
      {"text": "De ambos — revejo minha parte", "value": 0},
      {"text": "Nossa, com detalhes que eu erraria de novo", "value": 1},
      {"text": "Principalmente do outro, que não me valorizou", "value": 2},
      {"text": "Sempre do outro. Eu fui a vítima da história", "value": 3}
    ]},
    {"q": "Você fez terapia ou trabalhou o próprio comportamento relacional?", "options": [
      {"text": "Sim, e isso mudou coisas reais em mim", "value": -1},
      {"text": "Faço terapia, estou trabalhando isso", "value": -1},
      {"text": "Já tentei, mas não dei continuidade", "value": 1},
      {"text": "Nunca. Não vejo motivo", "value": 2}
    ]},
    {"q": "Como você reage quando não é o centro das atenções?", "options": [
      {"text": "Tranquilo(a) — escuto e faço perguntas", "value": 0},
      {"text": "Fico quieto(a), mas me interesso", "value": 1},
      {"text": "Fico entediado(a) e busco reacender o assunto para mim", "value": 2},
      {"text": "Fico irritado(a) e saio ou desqualifico o que está rolando", "value": 3}
    ]},
    {"q": "Você já usou alguém que admirava você para benefício próprio?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Não me lembro", "value": 1},
      {"text": "Em algum momento, sim", "value": 2},
      {"text": "Reconheço que sim, e mais de uma vez", "value": 3}
    ]},
    {"q": "Como está sua disposição para olhar isso de frente hoje?", "options": [
      {"text": "Estou aqui justamente para entender", "value": -1},
      {"text": "Reconheço que preciso mudar algo", "value": 0},
      {"text": "Acho que os outros exageram sobre mim", "value": 2},
      {"text": "Não preciso mudar. Quem não me aguenta que se afaste", "value": 3}
    ]}
  ],
  "results": [
    {"max": 7, "emoji": "🟢", "title": "Autoimagem saudável, poucos traços problemáticos",
     "text": "Você tem confiança sem precisar esmagar ninguém no caminho. Consegue receber crítica, pedir desculpas e comemorar o sucesso alheio — sinais de um narcisismo saudável: o amor-próprio que sustenta relações sem dominá-las. Continue exercitando a escuta: é ali que a intimidade de verdade se constrói.",
     "link": "/artigos/amor-proprio-narcisismo-saudavel.html", "linkText": "Ler: Amor-próprio vs. narcisismo"},
    {"max": 15, "emoji": "🟡", "title": "Traços narcísicos presentes — zona cinzenta",
     "text": "Você reconhece vários padrões narcísicos em si, mas também demonstra capacidade de reflexão e de rever comportamentos — e isso muda tudo. O narcisismo é um espectro; traços viram problema quando são rígidos e custam suas relações. Você está no ponto em que autoconhecimento e terapia evitam que isso vire uma prisão. Trabalhe empatia ativa e tolerância à crítica.",
     "link": "/artigos/narcisismo.html", "linkText": "Sinais, fases e como trabalhar isso"},
    {"max": 24, "emoji": "🟠", "title": "Traços narcísicos acentuados",
     "text": "Suas respostas apontam padrões fortes: dificuldade real de empatia, centralidade nas próprias necessidades e uma blindagem considerável contra a crítica. Isso costuma ter raiz em feridas antigas — não é maldade, é uma armadura que virou gaiola. Vale procurar um psicólogo especializado em questões relacionais. Você pode mudar, mas o primeiro passo é parar de achar que o problema é sempre o outro.",
     "link": "/artigos/narcisismo.html", "linkText": "O ciclo narcísico e como quebrá-lo"},
    {"max": 99, "emoji": "🔴", "title": "Padrão narcísico severo — busque ajuda",
     "text": "Suas respostas sugerem um padrão rígido de autoproteção brutal: incapacidade de admitir erro, desvalorização do outro, necessidade vital de admiração e histórico de manipulação. Esse grau sabota relações de forma sistemática e causa sofrimento em quem está perto de você e em você mesmo. Um profissional de saúde mental não julga — ele ajuda. Este é o momento de procurar um.",
     "link": "/artigos/como-sair-de-relacao-com-narcisista.html", "linkText": "Narcisismo: entender para mudar"}
  ]
}
}

# ─────────────────────────────────────────────────────────────────────────
# 2. MEU PARCEIRO ESTÁ PRONTO PARA UM RELACIONAMENTO? (sum: menor = mais pronto)
# ─────────────────────────────────────────────────────────────────────────
PARCEIRO_PRONTO = {
"slug": "parceiro-pronto-relacionamento",
"title": "Seu Parceiro Está Pronto para um Relacionamento? — Teste",
"desc": "12 perguntas para avaliar se a pessoa com quem você se envolve está emocionalmente disponível e pronta para algo sério — ou apenas buscando conforto. Teste gratuito.",
"breadcrumb": "Parceiro Pronto para Relacionar",
"h1": "⏳ Seu Parceiro Está Pronto para um Relacionamento?",
"intro": "Gostar é uma coisa. Estar disponível é outra. Responda pensando no comportamento real — não no que ele(a) promete que vai fazer.",
"related_text": "Prontidão emocional não é sobre sentimentos, é sobre disponibilidade real: tempo, constância, vulnerabilidade e disposição para o trabalho de uma relação.",
"related_link": "/artigos/estilos-de-apego-no-amor.html",
"related_label": "Ler: Estilos de Apego no Amor",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de prontidão para relacionamento do Amorfy. Deu o que pensar:",
  "questions": [
    {"q": "Ele(a) fala claramente sobre o que quer com você?", "options": [
      {"text": "Sim, sempre foi direto(a) e transparente", "value": 0},
      {"text": "Fala, mas de forma vaga", "value": 1},
      {"text": "Desvia do assunto quando toco no tema", "value": 2},
      {"text": "Nunca. Diz que 'não gosta de rótulos'", "value": 3}
    ]},
    {"q": "Como a última relação dele(a) terminou?", "options": [
      {"text": "Processou, aprendeu e seguiu em frente", "value": 0},
      {"text": "Terminou faz tempo e parece resolvido", "value": 1},
      {"text": "Ainda fala mal da ex com frequência", "value": 2},
      {"text": "Recém-terminou e não entendeu o que deu errado", "value": 3}
    ]},
    {"q": "Ele(a) demonstra vulnerabilidade quando algo está difícil?", "options": [
      {"text": "Sim, admite medo, tristeza, insegurança", "value": 0},
      {"text": "Com o tempo, depois de algum incentivo", "value": 1},
      {"text": "Quase nunca demonstra nada", "value": 2},
      {"text": "Se fecha por completo ou transforma em brincadeira", "value": 3}
    ]},
    {"q": "A disponibilidade de tempo na vida dele(a) comporta uma relação?", "options": [
      {"text": "Sim, ele(a) faz espaço sem eu pedir", "value": 0},
      {"text": "Razoavelmente, com ajustes normais", "value": 1},
      {"text": "Só sobra um pequeno espaço que eu preciso disputar", "value": 2},
      {"text": "Nunca está disponível. Aparece e some conforme a conveniência", "value": 3}
    ]},
    {"q": "Como ele(a) age quando você expressa uma necessidade?", "options": [
      {"text": "Leva a sério e tenta entender", "value": 0},
      {"text": "Escuta e ajusta quando consegue", "value": 1},
      {"text": "Diz que eu espero demais ou sou carente", "value": 2},
      {"text": "Vira briga, indiferença ou punição silenciosa", "value": 3}
    ]},
    {"q": "Existe coerência entre o que ele(a) diz e o que faz?", "options": [
      {"text": "Sempre — as atitudes confirmam", "value": 0},
      {"text": "Na maioria das vezes", "value": 1},
      {"text": "Raramente. Palavras bonitas, ações contraditórias", "value": 2},
      {"text": "Nunca. Diz que vai e não cumpre sistematicamente", "value": 3}
    ]},
    {"q": "Ele(a) tem rede de apoio própria — amigos, família, vida?", "options": [
      {"text": "Sim, vida saudável e independente", "value": 0},
      {"text": "Tem, mesmo que menor", "value": 1},
      {"text": "É bastante isolado(a)", "value": 2},
      {"text": "Sem rede, e parece esperar que eu seja tudo pra ele(a)", "value": 3}
    ]},
    {"q": "Quando algo dá errado entre vocês, quem inicia a reparação?", "options": [
      {"text": "Ambos, alternadamente", "value": 0},
      {"text": "Ele(a), quando percebe que magoou", "value": 1},
      {"text": "Quase sempre eu", "value": 2},
      {"text": "Ninguém — os problemas ficam pendurados no ar", "value": 3}
    ]},
    {"q": "Ele(a) demonstra interesse genuíno na sua vida, planos, carreira?", "options": [
      {"text": "Sim, engaja em detalhes", "value": 0},
      {"text": "Pergunta o básico, se esforça", "value": 1},
      {"text": "Só quando interessa a ele(a)", "value": 2},
      {"text": "Nunca pergunta nada sobre o que importa pra mim", "value": 3}
    ]},
    {"q": "Ele(a) faz terapia ou trabalha o próprio emocional?", "options": [
      {"text": "Sim, ativamente", "value": -1},
      {"text": "Já fez, e demonstra que absorveu", "value": 0},
      {"text": "Nunca, mas estaria aberto(a)", "value": 1},
      {"text": "Não, e não vê necessidade", "value": 2}
    ]},
    {"q": "Como vocês resolvem as diferenças de opinião?", "options": [
      {"text": "Diálogo — buscamos entendimento comum", "value": 0},
      {"text": "Um cede de cada vez, equilibrado", "value": 1},
      {"text": "Um sempre cede, e não é ele(a)", "value": 2},
      {"text": "Evitamos conversar sobre o que diverge", "value": 3}
    ]},
    {"q": "Você sente que está construindo algo ou adivinhando o que ele(a) quer?", "options": [
      {"text": "Construindo — caminhamos na mesma direção", "value": 0},
      {"text": "Construindo, com alguma incerteza", "value": 1},
      {"text": "Adivinhando quase todo dia", "value": 2},
      {"text": "Correndo atrás de migalhas", "value": 3}
    ]}
  ],
  "results": [
    {"max": 8, "emoji": "💚", "title": "Pronto(a) — e disponível de verdade",
     "text": "Ele(a) demonstra o que importa: clareza, constância, capacidade de reparação e disposição para o trabalho de uma relação. Prontidão não é perfeição — é estar presente e querer estar. Parece que você encontrou alguém que joga com você, não contra você. Cuide disso com a mesma maturidade que ele(a) oferece.",
     "link": "/artigos/comunicacao.html", "linkText": "Aprofundar: Comunicação Não-Violenta"},
    {"max": 16, "emoji": "🟡", "title": "Em processo — sinal verde com ressalvas",
     "text": "Ele(a) tem disponibilidade real, mas com pontos a trabalhar: talvez insegurança, um ex não resolvido, ou dificuldade de expressar vulnerabilidade. Nada fatal — quase ninguém está 100% pronto, e relações crescem junto. O que você precisa observar é a TENDÊNCIA: está melhorando ou estagnado? Fale abertamente sobre o que sente falta.",
     "link": "/artigos/estilos-de-apego-no-amor.html", "linkText": "Avaliar disponibilidade emocional"},
    {"max": 25, "emoji": "🟠", "title": "Pouco disponível — cuidado com a esperança",
     "text": "As respostas apontam um padrão que cansa: ambiguidade, inconsistência, pouco espaço real na vida dele(a) para você. Muitas vezes a pessoa gosta de você mas não tem capacidade de se comprometer (por medo, feridas ou imaturidade). Você não pode virar terapeuta dele(a), e promessas vazias não substituem ações. Antes de investir mais, exija clareza.",
     "link": "/artigos/dependencia-emocional-psicanalise.html", "linkText": "Entender dependência emocional"},
    {"max": 99, "emoji": "🔴", "title": "Não está pronto(a) — e talvez nem queira estar",
     "text": "As respostas descrevem alguém que não tem, no momento, estrutura para uma relação: esquiva crônica, desrespeito às suas necessidades, palavras e atos divorciados. Não importa quanto você faça — prontidão não se fabrica de fora. A pergunta honesta é: quanto de você está sendo gasto esperando alguém mudar? Você merece alguém que já esteja querendo estar aqui.",
     "link": "/artigos/medo-de-amar-contraintimidade.html", "linkText": "Medo de amar: contraintimidade"}
  ]
}
}

# ─────────────────────────────────────────────────────────────────────────
# 3. POR QUE EU AFASTO AS PESSOAS (category: 4 padrões)
# ─────────────────────────────────────────────────────────────────────────
AFASTO_PESSOAS = {
"slug": "por-que-afasto-pessoas",
"title": "Por Que Eu Afasto as Pessoas? — Teste de Padrão Relacional",
"desc": "12 perguntas para descobrir o que, em você, sabota relações: medo de intimidade, medo de abandono, autossabotagem ou necessidade de controle. Teste gratuito.",
"breadcrumb": "Por Que Afasto Pessoas",
"h1": "🚪 Por Que Eu Afasto as Pessoas?",
"intro": "Se as relações sempre começam bem e terminam do mesmo jeito, provavelmente há um padrão seu sabotando a festa. Este teste ajuda a nomear esse padrão.",
"related_text": "Padrões de fuga e sabotagem relacional têm raiz na infância e no apego — e podem ser reescritos com consciência e trabalho terapêutico.",
"related_link": "/artigos/medo-de-amar-contraintimidade.html",
"related_label": "Ler: Medo de Amar e Contraintimidade",
"show_disclaimer": True,
"quiz_data": {
  "mode": "category",
  "shareText": "Fiz o teste 'por que afasto as pessoas' do Amorfy. Dolorosamente preciso:",
  "questions": [
    {"q": "Quando uma relação começa a ficar séria, você...", "options": [
      {"text": "Sente um frio na barriga e vontade de recuar", "scores": {"medo_intimidade": 2}},
      {"text": "Fico feliz, mas começo a precisar de reafirmações constantes", "scores": {"medo_abandono": 2}},
      {"text": "Começo a me convencer de que não sou bom(boa) o bastante pra essa pessoa", "scores": {"autossabotagem": 2}},
      {"text": "Passo a reparar nos defeitos e querer 'arrumar' o outro", "scores": {"controle": 2}}
    ]},
    {"q": "O que mais te incomoda na intimidade?", "options": [
      {"text": "Sentir que estão invadindo meu espaço e minha liberdade", "scores": {"medo_intimidade": 2}},
      {"text": "O medo constante de ser deixado(a)", "scores": {"medo_abandono": 2}},
      {"text": "Achar que vão me descobrir e se decepcionar", "scores": {"autossabotagem": 2}},
      {"text": "Não poder prever o que o outro vai fazer", "scores": {"controle": 2}}
    ]},
    {"q": "Depois de um encontro ótimo, o que você costuma fazer?", "options": [
      {"text": "Dou um tempo de silêncio pra 'não parecer grudento(a)'", "scores": {"medo_intimidade": 2}},
      {"text": "Checo se a pessoa vai mandar mensagem; se demora, entro em pânico", "scores": {"medo_abandono": 2}},
      {"text": "Começo a listar motivos pelos quais não vai dar certo", "scores": {"autossabotagem": 2}},
      {"text": "Analiso cada palavra e gesto procurando sinais", "scores": {"controle": 2}}
    ]},
    {"q": "Como você reage quando a pessoa não responde rápido?", "options": [
      {"text": "Me fecho e dou gelo de volta", "scores": {"medo_intimidade": 2}},
      {"text": "Sofro, mando mais mensagens, fico ansioso(a)", "scores": {"medo_abandono": 2}},
      {"text": "Concluo que perdi o interesse dela e desisto", "scores": {"autossabotagem": 2}},
      {"text": "Cobro explicação sobre onde estava", "scores": {"controle": 2}}
    ]},
    {"q": "Qual é seu maior medo num relacionamento?", "options": [
      {"text": "Me perder dentro da relação", "scores": {"medo_intimidade": 2}},
      {"text": "Ser abandonado(a) de novo", "scores": {"medo_abandono": 2}},
      {"text": "Não ser digno(a) de amor", "scores": {"autossabotagem": 2}},
      {"text": "Ser traído(a) ou enganado(a)", "scores": {"controle": 2}}
    ]},
    {"q": "Quando alguém se aproxima demais, sua primeira reação é...", "options": [
      {"text": "Criar uma distância disfarçada de 'independência'", "scores": {"medo_intimidade": 2}},
      {"text": "Testar se a pessoa vai ficar, criando situações de prova", "scores": {"medo_abandono": 2}},
      {"text": "Fazer piada de mim mesmo(a) antes que façam", "scores": {"autossabotagem": 2}},
      {"text": "Querer saber tudo e estabelecer regras", "scores": {"controle": 2}}
    ]},
    {"q": "O que costuma provocar o fim das suas relações?", "options": [
      {"text": "Eu me distancio até a pessoa desistir", "scores": {"medo_intimidade": 2}},
      {"text": "Meu ciúme e minha necessidade de garantia esgotam o outro", "scores": {"medo_abandono": 2}},
      {"text": "Eu termino antes de ser terminado(a)", "scores": {"autossabotagem": 2}},
      {"text": "Minhas cobranças e críticas desgastam a relação", "scores": {"controle": 2}}
    ]},
    {"q": "Como você se sente quando o outro se abre emocionalmente?", "options": [
      {"text": "Desconfortável — prefiro leveza", "scores": {"medo_intimidade": 2}},
      {"text": "Fico grato(a), mas com medo de que vire dependência", "scores": {"medo_abandono": 2}},
      {"text": "Não acredito que seja sincero; deve estar mentindo", "scores": {"autossabotagem": 2}},
      {"text": "Fico analisando se o que ele(a) sente bate com o que eu esperava", "scores": {"controle": 2}}
    ]},
    {"q": "Diante de um conflito, sua tendência é...", "options": [
      {"text": "Me calar e me afastar", "scores": {"medo_intimidade": 2}},
      {"text": "Entrar em desespero e implorar por proximidade", "scores": {"medo_abandono": 2}},
      {"text": "Achar que é o fim e me antecipar", "scores": {"autossabotagem": 2}},
      {"text": "Querer vencer a discussão e ter a última palavra", "scores": {"controle": 2}}
    ]},
    {"q": "Você já sabotou uma relação boa 'do nada'?", "options": [
      {"text": "Sim, me afastei sem explicação clara", "scores": {"medo_intimidade": 2}},
      {"text": "Sim, com testes e cobranças que afastaram a pessoa", "scores": {"medo_abandono": 2}},
      {"text": "Sim, terminei com alguém ótimo por achar que não merecia", "scores": {"autossabotagem": 2}},
      {"text": "Sim, com excesso de controle e ciúme", "scores": {"controle": 2}}
    ]},
    {"q": "O que você mais valoriza no início de uma relação?", "options": [
      {"text": "Liberdade e leveza", "scores": {"medo_intimidade": 2}},
      {"text": "Garantias e declarações de compromisso", "scores": {"medo_abandono": 2}},
      {"text": "Ser aceito(a) mesmo com meus defeitos", "scores": {"autossabotagem": 2}},
      {"text": "Previsibilidade e constância", "scores": {"controle": 2}}
    ]},
    {"q": "Quando você percebe que está afastando alguém, você...", "options": [
      {"text": "Deixo acontecer — 'é assim que sou'", "scores": {"medo_intimidade": 2}},
      {"text": "Me agarro ainda mais, o que piora tudo", "scores": {"medo_abandono": 2}},
      {"text": "Confirmo minha teoria de que não presto pra relação", "scores": {"autossabotagem": 2}},
      {"text": "Tento controlar a situação para reverter", "scores": {"controle": 2}}
    ]}
  ],
  "results": {
    "medo_intimidade": {
      "emoji": "🧱", "title": "Seu padrão: Medo de Intimidade",
      "text": "Você afasta as pessoas erguendo um muro justamente quando a relação começa a dar certo. O medo de se perder, de ser invadido(a) ou de depender de alguém te faz recuar — e a distância que te protege é a mesma que te deixa sozinho(a). Intimidade não é prisão: é um espaço compartilhado. Aos poucos, treine ficar um pouco mais perto e falar do seu medo em vez de sumir.",
      "link": "/artigos/medo-de-amar-contraintimidade.html", "linkText": "Ler: Medo de Amar e Contraintimidade"},
    "medo_abandono": {
      "emoji": "🪢", "title": "Seu padrão: Medo de Abandono",
      "text": "Você afasta as pessoas se agarrando forte demais. O pavor de ser deixado(a) vira testes, cobranças e uma ansiedade que esgota quem tenta te amar — e acaba produzindo exatamente o abandono que você temia. A ferida é antiga, mas você não precisa viver refém dela. Busque segurança interna: terapia e o cultivo da sua própria vida ajudam a soltar a corda.",
      "link": "/artigos/estilos-de-apego-no-amor.html", "linkText": "Ler: Estilos de Apego no Amor"},
    "autossabotagem": {
      "emoji": "🪞", "title": "Seu padrão: Autossabotagem",
      "text": "Você afasta as pessoas antes que elas possam te rejeitar. Lá no fundo, não acredita que merece amor, então encontra defeitos, termina cedo demais ou se boicota quando tudo vai bem. Isso é uma narrativa antiga, não uma verdade. Amor-próprio se constrói — e terapia é o atalho mais honesto para reescrever essa história. Você é digno(a) de ser amado(a), do jeito que é.",
      "link": "/artigos/tracos-carater.html", "linkText": "Ler: Traços de Caráter"},
    "controle": {
      "emoji": "🎛️", "title": "Seu padrão: Necessidade de Controle",
      "text": "Você afasta as pessoas tentando controlar o incontrolável. A imprevisibilidade do outro te dá vertigem, então você cobra, analisa, estabelece regras e quer prever cada passo — e ninguém respira nesse regime. Relação é encontro de dois mistérios, não um projeto a ser gerenciado. Aprender a tolerar a incerteza (e a confiar) é o que vai te libertar desse exílio afetivo.",
      "link": "/artigos/ciume-o-que-ele-revela.html", "linkText": "Ler: Ciúme e o que ele revela"}
  }
}
}

# ─────────────────────────────────────────────────────────────────────────
# 4. AUTOSSABOTAGEM AMOROSA (sum: maior = mais sabotagem)
# ─────────────────────────────────────────────────────────────────────────
AUTOSSABOTAGEM = {
"slug": "autossabotagem-amorosa",
"title": "Você Sabota Seus Relacionamentos? — Teste de Autossabotagem",
"desc": "12 perguntas para identificar se você boicota o próprio amor: terminar cedo demais, criar brigas, não acreditar no afeto recebido. Teste gratuito.",
"breadcrumb": "Autossabotagem Amorosa",
"h1": "🧨 Você Sabota Seus Relacionamentos?",
"intro": "Às vezes o inimigo do amor não é o outro — é o padrão que a gente repete sem perceber. Descubra o quanto você boicota o que mais deseja.",
"related_text": "Autossabotagem amorosa é repetição de padrões antigos: você se protege da dor de ser rejeitado(a) rejeitando primeiro.",
"related_link": "/artigos/repeticao-compulsiva-no-amor.html",
"related_label": "Ler: Repetição Compulsiva no Amor",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de autossabotagem amorosa do Amorfy. O espelho foi duro:",
  "questions": [
    {"q": "Quando está tudo indo bem, o que você sente?", "options": [
      {"text": "Tranquilidade e alegria", "value": 0},
      {"text": "Uma leve desconfiança de que algo vai dar errado", "value": 1},
      {"text": "Ansiedade — fico esperando a outra metade do tombo", "value": 2},
      {"text": "Um incômodo tão grande que acabo criando um problema", "value": 3}
    ]},
    {"q": "Você já terminou um relacionamento bom 'do nada'?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Uma vez, por motivos reais", "value": 1},
      {"text": "Algumas vezes, sem saber bem o porquê", "value": 2},
      {"text": "Várias vezes, sempre me arrependo depois", "value": 3}
    ]},
    {"q": "Como você reage a elogios e declarações?", "options": [
      {"text": "Agradeço e acredito", "value": 0},
      {"text": "Agradeço, com um pouco de vergonha", "value": 1},
      {"text": "Desconfio: 'será que é verdade?'", "value": 2},
      {"text": "Minimizo ou devolvo: 'não sou tudo isso'", "value": 3}
    ]},
    {"q": "Você cria brigas ou procura defeitos quando a relação está calma?", "options": [
      {"text": "Não, aproveito a calma", "value": 0},
      {"text": "Raramente, e de forma sutil", "value": 1},
      {"text": "Com alguma frequência", "value": 2},
      {"text": "Sempre — a calmaria me deixa inquieto(a)", "value": 3}
    ]},
    {"q": "Você acredita que merece ser amado(a)?", "options": [
      {"text": "Sim, plenamente", "value": 0},
      {"text": "Na maior parte do tempo", "value": 1},
      {"text": "Tenho dúvidas frequentes", "value": 2},
      {"text": "Lá no fundo, não acredito", "value": 3}
    ]},
    {"q": "Quando alguém se apaixona por você, você...", "options": [
      {"text": "Sinto que é recíproco e natural", "value": 0},
      {"text": "Fico feliz, com alguma cautela", "value": 1},
      {"text": "Penso: 'essa pessoa vai se decepcionar'", "value": 2},
      {"text": "Desconfio da pessoa ou perco o interesse", "value": 3}
    ]},
    {"q": "Você costuma escolher pessoas indisponíveis ou complicadas?", "options": [
      {"text": "Não, busco quem quer o mesmo que eu", "value": 0},
      {"text": "Aconteceu uma ou outra vez", "value": 1},
      {"text": "Com frequência me atraio por gente complicada", "value": 2},
      {"text": "É um padrão: só me interesso pelo que não posso ter", "value": 3}
    ]},
    {"q": "Como você lida com a possibilidade de dar certo?", "options": [
      {"text": "Agarro a chance com as duas mãos", "value": 0},
      {"text": "Vou com cuidado, mas sigo em frente", "value": 1},
      {"text": "Saboto um pouco antes de me entregar", "value": 2},
      {"text": "Encontro um jeito de estragar antes que dê certo", "value": 3}
    ]},
    {"q": "Você se boicota em outras áreas (carreira, projetos) também?", "options": [
      {"text": "Não, sou realizado(a) e constante", "value": 0},
      {"text": "Raramente", "value": 1},
      {"text": "Em algumas áreas, sim", "value": 2},
      {"text": "Sim, é um padrão em tudo que me importa", "value": 3}
    ]},
    {"q": "Você faz terapia ou trabalha essas repetições?", "options": [
      {"text": "Sim, e tem me ajudado muito", "value": -1},
      {"text": "Faço terapia atualmente", "value": -1},
      {"text": "Já fiz, mas parei", "value": 1},
      {"text": "Nunca fiz e não penso em fazer", "value": 2}
    ]},
    {"q": "Quando a pessoa demonstra amor consistente, você...", "options": [
      {"text": "Me sinto seguro(a) e retribuo", "value": 0},
      {"text": "Levo um tempo pra confiar", "value": 1},
      {"text": "Fico desconfortável, quase com medo", "value": 2},
      {"text": "Acho estranho e desconfio: 'deve ter algo errado'", "value": 3}
    ]},
    {"q": "Você se arrepende de términos que provocou?", "options": [
      {"text": "Nunca passei por isso", "value": 0},
      {"text": "Raramente", "value": 1},
      {"text": "Algumas vezes", "value": 2},
      {"text": "Constantemente — o arrependimento me persegue", "value": 3}
    ]}
  ],
  "results": [
    {"max": 7, "emoji": "💚", "title": "Pouca autossabotagem — amor em dia",
     "text": "Você consegue receber amor, confiar no que sente e deixar as coisas boas acontecerem sem medo de estragar. Isso é um patrimônio emocional raro e valioso. Continue cuidando de você e da sua capacidade de se entregar — é ela que permite que o amor floresça.",
     "link": "/artigos/autoconhecimento.html", "linkText": "Ler: Autoconhecimento"},
    {"max": 15, "emoji": "🟡", "title": "Autossabotagem leve — pontual",
     "text": "Você tem alguns padrões de autossabotagem, mas nada que domine sua vida afetiva. Um pé atrás aqui, uma dúvida ali — o importante é que você percebe e consegue se corrigir. Nomear o padrão é metade do caminho. Observe os gatilhos e converse sobre suas inseguranças em vez de agir por impulso.",
     "link": "/artigos/repeticao-compulsiva-no-amor.html", "linkText": "Ler: Repetição Compulsiva no Amor"},
    {"max": 24, "emoji": "🟠", "title": "Autossabotagem frequente — padrão ativo",
     "text": "Você boicota o próprio amor com regularidade: termina cedo, cria brigas, não acredita no afeto que recebe e escolhe gente indisponível. Isso não é azar — é um padrão de proteção que virou autossabotagem. A raiz costuma estar em feridas antigas de rejeição ou abandono. Terapia focada em vínculos pode te ajudar a quebrar esse ciclo de uma vez.",
     "link": "/artigos/medo-de-amar-contraintimidade.html", "linkText": "Ler: Medo de Amar e Contraintimidade"},
    {"max": 99, "emoji": "🔴", "title": "Autossabotagem severa — o padrão manda em você",
     "text": "Suas respostas descrevem alguém preso num ciclo intenso de autossabotagem: sabota quando está bem, escolhe o inatingível, não acredita merecer amor e se arrepende dos próprios términos. Você não está quebrado(a) — está ferido(a) e repetindo uma história antiga. Este é um caso claro para acompanhamento psicológico. Você merece sair desse ciclo, e dá pra sair.",
     "link": "/artigos/tracos-carater.html", "linkText": "Ler: Traços de Caráter"}
  ]
}
}

# ─────────────────────────────────────────────────────────────────────────
# 5. CIÚME E INVEJA NO RELACIONAMENTO (sum: maior = mais intenso)
# ─────────────────────────────────────────────────────────────────────────
CIUME_INVEJA = {
"slug": "ciume-inveja-relacionamento",
"title": "Ciúme ou Inveja? — Teste de Emoções no Relacionamento",
"desc": "12 perguntas para entender se o que você sente é ciúme (medo de perder) ou inveja (incomodar-se com o que o outro tem) — e como isso afeta sua relação. Teste gratuito.",
"breadcrumb": "Ciúme e Inveja",
"h1": "💚💔 Ciúme ou Inveja no Relacionamento?",
"intro": "Ciúme é o medo de perder o que se tem; inveja é o incômodo com o que o outro tem. Elas se confundem — e ambas falam mais de você do que do outro. Descubra o que move suas emoções.",
"related_text": "Ciúme não é prova de amor: é um alarme que revela insegurança, medo de abandono e, às vezes, a projeção da nossa própria inveja.",
"related_link": "/artigos/ciume-o-que-ele-revela.html",
"related_label": "Ler: Ciúme e o que ele revela",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de ciúme e inveja do Amorfy. O resultado me fez repensar:",
  "questions": [
    {"q": "Quando seu parceiro(a) tem sucesso, você...", "options": [
      {"text": "Celebro de verdade", "value": 0},
      {"text": "Celebro, com uma pontinha de incômodo", "value": 1},
      {"text": "Fico misto — feliz e incomodado(a) ao mesmo tempo", "value": 2},
      {"text": "Fico incomodado(a) e às vezes minimizo a conquista", "value": 3}
    ]},
    {"q": "O que mais te atormenta numa relação?", "options": [
      {"text": "Nada específico — confio", "value": 0},
      {"text": "Pequenos pensamentos que logo passam", "value": 1},
      {"text": "Medo de ser trocado(a) por alguém 'melhor'", "value": 2},
      {"text": "Comparar minha vida com a do outro constantemente", "value": 3}
    ]},
    {"q": "Você compara seu relacionamento com o de outras pessoas?", "options": [
      {"text": "Quase nunca", "value": 0},
      {"text": "Às vezes, por curiosidade", "value": 1},
      {"text": "Com frequência", "value": 2},
      {"text": "Sempre — e saio me sentindo menor ou ressentido(a)", "value": 3}
    ]},
    {"q": "Você sente inveja de amigos, colegas ou do próprio parceiro(a)?", "options": [
      {"text": "Não", "value": 0},
      {"text": "Raramente", "value": 1},
      {"text": "Sim, e me sinto mal por isso", "value": 2},
      {"text": "Sim, e isso me consome", "value": 3}
    ]},
    {"q": "Você já fiscalizou o celular ou as redes do parceiro(a)?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Não, mas já tive vontade", "value": 1},
      {"text": "Algumas vezes", "value": 2},
      {"text": "Frequentemente", "value": 3}
    ]},
    {"q": "Como você reage quando o outro tem uma amizade próxima?", "options": [
      {"text": "Acho saudável", "value": 0},
      {"text": "Fico de boa, com alguma atenção", "value": 1},
      {"text": "Fico incomodado(a) e quero saber detalhes", "value": 2},
      {"text": "Fico hostil e tento afastar essa pessoa", "value": 3}
    ]},
    {"q": "Você acredita que o ciúme é prova de amor?", "options": [
      {"text": "Não — amor é confiança", "value": 0},
      {"text": "Um pouco de ciúme é natural", "value": 1},
      {"text": "Acho que demonstra que me importo", "value": 2},
      {"text": "Sim — quem não sente ciúme não ama", "value": 3}
    ]},
    {"q": "O sentimento de inveja já te levou a torcer contra alguém?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Não, mas já me senti aliviado(a) com fracasso alheio", "value": 1},
      {"text": "Algumas vezes, e me envergonho", "value": 2},
      {"text": "Sim, com frequência", "value": 3}
    ]},
    {"q": "Você sente que sua vida seria melhor se tivesse o que o outro tem?", "options": [
      {"text": "Não — tenho o que preciso", "value": 0},
      {"text": "De vez em quando", "value": 1},
      {"text": "Frequentemente me pego nesse pensamento", "value": 2},
      {"text": "Sempre. A grama do vizinho me obceca", "value": 3}
    ]},
    {"q": "Você faz terapia ou trabalha suas inseguranças?", "options": [
      {"text": "Sim, e evolui muito", "value": -1},
      {"text": "Faço terapia", "value": -1},
      {"text": "Já fiz, parei", "value": 1},
      {"text": "Nunca e não vejo por que", "value": 2}
    ]},
    {"q": "Quando você percebe ciúme ou inveja em si, você...", "options": [
      {"text": "Reconheço e procuro entender a raiz", "value": 0},
      {"text": "Tento respirar e não agir", "value": 1},
      {"text": "Fico remoendo e às vezes desconto no outro", "value": 2},
      {"text": "Deixo isso me dominar e vira briga", "value": 3}
    ]},
    {"q": "Como você se sente com a felicidade alheia, no geral?", "options": [
      {"text": "Me inspira", "value": 0},
      {"text": "Fico feliz, com alguma comparação", "value": 1},
      {"text": "Mistura de alegria e ressentimento", "value": 2},
      {"text": "Me angustia — por que eles e não eu?", "value": 3}
    ]}
  ],
  "results": [
    {"max": 7, "emoji": "💚", "title": "Emoções equilibradas — confiança e inspiração",
     "text": "Você vive o sucesso e a felicidade do outro como inspiração, não como ameaça. Isso fala de uma autoestima sólida e de segurança afetiva. Ciúme e inveja aparecem pouco, e quando aparecem você os reconhece e regula. Continue nutrindo essa relação saudável consigo mesmo(a).",
     "link": "/artigos/autoconhecimento.html", "linkText": "Ler: Autoconhecimento"},
    {"max": 15, "emoji": "🟡", "title": "Emoções presentes, mas sob controle",
     "text": "Ciúme e inveja batem à sua porta de vez em quando — o que é humano. A diferença é que você os percebe e não deixa que comandem suas atitudes. Vale investigar a raiz dessas inseguranças: quanto mais você entende de onde vêm, menos poder elas têm. Trabalhar a autocompaixão ajuda muito.",
     "link": "/artigos/ciume-o-que-ele-revela.html", "linkText": "Ler: Ciúme e o que ele revela"},
    {"max": 24, "emoji": "🟠", "title": "Ciúme e inveja intensos — pedindo atenção",
     "text": "Essas emoções aparecem com força e já interferem na sua relação e no seu bem-estar. Ciúme é medo de perder; inveja é comparação com o outro. Ambos nascem da insegurança e da falta de valor próprio — não do amor. Comece a nomear o que sente, evite agir por impulso e considere um acompanhamento para reconstruir sua autoestima.",
     "link": "/artigos/dependencia-emocional-psicanalise.html", "linkText": "Ler: Dependência Emocional"},
    {"max": 99, "emoji": "🔴", "title": "Ciúme e inveja dominantes — um ciclo que fere",
     "text": "Suas respostas descrevem emoções que tomaram o controle: fiscalização, comparação constante, ressentimento diante da felicidade alheia e a crença de que ciúme é amor. Isso não é amor — é insegurança e dor, e está corroendo sua relação e sua paz. Você não precisa viver assim. Procure ajuda psicológica: é possível reconstruir uma relação segura consigo mesmo(a) e com os outros.",
     "link": "/artigos/ciume-o-que-ele-revela.html", "linkText": "Ler: Ciúme e o que ele revela"}
  ]
}
}

# ─────────────────────────────────────────────────────────────────────────
# 6. RED FLAGS PRECOCES (sum: maior = mais alertas)
# ─────────────────────────────────────────────────────────────────────────
RED_FLAGS = {
"slug": "red-flags-precoces",
"title": "Red Flags no Início do Relacionamento — Teste de Sinais",
"desc": "12 perguntas para identificar sinais de alerta no começo de uma relação: pressa excessiva, ciúme precoce, desrespeito disfarçado. Teste gratuito.",
"breadcrumb": "Red Flags Precoces",
"h1": "🚩 Você Está Ignorando Red Flags no Início da Relação?",
"intro": "O início de uma relação é quando as red flags aparecem — mas o encantamento as esconde. Responda sobre os primeiros encontros e veja os sinais que você talvez esteja minimizando.",
"related_text": "Red flags precoces são os melhores preditores do futuro de uma relação: pressa, ciúme, desrespeito e controle disfarçados de paixão.",
"related_link": "/artigos/como-sair-de-relacao-com-narcisista.html",
"related_label": "Ler: Sair de Relação Narcisista",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de red flags do Amorfy. Queria ter feito antes:",
  "questions": [
    {"q": "Ele(a) quis ir rápido demais no começo?", "options": [
      {"text": "Não, o ritmo foi natural", "value": 0},
      {"text": "Um pouco acelerado, mas ok", "value": 1},
      {"text": "Bem rápido — declarações e planos logo no início", "value": 2},
      {"text": "Love bombing: intensidade avassaladora desde o primeiro encontro", "value": 3}
    ]},
    {"q": "Como ele(a) trata garçons, funcionários ou estranhos?", "options": [
      {"text": "Com respeito e gentileza", "value": 0},
      {"text": "Educado(a), mas distante", "value": 1},
      {"text": "Imponente ou exigente", "value": 2},
      {"text": "Grosseiro(a), arrogante ou humilhante", "value": 3}
    ]},
    {"q": "Ele(a) já demonstrou ciúme no começo da relação?", "options": [
      {"text": "Não", "value": 0},
      {"text": "Um ciúme leve e bem-humorado", "value": 1},
      {"text": "Ficou incomodado(a) com minhas amizades", "value": 2},
      {"text": "Cobrou, fiscalizou ou tentou me afastar de pessoas", "value": 3}
    ]},
    {"q": "Como ele(a) reage quando você diz 'não'?", "options": [
      {"text": "Aceita e respeita", "value": 0},
      {"text": "Aceita, mas insiste um pouco", "value": 1},
      {"text": "Fica emburrado(a) ou distante", "value": 2},
      {"text": "Pressiona até eu ceder", "value": 3}
    ]},
    {"q": "Ele(a) fala mal de todos os ex?", "options": [
      {"text": "Não, fala com maturidade", "value": 0},
      {"text": "Tem mágoas pontuais", "value": 1},
      {"text": "Fala mal da maioria", "value": 2},
      {"text": "Todos os ex eram 'loucos' ou 'vilões'", "value": 3}
    ]},
    {"q": "Ele(a) já te desrespeitou disfarçado de 'brincadeira'?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Não que eu perceba", "value": 1},
      {"text": "Já fez piadas que me machucaram", "value": 2},
      {"text": "Sempre — e quando me queixo, sou eu o 'sem humor'", "value": 3}
    ]},
    {"q": "Como ele(a) lida com suas conquistas e independência?", "options": [
      {"text": "Celebra e incentiva", "value": 0},
      {"text": "Apoia, com algum ajuste", "value": 1},
      {"text": "Fica incomodado(a) quando brilho", "value": 2},
      {"text": "Competitivo(a), minimiza ou sabota", "value": 3}
    ]},
    {"q": "Ele(a) quer saber onde você está e com quem, o tempo todo?", "options": [
      {"text": "Não, confiamos um no outro", "value": 0},
      {"text": "Pergunta por interesse, não por controle", "value": 1},
      {"text": "Cobra satisfação com frequência", "value": 2},
      {"text": "Fiscaliza, exige localização, controla", "value": 3}
    ]},
    {"q": "Como ele(a) se comporta quando você impõe um limite?", "options": [
      {"text": "Respeita na hora", "value": 0},
      {"text": "Respeita, mas reclama depois", "value": 1},
      {"text": "Testa o limite várias vezes", "value": 2},
      {"text": "Pune com frieza, chantagem ou briga", "value": 3}
    ]},
    {"q": "Você se sente à vontade sendo você mesmo(a) perto dele(a)?", "options": [
      {"text": "Totalmente", "value": 0},
      {"text": "Na maior parte do tempo", "value": 1},
      {"text": "Sinto que preciso medir as palavras", "value": 2},
      {"text": "Não — ando pisando em ovos", "value": 3}
    ]},
    {"q": "Ele(a) já te fez duvidar da sua memória ou percepção?", "options": [
      {"text": "Nunca", "value": 0},
      {"text": "Não que eu me lembre", "value": 1},
      {"text": "Algumas vezes, em discussões", "value": 2},
      {"text": "Frequentemente — gaslighting claro", "value": 3}
    ]},
    {"q": "Você já minimizou ou justificou o comportamento dele(a) para amigos?", "options": [
      {"text": "Nunca precisei", "value": 0},
      {"text": "Raramente", "value": 1},
      {"text": "Algumas vezes, por vergonha", "value": 2},
      {"text": "Sempre — escondo muita coisa de quem me ama", "value": 3}
    ]}
  ],
  "results": [
    {"max": 7, "emoji": "💚", "title": "Poucas red flags — relação com base sólida",
     "text": "O início dessa relação parece saudável: respeito, ritmo natural, confiança e espaço para você ser quem é. São esses os alicerces que sustentam o amor no longo prazo. Continue atento(a) — mas sem procurar problema onde não há. Aproveite, com os olhos abertos e o coração tranquilo.",
     "link": "/artigos/confianca.html", "linkText": "Ler: Construir Confiança"},
    {"max": 15, "emoji": "🟡", "title": "Algumas red flags — observe antes de se entregar",
     "text": "Há alguns sinais de alerta que merecem sua atenção: talvez uma pressa, um ciúme leve, um comentário que te desagradou. Nada é condenatório — pessoas são complexas e erram. Mas não ignore o que te incomoda: converse, observe a reação e veja se há mudança real. Red flag não é defeito, é padrão de comportamento.",
     "link": "/artigos/conflitos.html", "linkText": "Ler: Gestão de Conflitos"},
    {"max": 24, "emoji": "🟠", "title": "Muitas red flags — padrão preocupante",
     "text": "As respostas descrevem vários sinais de alerta que você pode estar minimizando por medo de ficar sozinho(a) ou pela intensidade do encantamento. Pressa, controle, ciúme, desrespeito disfarçado de brincadeira e a sensação de pisar em ovos não são 'detalhes' — são o termômetro de como será o futuro. Não deixe o amor-próprio ser negociado pela esperança de mudança.",
     "link": "/artigos/como-sair-de-relacao-com-narcisista.html", "linkText": "Ler: Sair de Relação Narcisista"},
    {"max": 99, "emoji": "🔴", "title": "Red flags sérias — priorize sua segurança",
     "text": "Suas respostas apontam um padrão de alerta grave: love bombing, controle, gaslighting, desrespeito e a sensação de estar constantemente pisando em ovos. Isso não é amor intenso — é a arquitetura de uma relação abusiva se formando. Priorize sua segurança emocional e física, busque apoio de pessoas de confiança e, se preciso, de ajuda profissional. Você merece um amor que te respeite.",
     "link": "/artigos/narcisismo.html", "linkText": "Ler: Tudo Sobre Narcisismo"}
  ]
}
}

ALL_QUIZZES = [MEU_NARCISISMO, PARCEIRO_PRONTO, AFASTO_PESSOAS, AUTOSSABOTAGEM, CIUME_INVEJA, RED_FLAGS]

if __name__ == "__main__":
    for q in ALL_QUIZZES:
        write_quiz(q)
        print(f"ok {q['slug']}")
