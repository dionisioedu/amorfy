#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Casos reais: 4 story pages (article template adapted) + generated via replacement."""
from article_template import render_article
import os

OUT = "/home/eduardo/projects/amorfy/casos"
os.makedirs(OUT, exist_ok=True)

def write_caso(meta):
    html = render_article(meta)
    html = html.replace('href="https://amorfy.com.br/artigos/' + meta["slug"], 'href="https://amorfy.com.br/casos/' + meta["slug"])
    html = html.replace('content="https://amorfy.com.br/artigos/' + meta["slug"], 'content="https://amorfy.com.br/casos/' + meta["slug"])
    html = html.replace('<li><a href="/artigos/">Artigos</a></li>\n      <li>' + meta["breadcrumb"], '<li><a href="/casos/">Casos Reais</a></li>\n      <li>' + meta["breadcrumb"])
    path = f"{OUT}/{meta['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK {path} ({len(html)} bytes)")

DISCLAIMER = '<p style="font-size:.85rem;color:var(--text-secondary)"><em>Hist&oacute;ria baseada em relatos reais. Nomes e detalhes foram alterados para preservar a privacidade dos envolvidos.</em></p>'

CASOS = [
{
"slug": "recomeco-apos-narcisista",
"title": "\"Levei 5 Anos Para Perceber\" — A História de Recomeço da Carla",
"desc": "Carla passou 5 anos num relacionamento com um narcisista sem perceber. Conheça a história real de como ela identificou o abuso e se reconstruiu.",
"breadcrumb": "Recomeço Após um Narcisista",
"tag": "Superação", "tag_color": "purple",
"date": "2025-07-12", "date_human": "12 Jul 2025", "read_min": "6",
"body": DISCLAIMER + """
<p>Carla, 34 anos, analista financeira, conheceu Rodrigo num aplicativo de namoro. "Ele parecia perfeito demais. E era exatamente isso: <em>parecia</em>."</p>

<h2>O conto de fadas</h2>
<p>Nos primeiros meses, Rodrigo era o homem mais atencioso do mundo. Mensagens de bom dia, jantares elaborados, declarações públicas. Em três meses, sugeriu morarem juntos. "Eu achava que tinha encontrado minha alma gêmea. Hoje sei que aquilo tem nome: <strong>love bombing</strong> — a fase de idealização que prende a vítima antes do abuso começar."</p>

<h2>A virada silenciosa</h2>
<p>Depois da mudança, começaram as críticas — sutis no início. A roupa que "não caía bem". As amigas que "não prestavam". O jeito de rir que era "escandaloso". "Cada crítica vinha embrulhada como 'cuidado' ou 'sinceridade'. Eu fui mudando aos poucos para agradá-lo. Quando percebi, tinha me afastado de todo mundo."</p>
<p>As brigas seguiam sempre o mesmo roteiro: qualquer reclamação dela terminava com ela pedindo desculpas. "Ele tinha um talento: distorcia tudo até eu duvidar da minha memória. Eu saía de cada discussão me sentindo louca. Anos depois descobri que isso tem nome: <strong>gaslighting</strong>."</p>

<h2>O estalo</h2>
<p>O ponto de virada veio de uma fonte inesperada: um teste online. "Uma amiga do trabalho me mandou um teste sobre relacionamento narcisista. Fiz rindo, achando exagero. Marquei quase todas as respostas mais graves. Fiquei olhando para aquele resultado e chorei por uma hora — porque no fundo eu j&aacute; sabia."</p>
<p>Ela começou terapia em segredo. "Minha psicóloga nunca disse 'termine'. Ela s&oacute; me ajudou a ver os padr&otilde;es. Em seis meses, eu tinha for&ccedil;a para sair."</p>

<h2>A reconstrução</h2>
<p>O término não foi limpo. Rodrigo alternou promessas de mudança, crises de vitimismo e ataques de raiva — o ciclo clássico tentando se reiniciar. "O contato zero foi a única coisa que funcionou. Bloqueei tudo. Doeu como abstinência — porque É uma abstinência."</p>
<p>Dois anos depois, Carla reconstruiu as amizades, voltou a dançar ("ele achava ridículo") e está num relacionamento novo. "O mais estranho no começo foi a paz. Eu esperava a bomba explodir a qualquer momento, porque era o que eu conhecia. Levei tempo para aceitar que amor podia ser... tranquilo."</p>

<div class="highlight-box">
  <h3>💡 O que a história da Carla ensina</h3>
  <p>1) Love bombing intenso e pressa por compromisso são sinais de alerta, não de paixão. 2) O isolamento acontece aos poucos, disfarçado de cuidado. 3) Se você sai de toda discussão se sentindo louco(a), preste atenção. 4) Contato zero é a estratégia mais eficaz pós-término. 5) Terapia não é luxo — é ferramenta de sobrevivência.</p>
</div>

<p>Se a história da Carla parece familiar, leia nosso <a href="/artigos/narcisismo.html">guia completo sobre narcisismo</a> ou faça o <a href="/testes/narcisista.html">teste de sinais de relacionamento narcisista</a>.</p>"""
},
{
"slug": "casamento-reconstruido",
"title": "\"Quase Assinamos o Divórcio\" — Como Marcos e Ana Reconstruíram o Casamento",
"desc": "Depois de 12 anos casados e uma crise que quase terminou em divórcio, Marcos e Ana reconstruíram a relação. A história real de um recomeço a dois.",
"breadcrumb": "Casamento Reconstruído",
"tag": "Sucesso", "tag_color": "rose",
"date": "2025-07-06", "date_human": "06 Jul 2025", "read_min": "6",
"body": DISCLAIMER + """
<p>Marcos, 41, e Ana, 39, estavam casados havia 12 anos quando sentaram na mesa da cozinha para conversar sobre divórcio. "Não tinha traição, não tinha briga feia", conta Ana. "Tinha algo pior: indiferença. A gente tinha virado sócio de uma empresa chamada família."</p>

<h2>A erosão silenciosa</h2>
<p>A crise não começou com um evento — foi acumulada. Dois filhos, duas carreiras, uma mudança de cidade. O tempo a dois foi a primeira variável cortada da equação. "A gente se falava só de logística: quem busca as crianças, quem paga o boleto", lembra Marcos. "Eu não lembrava a última conversa que não fosse sobre tarefas."</p>
<p>A intimidade física foi atrás. Meses sem se tocar. "E o pior: sem sentir falta", admite Ana. "Isso me assustou mais que qualquer briga. Briga pelo menos é energia. Ali só tinha silêncio."</p>

<h2>A conversa da mesa da cozinha</h2>
<p>Foi Marcos quem puxou o assunto do divórcio. "Falei com calma, sem raiva. E foi a primeira conversa honesta que a gente tinha em anos. A Ana chorou e disse uma frase que mudou tudo: <em>'eu não quero me separar de você — eu quero me separar dessa vida que a gente montou'</em>."</p>
<p>Decidiram tentar uma última cartada: seis meses de terapia de casal antes de qualquer papel assinado.</p>

<h2>O trabalho de reconstrução</h2>
<p>"A terapeuta foi direta: vocês não têm um problema de amor, têm um problema de <strong>prioridade</strong>. O casal virou a última prioridade da casa — atrás dos filhos, do trabalho, da família estendida e do celular."</p>
<p>As mudanças foram concretas e quase burocráticas no início:</p>
<ul>
  <li><strong>Sexta à noite protegida:</strong> programa a dois inegociável, sem filhos, sem celular</li>
  <li><strong>Check-in diário de 15 minutos:</strong> conversa sobre sentimentos — proibido falar de logística</li>
  <li><strong>Gratidão expressa:</strong> um agradecimento específico por dia, em voz alta</li>
  <li><strong>Toque sem finalidade:</strong> reaprender carinho físico sem pressão</li>
</ul>
<p>"No começo parecia artificial, forçado", ri Marcos. "A terapeuta avisou: vai parecer mesmo. Intimidade é hábito — e hábito se reconstrói com repetição, não com espontaneidade."</p>

<h2>Dois anos depois</h2>
<p>O casal não só permaneceu junto como descreve a relação atual como melhor que a dos primeiros anos. "A paixão do início era ignorância: a gente amava quem imaginava que o outro era. Hoje eu amo quem o Marcos é de verdade — com tudo que me irrita incluído", diz Ana.</p>

<div class="highlight-box">
  <h3>💡 O que a história deles ensina</h3>
  <p>1) Indiferença mata mais casamentos que briga. 2) O casal precisa ser prioridade estruturada — não sobra de tempo. 3) Reconexão parece artificial no início, e tudo bem. 4) Terapia de casal funciona melhor ANTES do ponto de não retorno. 5) O amor maduro é escolha renovada, não sentimento espontâneo.</p>
</div>

<p>Quer fortalecer sua relação? Leia <a href="/artigos/fases-relacionamento.html">as fases de um relacionamento</a> e faça o <a href="/testes/compatibilidade.html">teste de compatibilidade</a>.</p>"""
},
{
"slug": "dependencia-emocional",
"title": "\"Eu Não Sabia Ficar Só\" — Como Júlia Quebrou o Ciclo da Dependência Emocional",
"desc": "Júlia emendava um relacionamento no outro e aceitava migalhas por medo de ficar só. A história real de como ela quebrou o ciclo da dependência emocional.",
"breadcrumb": "Vencendo a Dependência Emocional",
"tag": "Superação", "tag_color": "pink",
"date": "2025-06-30", "date_human": "30 Jun 2025", "read_min": "5",
"body": DISCLAIMER + """
<p>Júlia, 29, designer, nunca tinha ficado solteira mais de dois meses desde os 16 anos. "Eu emendava um relacionamento no outro. Não por amor — por pânico de ficar sozinha. Qualquer pessoa que me desse atenção virava 'o amor da minha vida' em duas semanas."</p>

<h2>O padrão invisível</h2>
<p>Os relacionamentos de Júlia seguiam um roteiro: início intenso, entrega total e imediata, depois um parceiro cada vez mais distante e ela cada vez mais desesperada. "Eu me moldava para cada namorado. Mudava de gosto musical, de estilo, até de opinião política. Camaleoa emocional."</p>
<p>"Meu termômetro de valor próprio era ter alguém. Semana boa era semana com mensagens respondidas rápido. Eu aceitava migalhas e chamava de banquete."</p>

<h2>O fundo do poço produtivo</h2>
<p>O estalo veio após o quarto término em três anos — dessa vez, de um relacionamento que ela mesma reconhecia como ruim. "Chorei uma semana por um cara que me tratava mal. Na segunda semana, me peguei baixando aplicativo de novo. Parei com o dedo em cima da tela e pensei: <em>eu não quero um homem, eu quero um anestésico</em>."</p>
<p>Ela apagou o app e fez um combinado consigo mesma: <strong>um ano sem relacionamentos</strong>. "Todo mundo achou drástico. Foi a decisão mais importante da minha vida."</p>

<h2>O ano do deserto (e da colheita)</h2>
<p>Os primeiros três meses foram fisicamente desconfortáveis. "Fins de semana eram um buraco. Eu não sabia o que fazer comigo mesma — literalmente. Descobri que nunca tinha aprendido a me fazer companhia."</p>
<p>Com terapia e tempo, o desconforto virou descoberta:</p>
<ul>
  <li>Voltou a desenhar por prazer — hobby abandonado desde a adolescência</li>
  <li>Viajou sozinha pela primeira vez na vida</li>
  <li>Reconstruiu amizades que os relacionamentos tinham engolido</li>
  <li>Na terapia, mapeou a raiz: um pai emocionalmente ausente e a crença infantil de que amor precisa ser conquistado com desempenho</li>
</ul>

<h2>O relacionamento diferente</h2>
<p>Quatorze meses depois, Júlia conheceu alguém. "A diferença foi bizarra. Eu não PRECISAVA dele — eu gostava dele. São coisas opostas. Quando ele demorava a responder, eu continuava vivendo em vez de encarar o celular. Quando algo me incomodava, eu falava, porque não tinha mais pânico de perder."</p>
<p>"Descobri o segredo mais contraintuitivo do amor: <strong>você só ama bem quando não precisa desesperadamente do outro</strong>. Antes, eu não tinha relacionamentos — tinha reféns da minha carência."</p>

<div class="highlight-box">
  <h3>💡 O que a história da Júlia ensina</h3>
  <p>1) Emendar relacionamentos impede a cura e repete o padrão. 2) Pânico de solidão leva a escolhas ruins e a aceitar migalhas. 3) Ficar bem sozinho é pré-requisito para ficar bem acompanhado. 4) A raiz da dependência geralmente está na infância — terapia acelera o processo. 5) Amor saudável nasce de querer, não de precisar.</p>
</div>

<p>Reconheceu algum padrão? Leia sobre <a href="/artigos/autoconhecimento.html">autoconhecimento</a> e <a href="/artigos/traumas.html">como traumas moldam relacionamentos</a>.</p>"""
},
{
"slug": "amor-depois-dos-50",
"title": "\"Achei Que Meu Tempo Tinha Passado\" — O Recomeço de Fernando aos 56",
"desc": "Viúvo aos 52, Fernando achou que o amor tinha ficado no passado. A história real de um recomeço afetivo na maturidade — com medos, filhos adultos e esperança.",
"breadcrumb": "Amor Depois dos 50",
"tag": "Sucesso", "tag_color": "gold",
"date": "2025-06-22", "date_human": "22 Jun 2025", "read_min": "5",
"body": DISCLAIMER + """
<p>Fernando, 56, engenheiro aposentado, perdeu a esposa para um câncer após 27 anos de casamento. "Nos primeiros dois anos, a pergunta nem existia. Depois ela apareceu tímida: <em>será que acabou para mim?</em> Eu tinha certeza que sim. Amor era coisa do passado, capítulo encerrado."</p>

<h2>O luto e a culpa</h2>
<p>"Ninguém fala da culpa. Quando percebi que estava reparando em outra mulher — a professora do curso de fotografia — me senti traindo a Regina. Fiquei semanas sem voltar ao curso."</p>
<p>Foi o filho mais velho quem o confrontou: "Pai, a mãe te fez prometer que você ia viver, não que ia virar monumento. Estatua ninguém abraça." Fernando conta que chorou "como não chorava desde o enterro" — e voltou para o curso.</p>

<h2>Namorar aos 50+ é outro esporte</h2>
<p>A aproximação com Helena, 53, divorciada, foi lenta — meses de conversas depois da aula, um café que virou hábito. "Aos 20, você se apaixona por potencial. Aos 50, as pessoas já são quem são. Isso muda tudo — para melhor. Não tem jogo, não tem 'quem responde primeiro'. Tem duas pessoas que sabem que tempo é o único bem não renovável."</p>
<p>Mas houve desafios que a juventude não conhece:</p>
<ul>
  <li><strong>Filhos adultos com opiniões:</strong> a filha de Fernando demorou a aceitar. "Ela via a Helena como substituta da mãe. Precisei deixar claro: ninguém substitui ninguém. O coração não é uma vaga de estacionamento"</li>
  <li><strong>Patrimônios e histórias separadas:</strong> decidiram morar juntos mas manter finanças independentes — "conversa desconfortável e absolutamente necessária"</li>
  <li><strong>Comparação com o passado:</strong> "No início eu comparava tudo. A terapeuta me ensinou: comparar é normal, morar na comparação é que adoece"</li>
</ul>

<h2>O amor da maturidade</h2>
<p>Três anos depois, Fernando descreve a relação com uma serenidade que impressiona. "Com a Regina eu construí uma vida: filhos, casa, história. Com a Helena eu não construo nada — eu <em>vivo</em>. A gente viaja, cozinha, discute livro, dança mal. É um amor sem projeto, e eu descobri que isso não é falta — é liberdade."</p>
<p>"Se eu pudesse falar com o Fernando de 4 anos atrás, diria: seu tempo não passou. Coração não aposenta."</p>

<div class="highlight-box">
  <h3>💡 O que a história do Fernando ensina</h3>
  <p>1) Recomeçar não é trair quem partiu — é honrar a vida que continua. 2) A culpa faz parte do processo; não decida nada por ela. 3) Amor maduro tem vantagens: menos jogo, mais verdade. 4) Filhos adultos precisam de conversa clara, não de pedido de permissão. 5) Nunca é tarde — coração não tem prazo de validade.</p>
</div>

<p>A vida afetiva se transforma em cada fase. Leia também: <a href="/artigos/fases-relacionamento.html">as fases de um relacionamento</a> e <a href="/artigos/mitos-amor.html">mitos e verdades sobre o amor</a>.</p>"""
},
]

if __name__ == "__main__":
    for c in CASOS:
        write_caso(c)
