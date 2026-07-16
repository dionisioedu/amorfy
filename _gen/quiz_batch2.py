#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quizzes batch 2: narcisista, compatibilidade."""
from quiz_template import write_quiz

NARCISISTA = {
"slug": "narcisista",
"title": "Você Está em um Relacionamento Narcisista? — Teste de Sinais",
"desc": "12 perguntas para identificar sinais de abuso narcisista no seu relacionamento: gaslighting, desvalorização, controle e ciclo de idealização. Teste gratuito.",
"breadcrumb": "Relacionamento Narcisista",
"h1": "🚩 Você Está em um Relacionamento Narcisista?",
"intro": "Responda com honestidade às 12 perguntas sobre como seu parceiro age com você. Este teste identifica sinais de alerta — não é diagnóstico.",
"related_text": "Entenda o narcisismo a fundo: sinais, fases do abuso narcisista (idealização, desvalorização, descarte) e o caminho da recuperação.",
"related_link": "/artigos/narcisismo.html",
"related_label": "Ler: Tudo Sobre Narcisismo",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de relacionamento narcisista do Amorfy. Vale a reflexão:",
  "questions": [
    {"q": "Seu parceiro admite erros e pede desculpas genuínas?", "options": [
      {"text": "Sim, reconhece e muda o comportamento", "value": 0},
      {"text": "Às vezes, mas com 'mas' e justificativas", "value": 1},
      {"text": "Raramente — a culpa sempre acaba sendo minha", "value": 2},
      {"text": "Nunca. Ele é incapaz de se enxergar errado", "value": 3}
    ]},
    {"q": "Como ele reage quando você recebe atenção ou tem sucesso?", "options": [
      {"text": "Celebra comigo de verdade", "value": 0},
      {"text": "Parabeniza, mas muda de assunto para si", "value": 1},
      {"text": "Minimiza ou encontra defeitos na conquista", "value": 2},
      {"text": "Fica irritado, me pune com frieza ou compete comigo", "value": 3}
    ]},
    {"q": "Você já duvidou da sua própria memória ou percepção por causa dele?", "options": [
      {"text": "Não, minhas percepções são respeitadas", "value": 0},
      {"text": "Uma ou outra vez, em discussões acaloradas", "value": 1},
      {"text": "Com frequência ele diz que eu 'inventei' ou 'exagerei'", "value": 2},
      {"text": "Constantemente. Já não confio no que vejo e sinto", "value": 3}
    ]},
    {"q": "Como era o início da relação comparado a agora?", "options": [
      {"text": "Evoluiu naturalmente — carinho constante", "value": 0},
      {"text": "Esfriou um pouco, como em toda relação", "value": 1},
      {"text": "Era um conto de fadas intenso; hoje sou criticado(a) pelo que antes era amado", "value": 2},
      {"text": "Ciclos: fases de idealização, depois desprezo, depois 'lua de mel' de novo", "value": 3}
    ]},
    {"q": "Ele respeita seus limites quando você diz 'não'?", "options": [
      {"text": "Sim, mesmo sem gostar", "value": 0},
      {"text": "Aceita, mas fica emburrado ou distante", "value": 1},
      {"text": "Insiste, pressiona e me desgasta até eu ceder", "value": 2},
      {"text": "Meu 'não' vira briga, punição ou chantagem emocional", "value": 3}
    ]},
    {"q": "Como estão suas amizades e relações familiares desde que estão juntos?", "options": [
      {"text": "Normais — ele incentiva minhas relações", "value": 0},
      {"text": "Vejo menos as pessoas, mas por rotina", "value": 1},
      {"text": "Ele critica meus amigos/família e dificulta encontros", "value": 2},
      {"text": "Estou isolado(a). Sobrou praticamente só ele", "value": 3}
    ]},
    {"q": "Ele demonstra empatia quando você está sofrendo?", "options": [
      {"text": "Sim, se importa e acolhe", "value": 0},
      {"text": "Tenta, mas logo perde a paciência", "value": 1},
      {"text": "Minha dor vira drama, exagero ou 'mimimi'", "value": 2},
      {"text": "Já usou minhas fragilidades contra mim depois", "value": 3}
    ]},
    {"q": "Como ele fala dos ex-parceiros?", "options": [
      {"text": "Com respeito e maturidade", "value": 0},
      {"text": "Evita o assunto", "value": 1},
      {"text": "Todos eram 'loucos' ou 'problemáticos'", "value": 2},
      {"text": "Todos loucos — e já me comparou com eles como ameaça", "value": 3}
    ]},
    {"q": "Você sente que precisa 'pisar em ovos' para não irritá-lo?", "options": [
      {"text": "Não, me expresso livremente", "value": 0},
      {"text": "Em alguns assuntos delicados", "value": 1},
      {"text": "Na maior parte do tempo meço cada palavra", "value": 2},
      {"text": "Vivo em alerta constante — nunca sei qual versão dele vou encontrar", "value": 3}
    ]},
    {"q": "Como ele reage a críticas, mesmo leves e construtivas?", "options": [
      {"text": "Ouve e reflete", "value": 0},
      {"text": "Se defende, mas depois considera", "value": 1},
      {"text": "Explode ou revida com ataque pessoal", "value": 2},
      {"text": "Fúria ou punição silenciosa por dias", "value": 3}
    ]},
    {"q": "Quem você era antes da relação ainda existe?", "options": [
      {"text": "Sim — continuo com meus gostos, sonhos e opiniões", "value": 0},
      {"text": "Mudei algumas coisas, como todo casal", "value": 1},
      {"text": "Abandonei muito do que eu era para agradá-lo", "value": 2},
      {"text": "Não me reconheço mais. Minha autoestima foi corroída", "value": 3}
    ]},
    {"q": "Ele assume responsabilidade pelos problemas da relação?", "options": [
      {"text": "Sim, dividimos responsabilidades", "value": 0},
      {"text": "Parcialmente, com resistência", "value": 1},
      {"text": "Não — eu sou 'o problema' da relação, sempre", "value": 2},
      {"text": "Ele reescreve a história: eu fico com toda a culpa, sempre", "value": 3}
    ]}
  ],
  "results": [
    {"max": 8, "emoji": "💚", "title": "Poucos sinais de narcisismo", "text": "Suas respostas indicam uma relação com dinâmicas majoritariamente saudáveis: seu parceiro demonstra empatia, respeita limites e assume responsabilidade. Todo relacionamento tem atritos — o que importa é a capacidade de reparação, e ela parece existir aí. Continue cultivando comunicação aberta.", "link": "/artigos/comunicacao.html", "linkText": "Fortalecer: Comunicação Não-Violenta"},
    {"max": 17, "emoji": "⚠️", "title": "Sinais de alerta presentes", "text": "Suas respostas mostram padrões preocupantes: dificuldade com empatia, limites desrespeitados ou episódios de invalidação. Isso não confirma narcisismo — mas merece atenção séria. Observe se há PADRÃO (não episódios isolados) e converse com pessoas de confiança sobre o que você vive. Considere apoio terapêutico para enxergar a relação com clareza.", "link": "/artigos/narcisismo.html", "linkText": "Ler: sinais de abuso narcisista"},
    {"max": 99, "emoji": "🚨", "title": "Fortes sinais de relacionamento abusivo", "text": "Suas respostas indicam múltiplos padrões característicos de abuso narcisista: gaslighting, isolamento, ciclos de idealização e desvalorização, erosão da sua identidade. Você não está exagerando — e não é culpa sua. Procure apoio: pessoas de confiança e, principalmente, um psicólogo (idealmente com experiência em abuso emocional). Se houver qualquer violência, o CVV (188) e o 180 (Central da Mulher) atendem 24h.", "link": "/artigos/narcisismo.html", "linkText": "Ler: o caminho da recuperação"}
  ]
}
}

COMPATIBILIDADE = {
"slug": "compatibilidade",
"title": "Teste de Compatibilidade Amorosa — Vocês Combinam?",
"desc": "10 perguntas sobre valores, comunicação, intimidade e projetos de vida para medir a compatibilidade real do seu casal. Teste gratuito e imediato.",
"breadcrumb": "Compatibilidade Amorosa",
"h1": "💞 Teste de Compatibilidade Amorosa",
"intro": "Compatibilidade real não é ter tudo igual — é funcionar bem nas diferenças. Responda 10 perguntas sobre a sua relação.",
"related_text": "Entenda as fases que todo casal atravessa e por que a compatibilidade se constrói (não se encontra pronta).",
"related_link": "/artigos/fases-relacionamento.html",
"related_label": "Ler: As Fases de um Relacionamento",
"show_disclaimer": False,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de compatibilidade do Amorfy! Faça com seu par:",
  "questions": [
    {"q": "Sobre valores fundamentais (família, honestidade, fidelidade), vocês:", "options": [
      {"text": "Estão fortemente alinhados", "value": 3},
      {"text": "Concordam na maioria", "value": 2},
      {"text": "Divergem em pontos importantes", "value": 1},
      {"text": "Têm visões de mundo opostas", "value": 0}
    ]},
    {"q": "Quando vocês brigam, o que acontece?", "options": [
      {"text": "Discutimos com respeito e chegamos a acordos", "value": 3},
      {"text": "Esquenta, mas fazemos as pazes rápido e conversamos", "value": 2},
      {"text": "Brigas se repetem sobre os mesmos temas, sem solução", "value": 1},
      {"text": "Há gritos, ofensas ou dias de silêncio punitivo", "value": 0}
    ]},
    {"q": "Sobre planos de futuro (filhos, moradia, carreira, dinheiro):", "options": [
      {"text": "Já conversamos e temos projeto comum", "value": 3},
      {"text": "Concordamos no geral, faltam detalhes", "value": 2},
      {"text": "Evitamos o assunto — dá briga", "value": 1},
      {"text": "Queremos coisas incompatíveis", "value": 0}
    ]},
    {"q": "Vocês riem juntos?", "options": [
      {"text": "Muito — temos humor e piadas próprias do casal", "value": 3},
      {"text": "Com frequência razoável", "value": 2},
      {"text": "Cada vez menos", "value": 1},
      {"text": "Quase nunca — o clima é pesado", "value": 0}
    ]},
    {"q": "Na intimidade física, vocês:", "options": [
      {"text": "Estão satisfeitos e conversam abertamente sobre o assunto", "value": 3},
      {"text": "Têm altos e baixos normais", "value": 2},
      {"text": "Vivem um distanciamento que ninguém menciona", "value": 1},
      {"text": "A intimidade praticamente acabou e virou tabu", "value": 0}
    ]},
    {"q": "Como cada um lida com o jeito de ser do outro?", "options": [
      {"text": "Admiramos as diferenças — elas se complementam", "value": 3},
      {"text": "Aceitamos, com irritações ocasionais", "value": 2},
      {"text": "Um vive tentando mudar o outro", "value": 1},
      {"text": "As diferenças viraram fonte constante de crítica", "value": 0}
    ]},
    {"q": "Vocês confiam um no outro?", "options": [
      {"text": "Totalmente — sem necessidade de vigiar nada", "value": 3},
      {"text": "Sim, com inseguranças pontuais", "value": 2},
      {"text": "Há ciúme e desconfiança frequentes", "value": 1},
      {"text": "Já houve traição/mentiras não resolvidas", "value": 0}
    ]},
    {"q": "Quando um conquista algo, o outro:", "options": [
      {"text": "Vibra genuinamente — somos fãs um do outro", "value": 3},
      {"text": "Parabeniza e apoia", "value": 2},
      {"text": "Demonstra indiferença", "value": 1},
      {"text": "Compete, diminui ou se ressente", "value": 0}
    ]},
    {"q": "Vocês têm tempo de qualidade juntos?", "options": [
      {"text": "Sim, protegemos nossos rituais de casal", "value": 3},
      {"text": "Menos do que gostaríamos, mas existe", "value": 2},
      {"text": "Só dividimos logística: casa, contas, filhos", "value": 1},
      {"text": "Vivemos vidas paralelas sob o mesmo teto", "value": 0}
    ]},
    {"q": "Se você pudesse voltar no tempo, escolheria essa pessoa de novo?", "options": [
      {"text": "Sem pensar duas vezes", "value": 3},
      {"text": "Provavelmente sim", "value": 2},
      {"text": "Tenho dúvidas honestas", "value": 1},
      {"text": "Não", "value": 0}
    ]}
  ],
  "results": [
    {"max": 10, "emoji": "🔴", "title": "Compatibilidade crítica", "text": "As respostas indicam desgaste profundo: pouca conexão, conflitos sem reparação e projetos desalinhados. Isso não significa fim automático — significa que a relação precisa de decisão consciente: ou um recomeço com mudanças reais (idealmente com terapia de casal), ou uma conversa honesta sobre caminhos separados. O pior cenário é a inércia.", "link": "/artigos/fases-relacionamento.html", "linkText": "Entender as fases do relacionamento"},
    {"max": 17, "emoji": "🟡", "title": "Compatibilidade em construção", "text": "Existe base real — mas há áreas de atrito importantes que, ignoradas, tendem a crescer. A boa notícia: os problemas apontados (comunicação, tempo juntos, diferenças mal negociadas) têm ferramentas conhecidas. Escolham UMA área e trabalhem nela primeiro. Compatibilidade é menos sobre sorte e mais sobre habilidade.", "link": "/artigos/comunicacao.html", "linkText": "Aprender Comunicação Não-Violenta"},
    {"max": 24, "emoji": "🟢", "title": "Alta compatibilidade", "text": "Vocês têm o que a pesquisa aponta como núcleo dos casais duradouros: valores alinhados, admiração mútua, confiança e capacidade de reparar conflitos. Atenção aos pontos que pontuaram menos — e continuem investindo: gratidão expressa, novidade e tempo protegido a dois mantêm viva a conexão que vocês já têm.", "link": "/artigos/linguagens-do-amor.html", "linkText": "Descobrir as linguagens do amor"},
    {"max": 99, "emoji": "💎", "title": "Compatibilidade excepcional", "text": "Raro: vocês combinam valores, comunicação saudável, admiração mútua e projeto comum. São o casal que os outros perguntam 'qual é o segredo?'. O segredo, vocês já sabem: escolha diária. Sigam protegendo os rituais do casal e celebrando um ao outro — e inspirem outros casais com a história de vocês.", "link": "/casos/", "linkText": "Ler casos reais de casais"}
  ]
}
}

if __name__ == "__main__":
    write_quiz(NARCISISTA)
    write_quiz(COMPATIBILIDADE)
