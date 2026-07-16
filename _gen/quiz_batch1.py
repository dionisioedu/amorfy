#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quizzes batch 1: personalidade-amorosa, linguagem-do-amor."""
from quiz_template import write_quiz

PERSONALIDADE = {
"slug": "personalidade-amorosa",
"title": "Teste de Personalidade Amorosa — Descubra Seu Temperamento no Amor",
"desc": "Teste gratuito de 10 perguntas: descubra se você é colérico, sanguíneo, fleumático ou melancólico no amor e o que isso significa para seus relacionamentos.",
"breadcrumb": "Personalidade Amorosa",
"h1": "✨ Teste de Personalidade Amorosa",
"intro": "Como você ama? Responda 10 perguntas rápidas e descubra seu temperamento dominante nos relacionamentos.",
"related_text": "Depois do teste, aprofunde-se no guia completo dos 4 temperamentos e descubra como cada perfil ama, briga e se reconcilia.",
"related_link": "/artigos/temperamentos.html",
"related_label": "Ler: Os 4 Temperamentos e o Amor",
"show_disclaimer": False,
"quiz_data": {
  "mode": "category",
  "shareText": "Acabei de descobrir minha personalidade amorosa no Amorfy! Descubra a sua:",
  "questions": [
    {"q": "Quando você se apaixona, como age?", "options": [
      {"text": "Tomo a iniciativa e vou à luta — quero resultado", "scores": {"colerico": 2}},
      {"text": "Declaro para o mundo — quero celebrar e compartilhar", "scores": {"sanguineo": 2}},
      {"text": "Observo com calma antes de me aproximar", "scores": {"fleumatico": 2}},
      {"text": "Analiso cada detalhe e sinto tudo profundamente", "scores": {"melancolico": 2}}
    ]},
    {"q": "Numa briga com seu parceiro, sua reação típica é:", "options": [
      {"text": "Falo o que penso na hora, sem rodeios", "scores": {"colerico": 2}},
      {"text": "Tento aliviar o clima com humor ou mudo de assunto", "scores": {"sanguineo": 2}},
      {"text": "Evito o confronto — prefiro paz a ter razão", "scores": {"fleumatico": 2}},
      {"text": "Me fecho e rumino o que aconteceu por dias", "scores": {"melancolico": 2}}
    ]},
    {"q": "O que mais te incomoda num parceiro?", "options": [
      {"text": "Indecisão e lentidão", "scores": {"colerico": 2}},
      {"text": "Rotina, monotonia e falta de novidade", "scores": {"sanguineo": 2}},
      {"text": "Pressão, drama e cobranças constantes", "scores": {"fleumatico": 2}},
      {"text": "Superficialidade e falta de profundidade emocional", "scores": {"melancolico": 2}}
    ]},
    {"q": "Como você demonstra amor no dia a dia?", "options": [
      {"text": "Resolvendo problemas e protegendo quem amo", "scores": {"colerico": 2}},
      {"text": "Com surpresas, elogios e gestos românticos", "scores": {"sanguineo": 2}},
      {"text": "Estando presente, constante e disponível", "scores": {"fleumatico": 2}},
      {"text": "Lembrando de cada detalhe importante para o outro", "scores": {"melancolico": 2}}
    ]},
    {"q": "Seu maior medo num relacionamento é:", "options": [
      {"text": "Perder minha liberdade e autonomia", "scores": {"colerico": 2}},
      {"text": "Cair na mesmice e perder a graça", "scores": {"sanguineo": 2}},
      {"text": "Viver em conflito constante", "scores": {"fleumatico": 2}},
      {"text": "Amar mais do que sou amado", "scores": {"melancolico": 2}}
    ]},
    {"q": "Num fim de semana ideal a dois, você prefere:", "options": [
      {"text": "Atividade com desafio — trilha, competição, projeto juntos", "scores": {"colerico": 2}},
      {"text": "Festa, viagem ou algo totalmente novo", "scores": {"sanguineo": 2}},
      {"text": "Casa, série, comida boa e zero estresse", "scores": {"fleumatico": 2}},
      {"text": "Conversa profunda, museu, música — conexão de alma", "scores": {"melancolico": 2}}
    ]},
    {"q": "Quando seu parceiro está triste, você:", "options": [
      {"text": "Parto para a solução: o que precisa ser resolvido?", "scores": {"colerico": 2}},
      {"text": "Tento animar: piada, programa novo, distração", "scores": {"sanguineo": 2}},
      {"text": "Fico junto em silêncio, oferecendo presença", "scores": {"fleumatico": 2}},
      {"text": "Mergulho junto: quero entender cada camada da dor", "scores": {"melancolico": 2}}
    ]},
    {"q": "Sobre ciúme, você:", "options": [
      {"text": "Sinto como questão de território — o que é meu é meu", "scores": {"colerico": 2}},
      {"text": "Sinto pouco — confio no meu taco", "scores": {"sanguineo": 2}},
      {"text": "Raramente demonstro, mesmo quando sinto", "scores": {"fleumatico": 2}},
      {"text": "Sofro em silêncio imaginando cenários", "scores": {"melancolico": 2}}
    ]},
    {"q": "O que você mais valoriza num relacionamento longo?", "options": [
      {"text": "Parceria de verdade — um time que conquista junto", "scores": {"colerico": 2}},
      {"text": "Diversão — envelhecer rindo juntos", "scores": {"sanguineo": 2}},
      {"text": "Paz — um porto seguro para voltar todo dia", "scores": {"fleumatico": 2}},
      {"text": "Profundidade — alguém que me conhece por inteiro", "scores": {"melancolico": 2}}
    ]},
    {"q": "Como você lida com o término de uma relação?", "options": [
      {"text": "Corto, sigo em frente e foco no futuro", "scores": {"colerico": 2}},
      {"text": "Sofro rápido e logo estou aberto a conhecer gente nova", "scores": {"sanguineo": 2}},
      {"text": "Demoro a agir — às vezes fico mais tempo do que devia", "scores": {"fleumatico": 2}},
      {"text": "Revivo memórias por muito tempo — o luto é longo", "scores": {"melancolico": 2}}
    ]}
  ],
  "results": {
    "colerico": {"emoji": "🔥", "title": "Você é Colérico no Amor", "text": "Você ama com intensidade, iniciativa e proteção. É quem lidera a relação, resolve problemas e vai à luta pelo casal. Seus desafios: aprender a ouvir sem dominar, mostrar vulnerabilidade e ter paciência com ritmos diferentes do seu. Quando equilibrado, você é o parceiro mais leal e determinado que existe.", "link": "/artigos/temperamentos.html", "linkText": "Ler guia completo do temperamento colérico"},
    "sanguineo": {"emoji": "💨", "title": "Você é Sanguíneo no Amor", "text": "Você ama com alegria, romance e espontaneidade. É quem traz leveza, novidade e otimismo para a relação. Seus desafios: sustentar compromissos na fase da rotina, ouvir tanto quanto fala e não fugir quando a relação exige profundidade. Quando equilibrado, você é o parceiro que transforma a vida a dois numa aventura.", "link": "/artigos/temperamentos.html", "linkText": "Ler guia completo do temperamento sanguíneo"},
    "fleumatico": {"emoji": "🌿", "title": "Você é Fleumático no Amor", "text": "Você ama com calma, constância e lealdade. É o porto seguro da relação — presença que acalma e estabiliza. Seus desafios: não engolir insatisfações em silêncio, tomar iniciativa e enfrentar conversas difíceis em vez de adiá-las. Quando equilibrado, você é o parceiro mais confiável e pacífico que alguém pode ter.", "link": "/artigos/temperamentos.html", "linkText": "Ler guia completo do temperamento fleumático"},
    "melancolico": {"emoji": "🌙", "title": "Você é Melancólico no Amor", "text": "Você ama com profundidade, entrega e atenção aos detalhes. Busca conexão de alma, não relações superficiais. Seus desafios: moderar o perfeccionismo com o parceiro, perdoar sem ruminar e equilibrar intensidade com leveza. Quando equilibrado, você é o parceiro mais devotado e profundo que existe.", "link": "/artigos/temperamentos.html", "linkText": "Ler guia completo do temperamento melancólico"}
  }
}
}

LINGUAGEM = {
"slug": "linguagem-do-amor",
"title": "Qual é a Sua Linguagem do Amor? — Teste Gratuito",
"desc": "Palavras, tempo, presentes, atos de serviço ou toque? Descubra em 10 perguntas qual é a sua linguagem do amor dominante e como usá-la no relacionamento.",
"breadcrumb": "Linguagem do Amor",
"h1": "💬 Qual é a Sua Linguagem do Amor?",
"intro": "Cada pessoa dá e recebe amor de um jeito. Descubra o seu em 10 perguntas.",
"related_text": "Conheça as 5 linguagens em detalhes e aprenda a identificar (e falar) a linguagem do seu parceiro.",
"related_link": "/artigos/linguagens-do-amor.html",
"related_label": "Ler: As 5 Linguagens do Amor",
"show_disclaimer": False,
"quiz_data": {
  "mode": "category",
  "shareText": "Descobri minha linguagem do amor no Amorfy! Descubra a sua:",
  "questions": [
    {"q": "O que te faz sentir mais amado(a)?", "options": [
      {"text": "Ouvir 'eu te amo' e elogios sinceros", "scores": {"palavras": 2}},
      {"text": "Um dia inteiro juntos, sem pressa e sem celular", "scores": {"tempo": 2}},
      {"text": "Receber algo que mostra que pensaram em mim", "scores": {"presentes": 2}},
      {"text": "Quando fazem algo por mim sem eu pedir", "scores": {"servico": 2}}
    ]},
    {"q": "O que mais machuca você numa relação?", "options": [
      {"text": "Críticas duras e palavras frias", "scores": {"palavras": 2}},
      {"text": "Ser trocado(a) pelo celular ou trabalho", "scores": {"tempo": 2}},
      {"text": "Esquecerem meu aniversário ou datas especiais", "scores": {"presentes": 2}},
      {"text": "Promessas de ajuda que nunca se cumprem", "scores": {"servico": 2}}
    ]},
    {"q": "Como você naturalmente demonstra carinho?", "options": [
      {"text": "Falando: elogio, agradeço, declaro", "scores": {"palavras": 2}},
      {"text": "Reservando tempo exclusivo para a pessoa", "scores": {"tempo": 2}},
      {"text": "Dando lembranças e presentes pensados", "scores": {"presentes": 2}},
      {"text": "Com contato físico: abraço, mão dada, carinho", "scores": {"toque": 2}}
    ]},
    {"q": "Seu parceiro chega em casa depois de um dia péssimo. Você:", "options": [
      {"text": "Digo o quanto ele é capaz e vai superar", "scores": {"palavras": 2}},
      {"text": "Desligo tudo e sento para ouvir com atenção total", "scores": {"tempo": 2}},
      {"text": "Preparo algo especial: doce favorito, mimo surpresa", "scores": {"presentes": 2}},
      {"text": "Dou um abraço longo, sem precisar de palavras", "scores": {"toque": 2}}
    ]},
    {"q": "O presente ideal para você é:", "options": [
      {"text": "Uma carta escrita à mão, com sentimentos verdadeiros", "scores": {"palavras": 2}},
      {"text": "Uma viagem ou experiência para vivermos juntos", "scores": {"tempo": 2}},
      {"text": "Algo que eu mencionei de passagem meses atrás", "scores": {"presentes": 2}},
      {"text": "Não precisa de presente — só fica pertinho de mim", "scores": {"toque": 2}}
    ]},
    {"q": "Na rotina do casal, o que não pode faltar?", "options": [
      {"text": "'Bom dia', 'te amo', mensagens no meio do dia", "scores": {"palavras": 2}},
      {"text": "Nosso ritual: café juntos, série, caminhada", "scores": {"tempo": 2}},
      {"text": "Ajuda concreta: dividir tarefas, resolver as coisas", "scores": {"servico": 2}},
      {"text": "Carinho físico espontâneo ao longo do dia", "scores": {"toque": 2}}
    ]},
    {"q": "O que faria você se sentir valorizado(a) após uma conquista?", "options": [
      {"text": "Meu parceiro dizendo o quanto tem orgulho de mim", "scores": {"palavras": 2}},
      {"text": "Uma comemoração a dois, só nossa", "scores": {"tempo": 2}},
      {"text": "Um presente marcando a ocasião", "scores": {"presentes": 2}},
      {"text": "Ele assumindo as tarefas para eu descansar", "scores": {"servico": 2}}
    ]},
    {"q": "Qual atitude te conquistaria num relacionamento novo?", "options": [
      {"text": "Mensagens carinhosas e atenção verbal constante", "scores": {"palavras": 2}},
      {"text": "A pessoa priorizar tempo comigo mesmo sendo ocupada", "scores": {"tempo": 2}},
      {"text": "Pequenas surpresas: flor, doce, lembrancinha", "scores": {"presentes": 2}},
      {"text": "Gestos práticos: buscar, ajudar, cuidar de mim doente", "scores": {"servico": 2}}
    ]},
    {"q": "No cinema com seu amor, o melhor é:", "options": [
      {"text": "Comentar tudo juntos depois, trocando ideias", "scores": {"palavras": 2}},
      {"text": "O programa em si — estarmos juntos sem distração", "scores": {"tempo": 2}},
      {"text": "Ele ter comprado meu chocolate favorito sem avisar", "scores": {"presentes": 2}},
      {"text": "Ficar de mãos dadas ou abraçados a sessão inteira", "scores": {"toque": 2}}
    ]},
    {"q": "Se seu parceiro sumisse por uma semana de viagem, o que você mais sentiria falta?", "options": [
      {"text": "Das conversas e da voz dele", "scores": {"palavras": 2}},
      {"text": "Da presença — da rotina juntos", "scores": {"tempo": 2}},
      {"text": "Dos gestos de cuidado no dia a dia", "scores": {"servico": 2}},
      {"text": "Do abraço na hora de dormir", "scores": {"toque": 2}}
    ]}
  ],
  "results": {
    "palavras": {"emoji": "💬", "title": "Sua linguagem: Palavras de Afirmação", "text": "Para você, amor se ouve. Elogios sinceros, declarações e reconhecimento verbal enchem seu coração — e palavras duras ferem mais que tudo. Diga isso ao seu parceiro: um 'eu te amo' dito com verdade vale mais para você que qualquer presente. E lembre-se: nem todos falam essa linguagem — o silêncio do outro nem sempre é desamor.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Entender as 5 linguagens a fundo"},
    "tempo": {"emoji": "⏳", "title": "Sua linguagem: Tempo de Qualidade", "text": "Para você, amor se vive junto. Presença real — sem celular, sem pressa — é o que te faz sentir amado(a). Cancelamentos e distração te ferem profundamente. Comunique isso: seu parceiro pode achar que 'estar na mesma casa' basta, quando o que você precisa é atenção total, mesmo que por menos tempo.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Entender as 5 linguagens a fundo"},
    "presentes": {"emoji": "🎁", "title": "Sua linguagem: Presentes", "text": "Para você, amor se materializa. Não por materialismo — o presente é a prova visível de que pensaram em você na sua ausência. O valor emocional importa mais que o preço. Datas esquecidas doem como rejeição. Explique isso ao seu parceiro: uma flor na terça-feira aleatória vale mais que joia em data obrigatória.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Entender as 5 linguagens a fundo"},
    "servico": {"emoji": "🛠️", "title": "Sua linguagem: Atos de Serviço", "text": "Para você, amor é verbo. Quem te ama, age: ajuda sem pedir, resolve, cuida, cumpre o que promete. Palavras bonitas sem ação soam vazias. Preguiça e promessas quebradas são o que mais te machuca. Diga ao seu parceiro: 'me ajudar É me amar' — para você, não existe demonstração maior.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Entender as 5 linguagens a fundo"},
    "toque": {"emoji": "🤗", "title": "Sua linguagem: Toque Físico", "text": "Para você, amor se sente na pele. Abraços, mãos dadas, carinho espontâneo — o toque é seu canal primário de conexão, e não se resume a sexo. Frieza física te machuca mais que palavras duras. Comunique isso: seu parceiro precisa saber que um abraço demorado depois de um dia difícil vale mais que qualquer conselho.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Entender as 5 linguagens a fundo"}
  }
}
}

if __name__ == "__main__":
    write_quiz(PERSONALIDADE)
    write_quiz(LINGUAGEM)
