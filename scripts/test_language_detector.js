/**
 * scripts/test_language_detector.js
 * Unit tests for language detection, prefix matching, pathname routing, and root_index.html.
 */

const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

console.log('=== Running Language Detector Unit Tests ===\n');

// 1. Load module
const detector = require('../docs/en/javascripts/language-detector.js');

// Test 1: Supported Languages List
console.log('Test 1: Verify 11 supported languages metadata');
const expectedCodes = ['en', 'zh', 'zh-hant', 'ja', 'de', 'fr', 'es', 'pt', 'ko', 'ru', 'it'];
assert.strictEqual(Object.keys(detector.SUPPORTED_LANGS).length, 11, 'Must support exactly 11 languages');
expectedCodes.forEach(code => {
  assert.ok(detector.SUPPORTED_LANGS[code], `Missing language code: ${code}`);
});
console.log('  ✓ All 11 languages defined with native names.');

// Test 2: matchBrowserLocale with various locales
console.log('\nTest 2: Prefix matching for browser locales');
const testCases = [
  // Traditional Chinese
  { input: 'zh-TW', expected: 'zh-hant' },
  { input: 'zh-HK', expected: 'zh-hant' },
  { input: 'zh-MO', expected: 'zh-hant' },
  { input: 'zh-Hant', expected: 'zh-hant' },
  { input: 'zh-Hant-TW', expected: 'zh-hant' },
  { input: 'zh-hant-hk', expected: 'zh-hant' },

  // Simplified / Generic Chinese
  { input: 'zh-CN', expected: 'zh' },
  { input: 'zh-SG', expected: 'zh' },
  { input: 'zh-Hans', expected: 'zh' },
  { input: 'zh-Hans-CN', expected: 'zh' },
  { input: 'zh', expected: 'zh' },

  // Japanese
  { input: 'ja', expected: 'ja' },
  { input: 'ja-JP', expected: 'ja' },

  // German
  { input: 'de', expected: 'de' },
  { input: 'de-DE', expected: 'de' },
  { input: 'de-AT', expected: 'de' },
  { input: 'de-CH', expected: 'de' },

  // French
  { input: 'fr', expected: 'fr' },
  { input: 'fr-FR', expected: 'fr' },
  { input: 'fr-CA', expected: 'fr' },

  // Spanish
  { input: 'es', expected: 'es' },
  { input: 'es-ES', expected: 'es' },
  { input: 'es-MX', expected: 'es' },

  // Portuguese
  { input: 'pt', expected: 'pt' },
  { input: 'pt-BR', expected: 'pt' },
  { input: 'pt-PT', expected: 'pt' },

  // Korean
  { input: 'ko', expected: 'ko' },
  { input: 'ko-KR', expected: 'ko' },

  // Russian
  { input: 'ru', expected: 'ru' },
  { input: 'ru-RU', expected: 'ru' },

  // Italian
  { input: 'it', expected: 'it' },
  { input: 'it-IT', expected: 'it' },

  // English
  { input: 'en', expected: 'en' },
  { input: 'en-US', expected: 'en' },
  { input: 'en-GB', expected: 'en' },

  // Unsupported / empty
  { input: 'sv-SE', expected: null },
  { input: 'pl-PL', expected: null },
  { input: '', expected: null },
  { input: null, expected: null },
  { input: undefined, expected: null }
];

testCases.forEach(({ input, expected }) => {
  const result = detector.matchBrowserLocale(input);
  assert.strictEqual(result, expected, `Failed for locale: "${input}" (got "${result}", expected "${expected}")`);
});
console.log(`  ✓ Passed ${testCases.length} locale prefix matching assertions.`);

// Test 3: detectBrowserLanguage with simulated navigator
console.log('\nTest 3: detectBrowserLanguage priority and fallback');
const navCases = [
  { nav: { languages: ['ja-JP', 'en-US'] }, expected: 'ja' },
  { nav: { languages: ['zh-TW', 'zh-CN', 'en'] }, expected: 'zh-hant' },
  { nav: { languages: ['zh-CN', 'en'] }, expected: 'zh' },
  { nav: { languages: ['pt-BR', 'en'] }, expected: 'pt' },
  { nav: { languages: ['pl-PL', 'de-DE', 'en'] }, expected: 'de' },
  { nav: { languages: ['nl-NL', 'sv-SE'] }, expected: 'en' },
  { nav: { languages: [] }, expected: 'en' },
  { nav: { language: 'fr-FR' }, expected: 'fr' },
  { nav: { language: 'ko-KR' }, expected: 'ko' },
  { nav: { userLanguage: 'ru-RU' }, expected: 'ru' },
  { nav: {}, expected: 'en' },
  { nav: null, expected: 'en' }
];

navCases.forEach(({ nav, expected }) => {
  const result = detector.detectBrowserLanguage(nav);
  assert.strictEqual(result, expected, `Failed for nav: ${JSON.stringify(nav)} (got "${result}", expected "${expected}")`);
});
console.log(`  ✓ Passed ${navCases.length} navigator language resolution assertions.`);

// Test 4: Path parsing: getCurrentPageLang
console.log('\nTest 4: getCurrentPageLang pathname matching');
const pathCases = [
  { path: '/en/', expected: 'en' },
  { path: '/en', expected: 'en' },
  { path: '/en/power_tools/', expected: 'en' },
  { path: '/zh-hant/', expected: 'zh-hant' },
  { path: '/zh-hant/getting_started/', expected: 'zh-hant' },
  { path: '/zh/', expected: 'zh' },
  { path: '/zh/getting_started/', expected: 'zh' },
  { path: '/ja/file_operations/', expected: 'ja' },
  { path: '/de/navigation_and_tabs/', expected: 'de' },
  { path: '/fr/viewers_and_editors/', expected: 'fr' },
  { path: '/es/power_tools/', expected: 'es' },
  { path: '/pt/network_and_vfs/', expected: 'pt' },
  { path: '/ko/preferences_and_customization/', expected: 'ko' },
  { path: '/ru/keyboard_shortcuts/', expected: 'ru' },
  { path: '/it/faq_howtos/', expected: 'it' },
  { path: '/subpath/en/download/', expected: 'en' },
  { path: '/', expected: null },
  { path: '/stylesheets/extra.css', expected: null },
  { path: '/images/screenshot.png', expected: null }
];

pathCases.forEach(({ path, expected }) => {
  const result = detector.getCurrentPageLang(path);
  assert.strictEqual(result, expected, `Failed for path: "${path}" (got "${result}", expected "${expected}")`);
});
console.log(`  ✓ Passed ${pathCases.length} pathname matching assertions.`);

// Test 5: replaceLangInPath
console.log('\nTest 5: replaceLangInPath preserving deep suffix');
const replaceCases = [
  { path: '/en/power_tools/', from: 'en', to: 'fr', expected: '/fr/power_tools/' },
  { path: '/en/', from: 'en', to: 'ja', expected: '/ja/' },
  { path: '/en', from: 'en', to: 'ja', expected: '/ja' },
  { path: '/zh-hant/getting_started/', from: 'zh-hant', to: 'zh', expected: '/zh/getting_started/' },
  { path: '/zh/getting_started/', from: 'zh', to: 'zh-hant', expected: '/zh-hant/getting_started/' },
  { path: '/de/faq_howtos/index.html', from: 'de', to: 'it', expected: '/it/faq_howtos/index.html' },
  { path: '/sub/pt/download/', from: 'pt', to: 'ko', expected: '/sub/ko/download/' }
];

replaceCases.forEach(({ path, from, to, expected }) => {
  const result = detector.replaceLangInPath(path, from, to);
  assert.strictEqual(result, expected, `Failed replace for "${path}" from ${from} to ${to} (got "${result}", expected "${expected}")`);
});
console.log(`  ✓ Passed ${replaceCases.length} path replacement assertions.`);

// Test 6: Verify root_index.html syntax & execution via VM
console.log('\nTest 6: Verify root_index.html script extraction & simulated execution');
const rootHtml = fs.readFileSync(path.join(__dirname, '../root_index.html'), 'utf8');

// Ensure all 11 languages are present in fallback list
expectedCodes.forEach(code => {
  assert.ok(rootHtml.includes(`href="/${code}/"`), `root_index.html missing link for /${code}/`);
});
assert.ok(rootHtml.includes('<meta http-equiv="refresh" content="0; url=/en/">'), 'root_index.html must have noscript refresh to /en/');

// Extract inline script
const scriptMatch = rootHtml.match(/<script>([\s\S]*?)<\/script>/);
assert.ok(scriptMatch, 'root_index.html must contain a <script> block');
const scriptCode = scriptMatch[1];

function runRootScriptWithMock({ search = '', storedLang = null, navLanguages = ['en'] }) {
  let redirectedTo = null;
  const mockStorage = {
    getItem: (key) => (key === 'preferred_language' ? storedLang : null),
    setItem: (key, val) => {}
  };
  const mockWindow = {
    location: {
      search: search,
      hash: '',
      replace: (url) => { redirectedTo = url; }
    }
  };
  const mockNavigator = {
    languages: navLanguages
  };

  const sandbox = {
    window: mockWindow,
    navigator: mockNavigator,
    localStorage: mockStorage
  };

  vm.createContext(sandbox);
  vm.runInContext(scriptCode, sandbox);
  return redirectedTo;
}

assert.strictEqual(runRootScriptWithMock({ storedLang: 'ja' }), '/ja/', 'Stored preference ja failed');
assert.strictEqual(runRootScriptWithMock({ storedLang: 'zh-hant' }), '/zh-hant/', 'Stored preference zh-hant failed');
assert.strictEqual(runRootScriptWithMock({ search: '?lang=fr' }), '/fr/?lang=fr', 'URL param ?lang=fr failed');
assert.strictEqual(runRootScriptWithMock({ navLanguages: ['zh-TW', 'en'] }), '/zh-hant/', 'Browser locale zh-TW failed');
assert.strictEqual(runRootScriptWithMock({ navLanguages: ['de-DE'] }), '/de/', 'Browser locale de-DE failed');
assert.strictEqual(runRootScriptWithMock({ navLanguages: ['ru-RU'] }), '/ru/', 'Browser locale ru-RU failed');
assert.strictEqual(runRootScriptWithMock({ navLanguages: ['pt-BR'] }), '/pt/', 'Browser locale pt-BR failed');
assert.strictEqual(runRootScriptWithMock({ navLanguages: ['nl-NL'] }), '/en/', 'Fallback to /en/ failed');

console.log('  ✓ All root_index.html simulated execution tests passed successfully.');

// Test 7: Verify docs/en and docs/zh parity
console.log('\nTest 7: Verify parity between docs/en and docs/zh language-detector.js');
const enJs = fs.readFileSync(path.join(__dirname, '../docs/en/javascripts/language-detector.js'), 'utf8');
const zhJs = fs.readFileSync(path.join(__dirname, '../docs/zh/javascripts/language-detector.js'), 'utf8');
assert.strictEqual(enJs, zhJs, 'docs/en and docs/zh language-detector.js must be byte-for-byte identical');
console.log('  ✓ Both files are 100% identical.');

console.log('\n=== All Tests Passed! ===\n');
