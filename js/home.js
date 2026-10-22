/* Local catalog search; no requests or storage of search terms. */
(function () {
  'use strict';
  function normalize(value) {
    return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }
  function select(items, query, kind) {
    const terms = normalize(query).trim().split(/\s+/).filter(Boolean);
    return items.filter(item => (kind === 'all' || item.kind === kind) && terms.every(term => normalize(item.title + ' ' + item.desc + ' ' + item.topics).includes(term)));
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { select };
  if (typeof document === 'undefined') return;
  const source = document.getElementById('home-catalog');
  if (!source) return;
  const items = JSON.parse(source.textContent);
  const input = document.getElementById('home-search');
  const filters = document.querySelector('.home-filters');
  const results = document.getElementById('home-results');
  const feed = document.getElementById('home-feed');
  const count = document.getElementById('home-count');
  const more = document.getElementById('home-more');
  let kind = 'all', limit = 12;
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }
  function card(item) {
    const article = element('article', 'home-card home-card-' + item.kind);
    const link = element('a', 'home-card-link'); link.href = item.url;
    if (item.image) {
      const image = element('img'); image.src = item.image; image.alt = ''; image.width = 1536; image.height = 1024; image.loading = 'lazy'; link.append(image);
    } else {
      const art = element('div', 'home-quiz-art', '?'); art.setAttribute('aria-hidden', 'true'); link.append(art);
    }
    const body = element('div', 'home-card-body');
    body.append(element('span', 'home-label', item.label), element('h3', '', item.title), element('p', '', item.desc), element('span', 'home-card-meta', item.meta), element('span', 'home-read', item.kind === 'teste' ? 'Começar teste ↗' : 'Ler agora ↗'));
    link.append(body); article.append(link); return article;
  }
  function render(added = false) {
    const active = input.value.trim() !== '' || kind !== 'all';
    feed.hidden = active; results.hidden = !active;
    results.replaceChildren(); more.hidden = true;
    if (!active) { count.textContent = ''; return; }
    const found = select(items, input.value, kind);
    found.slice(0, limit).forEach(item => results.append(card(item)));
    count.textContent = found.length ? `${found.length} ${found.length === 1 ? 'conteúdo encontrado' : 'conteúdos encontrados'} · mostrando ${Math.min(limit, found.length)}` : 'Nenhum conteúdo encontrado. Tente outro termo ou selecione outro formato.';
    more.hidden = found.length <= limit;
    if (added) results.children[limit - 12]?.querySelector('a').focus();
  }
  input.disabled = false; filters.hidden = false;
  input.addEventListener('input', () => { limit = 12; render(); });
  filters.querySelectorAll('button').forEach(button => button.addEventListener('click', () => {
    kind = button.dataset.kind; limit = 12;
    filters.querySelectorAll('button').forEach(other => other.setAttribute('aria-pressed', String(other === button)));
    render();
  }));
  document.querySelectorAll('.home-shortcuts a, .home-start-secondary').forEach(link => link.addEventListener('click', () => {
    input.value = ''; kind = 'all'; limit = 12;
    filters.querySelectorAll('button').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.kind === 'all')));
    render();
  }, true));
  more.addEventListener('click', () => { limit += 12; render(true); });
})();
