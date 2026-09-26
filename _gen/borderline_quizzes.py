#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quizzes: borderline-autoavaliacao (self) + parceiro-borderline (partner)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from quiz_template import write_quiz

AUTO = {
"slug": "borderline",
"title": "Teste: Você Tem Traços de Borderline (TPB)? — Autoavaliação",
"desc": "Teste gratuito de 12 perguntas baseado nos critérios do DSM-5 sobre Transtorno de Personalidade Borderline. Avalie impulsividade, instabilidade emocional, medo de abandono e mais. Caráter informativo.",
"breadcrumb": "Traços de Borderline",
"h1": "🧠 Você Tem Traços de Borderline?",
"intro": "Responda com honestidade às 12 perguntas sobre como você se sente, reage e se relaciona. Este teste tem caráter <strong>informativo e educacional — não é diagnóstico</strong>. Em caso de sofrimento, procure um psicólogo ou psiquiatra.<br><br>Em crise emocional: <strong>CVV 188</strong> (24h, gratuito).",
"related_text": "Entenda o Transtorno de Personalidade Borderline em profundidade: sintomas, causas, impacto nos relacionamentos e caminhos de tratamento.",
"related_link": "/artigos/borderline.html",
"related_label": "Ler: Tudo Sobre Borderline",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz o teste de traços de borderline do Amorfy. Vale a reflexão:",
  "supportResult": {"emoji": "💛", "title": "Sua segurança merece atenção", "text": "<p>Você mencionou pensamentos ou experiências de autoagressão. Esse relato merece acolhimento independentemente de qualquer pontuação. Converse com um profissional de saúde e, se possível, com alguém de confiança. Este questionário não determina diagnóstico nem avalia seu risco atual.</p><p>Se houver risco imediato ou ferimento, ligue <a href=\"tel:192\">SAMU 192</a> ou procure uma UPA ou pronto-socorro. Para apoio emocional, o <a href=\"tel:188\">CVV 188</a> atende gratuitamente, 24 horas.</p><p><a href=\"https://www.gov.br/saude/pt-br/composicao/saes/samu-192\">Atendimento de urgência — Ministério da Saúde</a></p>"},
  "questions": [
    {"q": "Com que intensidade você sente medo de ser abandonado(a) ou rejeitado(a) por pessoas importantes?", "options": [
      {"text": "Quase nenhum — lido bem com separações e distância", "value": 0},
      {"text": "Incomoda, mas consigo manejar", "value": 1},
      {"text": "Sofro bastante e às vezes ajo por impulso (mensagens, ligações)", "value": 2},
      {"text": "É insuportável — entro em pânico e posso fazer qualquer coisa para evitar", "value": 3}
    ]},
    {"q": "Seus relacionamentos oscilam entre idealização intensa ('a pessoa perfeita') e desvalorização total ('ela não presta')?", "options": [
      {"text": "Não — vejo as pessoas de forma estável, com qualidades e defeitos", "value": 0},
      {"text": "Oscilo um pouco, mas dentro do normal", "value": 1},
      {"text": "Sim, meus sentimentos mudam radicalmente sobre as mesmas pessoas", "value": 2},
      {"text": "É um padrão constante: amor e ódio extremos, sem meio-termo", "value": 3}
    ]},
    {"q": "Você sente que sua identidade é instável — não sabe quem é, muda de objetivos, valores ou opiniões com frequência?", "options": [
      {"text": "Sei bem quem sou e o que quero", "value": 0},
      {"text": "Mudo um pouco dependendo da fase de vida", "value": 1},
      {"text": "Com frequência não me reconheço ou mudo radicalmente", "value": 2},
      {"text": "Nunca tive uma noção estável de mim mesmo(a) — me sinto vazio(a) ou 'copiando' os outros", "value": 3}
    ]},
    {"q": "Você tem comportamentos impulsivos que podem ser arriscados (gastos, abuso de substâncias, direção perigosa, compulsão alimentar, sexo desprotegido)?", "options": [
      {"text": "Não — sou controlado(a) e calculista", "value": 0},
      {"text": "Às vezes me excedo, mas nada grave", "value": 1},
      {"text": "Sim, com certa frequência e depois me arrependo", "value": 2},
      {"text": "Constantemente me coloco em risco sem pensar nas consequências", "value": 3}
    ]},
    {"q": "Você já se machucou de propósito ou pensou em se machucar em momentos de crise emocional?", "options": [
      {"text": "Nunca — essa ideia é completamente estranha para mim", "value": 0},
      {"text": "Já pensei vagamente, mas nunca fiz", "value": 1, "showSupport": True},
      {"text": "Sim, já me machuquei em momentos de desespero", "value": 2, "showSupport": True},
      {"text": "Isso acontece com frequência — é uma forma de aliviar a dor emocional", "value": 3, "showSupport": True}
    ]},
    {"q": "Suas emoções mudam rápido e com intensidade? (ex.: da euforia para a raiva ou tristeza profunda em horas)", "options": [
      {"text": "Meu humor é relativamente estável", "value": 0},
      {"text": "Tenho altos e baixos, como a maioria das pessoas", "value": 1},
      {"text": "Minhas emoções oscilam bastante — às vezes me sinto fora de controle", "value": 2},
      {"text": "Mudo de humor várias vezes ao dia, com intensidade extrema que me esgota", "value": 3}
    ]},
    {"q": "Você sente um vazio crônico — como se faltasse algo essencial dentro de você, independente do que aconteça?", "options": [
      {"text": "Não — me sinto completo(a) na maior parte do tempo", "value": 0},
      {"text": "Sinto um vazio ocasional, que passa", "value": 1},
      {"text": "O vazio é frequente e me incomoda bastante", "value": 2},
      {"text": "É uma sensação constante e angustiante — nada preenche", "value": 3}
    ]},
    {"q": "Você tem dificuldade em controlar a raiva, com explosões desproporcionais?", "options": [
      {"text": "Raramente fico com raiva e, quando fico, controlo bem", "value": 0},
      {"text": "Fico irritado(a) às vezes, mas dentro do normal", "value": 1},
      {"text": "Sim, tenho explosões que me assustam depois", "value": 2},
      {"text": "Perco o controle com frequência — quebro coisas, grito ou me torno agressivo(a)", "value": 3}
    ]},
    {"q": "Em momentos de estresse, você sente que as coisas não são reais (desrealização), ou tem pensamentos paranoicos (achar que todos estão contra você)?", "options": [
      {"text": "Não — minha percepção da realidade é estável", "value": 0},
      {"text": "Já senti algo parecido, mas raro e passageiro", "value": 1},
      {"text": "Acontece com certa frequência em momentos difíceis", "value": 2},
      {"text": "Sim, com frequência — me desconecto da realidade ou acho que estão tramando contra mim", "value": 3}
    ]},
    {"q": "Como você reage a críticas, mesmo construtivas?", "options": [
      {"text": "Ouço e reflito com calma", "value": 0},
      {"text": "Fico incomodado(a), mas lido", "value": 1},
      {"text": "Me desestabilizo — choro, me isolo ou revido", "value": 2},
      {"text": "É insuportável — sinto que a crítica confirma que sou uma pessoa horrível", "value": 3}
    ]},
    {"q": "Você sente que sua vida é instável em várias áreas ao mesmo tempo (relacionamentos, trabalho, autoimagem, finanças)?", "options": [
      {"text": "Tenho consistência e estabilidade razoável", "value": 0},
      {"text": "Algumas áreas oscilam, mas dá para manejar", "value": 1},
      {"text": "Sinto que estou sempre no caos ou à beira dele", "value": 2},
      {"text": "Minha vida é um turbilhão constante — nada se mantém por muito tempo", "value": 3}
    ]},
    {"q": "Você já buscou ou pensou em buscar ajuda profissional para seu sofrimento emocional?", "options": [
      {"text": "Sim, estou em tratamento e está ajudando", "value": -1},
      {"text": "Sim, já fiz terapia e foi positivo", "value": 0},
      {"text": "Penso em buscar, mas ainda não consegui", "value": 1},
      {"text": "Nunca busquei, apesar do sofrimento — não acredito que ajude", "value": 2}
    ]}
  ],
  "results": [
    {"max": 8, "emoji": "💚", "title": "Poucos traços de TPB", "text": "Você marcou poucas das situações descritas neste questionário. Esse resultado não confirma estabilidade emocional nem exclui dificuldades ou transtornos. Se algo causa sofrimento ou prejudica sua vida, procure avaliação profissional, independentemente da pontuação.", "link": "/artigos/inteligencia-emocional.html", "linkText": "Fortalecer: Inteligência Emocional no Amor"},
    {"max": 16, "emoji": "⚠️", "title": "Alguns traços presentes — atenção recomendada", "text": "Suas respostas indicam a presença de alguns traços associados ao TPB: certa instabilidade emocional, dificuldades com identidade ou relacionamentos que merecem atenção. <strong>Isso não significa que você tem borderline</strong> — esses traços podem estar relacionados a estresse, ansiedade, depressão ou fase de vida. Se esses padrões causam sofrimento significativo ou prejuízo na sua vida, uma avaliação com psicólogo ou psiquiatra pode trazer clareza e alívio.", "link": "/artigos/borderline.html", "linkText": "Ler: Tudo Sobre Borderline"},
    {"max": 24, "emoji": "🔶", "title": "Traços significativos de TPB", "text": "Suas respostas indicam múltiplos traços compatíveis com Transtorno de Personalidade Borderline, com instabilidade em várias áreas da vida e sofrimento emocional importante. <strong>Isso não é um diagnóstico</strong> — apenas um profissional de saúde mental pode diagnosticar, e somente após avaliação clínica completa. A boa notícia: o TPB tem tratamento eficaz. A Terapia Comportamental Dialética (DBT) foi desenvolvida especificamente para borderline e tem resultados sólidos. Procure um psicólogo ou psiquiatra. Você não está sozinho(a) e a melhora é possível. Em crise: <strong>CVV 188</strong> (24h, gratuito).", "link": "/artigos/borderline.html", "linkText": "Ler: Guia completo sobre Borderline"},
    {"max": 99, "emoji": "🔴", "title": "Traços intensos — buscar ajuda é urgente", "text": "Suas respostas indicam sofrimento emocional intenso com múltiplos traços de TPB, incluindo possíveis comportamentos de risco. Isto não substitui avaliação profissional, mas mostra que a busca por ajuda deve ser prioridade. <strong>Não enfrente isso sozinho(a).</strong> Procure hoje mesmo: CAPS da sua cidade (gratuito, sem agendamento), psicólogo particular, ou plano de saúde. Em crise com risco de autoagressão: <strong>CVV 188</strong> ou procure o pronto-socorro mais próximo. O borderline tem tratamento, e a vida pode ser muito mais estável do que parece possível agora. Dê o primeiro passo.", "link": "/artigos/borderline.html", "linkText": "Ler: Tratamentos e recuperação"}
  ]
}
}

PARCEIRO = {
"slug": "parceiro-borderline",
"title": "Teste: Seu Parceiro(a) Tem Traços de Borderline? — Sinais de Alerta",
"desc": "12 perguntas para identificar se seu parceiro ou parceira apresenta traços de Transtorno de Personalidade Borderline: instabilidade emocional, medo de abandono, impulsividade. Teste informativo.",
"breadcrumb": "Parceiro(a) Borderline",
"h1": "🤔 Seu Parceiro(a) Tem Traços de Borderline?",
"intro": "Responda com sinceridade sobre o comportamento <strong>do seu parceiro ou parceira</strong>. Este teste é informativo — <strong>você não pode diagnosticar outra pessoa</strong>. Se os sinais forem fortes, incentive a busca por avaliação profissional com empatia, sem acusação.",
"related_text": "Se seu parceiro tem borderline, aprenda estratégias práticas para construir um relacionamento saudável apesar dos desafios do transtorno.",
"related_link": "/artigos/relacionamento-borderline.html",
"related_label": "Ler: Como Manter um Relacionamento com Pessoa Borderline",
"show_disclaimer": True,
"quiz_data": {
  "mode": "sum",
  "shareText": "Fiz um teste sobre traços de borderline no parceiro(a). Reflexão importante:",
  "supportResult": {"emoji": "💛", "title": "Esse relato merece acolhimento", "text": "<p>Você mencionou pensamentos, ameaças ou episódios de autoagressão no seu parceiro ou parceira. Incentive a busca de ajuda profissional e cuide também da sua segurança. Este questionário não determina diagnóstico nem avalia o risco atual da pessoa.</p><p>Se houver risco imediato ou ferimento, ligue <a href=\"tel:192\">SAMU 192</a> ou procure uma UPA ou pronto-socorro. Para apoio emocional, o <a href=\"tel:188\">CVV 188</a> atende gratuitamente, 24 horas.</p><p><a href=\"https://www.gov.br/saude/pt-br/composicao/saes/samu-192\">Atendimento de urgência — Ministério da Saúde</a></p>"},
  "questions": [
    {"q": "Seu parceiro(a) demonstra medo intenso de abandono — real ou imaginário — com reações extremas?", "options": [
      {"text": "Não — lida de forma equilibrada com separações e distância", "value": 0},
      {"text": "Incomoda, mas nada fora do normal", "value": 1},
      {"text": "Sim, reage com desespero: mensagens, ligações, crises", "value": 2},
      {"text": "É insuportável para ele(a): ameaças, chantagem emocional ou atitudes drásticas", "value": 3}
    ]},
    {"q": "A relação oscila entre idealização intensa ('você é a pessoa mais perfeita do mundo') e desvalorização total ('você é horrível, me arrependi')?", "options": [
      {"text": "Não — a percepção dele(a) sobre mim e sobre os outros é estável", "value": 0},
      {"text": "Há pequenas oscilações, mas normais", "value": 1},
      {"text": "Sim, já passei de 'herói' a 'vilão' várias vezes", "value": 2},
      {"text": "É um ciclo constante: meses de paixão intensa, depois ódio e desprezo", "value": 3}
    ]},
    {"q": "Ele(a) tem uma noção instável de quem é — muda de objetivos, carreira, valores ou estilo de vida radicalmente?", "options": [
      {"text": "Não — tem identidade consistente", "value": 0},
      {"text": "Mudanças normais de fase de vida", "value": 1},
      {"text": "Sim, muda com frequência e de forma radical", "value": 2},
      {"text": "Não parece saber quem é — muda de tudo como quem troca de roupa", "value": 3}
    ]},
    {"q": "Há impulsividade perigosa: gastos excessivos, abuso de álcool/drogas, direção perigosa, compulsão alimentar?", "options": [
      {"text": "Não — é controlado(a) e responsável", "value": 0},
      {"text": "Às vezes se excede, como qualquer pessoa", "value": 1},
      {"text": "Sim, com frequência e isso gera problemas reais", "value": 2},
      {"text": "Constantemente — isso já causou crises sérias na nossa vida", "value": 3}
    ]},
    {"q": "Já houve ameaças de automutilação ou suicídio, ou comportamentos de autoagressão?", "options": [
      {"text": "Nunca — isso nunca fez parte da nossa relação", "value": 0},
      {"text": "Já mencionou pensamentos, mas sem ação", "value": 1, "showSupport": True},
      {"text": "Sim, já aconteceu em momentos de crise", "value": 2, "showSupport": True},
      {"text": "Sim, com frequência — é algo que me assusta e preocupa constantemente", "value": 3, "showSupport": True}
    ]},
    {"q": "O humor dele(a) muda de forma rápida e intensa — euforia, raiva, tristeza profunda em questão de horas?", "options": [
      {"text": "Não — o humor é relativamente estável", "value": 0},
      {"text": "Tem variações normais de humor", "value": 1},
      {"text": "Sim, oscila bastante — às vezes é cansativo acompanhar", "value": 2},
      {"text": "Muda várias vezes ao dia com intensidade que desgasta a relação", "value": 3}
    ]},
    {"q": "Ele(a) demonstra explosões de raiva intensas e desproporcionais ao gatilho?", "options": [
      {"text": "Não — raramente fica com raiva e controla bem", "value": 0},
      {"text": "Tem irritações normais", "value": 1},
      {"text": "Sim, as explosões são frequentes e assustam", "value": 2},
      {"text": "A raiva é um padrão dominante — quebra coisas, grita, pode ser verbalmente agressivo(a)", "value": 3}
    ]},
    {"q": "Ele(a) relata sentir um vazio crônico — algo que falta, angustiante, que nada preenche?", "options": [
      {"text": "Não — nunca mencionou isso", "value": 0},
      {"text": "Já comentou algo assim, mas nada central", "value": 1},
      {"text": "Sim, fala disso com frequência e parece sofrer", "value": 2},
      {"text": "É uma queixa constante que afeta profundamente a vida dele(a)", "value": 3}
    ]},
    {"q": "Ele(a) distorce fatos em discussões, fazendo você duvidar da sua memória ou percepção (gaslighting)?", "options": [
      {"text": "Não — nossas discussões são baseadas em fatos", "value": 0},
      {"text": "Às vezes discordamos sobre como as coisas aconteceram", "value": 1},
      {"text": "Sim, com frequência — saio das brigas confuso(a) sobre o que realmente aconteceu", "value": 2},
      {"text": "Constantemente — já não confio na minha própria percepção dos fatos", "value": 3}
    ]},
    {"q": "Em momentos de estresse, ele(a) tem pensamentos paranoicos ou sente que a realidade não é real?", "options": [
      {"text": "Não — a percepção de realidade é estável", "value": 0},
      {"text": "Já notei algo assim, mas raro", "value": 1},
      {"text": "Sim, acontece com frequência em momentos difíceis", "value": 2},
      {"text": "É comum — ele(a) perde contato com a realidade ou acha que estão conspirando", "value": 3}
    ]},
    {"q": "Você sente que está constantemente pisando em ovos, com medo da próxima explosão ou crise?", "options": [
      {"text": "Não — me sinto livre para ser eu mesmo(a) na relação", "value": 0},
      {"text": "Em alguns assuntos, meço mais as palavras", "value": 1},
      {"text": "Sim, com frequência — nunca sei o que vai desencadear uma crise", "value": 2},
      {"text": "Vivo em estado de alerta permanente — minha energia emocional vai toda para evitar crises", "value": 3}
    ]},
    {"q": "Ele(a) tem consciência de que algo não vai bem e já buscou ou aceitaria buscar ajuda?", "options": [
      {"text": "Sim, está em tratamento e há melhora visível", "value": -2},
      {"text": "Sim, já fez terapia ou está aberto(a) à ideia", "value": -1},
      {"text": "Não tem consciência — acha que o problema sou eu ou os outros", "value": 2},
      {"text": "Nega completamente e reage com raiva à sugestão de ajuda", "value": 3}
    ]}
  ],
  "results": [
    {"max": 7, "emoji": "💚", "title": "Poucos traços de TPB no parceiro(a)", "text": "As respostas indicam que seu parceiro ou parceira apresenta estabilidade emocional, senso de identidade e padrões de relacionamento saudáveis. Conflitos e diferenças existem em qualquer casal — o que você descreve parece dentro da normalidade. Continuem cultivando comunicação aberta e apoio mútuo.", "link": "/artigos/comunicacao.html", "linkText": "Fortalecer: Comunicação Não-Violenta"},
    {"max": 14, "emoji": "⚠️", "title": "Alguns sinais presentes — atenção", "text": "Seu parceiro ou parceira apresenta alguns traços compatíveis com TPB borderline: instabilidade emocional, medo de abandono ou dificuldades com regulação emocional. <strong>Isso não confirma diagnóstico</strong> — esses traços podem estar relacionados a estresse, depressão, ansiedade ou trauma. Se esses padrões causam sofrimento para vocês dois, uma avaliação profissional (psicólogo ou psiquiatra) pode ajudar. Aborde o tema com cuidado: 'tenho notado que você está sofrendo e me preocupo' é melhor que 'você tem borderline'.", "link": "/artigos/relacionamento-borderline.html", "linkText": "Ler: Como Manter um Relacionamento Saudável com Pessoa Borderline"},
    {"max": 22, "emoji": "🔶", "title": "Traços significativos — a relação pede atenção", "text": "As respostas indicam múltiplos traços compatíveis com TPB: oscilações intensas no relacionamento, explosões de raiva, medo de abandono extremo e possível desgaste significativo para você. <strong>Isso não é um diagnóstico para seu parceiro</strong> — apenas um profissional pode diagnosticar. O que você PODE fazer: incentive (com empatia, sem acusação) a busca por avaliação profissional, considere terapia de casal e, fundamentalmente, <strong>cuide de você</strong>. Relacionar-se com alguém com borderline não tratado é muito desgastante — sua saúde mental importa igualmente. Considere terapia para você também.", "link": "/artigos/relacionamento-borderline.html", "linkText": "Ler: Estratégias para o parceiro(a)"},
    {"max": 99, "emoji": "🔴", "title": "Sinais intensos — situação que requer cuidados sérios", "text": "Suas respostas descrevem um cenário com múltiplos sinais de alerta: instabilidade intensa, possíveis comportamentos de risco, raiva descontrolada e desgaste severo para você. Se houver violência física, psicológica ou ameaças à vida — dele ou sua — a prioridade é <strong>segurança imediata</strong>. Procure o CVV (188), uma delegacia da mulher (180) se aplicável, ou um psicólogo. Incentivar a avaliação profissional do seu parceiro é importante, mas <strong>não às custas da sua integridade</strong>. Você não pode curá-lo(a) — pode apoiar, mas o tratamento é responsabilidade dele(a). Busque apoio para você — terapia pode ajudar a enxergar seus limites com clareza.", "link": "/artigos/relacionamento-borderline.html", "linkText": "Ler: Como proteger sua saúde mental"}
  ]
}
}

if __name__ == "__main__":
    write_quiz(AUTO)
    write_quiz(PARCEIRO)
