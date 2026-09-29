#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rich SEO landing content (sections + FAQ) for each quiz page.

Imported by quiz_batch*/borderline_quizzes via enrich(); keeps the quiz dicts
focused on questions/results while the long-form copy lives here.

Keys are quiz slugs. Each entry:
  "sections": [{"heading", "html"} | {"heading", "type":"dimensions", "items":[{title,body}]}]
  "faq": [{"q", "a"}]
  "dimensions": quiz-engine dimension list (score bars on the result screen)
    - category mode: [{"key": <result key>, "label": ...}]
    - sum mode:      [{"label": ..., "min": n, "max": n}]
"""

LANDING = {
    "personalidade-amorosa": {
        "dimensions": [
            {"key": "colerico", "label": "Colérico — paixão e intensidade"},
            {"key": "sanguineo", "label": "Sanguíneo — leveza e conexão"},
            {"key": "fleumatico", "label": "Fleumático — calma e estabilidade"},
            {"key": "melancolico", "label": "Melancólico — profundidade e lealdade"},
        ],
        "sections": [
            {
                "heading": "O que é o teste de personalidade amorosa?",
                "html": "<p>Este teste parte de uma ideia simples e antiga: as pessoas não amam da mesma forma. A teoria dos <strong>quatro temperamentos</strong> — colérico, sanguíneo, fleumático e melancólico — vem da medicina grega e foi depois reelaborada pela psicologia moderna. Ela não substitui um diagnóstico clínico, mas funciona muito bem como uma lente prática para entender por que você reage do jeito que reage dentro de um relacionamento.</p>"
                "<p>Em 10 perguntas rápidas, o teste identifica qual temperamento domina a sua forma de amar. Não existe temperamento <em>melhor</em>: existe temperamento que combina com o seu e temperamento que te desgasta. Saber qual é o seu é o primeiro passo para parar de repetir os mesmos padrões.</p>",
            },
            {
                "heading": "Os quatro temperamentos no amor",
                "type": "dimensions",
                "items": [
                    {"title": "Colérico — o amor que incendeia", "body": "<p>Ama com intensidade, decide rápido e coloca a relação no centro da vida. Sabe o que quer e vai atrás. O risco é a impaciência: quando o outro não acompanha o ritmo, o colérico pode se tornar controlador ou explosivo.</p><p><strong>Combina com:</strong> fleumático (traz a calma que falta).</p>"},
                    {"title": "Sanguíneo — o amor que ilumina", "body": "<p>Sociável, caloroso, generoso com afeto. Faz o outro se sentir visto e celebrado. O risco é a constância: o sanguíneo se empolga rápido e também se distrai rápido quando a novidade passa.</p><p><strong>Combina com:</strong> melancólico (dá profundidade sem pesar).</p>"},
                    {"title": "Fleumático — o amor que abriga", "body": "<p>Estável, paciente, leal. É o porto seguro do casal — raramente provoca crise, quase sempre apazigua. O risco é a evitação: para não gerar conflito, o fleumático engole o que sente até virar um silêncio pesado.</p><p><strong>Combina com:</strong> colérico (dá direção e iniciativa).</p>"},
                    {"title": "Melancólico — o amor que aprofunda", "body": "<p>Sensível, leal, atento aos detalhes. Ama com uma entrega rara e memoriza o significado de cada gesto pequeno. O risco é a idealização: cobra de si e do outro uma perfeição que ninguém alcança, e sofre por diferenças que existem só na cabeça.</p><p><strong>Combina com:</strong> sanguíneo (traz leveza).</p>"},
                ],
            },
            {
                "heading": "Como usar o resultado na prática",
                "html": "<p>O resultado não é um rótulo — é um mapa. As três perguntas que valem mais que o nome do seu temperamento são: <strong>o que me faz sentir amado?</strong>, <strong>o que me faz fechar as portas?</strong> e <strong>o que eu espero que o outro adivinhe?</strong></p>"
                "<p>Compartilhe o resultado com a pessoa com quem você se relaciona e peça a ela que faça também. Um casal que conhece os dois temperamentos discute menos e negocia melhor — porque para de interpretar diferença como defeito.</p>",
            },
        ],
        "faq": [
            {"q": "O teste de personalidade amorosa tem base científica?", "a": "<p>A teoria dos quatro temperamentos não é um diagnóstico clínico nem substitui avaliação psicológica. Ela é uma ferramenta de autoconhecimento amplamente usada por terapeutas e coaches de relacionamento, com valor prático para identificar padrões de comportamento e comunicação. Trate o resultado como ponto de partida para reflexão, não como sentença.</p>"},
            {"q": "Posso ter mais de um temperamento ao mesmo tempo?", "a": "<p>Sim — quase todo mundo tem um perfil misto. O teste mostra o temperamento <em>dominante</em> e os secundários com peso menor. É comum alguém ser colérico na comunicação e melancólico nas expectativas afetivas, por exemplo.</p>"},
            {"q": "O temperamento muda com o tempo?", "a": "<p>A tendência de base é relativamente estável, mas a expressão dela muda com maturidade, terapia, ciclos de vida e experiências traumáticas. Muitas pessoas respondem o teste em momentos diferentes e percebem deslocamentos significativos.</p>"},
            {"q": "Meu resultado pode explicar por que meus relacionamentos repetem o mesmo problema?", "a": "<p>Pode ajudar bastante. Padrões de escolha (quem você atraia) e de reação (como você reage a conflito) costumam estar ligados ao temperamento. Para entender o mecanismo psicológico por trás da repetição, leia nosso artigo sobre <a href=\"/artigos/repeticao-compulsiva-no-amor.html\">repetição compulsiva no amor</a>.</p>"},
        ],
    },

    "linguagem-do-amor": {
        "dimensions": [
            {"key": "palavras", "label": "Palavras de afirmação"},
            {"key": "tempo", "label": "Tempo de qualidade"},
            {"key": "presentes", "label": "Presentes"},
            {"key": "servico", "label": "Atos de serviço"},
            {"key": "toque", "label": "Toque físico"},
        ],
        "sections": [
            {
                "heading": "O que é a linguagem do amor?",
                "html": "<p>A ideia das <strong>cinco linguagens do amor</strong>, popularizada pelo terapeuta Gary Chapman, parte de uma observação simples: pessoas diferentes se sentem amadas por gestos diferentes. Você pode dar tudo de si e ainda assim o outro sentir que falta — porque você está falando uma língua e ele escutando outra.</p>"
                "<p>Este teste identifica qual das cinco linguagens é a sua principal. Vale notar que sua língua materna de amor não é necessariamente a que você usa para demonstrar — muitas pessoas <em>dão</em> do jeito que gostariam de receber, outras dão o que aprenderam em casa. O teste mostra como você <strong>se sente mais amado</strong>.</p>",
            },
            {
                "heading": "As cinco linguagens, uma a uma",
                "type": "dimensions",
                "items": [
                    {"title": "Palavras de afirmação", "body": "<p>Elogios, agradecimentos e dizer &quot;eu te amo&quot; em voz alta têm peso desproporcional para você. Uma mensagem afetuosa durante o dia vale mais que qualquer presente. Em contrapartida, crítica dura ou indiferença verbal machucam mais do que o normal.</p>"},
                    {"title": "Tempo de qualidade", "body": "<p>Estar junto e <em>presente</em> — sem celular, sem pressa, com atenção inteira. Não é a quantidade de horas, é a qualidade da atenção. Você prefere uma conversa de uma hora a um jantar caro em que ninguém se olha.</p>"},
                    {"title": "Presentes", "body": "<p>Não é materialismo: o presente é um símbolo visível de que a pessoa pensou em você. Vale uma flor colhida na rua tanto quanto um objeto caro. O que importa é o gesto — &quot;eu vi isso e lembrei de você&quot;.</p>"},
                    {"title": "Atos de serviço", "body": "<p>Você se sente amado quando alguém faz algo concreto por você: traz um remédio quando você está doente, resolve aquilo que você adiou, assume uma tarefa sem precisar ser pedido. Palavras convencem menos que atitudes.</p>"},
                    {"title": "Toque físico", "body": "<p>Um abraço, um braço em volta, uma mão dada. Contato físico é a sua forma primária de segurança emocional. Em conversas difíceis, você repara imediatamente se o outro se afasta fisicamente — e isso pesa mais que o argumento em si.</p>"},
                ],
            },
            {
                "heading": "Se sua linguagem não é a do seu parceiro",
                "html": "<p>Uma incompatibilidade de linguagens não é incompatibilidade de amor — é incompatibilidade de <em>tradução</em>. Um casal em que uma pessoa é de toque e a outra de atos de serviço vai se sentir mutuamente carente enquanto ambos estão entregando muito.</p>"
                "<p>A solução não é forçar o outro a mudar de língua: é cada um aprender a expressar afeto na língua que o outro entende, mesmo que seja menos natural. Isso costuma exigir mais <strong>intenção</strong> do que <strong>sentimento</strong>.</p>",
            },
        ],
        "faq": [
            {"q": "Minha linguagem do amor pode ser mais de uma?", "a": "<p>Sim. A maioria das pessoas tem uma linguagem principal e uma secundária com pontuação próxima. Quando as duas primeiras colidem em peso, vale dizer que você precisa das duas para se sentir plenamente amado.</p>"},
            {"q": "A linguagem do amor muda?", "a": "<p>Pode mudar em momentos de vida — quem já foi muito de tempo de qualidade pode virar mais de atos de serviço após ter filhos, por exemplo, quando tempo escasso passa a ser o recurso mais precioso. Mudanças ficam mais raras depois dos 30.</p>"},
            {"q": "Como descobrir a linguagem do meu parceiro?", "a": "<p>Observe o que ele <em>cobra</em> em momentos de mágoa: &quot;você nunca me abraça&quot;, &quot;você não me dá atenção&quot;. A queixa revela a linguagem. Se quiser, peça diretamente que ele faça o teste — comparar os dois resultados é mais revelador que qualquer um isolado.</p>"},
            {"q": "Presentes realmente contam como amor?", "a": "<p>Contam, e não tem nada de superficial nisso. Para quem tem presente como linguagem, o objeto é <em>prova concreta</em> de que foi lembrado. Desprezar essa linguagem (&quot;mas eu faço tanto por ela&quot;) é uma das causas mais comuns de mágoa silenciosa em casais.</p>"},
        ],
    },

    "narcisista": {
        "dimensions": [
            {"label": "Relação saudável (0–8)", "min": 0, "max": 8},
            {"label": "Sinais de alerta (9–17)", "min": 9, "max": 17},
            {"label": "Fortes sinais de abuso (18+)", "min": 18, "max": 36},
        ],
        "sections": [
            {
                "heading": "O que este teste avalia",
                "html": "<p>Este teste de 12 perguntas mede a presença de <strong>padrões característicos de abuso narcisista</strong> no seu relacionamento. Ele não diagnostica o seu parceiro — diagnóstico de transtorno de personalidade narcisista exige avaliação clínica presencial, e uma pessoa pode ser profundamente ferida sem ter um diagnóstico.</p>"
                "<p>O que o teste mede é a <em>sua experiência</em>: com que frequência você é invalidadada, vigiada, desvalorizada ou colocada em dúvida sobre a própria percepção. Essas dinâmicas são o que machuca, independente de qualquer rótulo.</p>"
                "<p><strong>Importante:</strong> um episódio isolado não significa abuso. Procure <em>padrão</em> — repetição, ausência de reparação, escalada.</p>",
            },
            {
                "heading": "Os padrões que o teste procura",
                "type": "dimensions",
                "items": [
                    {"title": "Gaslighting — a dúvida plantada", "body": "<p>Você é levada a questionar a própria memória e sanidade: &quot;isso nunca aconteceu&quot;, &quot;você está exagerando&quot;, &quot;você está louca&quot;. Com o tempo, você para de confiar na sua percepção e passa a depender do outro para saber o que é real.</p>"},
                    {"title": "Ciclo de idealização e desvalorização", "body": "<p>Fases de adoração intensa seguidas de crítica súbita. A oscilação é a qualidade do apego, e é o que mais gera dependência: você fica esperando o retorno da versão encantadora que apareceu no começo.</p>"},
                    {"title": "Controle e isolamento", "body": "<p>Monitoramento, ciúme apresentado como cuidado, afastamento gradual de amigos e família. O isolamento é estratégico: menos testemunhas, menos contraponto à narrativa do abusador.</p>"},
                    {"title": "Ausência de responsabilidade", "body": "<p>Nunca há pedido de desculpa genuíno. A falha é sempre do outro, ou do mundo. Quando existe desculpa, vem com &quot;mas&quot; — e o problema volta a ser você.</p>"},
                ],
            },
            {
                "heading": "O que fazer com um resultado alto",
                "html": "<p>Se seu resultado apontou fortes sinais, comece pelo básico: <strong>você não está exagerando e não é culpa sua</strong>. Reconstrua uma rede de apoio fora da relação — alguém com quem você possa pensar em voz alta sem ser invalidada. Registre episódios por escrito; o gaslighting depende de você esquecer.</p>"
                "<p>Busque um psicólogo com experiência em abuso emocional. Em situação de violência, a central <strong>180</strong> (mulher) e o <strong>CVV 188</strong> atendem 24h. Saiba que sair de uma relação abusiva raramente é um evento único — costuma levar várias tentativas, e isso não indica fraqueza.</p>",
            },
        ],
        "faq": [
            {"q": "Este teste diagnostica narcisismo?", "a": "<p>Não. Nenhum teste online diagnostica transtorno de personalidade. Ele mede <em>padrões de abuso que você experienciou</em>. Diagnóstico exige avaliação clínica, e o foco útil aqui não é rotular o outro — é validar o que você vive e decidir o próximo passo.</p>"},
            {"q": "Meu parceiro é às vezes carinhoso. Ainda pode ser abuso?", "a": "<p>Sim, e essa é justamente a característica mais confusa do abuso narcisista: a oscilação entre encanto e desprezo. A calmaria faz parte do ciclo e costuma ser o que mantém a pessoa presa. O critério é o padrão ao longo do tempo, não os melhores dias.</p>"},
            {"q": "E se eu mesma tiver traços narcisistas?", "a": "<p>Fazer esse teste não te transforma no abusador. Se você reconheceu alguns traços em si mesma em relação a outras áreas da vida, isso pode ser explorado em terapia — e autocrítica honesta é o oposto de narcisismo patológico. Leia também <a href=\"/artigos/amor-proprio-narcisismo-saudavel.html\">narcisismo saudável</a>.</p>"},
            {"q": "Como sair de um relacionamento narcisista?", "a": "<p>De forma planejada, não impulsiva: monte rede de apoio, se possível consulte um advogado (sobre filhos e bens), evite confrontos que alimentem o ciclo. Nosso artigo <a href=\"/artigos/como-sair-de-relacao-com-narcisista.html\">Como sair de uma relação com narcisista</a> detalha o caminho. Para os filhos, veja <a href=\"/artigos/coparentalidade-com-narcisista.html\">coparentalidade com narcisista</a>.</p>"},
        ],
    },

    "compatibilidade": {
        "dimensions": [
            {"label": "Base frágil (0–14)", "min": 0, "max": 14},
            {"label": "Compatibilidade média (15–28)", "min": 15, "max": 28},
            {"label": "Alta compatibilidade (29+)", "min": 29, "max": 42},
        ],
        "sections": [
            {
                "heading": "O que é compatibilidade de casal?",
                "html": "<p>Compatibilidade não é ser parecido. Casais muito similares muitas vezes se estagnam; casais muito diferentes às vezes não conseguem negociar nada. O que sustenta uma relação no longo prazo não é a semelhança de gostos — é a <strong>semelhança de valores</strong> e a <strong>capacidade de resolver conflito</strong>.</p>"
                "<p>Este teste avalia quatro eixos que a pesquisa de relacionamento aponta como preditivos: comunicação, resolução de conflito, alinhamento de valores e segurança emocional. O resultado é um retrato de como vocês funcionam <em>hoje</em>, não uma sentença futura.</p>",
            },
            {
                "heading": "Os quatro eixos avaliados",
                "type": "dimensions",
                "items": [
                    {"title": "Comunicação", "body": "<p>Vocês conseguem dizer o que precisam sem escalada? Escutam para entender ou para responder? Crítica, defensividade, desprezo e obstrução — os &quot;quatro cavaleiros&quot; identificados por John Gottman — são os melhores preditores de ruptura.</p>"},
                    {"title": "Resolução de conflito", "body": "<p>Nenhum casal evita conflito; os que duram <em>reparam</em> bem. Após uma discussão, existe reconciliação real, ou o assunto fica engavetado e volta pior depois? Reparação é a habilidade mais decisiva de toda relação.</p>"},
                    {"title": "Alinhamento de valores", "body": "<p>Dinheiro, filhos, família de origem, religião, ambição, fidelidade, divisão de trabalho. Divergências aqui são as que mais geram ruptura tardia — porque não desaparecem com o tempo, só se acumulam.</p>"},
                    {"title": "Segurança emocional", "body": "<p>Você pode ser vulnerável sem medo de punição? Nesta relação, você é livre para discordar, para estar triste, para falhar? Um relacionamento em que você regula o outro a todo momento é desgastante por definição.</p>"},
                ],
            },
            {
                "heading": "Compatibilidade baixa não significa término",
                "html": "<p>Um resultado baixo não diz &quot;termine&quot;. Ele diz que a relação exige trabalho explícito — e que hoje vocês não estão fazendo esse trabalho. Compatibilidade é <strong>construída</strong>, não descoberta: casais antigos que parecem feitos um para o outro normalmente passaram décadas desenvolvendo exatamente esses quatro eixos.</p>"
                "<p>Se o resultado revelou fragilidade em comunicação ou conflito, terapia de casal tem bons resultados nesses pontos específicos. Se revelou divergência profunda de valores (filhos, fidelidade, projeto de vida), é mais honesto reconhecer isso cedo do que esperar que mude.</p>",
            },
        ],
        "faq": [
            {"q": "Preciso que meu parceiro responda também?", "a": "<p>O teste funciona melhor respondido individualmente e depois comparado. A diferença entre as duas percepções é frequentemente a informação mais valiosa — quem está mais satisfeito costuma ser quem está menos atento ao que o outro sente.</p>"},
            {"q": "Casais muito diferentes podem dar certo?", "a": "<p>Sim, se os valores centrais estiverem alinhados. Divergir no gosto musical não é problema; divergir sobre ter filhos, fidelidade ou prioridade da carreira é. A regra prática: diferenças de <em>estilo</em> são administráveis, diferenças de <em>valores</em> não.</p>"},
            {"q": "Como melhorar uma compatibilidade baixa?", "a": "<p>Comece pela comunicação — é o eixo que mais destrava os outros. Nossa série sobre <a href=\"/artigos/comunicacao.html\">comunicação não-violenta</a> e <a href=\"/artigos/conflitos.html\">como resolver conflitos</a> traz técnicas concretas. Mudar uma variável por vez é mais eficaz que tentar consertar tudo.</p>"},
            {"q": "Compatibilidade pode melhorar com o tempo?", "a": "<p>Pode, mas não automaticamente. Sem intenção, o tempo tende a aprofundar os padrões existentes — inclusive os ruins. Casais que melhoram são os que transformam insatisfação em conversa e conversa em acordo.</p>"},
        ],
    },

    "borderline": {
        "dimensions": [
            {"label": "Baixa presença de traços (0–12)", "min": 0, "max": 12},
            {"label": "Traços moderados (13–24)", "min": 13, "max": 24},
            {"label": "Elevada presença de traços (25+)", "min": 25, "max": 48},
        ],
        "sections": [
            {
                "heading": "O que este teste avalia",
                "html": "<p>Este teste de autoavaliação explora traços associados ao <strong>Transtorno de Personalidade Borderline (TPB)</strong> a partir de dimensões inspiradas nos critérios do DSM-5: medo de abandono, instabilidade dos relacionamentos, identidade difusa, impulsividade, oscilação de humor, vazio, raiva intensa e ideação paranoica.</p>"
                "<p>O TPB é um dos transtornos mais <strong>estigmatizados</strong> e, ironicamente, um dos que têm melhor resposta a tratamento — especialmente à terapia comportamental dialética (DBT). Ter traços elevados não significa ser &quot;difícil&quot; ou &quot;quebrada&quot;. Significa que sua regulação emocional funciona de um jeito que exige mais recursos.</p>"
                "<p>Este teste é informativo e <strong>não substitui avaliação profissional</strong>. Nenhum resultado online fecha diagnóstico.</p>",
            },
            {
                "heading": "As dimensões do TPB que o teste observa",
                "type": "dimensions",
                "items": [
                    {"title": "Medo de abandono", "body": "<p>Pavor — desproporcional ao contexto — de ser deixado. Um atraso, um tom mais seco, uma resposta curta podem ser lidos como prenúncio de abandono e disparar uma crise interna.</p>"},
                    {"title": "Oscilação de humor", "body": "<p>Mudanças rápidas entre bem-estar e desespero, muitas vezes em questão de horas. Não é &quot;drama&quot;: é reatividade emocional intensa com retorno lento à linha de base.</p>"},
                    {"title": "Instabilidade de identidade", "body": "<p>Sensação de não saber quem se é, mudança de objetivos, crenças e autopercepção conforme a companhia. Dificuldade em manter um sentido contínuo de si.</p>"},
                    {"title": "Impulsividade e autossabotagem", "body": "<p>Impulsos com alto custo: gastos, substâncias, direção, sexo desprotegido, rompimentos súbitos. Frequentemente a pessoa sabe que vai se arrepender e faz mesmo assim — porque a regulação emocional falha no momento crítico.</p>"},
                ],
            },
            {
                "heading": "Se o resultado foi alto",
                "html": "<p>Vale lembrar: um teste pode ter alta pontuação em pessoas que estão em <strong>um momento de crise</strong> e não têm TPB — luto, abuso em curso, burnout e trauma complexo podem simular vários desses traços. Daí a importância de avaliação presencial.</p>"
                "<p>Se muitos itens soaram familiares, o caminho mais útil é procurar um psicólogo que trabalhe com <strong>DBT</strong> ou terapia focada em trauma. TPB tem tratamento com boa evidência — pessoas com o transtorno lideram vidas plenas, e &quot;ter TPB&quot; não define o que você é capaz de amar ou de realizar.</p>",
            },
        ],
        "faq": [
            {"q": "Um resultado alto significa que eu tenho TPB?", "a": "<p>Não. Nenhum teste online fecha diagnóstico de transtorno de personalidade — e há sobreposição enorme entre TPB, trauma complexo, bipolaridade e TDAH. Este resultado indica que vale buscar uma <em>avaliação profissional</em>, e só isso.</p>"},
            {"q": "TPB tem tratamento?", "a": "<p>Sim, e um dos melhores entre os transtornos de personalidade. A terapia comportamental dialética (DBT) e a psicoterapia focada em transferência (TFP) têm evidência robusta. Muitas pessoas deixam de preencher critérios diagnósticos após anos de tratamento consistente.</p>"},
            {"q": "Dá para ter um relacionamento saudável com TPB?", "a": "<p>Sim. Relações estáveis e amorosas são possíveis — e conhecer o próprio funcionamento emocional ajuda muito. Nosso artigo <a href=\"/artigos/tenho-borderline-e-quero-amar.html\">Tenho borderline e quero amar</a> é escrito especificamente para isso.</p>"},
            {"q": "O que é DBT e por que é recomendada?", "a": "<p>A Terapia Comportamental Dialética combina aceitação e mudança: ensina habilidades de tolerância ao mal-estar, regulação emocional, eficácia interpessoal e mindfulness. Foi desenvolvida por Marsha Linehan, que tinha o próprio diagnóstico, e é hoje o padrão-ouro para TPB.</p>"},
        ],
    },

    "parceiro-borderline": {
        "dimensions": [
            {"label": "Dinâmica pouco afetada (0–12)", "min": 0, "max": 12},
            {"label": "Sinais moderados (13–24)", "min": 13, "max": 24},
            {"label": "Dinâmica marcadamente afetada (25+)", "min": 25, "max": 48},
        ],
        "sections": [
            {
                "heading": "Para quem é este teste",
                "html": "<p>Este teste é para quem <strong>convive ou se relaciona</strong> com alguém que tem traços de borderline — e sente que a relação oscila entre intensidade e instabilidade de um jeito cansativo. Ele avalia a <em>dinâmica da relação</em>, não a pessoa: como você experiencia a montanha-russa, o que você já tentou e o quanto isso tem custado.</p>"
                "<p>Muitos parceiros chegam exaustos, confusos e se perguntando se estão loucos. Uma pista importante: se você se pega <strong>pisando em ovos</strong> e regulando o humor do outro para manter a paz, provavelmente está assumindo um papel que não é saudável para ninguém.</p>",
            },
            {
                "heading": "As dinâmicas mais comuns",
                "type": "dimensions",
                "items": [
                    {"title": "Ciclo de idealização e desvalorização", "body": "<p>Fases de adoração intensa seguidas de desprezo, muitas vezes sem gatilho claro. Você fica tentando reproduzir a fase boa — e comete o erro de acreditar que o problema é algo que você fez ou deixou de fazer.</p>"},
                    {"title": "Pisando em ovos", "body": "<p>Antes de falar qualquer coisa minimamente difícil, você calcula o risco. Ferimentos banais (um atraso, um &quot;hmm&quot;) podem virar crise. Isso faz o parceiro desenvolver hipervigilância — um estresse crônico com efeitos reais na saúde.</p>"},
                    {"title": "Punição por limite", "body": "<p>Toda tentativa de estabelecer limite (dormir mais cedo, sair sozinho, falar do próprio cansaço) pode ser lida como abandono — e respondida com escalada emocional, ameaça ou punição. O resultado é que os limites nunca se firmam.</p>"},
                    {"title": "Esgotamento do cuidador", "body": "<p>Você se tornou o regulador emocional da relação. Isso é insustentável: ninguém pode ser responsável pela estabilidade emocional de outra pessoa. O desgaste costuma vir acompanhado de culpa por sentir cansaço.</p>"},
                ],
            },
            {
                "heading": "Como cuidar de você nessa relação",
                "html": "<p>A primeira coisa a entender é que <strong>você não pode ser o terapeuta do seu parceiro</strong>. Apoiar é diferente de tratar. Amar é diferente de assumir. Muitas pessoas confundem as duas coisas e chegam ao esgotamento achando que &quot;se amassem o suficiente, resolveria&quot;.</p>"
                "<p>Limites não são crueldade. Um limite claro é o maior presente que você pode dar a uma relação com esse perfil — ele reduz a ansiedade de ambos. Também é legítimo pedir que o parceiro esteja em tratamento, e é legítimo buscar apoio terapêutico <strong>para você</strong>, não apenas para ele. Leia nosso artigo <a href=\"/artigos/relacionamento-borderline.html\">Relacionamento com pessoa borderline</a> para o panorama completo.</p>",
            },
        ],
        "faq": [
            {"q": "Isso significa que a pessoa tem borderline?", "a": "<p>Não. O teste avalia a dinâmica do relacionamento, não faz diagnóstico de terceiros — o que aliás seria eticamente problemático. Mesmo que houvesse diagnóstico, a pergunta útil não é &quot;o que ele tem&quot; e sim &quot;o que eu tolero e o que eu preciso&quot;.</p>"},
            {"q": "Como falar sobre tratamento sem que ele(a) se sinta atacado(a)?", "a": "<p>Uma abordagem que funciona melhor: comece pelo <em>você</em>, não pelo outro. &quot;Eu tenho me sentido esgotado e queria apoio profissional para mim&quot; abre menos defesa do que &quot;você precisa se tratar&quot;. Terapeutas de casal ajudam exatamente nessa conversa.</p>"},
            {"q": "É possível ter um relacionamento estável com uma pessoa borderline?", "a": "<p>Sim, especialmente quando há tratamento consistente e limites claros. O que faz a diferença não é o diagnóstico e sim se ambas as partes assumem responsabilidade pela própria parte do ciclo — e se existe reparação após as crises.</p>"},
            {"q": "Estou exausto(a). Isso é normal?", "a": "<p>É comum, mas não é saudável nem inevitável. Esgotamento do cuidador é um fenômeno documentado, com sintomas de ansiedade, insônia e perda de interesse. Isso é um sinal claro de que você precisa de apoio próprio — veja <a href=\"/artigos/capacidade-de-ficar-so.html\">capacidade de ficar só</a> e <a href=\"/artigos/dependencia-emocional-psicanalise.html\">dependência emocional</a>.</p>"},
        ],
    },
    "meus-tracos-narcisistas": {
        "dimensions": [
            {"label": "Autoimagem saudável (0–7)", "min": 0, "max": 7},
            {"label": "Traços presentes (8–15)", "min": 8, "max": 15},
            {"label": "Traços acentuados (16–24)", "min": 16, "max": 24},
            {"label": "Padrão severo (25+)", "min": 25, "max": 35},
        ],
        "sections": [
            {
                "heading": "Por que fazer um teste de traços narcisistas em si mesmo?",
                "html": "<p>A maioria dos testes sobre narcisismo pergunta sobre o <em>outro</em>. Este inverte o espelho — e é aí que mora o valor. O narcisismo é um espectro presente em todos nós em algum grau: o que separa o traço saudável do problemático não é a presença, é a <strong>rigidez</strong> e o <strong>custo para os outros</strong>.</p>"
                "<p>Responder com honestidade é mais difícil do que parece, porque o próprio padrão narcísico tende a proteger a autoimagem da crítica. Se você chegou até aqui e respondeu de verdade, já está à frente da maioria.</p>",
            },
            {
                "heading": "O que o teste avalia",
                "type": "dimensions",
                "items": [
                    {"title": "Tolerância à crítica", "body": "<p>Como você recebe um apontamento. Traços narcísicos se revelam na reação desproporcional a uma crítica pequena: raiva, frieza, desejo de revanche ou distorção da memória para sair como vítima.</p>"},
                    {"title": "Capacidade de empatia", "body": "<p>Conseguir se colocar no lugar do outro sem transformar tudo em você. A dificuldade de escutar uma dor sem competir (&quot;isso não é nada, comigo foi pior&quot;) é um marcador importante.</p>"},
                    {"title": "Relação com admiração", "body": "<p>Quanto do seu bem-estar depende de ser notado. A autoestima que se sustenta de dentro difere da que precisa de abastecimento externo constante — e a segunda desgasta quem está por perto.</p>"},
                    {"title": "Assunção de responsabilidade", "body": "<p>Conseguir pedir desculpa genuína e revisar a própria parte no fim de uma relação. A incapacidade de se enxergar errado é o coração do padrão narcísico.</p>"},
                ],
            },
            {
                "heading": "O que fazer com um resultado alto",
                "html": "<p>Um resultado alto não é uma condenação — é um diagnóstico de <em>custo</em>. Traços narcísicos quase sempre nascem de feridas antigas: pessoas que precisaram se blindar para sobreviver, e a blindagem virou prisão. O tratamento existe e funciona.</p>"
                "<p>O passo mais transformador é procurar um psicólogo especializado em questões de personalidade e vínculo. Leia também nosso artigo sobre <a href=\"/artigos/amor-proprio-narcisismo-saudavel.html\">amor-próprio versus narcisismo</a> para entender a fronteira entre cuidar de si e se fechar para o outro.</p>",
            },
        ],
        "faq": [
            {"q": "Todo mundo tem um pouco de narcisismo?", "a": "<p>Sim. O narcisismo saudável é o amor-próprio que nos permite estabelecer limites, cuidar de nós e buscar realização. Ele vira problema quando se torna rígido, quando o outro vira ferramenta e quando a crítica é impossível de ser recebida.</p>"},
            {"q": "Fazer este teste significa que tenho transtorno de personalidade narcisista?", "a": "<p>Não. O teste mede traços e padrões de comportamento, não faz diagnóstico clínico — que exige avaliação profissional presencial. Apenas um psicólogo ou psiquiatra pode diagnosticar transtorno de personalidade.</p>"},
            {"q": "Dá para mudar traços narcísicos?", "a": "<p>Dá, quando existe desejo genuíno. O desafio é que o próprio padrão tende a resistir à mudança (a crítica é vivida como ataque). Por isso o acompanhamento terapêutico é tão importante: ele cria um espaço seguro para olhar esses padrões sem defesa.</p>"},
            {"q": "Meu resultado foi alto. Por onde começo?", "a": "<p>Comece reconhecendo o que já fez: responder honestamente é o primeiro e mais difícil passo. Depois, busque um psicólogo. Leia nosso artigo sobre <a href=\"/artigos/narcisismo.html\">narcisismo</a> para entender o espectro e os caminhos de tratamento.</p>"},
        ],
    },

    "parceiro-pronto-relacionamento": {
        "dimensions": [
            {"label": "Pronto(a) (0–8)", "min": 0, "max": 8},
            {"label": "Em processo (9–16)", "min": 9, "max": 16},
            {"label": "Pouco disponível (17–25)", "min": 17, "max": 25},
            {"label": "Não está pronto(a) (26+)", "min": 26, "max": 35},
        ],
        "sections": [
            {
                "heading": "O que significa estar pronto para um relacionamento",
                "html": "<p>Gostar de alguém e estar <strong>disponível</strong> para essa pessoa são duas coisas diferentes — e confundir as duas é a causa de muito sofrimento. Prontidão não é sobre o tamanho do sentimento: é sobre <em>capacidade real</em> de se comprometer, de fazer espaço na vida e de suportar o trabalho que uma relação exige.</p>"
                "<p>Este teste avalia o que se vê, não o que se escuta. Palavras bonitas e promessas não sustentam um vínculo; <strong>coerência</strong>, <strong>constância</strong> e <strong>reparação</strong> sim.</p>",
            },
            {
                "heading": "Os sinais que o teste procura",
                "type": "dimensions",
                "items": [
                    {"title": "Clareza e intenção", "body": "<p>Uma pessoa pronta fala o que quer sem ambiguidade. Quem vive de &quot;não gosto de rótulos&quot;, de conversas vagas e de deixar tudo &quot;em aberto&quot; está, na prática, te dizendo que não quer se comprometer — só não tem coragem de falar claro.</p>"},
                    {"title": "Disponibilidade real", "body": "<p>Tempo, energia e espaço na vida. Alguém que aparece e some conforme a conveniência, que só sobra espaço quando interessa, não está pronto — independente do quanto diz que te ama.</p>"},
                    {"title": "Vulnerabilidade", "body": "<p>Estar pronto inclui a capacidade de se abrir, admitir medo e insegurança, e deixar o outro entrar. Quem se fecha por completo ou transforma tudo em piada ainda não está disponível para intimidade.</p>"},
                    {"title": "Resolução do passado", "body": "<p>Uma pessoa que ainda fala mal de todos os ex, que recém saiu de uma relação sem processar, ou que ainda está emocionalmente presa ao passado, não tem espaço livre para construir um novo vínculo.</p>"},
                ],
            },
            {
                "heading": "O que fazer se ele(a) não está pronto",
                "html": "<p>A resposta mais difícil e mais libertadora é esta: <strong>você não pode fabricar a prontidão do outro</strong>. Você pode esperar, insistir, fazer tudo certo — e ainda assim a disponibilidade só nasce de dentro, no tempo (e na terapia) da pessoa.</p>"
                "<p>Em vez de tentar convencer alguém a querer o que não quer, pergunte-se o que <em>você</em> quer e o quanto está disposto(a) a esperar. Leia nosso artigo sobre <a href=\"/artigos/dependencia-emocional-psicanalise.html\">dependência emocional</a> para reconhecer quando a espera virou apego doentio.</p>",
            },
        ],
        "faq": [
            {"q": "Ele(a) diz que me ama mas some. Isso é prontidão?", "a": "<p>Não. Amor é comportamento, não declaração. Uma pessoa que ama de verdade mas não consegue estar presente pode ter feridas a tratar — mas o efeito sobre você é o mesmo. Consistência é o teste definitivo de prontidão.</p>"},
            {"q": "Posso ajudar alguém a ficar pronto(a)?", "a": "<p>Você pode apoiar, mas não pode fazer o trabalho pelo outro. A prontidão emocional se constrói com autoconhecimento e, muitas vezes, terapia. Virar terapeuta do parceiro é um atalho para o esgotamento.</p>"},
            {"q": "Quanto tempo é razoável esperar?", "a": "<p>Não há um número mágico, mas há um sinal: a tendência. Se em meses os comportamentos não mudam, dificilmente mudarão apenas com o tempo. Coloque um limite interno de quanto de você está disposto(a) a investir sem reciprocidade.</p>"},
            {"q": "E se a pessoa é maravilhosa mas tem medo de se comprometer?", "a": "<p>Esse é o caso mais doloroso, porque o medo é real e a pessoa não é vilã. Ainda assim, medo não justifica comportamento inconsistente indefinidamente. A questão é se o medo está sendo tratado ou apenas administrado às suas custas. Veja <a href=\"/artigos/medo-de-amar-contraintimidade.html\">medo de amar e contraintimidade</a>.</p>"},
        ],
    },

    "por-que-afasto-pessoas": {
        "dimensions": [
            {"key": "medo_intimidade", "label": "Medo de intimidade"},
            {"key": "medo_abandono", "label": "Medo de abandono"},
            {"key": "autossabotagem", "label": "Autossabotagem"},
            {"key": "controle", "label": "Necessidade de controle"},
        ],
        "sections": [
            {
                "heading": "Por que algumas pessoas afastam o que mais desejam",
                "html": "<p>Quando os relacionamentos parecem sempre começar bem e terminar do mesmo jeito, raramente é azar. É <strong>padrão</strong> — um conjunto de respostas automáticas que você aprendeu cedo e repete sem perceber. O padrão te protegeu em algum momento; hoje, ele te isola.</p>"
                "<p>Este teste ajuda a nomear o seu padrão dominante. Dar nome é o primeiro passo, porque só se muda o que se vê.</p>",
            },
            {
                "heading": "Os quatro padrões de afastamento",
                "type": "dimensions",
                "items": [
                    {"title": "Medo de intimidade", "body": "<p>Você ergue muros justamente quando a relação começa a dar certo. A proximidade é vivida como invasão ou perda de liberdade, então você cria distância — e chama isso de independência. O muro que protege é o mesmo que isola.</p>"},
                    {"title": "Medo de abandono", "body": "<p>Você se agarra tão forte que sufoca. O pavor de ser deixado(a) vira testes, cobranças e uma ansiedade que esgota o outro — e acaba produzindo exatamente o abandono que temia.</p>"},
                    {"title": "Autossabotagem", "body": "<p>Você rejeita antes de ser rejeitado(a). Lá no fundo não acredita que merece amor, então encontra defeitos, termina cedo demais ou se boicota quando tudo vai bem. A narrativa antiga vira profecia.</p>"},
                    {"title": "Necessidade de controle", "body": "<p>A imprevisibilidade do outro te dá vertigem. Você cobra, analisa, estabelece regras e quer prever cada passo — e ninguém respira nesse regime. Confiar e tolerar incerteza é o que te libertaria.</p>"},
                ],
            },
            {
                "heading": "Como reescrever o padrão",
                "html": "<p>Padrões relacionais nascem na infância e se consolidam no vínculo — por isso são tão teimosos. A boa notícia é que <strong>padrão se reescreve em vínculo</strong>: justamente numa relação segura (terapêutica ou afetiva) você pode experimentar formas novas de estar com o outro.</p>"
                "<p>Comece pequeno: na próxima vez que sentir o impulso de fugir, agarrar, sabotar ou controlar, <strong>pausa e nomeia</strong>. Diga o que sente em vez de agir o padrão. Leia nosso artigo sobre <a href=\"/artigos/estilos-de-apego-no-amor.html\">estilos de apego no amor</a> para entender a raiz desses comportamentos.</p>",
            },
        ],
        "faq": [
            {"q": "Eu posso ter mais de um padrão?", "a": "<p>Sim. Os padrões se misturam e variam conforme a pessoa com quem você se relaciona. O teste aponta o dominante, mas é comum reconhecer traços de dois ou mais.</p>"},
            {"q": "De onde vêm esses padrões?", "a": "<p>Quase sempre da infância, do tipo de apego que você desenvolveu com os cuidadores. Um lar imprevisível pode gerar medo de abandono; um lar que sufocava, medo de intimidade. Veja <a href=\"/artigos/estilos-de-apego-no-amor.html\">estilos de apego</a>.</p>"},
            {"q": "É possível mudar sozinho(a)?", "a": "<p>É possível começar sozinho(a) — reconhecer o padrão e pausar antes de agir já é mudança. Mas como esses padrões nascem em vínculo, a transformação mais profunda costuma acontecer em vínculo: terapia ou uma relação consciente.</p>"},
            {"q": "Como parar de afastar alguém que eu amo?", "a": "<p>O antídoto do padrão é a comunicação honesta: em vez de fugir, agarrar, sabotar ou controlar, diga o que sente e o que precisa. Compartilhe o resultado deste teste com a pessoa — entender juntos o mecanismo desarma boa parte da repetição.</p>"},
        ],
    },

    "autossabotagem-amorosa": {
        "dimensions": [
            {"label": "Pouca sabotagem (0–7)", "min": 0, "max": 7},
            {"label": "Sabotagem leve (8–15)", "min": 8, "max": 15},
            {"label": "Sabotagem frequente (16–24)", "min": 16, "max": 24},
            {"label": "Sabotagem severa (25+)", "min": 25, "max": 35},
        ],
        "sections": [
            {
                "heading": "O que é autossabotagem amorosa",
                "html": "<p>Autossabotagem é quando você boicota aquilo que mais deseja — geralmente sem perceber. No amor, ela aparece de formas reconhecíveis: terminar cedo demais, criar brigas quando está tudo bem, não acreditar no afeto que recebe, ou escolher sistematicamente pessoas indisponíveis.</p>"
                "<p>O mecanismo é uma <strong>proteção invertida</strong>: por medo de ser rejeitado(a), você rejeita primeiro. Por medo de dar errado, você estraga antes. É o controle que você acha que tem sobre uma dor que acha inevitável.</p>",
            },
            {
                "heading": "As faces da autossabotagem",
                "type": "dimensions",
                "items": [
                    {"title": "Término preventivo", "body": "<p>Terminar uma relação boa &quot;do nada&quot;, sem motivo claro, movido por uma ansiedade difusa. Depois vem o arrependimento — e a repetição. É o medo de ser abandonado(a) agindo antes que o outro o faça.</p>"},
                    {"title": "Criação de crises", "body": "<p>Quando a relação está calma e estável, um incômodo cresce até virar briga. A calmaria é vivida como suspeita, então você a interrompe com um problema. Brigar é uma forma (disfuncional) de sentir que a relação é real.</p>"},
                    {"title": "Descrédito do afeto", "body": "<p>Desconfiar de elogios, minimizar declarações, achar que o outro &quot;vai se decepcionar&quot; quando te conhecer de verdade. Você não acredita que merece amor, então não deixa o amor chegar.</p>"},
                    {"title": "Atração pelo indisponível", "body": "<p>Escolher sempre quem não pode ou não quer te amar: gente casada, distante, comprometida com outra coisa. É o jeito mais seguro de nunca precisar se entregar de verdade.</p>"},
                ],
            },
            {
                "heading": "Como quebrar o ciclo",
                "html": "<p>O primeiro passo é <strong>reconhecer o padrão</strong> e perceber que ele é uma repetição, não uma coincidência. A autossabotagem é, antes de tudo, uma forma de ansiedade: você antecipa a dor para tentar controlá-la.</p>"
                "<p>Terapia — especialmente abordagens focadas em vínculos e em esquemas — é o caminho mais eficaz. Leia nosso artigo sobre <a href=\"/artigos/repeticao-compulsiva-no-amor.html\">repetição compulsiva no amor</a> para entender por que você reencena a mesma história.</p>",
            },
        ],
        "faq": [
            {"q": "Por que eu saboto uma relação boa?", "a": "<p>Porque a relação boa ameaça a sua crença de que você não merece amor. Quando algo contradiz uma crença profunda, a mente tenta restaurar a coerência — às vezes estragando exatamente o que a contradiz. É inconsciente, por isso precisa ser trazido à consciência.</p>"},
            {"q": "Autossabotagem é falta de amor?", "a": "<p>Não. É geralmente o oposto: excesso de medo. Você ama, mas o medo de perder (ou de não merecer) é maior que a confiança no vínculo. O amor existe; o que falta é a segurança interna para recebê-lo.</p>"},
            {"q": "Como saber se estou me sabotando agora?", "a": "<p>Pergunte-se: essa decisão vem do medo ou do amor? Quando você age para fugir de uma dor imaginária (terminar antes de ser trocado, brigar antes de ser criticado), é sabotagem. Quando age para construir algo real, é entrega.</p>"},
            {"q": "Isso tem cura?", "a": "<p>Sim, com trabalho. Não é um defeito de caráter — é um padrão aprendido que pode ser desaprendido. A combinação de autoconhecimento, terapia e a experiência de uma relação segura é o que reescreve o padrão. Veja <a href=\"/artigos/tracos-carater.html\">traços de caráter</a>.</p>"},
        ],
    },

    "ciume-inveja-relacionamento": {
        "dimensions": [
            {"label": "Emoções equilibradas (0–7)", "min": 0, "max": 7},
            {"label": "Presentes, sob controle (8–15)", "min": 8, "max": 15},
            {"label": "Intensas (16–24)", "min": 16, "max": 24},
            {"label": "Dominantes (25+)", "min": 25, "max": 35},
        ],
        "sections": [
            {
                "heading": "Ciúme e inveja: duas emoções que se confundem",
                "html": "<p>Ciúme é o <strong>medo de perder</strong> o que se tem. Inveja é o <strong>incômodo com o que o outro tem</strong>. No relacionamento elas se misturam e se alimentam: a inveja da vida do outro pode virar medo de que ele te troque, e o ciúme pode mascarar a inveja de quem o outro é ou conquistou.</p>"
                "<p>Nenhuma das duas é, em si, má — são emoções humanas e informativas. O problema é quando elas comandam suas atitudes em vez de apenas passar por você.</p>",
            },
            {
                "heading": "O que suas emoções estão tentando dizer",
                "type": "dimensions",
                "items": [
                    {"title": "Ciúme — o alarme da insegurança", "body": "<p>Ciúme fala de medo de abandono e de autoestima frágil. É um alarme — mas um alarme que apita para a sua insegurança, não necessariamente para uma ameaça real. Quem confia em si sente menos ciúme, não porque o outro é perfeito, mas porque não depende do outro para se sentir seguro.</p>"},
                    {"title": "Inveja — a comparação que adoece", "body": "<p>A inveja compara sua vida à do outro e sai perdendo. Ela diz mais sobre o que você sente que falta em você do que sobre o que o outro tem. Transformada em consciência, a inveja pode virar bússola: ela aponta o que você deseja para si.</p>"},
                    {"title": "A projeção que confunde tudo", "body": "<p>Muitas vezes o ciúme é inveja projetada: você se incomoda com a liberdade, o sucesso ou a felicidade do outro e transforma isso em suspeita de traição. Separar as duas é o primeiro passo para não descontar no outro o que é seu.</p>"},
                ],
            },
            {
                "heading": "Do alarme à consciência",
                "html": "<p>A meta não é nunca sentir ciúme ou inveja — é <strong>sentir e não obedecer</strong>. Emoção nomeada perde força; emoção agida vira estrago. Na próxima vez que o ciúme ou a inveja baterem, pare e pergunte: o que isso está me mostrando sobre o que eu preciso trabalhar em mim?</p>"
                "<p>Leia nosso artigo <a href=\"/artigos/ciume-o-que-ele-revela.html\">ciúme e o que ele revela</a> para ir mais fundo nessa emoção que, bem lida, vira autoconhecimento.</p>",
            },
        ],
        "faq": [
            {"q": "Ciúme é prova de amor?", "a": "<p>Não. Ciúme é prova de medo e insegurança. Amor é confiança, respeito e desejo de bem do outro. A crença de que &quot;quem não sente ciúme não ama&quot; romantiza o controle e é uma das portas de entrada para relações abusivas.</p>"},
            {"q": "Qual a diferença entre ciúme normal e ciúme doentio?", "a": "<p>O ciúme normal é passageiro e não controla suas ações. O doentio é intenso, frequente e te leva a fiscalizar, cobrar e controlar. Quando o ciúme vira comportamento de posse, é sinal de alerta. Veja <a href=\"/artigos/ciume-o-que-ele-revela.html\">ciúme e o que ele revela</a>.</p>"},
            {"q": "Como lidar com a inveja do sucesso do parceiro?", "a": "<p>Nomeie o sentimento para si sem culpa. Depois, transforme a comparação em pergunta: o que a conquista do outro desperta em mim que eu quero para a minha vida? A inveja consciente vira motor de crescimento; a inveja negada vira ressentimento.</p>"},
            {"q": "Essas emoções podem acabar com a relação?", "a": "<p>Podem, quando não são tratadas. Ciúme e inveja intensos corroem a confiança e a admiração — dois pilares do vínculo. Mas trabalhadas (com autoconhecimento e, se preciso, terapia), elas podem se tornar ponto de partida para uma relação mais consciente. Leia <a href=\"/artigos/dependencia-emocional-psicanalise.html\">dependência emocional</a>.</p>"},
        ],
    },

    "red-flags-precoces": {
        "dimensions": [
            {"label": "Poucas red flags (0–7)", "min": 0, "max": 7},
            {"label": "Algumas red flags (8–15)", "min": 8, "max": 15},
            {"label": "Muitas red flags (16–24)", "min": 16, "max": 24},
            {"label": "Red flags sérias (25+)", "min": 25, "max": 36},
        ],
        "sections": [
            {
                "heading": "Por que as red flags aparecem no início",
                "html": "<p>O início de uma relação é quando as red flags estão mais visíveis — e é justamente quando menos as enxergamos. O encantamento, a novidade e a esperança funcionam como um filtro cor-de-rosa que esconde sinais que, vistos de fora, seriam óbvios.</p>"
                "<p>Este teste te ajuda a olhar os primeiros encontros com honestidade. A premissa é simples: <strong>como alguém trata você no começo é a versão mais generosa</strong> do que virá depois. Se já há alertas agora, a tendência é que aumentem.</p>",
            },
            {
                "heading": "Red flags que o teste procura",
                "type": "dimensions",
                "items": [
                    {"title": "Love bombing", "body": "<p>Intensidade avassaladora desde o primeiro encontro: declarações, planos de futuro e promessas desproporcionais ao tempo de relação. A pressa de te conquistar é, muitas vezes, pressa de te controlar antes que você perceba quem ele(a) é.</p>"},
                    {"title": "Desrespeito disfarçado", "body": "<p>Piadas que machucam &quot;sem querer&quot;, comentários que diminuem, grosseria com garçons e funcionários. Como a pessoa trata quem não pode retribuir é um dos preditores mais confiáveis de como te tratará quando o encanto passar.</p>"},
                    {"title": "Ciúme e controle precoces", "body": "<p>Ciúme apresentado como cuidado no primeiro mês, querer saber onde você está o tempo todo, se incomodar com suas amizades. Controle no início vira prisão no futuro — ele não diminui, só muda de forma.</p>"},
                    {"title": "Gaslighting embrionário", "body": "<p>Fazer você duvidar da sua memória ou percepção (&quot;isso nunca aconteceu&quot;, &quot;você está exagerando&quot;) já nos primeiros meses. É o início de uma dinâmica que, sem intervenção, vira abuso psicológico.</p>"},
                ],
            },
            {
                "heading": "O que fazer quando você identifica red flags",
                "html": "<p>O objetivo deste teste não é te deixar paranoico(a), é te devolver a <strong>lucidez</strong> que o encantamento rouba. Uma red flag isolada pode ser um erro humano; um <strong>conjunto delas</strong> é um padrão — e padrão é o que prevê o futuro.</p>"
                "<p>Se o resultado apontou muitos alertas, converse com alguém de confiança e conte o que tem vivido — o isolamento é o terreno onde essas dinâmicas prosperam. Leia nosso artigo sobre <a href=\"/artigos/narcisismo.html\">narcisismo</a> e sobre <a href=\"/artigos/como-sair-de-relacao-com-narcisista.html\">sair de relação narcisista</a>. Em situações de violência, CVV 188 atende 24h.</p>",
            },
        ],
        "faq": [
            {"q": "Qual a red flag mais perigosa no início?", "a": "<p>O love bombing combinado com pressa de exclusividade. É o padrão que mais se confunde com paixão e o que mais rapidamente evolui para controle. Desconfie de quem te coloca num pedestal cedo demais.</p>"},
            {"q": "Uma red flag é motivo para terminar?", "a": "<p>Não necessariamente. Um deslize isolado pode ser conversado e corrigido. O que pede atenção é a repetição e a escalada. Converse, observe a reação: se a pessoa nega, minimiza ou te culpa, é uma segunda red flag.</p>"},
            {"q": "Por que eu ignoro red flags que todo mundo vê?", "a": "<p>Porque o encantamento desativa o julgamento crítico, e porque às vezes você repete padrões antigos de escolha. Reconhecer que ignorou não é vergonha — é o começo da mudança. Veja <a href=\"/artigos/repeticao-compulsiva-no-amor.html\">repetição compulsiva</a>.</p>"},
            {"q": "Consigo mudar um parceiro com red flags?", "a": "<p>Você não muda ninguém — e tentar é o caminho mais comum para se perder em relações abusivas. As pessoas mudam por escolha própria, geralmente com ajuda profissional. Seu trabalho é escolher com lucidez, não reformar o outro.</p>"},
        ],
    },
}


def enrich(meta):
    """Attach landing content + FAQ + engine dimensions to a quiz dict (in place)."""
    entry = LANDING.get(meta.get("slug"))
    if not entry:
        return meta
    if entry.get("sections"):
        meta["landing_sections"] = entry["sections"]
    if entry.get("faq"):
        meta["faq"] = entry["faq"]
    if entry.get("dimensions"):
        meta["quiz_data"]["dimensions"] = entry["dimensions"]
    return meta
