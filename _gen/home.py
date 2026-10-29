"""Home editorial e catálogo pesquisável, atualizados a cada build."""
import json
from html import escape
from pathlib import Path
from article_template import CATEGORIES
from professionals import contact_cta
from documented_cases import CASES


def catalog(articles, quizzes):
    items = []
    for a in sorted(articles, key=lambda a: (a.get("date", ""), a["slug"]), reverse=True):
        items.append(dict(title=a["title"], desc=a["desc"], url=f'/artigos/{a["slug"]}.html',
                          publication_order=a.get("publication_order", 0), kind="noticia" if a.get("news") else "artigo", image=a.get("image", ""),
                          label="Leitura técnica" if a.get("technical") else ("Notícia" if a.get("news") else "Artigo"), date=a.get("date", ""),
                          meta=f'{a.get("read_min", 5)} min de leitura',
                          topics=" ".join(CATEGORIES[c][0] for c in a.get("categories", []) if c in CATEGORIES)))
    for q in quizzes:
        items.append(dict(title=q["title"].split(" — ")[0], desc=q["desc"], url=f'/testes/{q["slug"]}.html',
                          kind="teste", image="", label="Teste", date="", meta="Gratuito · Sem cadastro", topics="autoconhecimento"))
    for c in CASES:
        items.append(dict(title=c["title"], desc=c["desc"], url=f'/casos/{c["slug"]}.html',
                          kind="caso", image=c["image"], label="Caso documentado", date=c["date"],
                          meta=f'{c["read_min"]} min de leitura', topics=c["tag"]))
    return sorted(items, key=lambda item: (-int(item["date"].replace("-", "") or "0"), -item.get("publication_order", 0), item["url"]))


def card(item):
    a = {k: escape(str(v), quote=True) for k, v in item.items()}
    image = (f'<img src="{a["image"]}" alt="" width="1536" height="1024" loading="lazy" decoding="async">' if a["image"] else '<div class="home-quiz-art" aria-hidden="true">?</div>')
    date = f'<time datetime="{a["date"]}">{a["date"][8:10]}/{a["date"][5:7]}/{a["date"][:4]}</time> · ' if a["date"] else ""
    return f'<article class="home-card home-card-{a["kind"]}"><a href="{a["url"]}" class="home-card-link">{image}<div class="home-card-body"><span class="home-label">{a["label"]}</span><h3>{a["title"]}</h3><p>{a["desc"]}</p><span class="home-card-meta">{date}{a["meta"]}</span><span class="home-read">{"Começar teste" if a["kind"] == "teste" else "Ler agora"} <span aria-hidden="true">↗</span></span></div></a></article>'


def write_home(articles, quizzes, output):
    items = catalog(articles, quizzes)
    news = [a for a in items if a["kind"] == "noticia"][:3]
    posts = [a for a in items if a["kind"] == "artigo"][:6]
    tests = [a for a in items if a["kind"] == "teste" and a["url"] in ["/testes/personalidade-amorosa.html", "/testes/linguagem-do-amor.html", "/testes/compatibilidade.html"]]
    recent = [a for a in items if a["date"]]
    featured = recent[0]
    f = {k: escape(str(v), quote=True) for k, v in featured.items()}
    feature_image = (f'<img src="{f["image"]}" alt="" width="1536" height="1024" fetchpriority="high">'
                     if f["image"] else '<div class="home-feature-placeholder" aria-hidden="true">Amorfy</div>')
    feature = f'<article class="home-feature home-feature-{f["kind"]}"><a href="{f["url"]}">{feature_image}<div class="home-feature-text"><span class="home-feature-tag">MAIS RECENTE · {f["label"]}</span><h2>{f["title"]}</h2><p>{f["desc"]}</p><span><time datetime="{f["date"]}">{f["date"][8:10]}/{f["date"][5:7]}/{f["date"][:4]}</time> · {f["meta"]} <span aria-hidden="true">↗</span></span></div></a></article>'
    values = dict(recent="".join(map(card, recent[3:9])), side="".join(map(card, recent[1:3])), latest_date=recent[0]["date"][8:10] + "/" + recent[0]["date"][5:7] + "/" + recent[0]["date"][:4], cases="".join(card(a) for a in items if a["kind"] == "caso"), care=contact_cta(), feature=feature, news="".join(map(card, news)), articles="".join(map(card, posts)), quizzes="".join(map(card, tests)),
                  topics="".join(f'<a href="/temas/{slug}.html">{escape(label)} <span aria-hidden="true">↗</span></a>' for slug, (label, _) in CATEGORIES.items() if slug != "noticias"),
                  catalog=json.dumps(items, ensure_ascii=False).replace("<", "\\u003c"))
    template = Path(__file__).with_name("home_template.tmpl").read_text(encoding="utf-8")
    for key, value in values.items():
        template = template.replace("@@" + key + "@@", value)
    (Path(output) / "index.html").write_text(template, encoding="utf-8")
