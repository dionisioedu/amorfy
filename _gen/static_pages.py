#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static pages: sobre.html (com contato), privacidade.html, termos.html."""

from pathlib import Path

HEAD = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="google-adsense-account" content="ca-pub-6858130394830057">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://amorfy.com.br/{slug}.html">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="https://amorfy.com.br/{slug}.html">
  <meta property="og:type" content="website">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:type" content="image/png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Amorfy — testes, artigos e histórias reais sobre relacionamentos">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:image" content="{og_image}">
  <meta name="twitter:image:alt" content="Amorfy">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="stylesheet" href="/css/style.css">
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6858130394830057" crossorigin="anonymous"></script>
</head>
<body>

<header class="site-header">
  <div class="header-inner">
    <a href="/" class="logo"><img src="/favicon.svg" alt="" width="38" height="38">Amorfy</a>
    <button class="nav-toggle" aria-label="Abrir menu" aria-expanded="false" aria-controls="site-navigation">&#9776;</button>
    <nav><ul class="nav-links" id="site-navigation">
      <li><a href="/">In&iacute;cio</a></li>
      <li><a href="/testes/">Testes</a></li>
      <li><a href="/artigos/">Artigos</a></li>
      <li><a href="/casos/">Casos Reais</a></li>
      <li><a href="/sobre.html">Sobre</a></li>
      <li><a href="/perguntas-frequentes.html">FAQ</a></li>
    </ul></nav>
  </div>
</header>

<main>
  <article>
    <header class="article-header">
      <h1>{h1}</h1>
    </header>
    <div class="article-body">
{body}
    </div>
  </article>
</main>
"""

FOOT = """
<footer class="site-footer">
  <div class="footer-inner">
    <div class="footer-col"><h4>Amorfy &#128150;</h4><p style="color:var(--text-secondary);font-size:.9rem">Seu guia completo sobre relacionamentos, autoconhecimento e amor pr&oacute;prio.</p></div>
    <div class="footer-col"><h4>Navegue</h4><ul><li><a href="/testes/">Testes</a></li><li><a href="/artigos/">Artigos</a></li><li><a href="/casos/">Casos Reais</a></li><li><a href="/perguntas-frequentes.html">FAQ</a></li><li><a href="/sobre.html">Sobre</a></li></ul></div>
    <div class="footer-col"><h4>Legal</h4><ul><li><a href="/privacidade.html">Pol&iacute;tica de Privacidade</a></li><li><a href="/termos.html">Termos de Uso</a></li></ul></div>
  </div>
  <div class="footer-bottom">&copy; 2026 Amorfy. Desenvolvido por <a href="https://dionisio.dev">Dionisio Software</a>.</div>
</footer>

<script src="/js/main.js"></script>
</body>
</html>
"""

PAGES = [
{
"slug": "sobre",
"title": "Sobre o Amorfy — Quem Somos e Nossa Missão",
"desc": "O Amorfy é um portal de conteúdo sobre relacionamentos, autoconhecimento e psicologia do amor. Conheça nossa missão e entre em contato.",
"h1": "Sobre o Amorfy 💖",
"body": """<p>O <strong>Amorfy</strong> nasceu de uma pergunta simples: por que aprendemos matemática, história e geografia na escola — mas ninguém nos ensina a amar?</p>

<p>Relacionamentos são a fonte das nossas maiores alegrias e das nossas dores mais profundas. Ainda assim, a maioria de nós navega o amor no improviso, repetindo padrões que não escolheu e tropeçando nos mesmos erros.</p>

<h2>Nossa missão</h2>
<p>Traduzir a psicologia dos relacionamentos — temperamentos, linguagens do amor, comunicação, traumas, transtornos de personalidade — em <strong>conteúdo acessível, prático e baseado em evidências</strong>, para que qualquer pessoa possa entender melhor a si mesma e construir relações mais saudáveis.</p>

<h2>O que você encontra aqui</h2>
<ul>
  <li><strong><a href="/testes/">Testes interativos:</a></strong> personalidade amorosa, linguagens do amor, sinais de relacionamento narcisista e compatibilidade</li>
  <li><strong><a href="/artigos/">Artigos aprofundados:</a></strong> guias completos sobre psicologia dos relacionamentos</li>
  <li><strong><a href="/casos/">Casos reais:</a></strong> histórias verdadeiras (anonimizadas) de superação e recomeço</li>
</ul>

<h2>Nosso compromisso com a responsabilidade</h2>
<p>Nossos conteúdos e testes têm caráter <strong>informativo e educacional</strong>. Eles não substituem — em nenhuma hipótese — avaliação, diagnóstico ou tratamento por psicólogos ou psiquiatras. Se você está sofrendo, procure ajuda profissional. Em crise, o <strong>CVV atende 24h pelo telefone 188</strong> (ligação gratuita).</p>

<h2>📬 Contato</h2>
<p>Dúvidas, sugestões, correções ou parcerias? Fale com a gente:</p>
<ul>
  <li><strong>E-mail:</strong> <a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a></li>
  <li><strong>Assuntos comerciais e imprensa:</strong> <a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a></li>
</ul>
<p>Quer sugerir um tema de artigo ou compartilhar sua história (anonimamente) na seção de casos reais? Adoramos ouvir leitores — escreva para o e-mail acima.</p>

<div class="highlight-box">
  <h3>💡 Quem faz</h3>
  <p>O Amorfy é desenvolvido e mantido pela <a href="https://dionisio.dev">Dionisio Software</a>, com curadoria de conteúdo baseada em literatura de psicologia e pesquisa científica sobre relacionamentos.</p>
</div>"""
},
{
"slug": "privacidade",
"title": "Política de Privacidade — Amorfy",
"desc": "Política de privacidade do Amorfy: como tratamos dados, cookies, Google AdSense e seus direitos conforme a LGPD.",
"h1": "Política de Privacidade",
"body": """<p><em>Última atualização: 16 de julho de 2025</em></p>

<p>Esta Política de Privacidade descreve como o <strong>Amorfy</strong> (amorfy.com.br) coleta, usa e protege informações quando você visita nosso site.</p>

<h2>1. Informações que coletamos</h2>
<ul>
  <li><strong>Dados de navegação:</strong> como a maioria dos sites, coletamos automaticamente informações como endereço IP, tipo de navegador, páginas visitadas, tempo de permanência e origem do acesso, por meio de cookies e tecnologias similares.</li>
  <li><strong>Respostas de testes:</strong> os testes interativos do Amorfy são processados <strong>inteiramente no seu navegador</strong>. Suas respostas não são enviadas, armazenadas ou associadas a você em nossos servidores.</li>
  <li><strong>E-mail (newsletter):</strong> se você se inscrever na newsletter, coletamos seu endereço de e-mail exclusivamente para envio de conteúdo. Você pode cancelar a qualquer momento.</li>
</ul>

<h2>2. Cookies e publicidade (Google AdSense)</h2>
<p>Exibimos anúncios fornecidos pelo <strong>Google AdSense</strong>. O Google e seus parceiros utilizam cookies para exibir anúncios com base em suas visitas anteriores a este e a outros sites.</p>
<ul>
  <li>O cookie <strong>DART</strong> permite ao Google exibir anúncios personalizados.</li>
  <li>Você pode desativar a publicidade personalizada nas <a href="https://adssettings.google.com" rel="noopener" target="_blank">Configurações de Anúncios do Google</a>.</li>
  <li>Também pode gerenciar cookies de terceiros em <a href="https://optout.aboutads.info" rel="noopener" target="_blank">aboutads.info</a>.</li>
</ul>
<p>Para mais detalhes sobre como o Google trata dados, consulte a <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">política de parceiros do Google</a>.</p>

<h2>3. Como usamos as informações</h2>
<ul>
  <li>Operar, manter e melhorar o site e seus conteúdos</li>
  <li>Medir audiência e entender quais conteúdos são mais úteis</li>
  <li>Exibir publicidade que viabiliza o site gratuito</li>
  <li>Enviar a newsletter, quando solicitada por você</li>
</ul>

<h2>4. Compartilhamento de dados</h2>
<p>Não vendemos, alugamos ou comercializamos seus dados pessoais. Dados de navegação são compartilhados apenas com provedores essenciais (hospedagem, publicidade e métricas), nos limites descritos nesta política.</p>

<h2>5. Seus direitos (LGPD)</h2>
<p>Conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), você tem direito a: confirmar a existência de tratamento de dados, acessar seus dados, corrigi-los, solicitar anonimização ou exclusão, e revogar consentimentos. Para exercer qualquer direito, escreva para <a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a>.</p>

<h2>6. Segurança</h2>
<p>Adotamos medidas razoáveis de segurança para proteger as informações. Nenhuma transmissão pela internet, porém, é 100% segura.</p>

<h2>7. Conteúdo e serviços de terceiros</h2>
<p>Nosso site utiliza serviços de terceiros que podem coletar dados regidos por suas próprias políticas: Google AdSense (publicidade) e Google Fonts (fontes). Links externos levam a sites cujas práticas de privacidade não controlamos.</p>

<h2>8. Crianças e adolescentes</h2>
<p>O Amorfy não se destina a menores de 18 anos e não coleta intencionalmente dados de menores.</p>

<h2>9. Alterações nesta política</h2>
<p>Podemos atualizar esta política periodicamente. A data da última atualização aparece no topo da página. Alterações relevantes serão destacadas no site.</p>

<h2>10. Contato</h2>
<p>Dúvidas sobre esta política: <a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a>.</p>"""
},
{
"slug": "termos",
"title": "Termos de Uso — Amorfy",
"desc": "Termos de uso do Amorfy: condições de utilização do site, isenção de responsabilidade sobre conteúdos informativos e propriedade intelectual.",
"h1": "Termos de Uso",
"body": """<p><em>Última atualização: 16 de julho de 2025</em></p>

<p>Ao acessar o site <strong>Amorfy</strong> (amorfy.com.br), você concorda com os termos abaixo. Se não concordar, por favor não utilize o site.</p>

<h2>1. Natureza do conteúdo — aviso importante</h2>
<p>Todo o conteúdo do Amorfy — artigos, testes, casos e demais materiais — tem caráter <strong>exclusivamente informativo e educacional</strong>.</p>
<ul>
  <li><strong>Não é aconselhamento psicológico, médico ou jurídico.</strong></li>
  <li>Os testes interativos são ferramentas de reflexão e entretenimento — <strong>não são instrumentos de diagnóstico</strong>.</li>
  <li>Nenhum conteúdo substitui avaliação por psicólogo, psiquiatra ou outro profissional habilitado.</li>
  <li>Se você está em sofrimento emocional, procure ajuda profissional. Em crise, ligue <strong>188 (CVV, 24h, gratuito)</strong>. Em situação de violência doméstica, ligue <strong>180</strong>.</li>
</ul>

<h2>2. Uso permitido</h2>
<p>Você pode acessar e compartilhar links para nossos conteúdos livremente. É proibido: reproduzir conteúdo integral sem autorização e crédito, utilizar o site para fins ilícitos, ou tentar comprometer sua segurança e funcionamento.</p>

<h2>3. Propriedade intelectual</h2>
<p>Textos, testes, marca, logotipo e identidade visual do Amorfy são protegidos por direitos autorais. Citações parciais são permitidas com crédito e link para a página original.</p>

<h2>4. Casos reais</h2>
<p>As histórias da seção "Casos Reais" são baseadas em relatos reais com <strong>nomes, profissões e detalhes alterados</strong> para preservar a privacidade dos envolvidos. Qualquer semelhança com pessoas específicas é coincidência decorrente da natureza universal dessas experiências.</p>

<h2>5. Publicidade</h2>
<p>O site é mantido por publicidade (Google AdSense). Não endossamos os produtos anunciados; anúncios são fornecidos pelo Google conforme suas próprias políticas. Consulte nossa <a href="/privacidade.html">Política de Privacidade</a>.</p>

<h2>6. Isenção de responsabilidade</h2>
<p>O Amorfy não se responsabiliza por decisões tomadas com base nos conteúdos do site, pela disponibilidade ininterrupta do serviço, ou por conteúdos de sites externos vinculados. O uso das informações é de responsabilidade exclusiva do usuário.</p>

<h2>7. Alterações</h2>
<p>Estes termos podem ser atualizados a qualquer momento, com vigência a partir da publicação nesta página.</p>

<h2>8. Contato e legislação</h2>
<p>Dúvidas: <a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a>. Estes termos são regidos pelas leis da República Federativa do Brasil.</p>"""
},
]

def write_page(meta, out_dir=None):
    out_dir = Path(out_dir) if out_dir is not None else Path(__file__).resolve().parent.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    meta = dict(meta)
    meta["og_image"] = f"https://amorfy.com.br/og/{meta['slug']}.png"
    html = HEAD.format(**meta) + FOOT
    path = out_dir / f"{meta['slug']}.html"
    path.write_text(html, encoding="utf-8")
    print(f"OK {path} ({len(html)} bytes)")


if __name__ == "__main__":
    for p in PAGES:
        write_page(p)
