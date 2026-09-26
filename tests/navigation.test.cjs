const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

test('menu announces open/closed state and Escape restores focus', () => {
  const events = {}, attributes = {};
  let click, open = false, focused = false;
  const toggle = {
    setAttribute(key, value) { attributes[key] = value; },
    addEventListener(event, fn) { click = fn; },
    focus() { focused = true; }
  };
  const nav = { classList: {
    toggle(name, value) { open = value; }, contains() { return open; }
  } };
  const document = {
    addEventListener(event, fn) { (events[event] ||= []).push(fn); },
    querySelector(selector) { return selector === '.nav-toggle' ? toggle : nav; },
    querySelectorAll() { return []; }
  };
  vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../js/main.js'), 'utf8'), {
    document, window: { location: { pathname: '/' } }
  });
  events.DOMContentLoaded.forEach(fn => fn());
  assert.equal(attributes['aria-expanded'], 'false');
  click();
  assert.equal(open, true);
  assert.equal(attributes['aria-expanded'], 'true');
  assert.equal(attributes['aria-label'], 'Fechar menu');
  events.keydown.forEach(fn => fn({ key: 'Escape' }));
  assert.equal(open, false);
  assert.equal(attributes['aria-expanded'], 'false');
  assert.equal(attributes['aria-label'], 'Abrir menu');
  assert(focused);
  click(); click();
  assert.equal(open, false);
});
