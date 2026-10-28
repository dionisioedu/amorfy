"""Diretório público: apenas perfis autorizados, sem coleta de dados clínicos."""
import json
import re
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import urlparse

DATA = Path(__file__).with_name('professionals') / 'profiles.json'
ROLES = {'psicologia': 'Psicologia', 'psicanalise': 'Psicanálise', 'terapia': 'Terapia'}


def load_profiles(path=DATA):
    profiles = json.loads(Path(path).read_text(encoding='utf-8-sig'))
    published, slugs = [], set()
    for p in profiles:
        if not p.get('published'):
            continue
        if p.get('consent_publication') is not True:
            raise ValueError('Perfil público exige autorização de divulgação.')
        for field in ('slug', 'name', 'title', 'bio', 'formation', 'audience', 'location', 'contact_url', 'reviewed_on'):
            if not isinstance(p.get(field), str) or not p[field].strip():
                raise ValueError('Campo obrigatório: ' + field)
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', p['slug']) or p['slug'] == 'index' or p['slug'] in slugs:
            raise ValueError('Slug inválido ou duplicado.')
        slugs.add(p['slug'])
        if p.get('kind') not in ROLES or p.get('relationship') not in ('owner', 'partner'):
            raise ValueError('Categoria ou vínculo inválido.')
        if p['kind'] == 'psicologia' and not re.fullmatch(r'\d{2}/\d{3,8}', p.get('registration', '')):
            raise ValueError('Perfil de Psicologia exige CRP no formato regional/número.')
        if not p.get('modes') or any(m not in ('Online', 'Presencial') for m in p['modes']):
            raise ValueError('Modalidade inválida.')
        contact = urlparse(p['contact_url'])
        if contact.scheme != 'https' or not contact.hostname or contact.username or contact.password or contact.fragment:
            raise ValueError('Contato deve ser um link HTTPS público, sem credenciais.')
        if contact.query:
            raise ValueError('Use contato sem parâmetros, mensagens pré-preenchidas ou rastreamento.')
        if p.get('email') and not re.fullmatch(r'[A-Za-z0-9.!#$%&*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', p['email']):
            raise ValueError('E-mail inválido.')
        date.fromisoformat(p['reviewed_on'])
        published.append(p)
    return sorted(published, key=lambda p: p['name'].casefold())


def contact_cta():
    active = bool(load_profiles())
    title = 'Quer conversar com um profissional?' if active else 'Pensando em buscar atendimento?'
    text = 'Conheça os perfis, a modalidade de atendimento e os contatos dos profissionais.' if active else 'Veja o que perguntar antes de escolher um profissional e acompanhe a formação da nossa rede.'
    return f'<aside class="care-cta"><div><h2>{title}</h2><p>{text}</p></div><a class="btn btn-secondary" href="/profissionais/">{"Conhecer profissionais" if active else "Conhecer a rede"} →</a></aside>'


def affiliation(p):
    return 'Responsável pelo Amorfy — divulgação de serviço próprio.' if p['relationship'] == 'owner' else 'Profissional parceiro — divulgação de seu serviço no Amorfy.'


def page(title, desc, slug, body, schema=None):
    from static_pages import HEAD, FOOT
    markup = HEAD.format(title=escape(title), desc=escape(desc, quote=True), slug=slug, og_image='https://amorfy.com.br/og.png', h1=escape(title), body=body) + FOOT
    markup = re.sub(r'  <script async src="https://pagead2[^\n]+\n', '', markup)
    markup = markup.replace('<meta name="google-adsense-account" content="ca-pub-6858130394830057">', '<meta name="referrer" content="no-referrer">')
    if slug == 'profissionais/index':
        markup = markup.replace('https://amorfy.com.br/profissionais/index.html', 'https://amorfy.com.br/profissionais/')
    if schema:
        data = json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c')
        markup = markup.replace('</head>', '<script type="application/ld+json">'+data+'</script>\n</head>')
    return markup


def write_professionals(output):
    profiles = load_profiles()
    dest = Path(output) / 'profissionais'
    dest.mkdir(parents=True, exist_ok=True)
    intro = '<p class="care-intro">Um espaço para conhecer profissionais, entender como trabalham e escolher com quem conversar. O primeiro contato é feito diretamente pelo canal informado em cada perfil.</p>'
    cards = []
    for p in profiles:
        e = {k: escape(v, quote=True) for k, v in p.items() if isinstance(v, str)}
        modes = escape(' · '.join(p['modes']))
        registration = '<p><strong>CRP '+escape(p['registration'])+'</strong></p>' if p['kind'] == 'psicologia' else ''
        avatar = '<img class="care-avatar" src="/images/professional-placeholder.svg" alt="Foto do profissional ainda não disponível" width="120" height="120">'
        email = f'<p><a href="mailto:{e["email"]}">Contato por e-mail</a></p>' if p.get('email') else ''
        cards.append(f'<article class="care-card">{avatar}<p>{escape(ROLES[p["kind"]])} · {modes}</p><h2><a href="/profissionais/{e["slug"]}.html">{e["name"]}</a></h2><p>{e["title"]}</p>{registration}<p>{e["location"]}</p><p>{e["audience"]}</p><small>{affiliation(p)}</small><p><a class="btn btn-secondary" href="/profissionais/{e["slug"]}.html">Ver perfil e contato →</a></p></article>')
        body = f'{avatar}<p><a href="/profissionais/">← Todos os profissionais</a></p><p class="care-disclosure">{affiliation(p)}</p><p><strong>{e["title"]}</strong> · {modes}</p>{registration}<h2>Apresentação</h2><p>{e["bio"]}</p><h2>Formação</h2><p>{e["formation"]}</p><h2>Público e modalidade</h2><p>{e["audience"]}</p><p>{modes} · {e["location"]}</p><h2>Primeiro contato</h2><p>Consulte disponibilidade, condições do atendimento, honorários e política de cancelamento diretamente com o profissional. O contato não confirma agendamento.</p><p><a class="btn btn-primary" href="{e["contact_url"]}" rel="noopener noreferrer">Entrar em contato ↗</a></p>{email}<p>Você sairá do Amorfy. A conversa será tratada pelo profissional e pela plataforma escolhida. Não há envio de respostas de testes ou histórico de leitura.</p><p><small>Dados de apresentação atualizados em {e["reviewed_on"]}. A presença no diretório não garante resultados.</small></p>'
        schema = {'@context':'https://schema.org','@type':'ProfilePage','url':'https://amorfy.com.br/profissionais/'+p['slug']+'.html','mainEntity':{'@type':'Person','name':p['name'],'jobTitle':p['title'],'description':p['bio']}}
        (dest/(p['slug']+'.html')).write_text(page(p['name']+' — '+p['title'],p['bio'][:155],'profissionais/'+p['slug'],body,schema),encoding='utf-8')
    listing = '<div class="care-grid">'+''.join(cards)+'</div>' if cards else '<div class="highlight-box"><h2>Estamos formando nossa rede</h2><p>Ainda não há perfis de atendimento publicados. Os contatos serão disponibilizados após autorização de divulgação e revisão das informações profissionais.</p><a href="#participar">Sou profissional e quero participar →</a></div>'
    guidance = '''<h2>Como escolher com mais clareza</h2><ol><li><strong>Conheça a formação.</strong> Leia o percurso de formação e pergunte sobre a prática oferecida. O uso do título terapeuta ou psicanalista, sozinho, não informa uma graduação em Psicologia.</li><li><strong>Confira a identificação.</strong> Para serviços de Psicologia, consulte o nome e o CRP no <a href="https://cadastro.cfp.org.br/" rel="noreferrer">Cadastro Nacional de Psicólogas e Psicólogos</a>.</li><li><strong>Converse sobre o atendimento.</strong> Pergunte sobre modalidade, público atendido, funcionamento das sessões, sigilo, honorários e cancelamento.</li><li><strong>Decida com liberdade.</strong> Você pode esclarecer dúvidas e optar por outro profissional. Nenhum teste do Amorfy determina diagnóstico ou necessidade de tratamento.</li></ol>
<h2>Transparência da rede</h2><p>Os perfis são apresentados em ordem alfabética, sem ranking clínico. O vínculo com o Amorfy aparece em cada perfil, inclusive quando se tratar de serviço próprio do responsável pelo site. A listagem não representa avaliação de eficácia nem garantia de resultado.</p><p>O Amorfy oferece informação e divulgação de contatos. O atendimento, o agendamento e as condições do serviço são combinados com cada profissional. Este diretório não funciona como pronto atendimento.</p>
<h2>Sua privacidade no primeiro contato</h2><p>Esta área não solicita sintomas, diagnósticos, relatos pessoais ou respostas dos testes, e não carrega anúncios. Os links de contato não incluem dados de navegação ou resultados. As plataformas externas têm suas próprias políticas de privacidade; a hospedagem do site pode registrar dados técnicos de acesso.</p>
<h2 id="participar">Você é profissional e quer participar?</h2><p>Envie sua apresentação profissional à equipe: nome de divulgação, título, formação, registro quando aplicável, público atendido, modalidade, cidade e link profissional de contato. Não envie documentos de pacientes, relatos clínicos ou informações de terceiros.</p><p><a class="btn btn-secondary" href="mailto:contato@amorfy.com.br?subject=Participar%20da%20rede%20Amorfy">Solicitar inclusão por e-mail</a></p><p>O envio inicia uma conversa; não publica um perfil automaticamente. Antes da publicação, confirmaremos as informações e a autorização para divulgar os campos públicos. Para corrigir ou retirar um perfil, use o mesmo contato.</p>
<h2>Referências para esta área</h2><ul><li><a href="https://transparencia.cfp.org.br/crp10/pergunta-frequente/publicidade-profissional/">Orientações do Conselho Regional de Psicologia sobre publicidade profissional</a>.</li><li><a href="https://www.gov.br/anpd/pt-br/documentos-e-publicacoes/glossario-anpd">Glossário da ANPD: dados pessoais sensíveis</a>.</li></ul>'''
    (dest/'index.html').write_text(page('Profissionais e atendimento','Conheça a rede Amorfy, saiba o que perguntar ao escolher atendimento e consulte os perfis profissionais disponíveis.','profissionais/index',intro+listing+guidance),encoding='utf-8')
