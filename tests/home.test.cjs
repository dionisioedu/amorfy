const {test} = require('node:test');
const assert = require('node:assert/strict');
const {select} = require('../js/home.js');
const items = [
  {kind:'artigo',title:'Ciúme digital',desc:'Conversa e acordos',topics:'Relacionamentos'},
  {kind:'teste',title:'Como você ama?',desc:'Perguntas sobre comunicação',topics:'Autoconhecimento'},
  {kind:'noticia',title:'Novas pesquisas',desc:'Intimidade digital',topics:'Relacionamentos'}
];
test('home search ignores accents/case and searches descriptions and topics', () => {
  assert.equal(select(items,'CIUME','all')[0],items[0]);
  assert.equal(select(items,'comunicacao','teste')[0],items[1]);
  assert.equal(select(items,'relacionamentos','all').length,2);
});
test('home search combines terms and format, handles empty and unmatched queries', () => {
  assert.deepEqual(select(items,'digital conversa','all'),[items[0]]);
  assert.deepEqual(select(items,'digital','noticia'),[items[2]]);
  assert.deepEqual(select(items,'digital','teste'),[]);
  assert.deepEqual(select(items,'   ','all'),items);
  assert.deepEqual(select(items,'<script>','all'),[]);
});
