// Amorfy — Shared JavaScript
(function() {
  'use strict';

  // Mobile nav toggle
  document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('.nav-links');
    if (toggle && nav) {
      function setMenu(open) {
        nav.classList.toggle('open', open);
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
      }
      setMenu(false);
      toggle.addEventListener('click', function() {
        setMenu(!nav.classList.contains('open'));
      });
      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && nav.classList.contains('open')) {
          setMenu(false);
          toggle.focus();
        }
      });
    }
  });

  // Highlight active nav link
  document.addEventListener('DOMContentLoaded', function() {
    const current = window.location.pathname;
    document.querySelectorAll('.nav-links a').forEach(function(link) {
      const href = link.getAttribute('href');
      if (href === current || (href !== '/' && current.startsWith(href.replace(/\/$/, '')))) {
        link.classList.add('active');
      }
    });
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      const target = document.getElementById(decodeURIComponent(this.hash.slice(1)));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' });
      }
    });
  });

  // Intersection Observer for fade-in animations
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('animate-in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .story-card, .step, .dimension-card, .article-body h2, .article-body h3').forEach(function(el) {
      observer.observe(el);
    });
  }

  // Reading progress bar (articles only)
  document.addEventListener('DOMContentLoaded', function() {
    try {
    const body = document.querySelector('.article-body');
    if (!body) return;
    const bar = document.createElement('div');
    bar.className = 'read-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);
    let ticking = false;
    function update() {
      const rect = body.getBoundingClientRect();
      const total = rect.height - window.innerHeight;
      const scrolled = -rect.top;
      const pct = total > 0 ? Math.min(100, Math.max(0, (scrolled / total) * 100)) : 0;
      bar.style.width = pct + '%';
      ticking = false;
    }
    window.addEventListener('scroll', function() {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    window.addEventListener('resize', update, { passive: true });
    update();
    } catch (e) { /* minimal DOM */ }
  });

  // Auto-build a table of contents from h2s in long articles
  document.addEventListener('DOMContentLoaded', function() {
    try {
    const body = document.querySelector('.article-body');
    if (!body) return;
    const h2s = Array.from(body.querySelectorAll('h2'));
    if (h2s.length < 3) return; // only for substantial articles
    const slugify = function(s) {
      return s.toLowerCase()
        .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
        .replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-').slice(0, 60);
    };
    const used = {};
    const items = h2s.map(function(h) {
      let id = h.id || slugify(h.textContent);
      if (used[id]) { used[id]++; id = id + '-' + used[id]; } else { used[id] = 1; }
      h.id = id;
      return { id: id, text: h.textContent.trim() };
    });
    const nav = document.createElement('nav');
    nav.className = 'article-toc';
    nav.setAttribute('aria-label', 'Sumário do artigo');
    nav.innerHTML = '<h4>Neste artigo</h4><ol>' +
      items.map(function(i) { return '<li><a href="#' + i.id + '">' + i.text + '</a></li>'; }).join('') +
      '</ol>';
    const firstH2 = h2s[0];
    body.insertBefore(nav, firstH2);
    } catch (e) { /* minimal DOM */ }
  });

  // Cookie consent (LGPD) — banner global, uma decisão por navegador
  document.addEventListener('DOMContentLoaded', function() {
    try {
    var KEY = 'amorfy_consent';
    var stored = null;
    try { stored = window.localStorage.getItem(KEY); } catch (e) { stored = null; }
    if (stored) return;

    var banner = document.createElement('div');
    banner.className = 'cookie-consent';
    banner.setAttribute('role', 'dialog');
    banner.setAttribute('aria-label', 'Consentimento de cookies');
    banner.innerHTML =
      '<div class="cookie-consent-inner">' +
      '<p>Usamos cookies e tecnologias similares para exibir anúncios e entender como o site é usado. ' +
      'Ao continuar, você concorda com o uso de cookies conforme nossa ' +
      '<a href="/privacidade.html">Política de Privacidade</a>.</p>' +
      '<div class="cookie-consent-actions">' +
      '<button type="button" class="btn btn-secondary" data-consent="essential">Só o essencial</button>' +
      '<button type="button" class="btn btn-primary" data-consent="all">Aceitar</button>' +
      '</div></div>';
    document.body.appendChild(banner);

    function decide(value) {
      try { window.localStorage.setItem(KEY, value); } catch (e) { /* ignore */ }
      banner.classList.add('cookie-consent-hidden');
    }
    banner.querySelectorAll('[data-consent]').forEach(function(btn) {
      btn.addEventListener('click', function() { decide(this.getAttribute('data-consent')); });
    });
    } catch (e) { /* minimal DOM */ }
  });
})();
