// Amorfy — Quiz Engine
// Usage: define window.QUIZ_DATA = { mode, questions, results, ... } then this engine renders it.
// mode "category": each option adds points to categories; highest category wins.
// mode "sum": each option has a numeric value; total falls into a range result.
(function() {
  'use strict';

  function initQuiz() {
    var data = window.QUIZ_DATA;
    var root = document.getElementById('quiz');
    if (!data || !root) return;

    var current = 0;
    var scores = {};
    var total = 0;

    function focusHeading() {
      root.querySelector('h2').focus({ preventScroll: true });
    }

    function render(moveFocus) {
      if (current >= data.questions.length) return renderResult();
      var q = data.questions[current];
      var pct = Math.round((current / data.questions.length) * 100);
      var html = '<div class="quiz-card">';
      html += '<div class="quiz-progress" role="progressbar" aria-label="Perguntas respondidas" aria-valuemin="0" aria-valuemax="' + data.questions.length + '" aria-valuenow="' + current + '"><div class="quiz-progress-bar" style="width:' + pct + '%"></div></div>';
      html += '<p id="quiz-step" style="color:var(--text-secondary);font-size:.85rem;margin-bottom:.75rem">Pergunta ' + (current + 1) + ' de ' + data.questions.length + '</p>';
      html += '<h2 class="quiz-question" tabindex="-1" aria-describedby="quiz-step">' + q.q + '</h2>';
      html += '<div class="quiz-options">';
      q.options.forEach(function(opt, i) {
        html += '<button class="quiz-option" data-i="' + i + '">' + opt.text + '</button>';
      });
      html += '</div></div>';
      root.innerHTML = html;
      if (moveFocus) focusHeading();

      var answered = false;
      var options = root.querySelectorAll('.quiz-option');
      options.forEach(function(btn) {
        btn.addEventListener('click', function() {
          if (answered) return;
          answered = true;
          options.forEach(function(option) { option.disabled = true; });
          btn.classList.add('selected');
          var opt = q.options[parseInt(btn.dataset.i, 10)];
          if (data.mode === 'category') {
            for (var k in opt.scores) scores[k] = (scores[k] || 0) + opt.scores[k];
          } else {
            total += opt.value || 0;
          }
          setTimeout(function() {
            if (opt.showSupport && data.supportResult) {
              renderResult(data.supportResult);
            } else {
              current++;
              render(true);
            }
            window.scrollTo({top: root.offsetTop - 100, behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'});
          }, 350);
        });
      });
    }

    function winner() {
      var best = null, bestScore = -1;
      for (var k in scores) {
        if (scores[k] > bestScore) { bestScore = scores[k]; best = k; }
      }
      return best;
    }

    function renderResult(override) {
      var res = override;
      if (!res && data.mode === 'category') {
        res = data.results[winner()];
      } else if (!res) {
        for (var i = 0; i < data.results.length; i++) {
          if (total <= data.results[i].max) { res = data.results[i]; break; }
        }
        if (!res) res = data.results[data.results.length - 1];
      }
      var html = '<div class="quiz-card"><div class="quiz-result">';
      html += '<div style="font-size:3.5rem;margin-bottom:.5rem">' + (res.emoji || '💖') + '</div>';
      html += '<h2 tabindex="-1">' + res.title + '</h2>';
      html += '<div class="result-text">' + res.text + '</div>';
      if (res.link) html += '<a href="' + res.link + '" class="btn btn-primary" style="margin-bottom:1rem">' + (res.linkText || 'Saiba mais') + '</a>';
      html += '<div class="share-buttons">';
      html += '<button class="btn btn-secondary" id="quiz-retry">🔄 Refazer teste</button>';
      html += '<a class="btn btn-purple" href="https://wa.me/?text=' + encodeURIComponent(data.shareText + ' https://amorfy.com.br' + window.location.pathname) + '" target="_blank" rel="noopener">📲 Compartilhar</a>';
      html += '</div></div></div>';
      root.innerHTML = html;
      focusHeading();
      var retry = document.getElementById('quiz-retry');
      if (retry) retry.addEventListener('click', function() {
        current = 0; scores = {}; total = 0; render(true);
      });
      // Refresh ads after result
      try { (adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    }

    render();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuiz);
  } else {
    initQuiz();
  }
})();
