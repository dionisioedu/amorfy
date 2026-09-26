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

    document.querySelectorAll('.card, .story-card, .article-body h2, .article-body h3').forEach(function(el) {
      observer.observe(el);
    });
  }
})();
