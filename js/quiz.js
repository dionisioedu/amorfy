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
      html += '<div class="result-emoji">' + (res.emoji || '💖') + '</div>';
      html += '<h2 tabindex="-1">' + res.title + '</h2>';
      html += '<div class="result-text">' + res.text + '</div>';
      html += scoreBars();
      if (res.link) html += '<a href="' + res.link + '" class="btn btn-primary" style="margin-bottom:1rem">' + (res.linkText || 'Saiba mais') + '</a>';
      html += '<div class="share-buttons">';
      html += '<button class="btn btn-secondary" id="quiz-retry">🔄 Refazer teste</button>';
      html += '<a class="btn btn-purple" href="https://wa.me/?text=' + encodeURIComponent(data.shareText + ' https://amorfy.com.br' + window.location.pathname) + '" target="_blank" rel="noopener">📲 Compartilhar</a>';
      html += '</div></div></div>';
      root.innerHTML = html;
      focusHeading();
      animateScores();
      var retry = document.getElementById('quiz-retry');
      if (retry) retry.addEventListener('click', function() {
        current = 0; scores = {}; total = 0; render(true);
      });
      // Refresh ads after result
      try { (adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    }

    // Builds dimension score bars if the quiz data declares `dimensions`.
    // dimensions: [{key, label}] for category mode, or [{label, min, max}] for sum mode.
    function scoreBars() {
      var dims = data.dimensions;
      if (!dims || !dims.length) return '';
      var rows = [];
      if (data.mode === 'category') {
        var maxScore = 0;
        dims.forEach(function(d) { maxScore = Math.max(maxScore, scores[d.key] || 0); });
        if (maxScore <= 0) return '';
        dims.slice().sort(function(a, b) { return (scores[b.key] || 0) - (scores[a.key] || 0); })
          .forEach(function(d) {
            var v = scores[d.key] || 0;
            var pct = Math.round((v / maxScore) * 100);
            rows.push(dimRow(d.label, v, maxScore, pct, false));
          });
      } else {
        var lo = Infinity, hi = -Infinity;
        dims.forEach(function(d) {
          if (typeof d.min === 'number') lo = Math.min(lo, d.min);
          if (typeof d.max === 'number') hi = Math.max(hi, d.max);
        });
        // Sum mode: render each declared band with a tick for the achieved total.
        dims.forEach(function(d) {
          var mid = (d.min + d.max) / 2;
          var pct = (typeof d.max === 'number' && typeof d.min === 'number')
            ? Math.round(((mid - lo) / ((hi - lo) || 1)) * 100)
            : 0;
          rows.push(dimRow(d.label, null, null, pct, total <= d.max));
        });
      }
      return '<div class="quiz-scores"><h3>Seu perfil</h3>' + rows.join('') + '</div>';
    }

    function dimRow(label, value, max, pct, highlight) {
      var h = '<div class="score-row">';
      h += '<div class="score-row-head"><span>' + label + '</span>';
      if (value !== null && value !== undefined) h += '<span>' + value + '/' + max + '</span>';
      h += '</div>';
      h += '<div class="score-track"><div class="score-fill' + (highlight ? '' : ' dim') + '" data-w="' + pct + '%"></div></div>';
      h += '</div>';
      return h;
    }

    function animateScores() {
      var fills = root.querySelectorAll('.score-fill');
      if (!fills.length) return;
      var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduce) { fills.forEach(function(f) { f.style.width = f.dataset.w; }); return; }
      requestAnimationFrame(function() {
        setTimeout(function() {
          fills.forEach(function(f) { f.style.width = f.dataset.w; });
        }, 60);
      });
    }

    render();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initQuiz);
  } else {
    initQuiz();
  }
})();
