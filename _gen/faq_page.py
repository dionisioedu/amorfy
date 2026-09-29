#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""FAQ page (perguntas-frequentes.html) — accordion + FAQPage schema.

Pure front-end: no backend, no login. Renders grouped <details> accordions
with the v2.1 .accordion-item styles plus a JSON-LD FAQPage block.
"""

import json
from pathlib import Path

from static_pages import HEAD, FOOT

SLUG = "perguntas-frequentes"
TITLE = "Perguntas Frequentes sobre Relacionamentos, Testes e Amor Próprio — Amorfy"
DESC = ("Respostas diretas para as dúvidas mais comuns sobre relacionamentos, "
        "linguagens do amor, narcisismo, borderline, autoestima e os testes do Amorfy.")

GROUPS = [
    ("Sobre o Amorfy", [
        {"q": "O Amorfy é um site de psicologia?", "a":
         "<p>Somos um portal de <em>conteúdo educacional</em> sobre relacionamentos, autoconhecimento e psicologia do amor. Traduzimos literatura de psicologia e pesquisa científica sobre relações em linguagem acessível. Não somos um serviço de atendimento psicológico e não substituímos consulta profissional.</p>"},
        {"q": "Nossos conteúdos podem substituir terapia?", "a":
         "<p>Não. Nossos artigos e testes são informativos e servem para autoconhecimento, reflexão e conversa. Diagnóstico e tratamento de qualquer questão de saúde mental exigem avaliação por psicólogo ou psiquiatra. Em crise, ligue <strong>188 (CVV)</strong> gratuitamente, 24h.</p>"},
        {"q": "O Amorfy cobra por algo?", "a":
         "<p>Não. Todo o conteúdo — testes, artigos e casos reais — é gratuito. O site é sustentado por publicidade (Google AdSense). Não há planos pagos nem necessidade de criar conta.</p>"},
        {"q": "Meus dados de teste são armazenados?", "a":
         "<p>Não. Os testes rodam <strong>inteiramente no seu navegador</strong>: suas respostas nunca são enviadas nem salvas em servidores. Veja detalhes na <a href=\"/privacidade.html\">Política de Privacidade</a>.</p>"},
    ]),
    ("Sobre os testes", [
        {"q": "Os testes têm validade científica?", "a":
         "<p>Nossos testes são inspirados em conceitos estabelecidos (temperamentos, linguagens do amor, critérios do DSM-5, pesquisa de Gottman sobre casais), mas <strong>não são instrumentos psicométricos validados</strong>. São ferramentas de reflexão e autoconhecimento — trate o resultado como um ponto de partida, não como diagnóstico.</p>"},
        {"q": "Qual a diferença entre o teste e um diagnóstico?", "a":
         "<p>Diagnóstico exige avaliação clínica, presencial, com um profissional formado, considerando história de vida, contexto e critérios formais. Um teste online não conhece seu contexto. Ele pode apontar direções úteis e orientar uma busca por ajuda, mas nunca fechar uma questão clínica.</p>"},
        {"q": "Posso fazer quantos testes eu quiser?", "a":
         "<p>Sim, quantas vezes quiser — não há limite, cadastro ou custo. Você pode refazer um teste depois de alguns meses e comparar os resultados; mudanças percebidas ao longo do tempo costumam ser informativas.</p>"},
        {"q": "Como escolho qual teste fazer primeiro?", "a":
         "<p>Se a pergunta é &quot;como eu amo?&quot;, comece pela <a href=\"/testes/personalidade-amorosa.html\">personalidade amorosa</a> ou pela <a href=\"/testes/linguagem-do-amor.html\">linguagem do amor</a>. Se a dúvida é sobre um relacionamento específico que te faz mal, comece pelos testes de <a href=\"/testes/narcisista.html\">sinais de abuso narcisista</a> ou <a href=\"/testes/parceiro-borderline.html\">parceiro com traços borderline</a>.</p>"},
    ]),
    ("Relacionamentos", [
        {"q": "Como sei se meu relacionamento é saudável?", "a":
         "<p>Alguns marcadores objetivos: você pode discordar sem medo de punição, existe reparação após conflitos, você mantém vida própria, e a relação te dá mais energia do que custa. Não existe casal sem conflito — existe casal que resolve e casal que acumula.</p>"},
        {"q": "Ele(a) mudou, ou sempre foi assim?", "a":
         "<p>Na maioria dos casos, o padrão já existia em versão suave no começo e se intensificou. Máscaras caem quando a insegurança de perder você diminui — casamento, mudança, gravidez e dependência financeira costumam ser gatilhos. Olhar para trás com honestidade ajuda a ver os sinais que a empolgação encobriu.</p>"},
        {"q": "Por que repito sempre o mesmo tipo de relacionamento?", "a":
         "<p>Porque a escolha de parceiro costuma seguir padrões aprendidos cedo, na família de origem — e o familiar, mesmo quando doloroso, gera sensação de &quot;lar&quot;. Entender o mecanismo é o primeiro passo para interrompê-lo. Leia <a href=\"/artigos/repeticao-compulsiva-no-amor.html\">repetição compulsiva no amor</a>.</p>"},
        {"q": "É normal sentir falta de um relacionamento ruim?", "a":
         "<p>Sim, é muito comum — e não significa que o relacionamento era bom, nem que você quer voltar. Vínculos intensos criam dependência emocional que persiste independente da qualidade da relação. O luto por uma relação abusiva é real e merece ser tratado como luto.</p>"},
    ]),
    ("Narcisismo e abuso", [
        {"q": "Como identificar alguém com traços narcisistas?", "a":
         "<p>Sinais frequentes: incapacidade de pedir desculpas genuínas, necessidade constante de admiração, desvalorização súbita após fase de encanto, gaslighting (fazer você duvidar da própria percepção) e falta de empatia quando você sofre. O critério importante é o <strong>padrão</strong>, não episódios isolados.</p>"},
        {"q": "Meu parceiro tem dias em que é maravilhoso. Ainda é abuso?", "a":
         "<p>Sim, e essa oscilação é característica do ciclo de abuso: idealização, desvalorização e descarte. As fases boas são o que mantém a pessoa presa — e por isso o critério nunca deve ser os melhores dias, mas o padrão ao longo do tempo.</p>"},
        {"q": "O que é gaslighting?", "a":
         "<p>É uma forma de manipulação em que a pessoa distorce fatos, nega o que disse e questiona a sua memória ou sanidade até você duvidar de si mesma. O nome vem do filme <em>Gaslight</em> (1944). Combater exige <strong>registro</strong>: anotar o que aconteceu rompe o efeito da negação.</p>"},
        {"q": "Estou em situação de risco. O que faço?", "a":
         "<p>Em emergência, ligue <strong>190</strong>. Para violência contra a mulher, <strong>180</strong> (24h, gratuito). Apoio emocional 24h: <strong>CVV 188</strong>. Se possível, conte para alguém de confiança e busque apoio profissional e jurídico antes de qualquer confronto.</p>"},
    ]),
    ("Borderline", [
        {"q": "O que é o transtorno de personalidade borderline?", "a":
         "<p>É um transtorno caracterizado por instabilidade emocional intensa, medo de abandono, instabilidade de identidade e das relações, impulsividade e oscilações de humor. É um dos transtornos com melhor resposta a tratamento — especialmente à terapia comportamental dialética (DBT).</p>"},
        {"q": "Pessoa com borderline pode ter relacionamento saudável?", "a":
         "<p>Sim. Relações estáveis são possíveis, especialmente quando há tratamento consistente e limites claros de ambas as partes. O diagnóstico não define a capacidade de amar nem de sustentar uma relação.</p>"},
        {"q": "Sou parceiro(a) de alguém com borderline e estou exausto(a). É normal?", "a":
         "<p>É comum, mas não é saudável nem inevitável. O chamado &quot;esgotamento do cuidador&quot; tem sintomas reais. Lembre-se: você não pode ser o terapeuta do seu parceiro — apoiar é diferente de tratar. Busque <strong>apoio para você</strong>, não apenas para ele.</p>"},
    ]),
    ("Amor próprio e autoestima", [
        {"q": "O que é amor próprio, na prática?", "a":
         "<p>Não é autoajuda genérica. É a capacidade de estabelecer limites, não trocar sua dignidade por companhia, e reconhecer que suas necessidades têm tanto peso quanto as do outro. Amor próprio é comportamento observável, não um sentimento vago.</p>"},
        {"q": "Como parar de depender emocionalmente de alguém?", "a":
         "<p>Comece ampliando a rede: amizades, atividades, projetos próprios. Dependência emocional se sustenta na escassez — quanto menos fontes de afeto e sentido você tem, mais uma única pessoa pesa. Terapia ajuda muito nesse processo. Leia <a href=\"/artigos/dependencia-emocional-psicanalise.html\">dependência emocional</a>.</p>"},
        {"q": "É saudável gostar de ficar sozinho?", "a":
         "<p>Muito. A <a href=\"/artigos/capacidade-de-ficar-so.html\">capacidade de ficar só</a> é um dos melhores indicadores de saúde emocional — quem tolera a própria companhia escolhe parceiros por desejo, não por desespero.</p>"},
    ]),
    ("Conteúdo e colaboração", [
        {"q": "Como sugiro um tema de artigo?", "a":
         "<p>Escreva para <a href=\"mailto:contato@amorfy.com.br\">contato@amorfy.com.br</a>. Adoramos sugestões de leitores — muitas das nossas pautas vieram de perguntas reais de quem nos acompanha.</p>"},
        {"q": "Posso enviar minha história para os Casos Reais?", "a":
         "<p>Sim, e agradecemos. As histórias são publicadas com nomes, profissões e detalhes alterados para preservar integralmente sua privacidade. Envie para <a href=\"mailto:contato@amorfy.com.br\">contato@amorfy.com.br</a>.</p>"},
        {"q": "Encontrei um erro no conteúdo. Como reporto?", "a":
         "<p>Mande um e-mail para <a href=\"mailto:contato@amorfy.com.br\">contato@amorfy.com.br</a> com o link da página e o trecho. Levamos correções a sério e atualizamos as páginas rapidamente.</p>"},
    ]),
]


def render_accordion(groups):
    parts = []
    for gi, (group_title, items) in enumerate(groups, start=1):
        parts.append(f'<h2 class="faq-group">{group_title}</h2>')
        parts.append('<div class="accordion">')
        for i, item in enumerate(items):
            open_attr = " open" if gi == 1 and i == 0 else ""
            parts.append(
                f'<details class="accordion-item"{open_attr}>'
                f'<summary><span>{item["q"]}</span></summary>'
                f'<div class="accordion-body">{item["a"]}</div>'
                f'</details>'
            )
        parts.append('</div>')
    return "\n".join(parts)


def render_schema(groups):
    entities = []
    for _title, items in groups:
        for item in items:
            answer = item["a"]
            for tag in ("<p>", "</p>", "<strong>", "</strong>", "<em>", "</em>"):
                answer = answer.replace(tag, "")
            # strip remaining tags
            clean = []
            in_tag = False
            for ch in answer:
                if ch == "<":
                    in_tag = True
                elif ch == ">":
                    in_tag = False
                elif not in_tag:
                    clean.append(ch)
            entities.append({
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": "".join(clean).strip()},
            })
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": entities,
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def build(out_dir=None):
    out_dir = Path(out_dir) if out_dir is not None else Path(__file__).resolve().parent.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    body_parts = [
        '<p class="faq-intro">Reunimos aqui as perguntas que mais chegam pelos nossos canais. '
        'Se você não encontrar sua dúvida, escreva para '
        '<a href="mailto:contato@amorfy.com.br">contato@amorfy.com.br</a> — a gente responde.</p>',
        render_accordion(GROUPS),
        '<div class="highlight-box">'
        '<h3>💡 Preciso de ajuda profissional</h3>'
        '<p>Se você está passando por sofrimento intenso, lembre-se: o <strong>CVV atende 24h '
        'ligando 188</strong> (gratuito). Para violência contra a mulher, <strong>180</strong>. '
        'Em emergência, <strong>190</strong>.</p></div>',
    ]
    body = "\n".join(body_parts)

    meta = {
        "slug": SLUG,
        "title": TITLE,
        "desc": DESC,
        "h1": "Perguntas Frequentes",
        "body": body,
        "og_image": f"https://amorfy.com.br/og/{SLUG}.png",
    }
    head = HEAD.format(**meta)
    # HEAD already emitted <main><article>...{body}...</article></main>; drop its tail
    # and rebuild the article with a custom header (meta line) while keeping <main>.
    head = head.split("<main>")[0]
    schema = ('<script type="application/ld+json">' + render_schema(GROUPS) + '</script>')
    head = head.replace("</head>", schema + "\n</head>")

    html = head + f'<main><article><header class="article-header"><h1>{meta["h1"]}</h1>'
    html += '<p class="article-meta">Atualizado em fevereiro de 2026</p></header>'
    html += f'<div class="article-body">{body}</div></article></main>' + FOOT
    path = out_dir / f"{SLUG}.html"
    path.write_text(html, encoding="utf-8")
    print(f"OK {path} ({len(html)} bytes)")
    return path


if __name__ == "__main__":
    build()