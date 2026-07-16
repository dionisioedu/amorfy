// Amorfy — Shared JavaScript
(function() {
  'use strict';

  // Mobile nav toggle
  document.addEventListener('DOMContentLoaded', function() {
    const toggle = document.querySelector('.nav-toggle');
    const nav = document.querySelector('.nav-links');
    if (toggle && nav) {
      toggle.addEventListener('click', function() {
        nav.classList.toggle('open');
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
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
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
