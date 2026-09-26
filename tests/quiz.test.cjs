const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const project = path.resolve(__dirname, '..');
const source = fs.readFileSync(path.join(project, 'js/quiz.js'), 'utf8');
function readQuiz(slug) {
  const page = fs.readFileSync(path.join(project, 'testes', slug + '.html'), 'utf8');
  return JSON.parse(page.match(/window.QUIZ_DATA = (.*?);\s*<\/script>/s)[1]);
}

function start(data, reducedMotion = false) {
  let html = '', buttons = [], retry, focusCount = 0, scroll;
  const timers = [];
  const root = {
    offsetTop: 100,
    querySelectorAll() { return buttons; },
    querySelector() { return { focus() { focusCount++; } }; },
    set innerHTML(value) {
      html = value;
      buttons = [...value.matchAll(/data-i="(\d+)"/g)].map(match => ({
        dataset: { i: match[1] }, disabled: false,
        classList: { add() {} },
        addEventListener(event, fn) { this.click = fn; }
      }));
    }
  };
  vm.runInNewContext(source, {
    window: {
      QUIZ_DATA: data, location: { pathname: '/testes/' },
      scrollTo(value) { scroll = value; }, matchMedia() { return { matches: reducedMotion }; }
    },
    document: {
      readyState: 'complete',
      getElementById(id) {
        return id === 'quiz' ? root : { addEventListener(event, fn) { retry = fn; } };
      }
    },
    setTimeout(fn) { timers.push(fn); }, encodeURIComponent
  });
  return {
    get html() { return html; }, get buttons() { return buttons; }, timers,
    get focusCount() { return focusCount; }, get scroll() { return scroll; },
    answer(i) { buttons[i].click(); timers.shift()(); }, retry() { retry(); }
  };
}

for (const slug of ['borderline', 'parceiro-borderline']) {
  for (const choice of [1, 2, 3]) {
    test(`${slug}: support takes precedence for option ${choice}, even at low scores`, () => {
      const data = readQuiz(slug), quiz = start(data);
      const index = data.questions.findIndex(q => q.options.some(o => o.showSupport));
      for (let i = 0; i < index; i++) quiz.answer(0);
      quiz.answer(choice);
      assert(quiz.html.includes(data.supportResult.title));
      assert(quiz.html.includes('tel:192'));
      assert(quiz.html.includes('tel:188'));
      assert(!quiz.html.includes(data.results[0].title));
      quiz.retry();
      for (const q of data.questions) quiz.answer(0);
      assert(quiz.html.includes(data.results[0].title));
    });
  }
}

for (const slug of ['borderline', 'compatibilidade', 'linguagem-do-amor', 'narcisista', 'parceiro-borderline', 'personalidade-amorosa']) {
  test(`${slug}: normal completion and retry`, () => {
    const data = readQuiz(slug), quiz = start(data);
    for (let i = 0; i < data.questions.length; i++) {
      assert(quiz.html.includes(`Pergunta ${i + 1} de ${data.questions.length}`));
      assert(quiz.buttons.every(b => !b.disabled));
      quiz.answer(0);
    }
    assert(quiz.html.includes('quiz-retry'));
    quiz.retry();
    assert(quiz.html.includes(`Pergunta 1 de ${data.questions.length}`));
  });
}

for (const mode of ['sum', 'category']) {
  test(`${mode}: repeated and competing clicks count only once`, () => {
    const data = {
      mode, shareText: 'Test',
      questions: [1, 2].map(i => ({ q: `Question ${i}`, options: [
        { text: 'A', value: 1, scores: { a: 1 } },
        { text: 'B', value: 0, scores: { b: 2 } }
      ] })),
      results: mode === 'sum' ? [
        { max: 1, title: 'Correct', text: '' }, { max: 99, title: 'Duplicate', text: '' }
      ] : { a: { title: 'Duplicate', text: '' }, b: { title: 'Correct', text: '' } }
    };
    const quiz = start(data), first = quiz.buttons;
    first[0].click(); first[0].click(); first[1].click();
    assert(first.every(b => b.disabled));
    assert.equal(quiz.timers.length, 1);
    quiz.timers.shift()();
    assert(quiz.html.includes('Question 2'));
    first[0].click();
    assert.equal(quiz.timers.length, 0);
    quiz.answer(1);
    assert(quiz.html.includes('>Correct</h2>'));
  });
}

test('keyboard focus follows question, result and retry; reduced motion is respected', () => {
  const data = readQuiz('compatibilidade'), quiz = start(data, true);
  assert.equal(quiz.focusCount, 0, 'initial render must not steal focus');
  assert(quiz.html.includes('role="progressbar"'));
  assert(quiz.html.includes('aria-describedby="quiz-step"'));
  for (let i = 0; i < data.questions.length; i++) {
    quiz.answer(0);
    assert.equal(quiz.focusCount, i + 1);
    assert.equal(quiz.scroll.behavior, 'auto');
  }
  quiz.retry();
  assert.equal(quiz.focusCount, data.questions.length + 1);
});
