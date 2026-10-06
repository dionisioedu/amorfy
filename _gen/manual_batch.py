#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Artigos mantidos manualmente, migrados para o pipeline: borderline, narcisismo, temperamentos."""
from article_template import write_article

ARTICLES = [
{
"slug": "borderline",
"title": "Transtorno de Personalidade Borderline e Relacionamentos — Um Guia com Empatia",
"desc": "Entenda o Transtorno de Personalidade Borderline (TPB), como ele afeta os relacionamentos amorosos e quais os caminhos para o tratamento e a estabilidade emocional.",
"breadcrumb": "Borderline e Relacionamentos",
"tag": "Saúde Mental", "tag_color": "pink",
"date": "2026-09-11", "date_human": "11 Set 2026", "read_min": "10",
"body": """<p>O Transtorno de Personalidade Borderline (TPB) é um dos transtornos mais estigmatizados e incompreendidos. Estima-se que afete <strong>1,6% da população geral</strong> e até 20% dos pacientes psiquiátricos internados. Nos relacionamentos amorosos, seus efeitos podem ser intensos — mas com tratamento adequado, <strong>a recuperação e a estabilidade são totalmente possíveis</strong>.</p>

<h2>O que é o TPB?</h2>

<p>O TPB é um transtorno caracterizado por <strong>instabilidade emocional intensa, relacionamentos turbulentos, medo de abandono e senso de identidade difuso</strong>. Não é um defeito de caráter — é uma condição de saúde mental com bases neurobiológicas e ambientais, geralmente ligada a traumas na infância e/ou predisposição genética.</p>

<h3>Critérios diagnósticos (DSM-5):</h3>
<ul>
  <li>Esforços desesperados para evitar abandono real ou imaginado</li>
  <li>Relacionamentos instáveis e intensos (idealização seguida de desvalorização)</li>
  <li>Perturbação da identidade (autoimagem instável)</li>
  <li>Impulsividade em áreas potencialmente autodestrutivas</li>
  <li>Comportamentos ou ameaças suicidas recorrentes</li>
  <li>Instabilidade afetiva (mudanças de humor intensas em horas)</li>
  <li>Sensação crônica de vazio</li>
  <li>Raiva inapropriada e intensa</li>
  <li>Ideias paranoides transitórias relacionadas ao estresse</li>
</ul>

<h2>Como o TPB afeta os relacionamentos</h2>

<p>Pessoas com TPB amam <strong>com uma intensidade que a maioria das pessoas nunca experimentará</strong>. Mas essa mesma intensidade pode gerar turbulências.</p>

<h3>O ciclo do relacionamento borderline:</h3>

<p><strong>1. Idealização:</strong> o parceiro é visto como perfeito, a salvação, a única pessoa que entende. Há uma entrega total e avassaladora.</p>

<p><strong>2. Medo do abandono:</strong> qualquer sinal de distanciamento — real ou percebido — dispara pânico. Uma mensagem não respondida pode ser interpretada como rejeição total.</p>

<p><strong>3. Desvalorização:</strong> para se proteger da dor do possível abandono, a pessoa desvaloriza o parceiro. "Ele(a) nunca me amou de verdade."</p>

<p><strong>4. Crise:</strong> comportamentos impulsivos, ameaças, tentativas de manipulação emocional (não por maldade, mas por desespero).</p>

<p><strong>5. Reconciliação:</strong> pedidos intensos de desculpas, promessas de mudança, nova idealização — e o ciclo recomeça.</p>

<div class="highlight-box">
  <h3>💡 Importante: TPB ≠ Pessoa Tóxica</h3>
  <p>Pessoas com TPB não são "tóxicas" ou "manipuladoras por maldade". Elas estão sofrendo. O comportamento disfuncional é um <strong>mecanismo de defesa</strong> contra uma dor emocional insuportável. Com tratamento, esses padrões podem ser transformados.</p>
</div>

<h2>Tratamentos que Funcionam</h2>

<h3>Terapia Comportamental Dialética (DBT)</h3>
<p>Criada por Marsha Linehan (que também tem TPB), a DBT é o padrão-ouro. Ensina quatro habilidades: <strong>mindfulness, tolerância ao estresse, regulação emocional e efetividade interpessoal</strong>. Reduz significativamente comportamentos autodestrutivos e ideação suicida.</p>

<h3>Terapia dos Esquemas</h3>
<p>Trabalha os "esquemas" — crenças profundas formadas na infância que distorcem a percepção dos relacionamentos. Ajuda a pessoa a desenvolver um "adulto saudável" interno.</p>

<h3>Mentalização (MBT)</h3>
<p>Ensina a capacidade de entender os próprios estados mentais e os dos outros — habilidade que costuma ser prejudicada no TPB.</p>

<h3>Medicação</h3>
<p>Não há remédio específico para TPB, mas medicamentos podem ajudar com sintomas associados como depressão, ansiedade e instabilidade de humor. Sempre sob orientação psiquiátrica.</p>

<h2>Para Quem Ama Alguém com TPB</h2>

<p>Amar alguém com TPB pode ser exaustivo, confuso e doloroso. Mas também pode ser profundamente transformador. Algumas orientações:</p>

<ul>
  <li><strong>Estabeleça limites claros e consistentes:</strong> com amor, mas com firmeza. A consistência é terapêutica.</li>
  <li><strong>Não leve ataques para o lado pessoal:</strong> quando a pessoa com TPB ataca, ela está expressando sua própria dor interna.</li>
  <li><strong>Valide as emoções sem validar comportamentos destrutivos:</strong> "Entendo que você está sofrendo, mas não aceito que grite comigo."</li>
  <li><strong>Incentive o tratamento:</strong> a DBT salva vidas. Ofereça-se para acompanhar nas primeiras sessões.</li>
  <li><strong>Cuide de você também:</strong> considere terapia para si mesmo. O desgaste emocional é real.</li>
</ul>

<p>Preparamos um guia completo só sobre isso: <a href="/artigos/relacionamento-borderline.html">Como Manter um Relacionamento Saudável com uma Pessoa Borderline</a> — validação, limites, protocolo de crise e autocuidado.</p>

<div class="highlight-box">
  <h3>🧠 Testes relacionados</h3>
  <p>Quer refletir sobre sinais concretos? Faça o <a href="/testes/borderline.html">teste de autoavaliação de traços de borderline</a> ou o <a href="/testes/parceiro-borderline.html">teste de sinais no parceiro(a)</a>. Ambos são informativos — não substituem avaliação profissional.</p>
</div>

<h2>Prognóstico e Esperança</h2>

<p>Estudos longitudinais mostram que <strong>a maioria das pessoas com TPB apresenta remissão dos sintomas</strong> ao longo do tempo, especialmente com tratamento adequado. Após 10 anos de tratamento, até 85% dos pacientes não preenchem mais os critérios diagnósticos.</p>

<p>O TPB não é uma sentença perpétua. Com o suporte certo, a pessoa pode construir <strong>relacionamentos estáveis, saudáveis e profundamente significativos</strong>.</p>

<blockquote>Ter borderline não é escolha. Mas buscar tratamento, aprender a se regular e construir relações saudáveis — isso, sim, é uma escolha corajosa e possível.</blockquote>"""
},
{
"slug": "narcisismo",
"title": "Narcisismo nos Relacionamentos — Como Identificar, Sobreviver e se Curar",
"desc": "Guia completo sobre narcisismo nos relacionamentos: sinais de alerta, fases do abuso narcisista, perfil do narcisista e caminhos para a recuperação emocional.",
"breadcrumb": "Narcisismo nos Relacionamentos",
"tag": "Alerta", "tag_color": "purple",
"date": "2026-09-10", "date_human": "10 Set 2026", "read_min": "12",
"body": """<p>O narcisismo nos relacionamentos é um dos temas mais buscados atualmente — e não é por acaso. Estima-se que entre <strong>1% e 6% da população</strong> tenha Transtorno de Personalidade Narcisista (TPN), e muitas outras pessoas apresentam traços narcisistas significativos sem o diagnóstico completo.</p>

<p>Este artigo vai ajudar você a entender, identificar e, principalmente, <strong>se proteger e se curar</strong> de relacionamentos com pessoas narcisistas.</p>

<h2>O que é o Transtorno de Personalidade Narcisista?</h2>

<p>O TPN é um transtorno de personalidade caracterizado por um <strong>padrão persistente de grandiosidade, necessidade de admiração e falta de empatia</strong>. Diferente do que muitos pensam, o narcisista não se ama — ele depende da validação externa para sustentar uma autoestima frágil e inflada artificialmente.</p>

<h3>Características principais (DSM-5):</h3>
<ul>
  <li>Sensação grandiosa de autoimportância</li>
  <li>Preocupação com fantasias de sucesso, poder ou beleza ilimitados</li>
  <li>Crença de ser "especial" e único</li>
  <li>Necessidade excessiva de admiração</li>
  <li>Senso de merecimento de tratamento especial</li>
  <li>Exploração interpessoal (usa os outros para seus fins)</li>
  <li>Falta de empatia genuína</li>
  <li>Inveja frequente ou crença de que os outros o invejam</li>
  <li>Comportamentos arrogantes e prepotentes</li>
</ul>

<div class="highlight-box">
  <h3>⚠️ Importante</h3>
  <p>Apenas um profissional de saúde mental pode diagnosticar. Este artigo é informativo. Se você está em um relacionamento abusivo, busque ajuda profissional e uma rede de apoio segura.</p>
</div>

<h2>As 4 Fases do Relacionamento Narcisista</h2>

<p>Relacionamentos com narcisistas seguem um padrão previsível e devastador. Reconhecer essas fases é o primeiro passo para se libertar.</p>

<h3>Fase 1: Idealização (Love Bombing)</h3>
<p>No início, você é a pessoa mais incrível do mundo. O narcisista te cobre de atenção, presentes, elogios e promessas de um futuro perfeito. É intenso, rápido e intoxicante. Essa fase cria um <strong>vício emocional</strong> — você se acostuma com a dose altíssima de dopamina.</p>

<h3>Fase 2: Desvalorização</h3>
<p>Gradualmente, os elogios se transformam em críticas. O que antes era "adorável" vira "irritante". O narcisista alterna entre afeto e frieza, criando <strong>confusão emocional</strong>. Você começa a duvidar de si mesmo, a se sentir inadequado, a andar em ovos.</p>

<h3>Fase 3: Descarte</h3>
<p>O narcisista termina a relação de forma abrupta e cruel — muitas vezes por mensagem, com outra pessoa já engatilhada, ou simplesmente desaparecendo. O descarte é calculado para <strong>machucar profundamente</strong> e reafirmar o poder dele sobre você.</p>

<h3>Fase 4: Hoovering (Aspiração)</h3>
<p>Depois do descarte, o narcisista volta. Manda mensagem, pede desculpas, promete mudanças, declara amor eterno. O objetivo é <strong>sugar você de volta</strong> para o ciclo — e o ciclo recomeça com nova idealização, seguida de desvalorização e descarte.</p>

<h2>Sinais de Alerta (Red Flags)</h2>

<ul>
  <li><strong>Relacionamento rápido demais:</strong> declarações de amor em semanas, planos de casamento em meses.</li>
  <li><strong>Falta de amigos de longa data:</strong> o narcisista raramente mantém amizades duradouras.</li>
  <li><strong>Histórico de ex "loucos":</strong> todos os ex-parceiros são descritos como problemáticos — menos ele.</li>
  <li><strong>Nunca assume culpa:</strong> desculpas genéricas ("sinto muito que você se sinta assim") em vez de responsabilidade real.</li>
  <li><strong>Invalidação emocional:</strong> seus sentimentos são sempre "exagero" ou "drama".</li>
  <li><strong>Gaslighting:</strong> distorce fatos para fazer você duvidar da própria memória e sanidade.</li>
  <li><strong>Isolamento:</strong> sutilmente afasta você de amigos e família.</li>
</ul>

<h2>Tipos de Narcisismo</h2>

<h3>Narcisismo Grandioso</h3>
<p>O estereótipo clássico: extrovertido, arrogante, dominador. Busca os holofotes e se irrita quando não é o centro das atenções. É o mais fácil de identificar.</p>

<h3>Narcisismo Vulnerável (ou Encoberto)</h3>
<p>Mais difícil de detectar. Aparenta ser sensível, introvertido e até inseguro. Na verdade, usa a vitimização para manipular. Frases como "ninguém me entende" ou "todo mundo me abandona" são frequentes. É o <strong>lobo em pele de cordeiro</strong>.</p>

<h3>Narcisismo Maligno</h3>
<p>Combina traços narcisistas com antissociais e paranoicos. É o tipo mais perigoso — sente prazer em manipular e destruir. Felizmente, é raro.</p>

<h2>Como se Curar Após um Relacionamento Narcisista</h2>

<ol>
  <li><strong>Contato Zero:</strong> bloqueie em todas as redes, mensagens e telefone. É essencial para quebrar o ciclo químico do vício emocional.</li>
  <li><strong>Terapia especializada:</strong> profissionais que entendem de trauma narcisista são fundamentais. EMDR e TCC podem ajudar muito.</li>
  <li><strong>Reconstrua sua identidade:</strong> o narcisista apagou quem você era. Redescubra seus gostos, hobbies e valores.</li>
  <li><strong>Grupos de apoio:</strong> conversar com pessoas que passaram pelo mesmo é extremamente validante.</li>
  <li><strong>Entenda o trauma:</strong> o abuso narcisista causa sintomas similares ao TEPT. Não se culpe — você foi vítima de manipulação sistemática.</li>
  <li><strong>Fortaleça seus limites:</strong> aprenda a dizer não e a reconhecer sinais de alerta em futuras relações.</li>
</ol>

<p>Se você suspeita que está em um relacionamento narcisista, <a href="/testes/narcisista.html">faça nosso teste gratuito</a> para avaliar os sinais. E para olhar o próprio padrão, responda ao <a href="/testes/meus-tracos-narcisistas.html">teste de traços narcisistas em você</a>.</p>

<blockquote>Você não está sozinho(a). O que aconteceu não é culpa sua. A recuperação é possível — e você merece um amor saudável e genuíno.</blockquote>"""
},
{
"slug": "temperamentos",
"title": "Os 4 Temperamentos e Como Cada Um Ama — Guia Completo",
"desc": "Colérico, melancólico, fleumático e sanguíneo. Descubra como seu temperamento influencia seus relacionamentos amorosos e aprenda a lidar com cada perfil.",
"breadcrumb": "Os 4 Temperamentos e o Amor",
"tag": "Psicologia", "tag_color": "rose",
"date": "2026-07-21", "date_human": "21 Jul 2026", "read_min": "8",
"body": """<p>Você já se perguntou por que algumas pessoas são intensas e passionais, enquanto outras são calmas e ponderadas no amor? A resposta pode estar nos quatro temperamentos — uma das teorias mais antigas da psicologia da personalidade, que remonta a Hipócrates e foi refinada ao longo dos séculos.</p>

<p>Entender os temperamentos não é sobre rotular pessoas, mas sobre <strong>compreender padrões de comportamento</strong> que influenciam profundamente como amamos, nos comunicamos e lidamos com conflitos nos relacionamentos.</p>

<h2>O que são os temperamentos?</h2>

<p>Os quatro temperamentos são perfis de personalidade baseados em traços inatos — tendências naturais que já nascem conosco. Diferente do caráter (que se forma com experiências), o temperamento é a nossa "configuração de fábrica".</p>

<p>Os quatro tipos são: <strong>Colérico</strong> (fogo), <strong>Sanguíneo</strong> (ar), <strong>Fleumático</strong> (água) e <strong>Melancólico</strong> (terra). A maioria das pessoas é uma combinação de dois temperamentos, com um dominante.</p>

<h2>🔥 Temperamento Colérico no Amor</h2>

<p>O colérico é o líder nato — determinado, intenso e orientado a resultados. No amor, é a pessoa que <strong>toma a iniciativa, protege e assume o controle</strong>.</p>

<h3>Como o colérico ama:</h3>
<ul>
  <li><strong>Intensidade total:</strong> quando ama, ama com tudo. Não existe meio-termo.</li>
  <li><strong>Proteção e provisão:</strong> demonstra amor cuidando e resolvendo problemas práticos.</li>
  <li><strong>Precisa de autonomia:</strong> não suporta ser controlado ou sentir-se dependente.</li>
  <li><strong>Direto e franco:</strong> pode soar rude sem intenção — diz o que pensa sem rodeios.</li>
</ul>

<h3>Desafios nos relacionamentos:</h3>
<ul>
  <li>Tendência a dominar e não ouvir o parceiro</li>
  <li>Impaciência com a lentidão ou indecisão alheia</li>
  <li>Dificuldade em demonstrar vulnerabilidade</li>
  <li>Pode transformar discussões em competições</li>
</ul>

<h3>Dicas para amar um colérico:</h3>
<ul>
  <li>Seja direto na comunicação — sem indiretas</li>
  <li>Reconheça suas conquistas e capacidades</li>
  <li>Dê espaço para autonomia e decisões</li>
  <li>Não tente controlá-lo; convide, não imponha</li>
</ul>

<div class="highlight-box">
  <h3>💡 Compatibilidade</h3>
  <p>Coléricos tendem a se dar bem com fleumáticos (que trazem calma) e outros coléricos (parceria de alta energia). Com melancólicos, pode haver atrito entre ação e reflexão.</p>
</div>

<h2>🌿 Temperamento Fleumático no Amor</h2>

<p>O fleumático é o pacificador — calmo, estável e avesso a conflitos. É o parceiro que <strong>traz equilíbrio e constância</strong> para qualquer relação.</p>

<h3>Como o fleumático ama:</h3>
<ul>
  <li><strong>Amor tranquilo e constante:</strong> não faz grandes declarações, mas está sempre presente.</li>
  <li><strong>Lealdade inabalável:</strong> quando se compromete, é para valer.</li>
  <li><strong>Ouvinte excepcional:</strong> sabe escutar sem julgar ou interromper.</li>
  <li><strong>Evita dramas:</strong> prefere paz a ter razão — às vezes até demais.</li>
</ul>

<h3>Desafios nos relacionamentos:</h3>
<ul>
  <li>Pode ser passivo demais, evitando conversas difíceis</li>
  <li>Tendência a procrastinar decisões importantes</li>
  <li>Pode parecer desinteressado pela falta de iniciativa</li>
  <li>Guarda ressentimentos em silêncio em vez de confrontar</li>
</ul>

<h3>Dicas para amar um fleumático:</h3>
<ul>
  <li>Não o pressione — dê tempo para processar</li>
  <li>Crie um ambiente seguro para ele se expressar</li>
  <li>Valorize sua presença constante, mesmo que silenciosa</li>
  <li>Inicie atividades e convide-o gentilmente</li>
</ul>

<h2>💨 Temperamento Sanguíneo no Amor</h2>

<p>O sanguíneo é a alma da festa — extrovertido, entusiasmado e cheio de energia. No amor, é o parceiro que <strong>traz alegria, espontaneidade e romance</strong>.</p>

<h3>Como o sanguíneo ama:</h3>
<ul>
  <li><strong>Amor expressivo e demonstrativo:</strong> surpresas, declarações públicas, gestos românticos.</li>
  <li><strong>Otimismo contagiante:</strong> vê o lado bom mesmo nas crises.</li>
  <li><strong>Sociabilidade:</strong> adora compartilhar a vida social com o parceiro.</li>
  <li><strong>Vive o presente:</strong> intensamente focado no aqui e agora.</li>
</ul>

<h3>Desafios nos relacionamentos:</h3>
<ul>
  <li>Pode ser impulsivo em decisões que afetam o casal</li>
  <li>Dificuldade em manter compromissos de longo prazo</li>
  <li>Tédio com rotina — precisa de novidade constante</li>
  <li>Pode falar mais do que ouve</li>
</ul>

<h3>Dicas para amar um sanguíneo:</h3>
<ul>
  <li>Surpreenda com novidades e aventuras</li>
  <li>Celebre suas ideias (mesmo as malucas)</li>
  <li>Ajude a criar estrutura sem sufocar</li>
  <li>Seja seu fã número um — eles precisam de aplausos</li>
</ul>

<h2>🌙 Temperamento Melancólico no Amor</h2>

<p>O melancólico é o profundo — sensível, analítico e perfeccionista. No amor, é o parceiro que <strong>ama com profundidade, lealdade e entrega total</strong>.</p>

<h3>Como o melancólico ama:</h3>
<ul>
  <li><strong>Amor profundo e significativo:</strong> não se contenta com superficialidades.</li>
  <li><strong>Extremamente leal:</strong> quando ama, é para a vida toda.</li>
  <li><strong>Detalhista e atencioso:</strong> lembra de cada detalhe importante.</li>
  <li><strong>Conexão emocional intensa:</strong> busca fusão de almas, não só corpos.</li>
</ul>

<h3>Desafios nos relacionamentos:</h3>
<ul>
  <li>Tendência ao perfeccionismo — espera muito de si e do outro</li>
  <li>Pode ser crítico demais com o parceiro</li>
  <li>Ruminação de mágoas e dificuldade em perdoar</li>
  <li>Oscilações de humor que confundem o parceiro</li>
</ul>

<h3>Dicas para amar um melancólico:</h3>
<ul>
  <li>Ofereça segurança e consistência emocional</li>
  <li>Ouça profundamente — eles precisam ser compreendidos</li>
  <li>Valorize seus sentimentos, mesmo que pareçam exagerados</li>
  <li>Ajude a equilibrar profundidade com leveza</li>
</ul>

<h2>Encontrando o equilíbrio</h2>

<p>Nenhum temperamento é "melhor" que outro. Cada um traz dons e desafios únicos. O segredo para relacionamentos saudáveis não é encontrar alguém com o temperamento "certo", mas sim:</p>

<ol>
  <li><strong>Conhecer seu próprio temperamento</strong> e como ele afeta suas reações.</li>
  <li><strong>Reconhecer o temperamento do parceiro</strong> e adaptar sua comunicação.</li>
  <li><strong>Valorizar as diferenças</strong> em vez de tentar mudar o outro.</li>
  <li><strong>Desenvolver as virtudes</strong> que equilibram os excessos do seu temperamento.</li>
</ol>

<p>Quer descobrir seu temperamento e como ele afeta sua vida amorosa? <a href="/testes/personalidade-amorosa.html">Faça nosso teste de personalidade amorosa</a> e receba insights personalizados.</p>"""
},
]

if __name__ == "__main__":
    for a in ARTICLES:
        write_article(a)

