# Multilingual Landing Pages & User Guide Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform `landing/index.html` into a template-driven, 11-language localized product landing site at `/{lang}/` with automatic root locale redirection, and migrate the existing User Guide documentation under `/guide/{lang}/`.

**Architecture:**
- Extract `landing/index.html` into a shared `landing/template.html` with an embedded glassmorphic 11-language switcher and guide link bindings.
- Extract copy into 11 structured translation files (`landing/i18n/{lang}.json`).
- Build a Python generator `scripts/build_landing.py` to compile landing pages to `site/{lang}/index.html` and synchronize `landing/images/` to `site/images/`.
- Update Zensical generator `scripts/generate_configs.py` to relocate MkDocs output to `site/guide/{lang}/` and base URL to `https://cmder.aitobox.com/guide/{lang}/`.
- Extend client-side language detector and unit tests to seamlessly handle both `/{lang}/` and `/guide/{lang}/`.
- Update `test.sh` and `.github/workflows/deploy.yml` for unified one-command build and automated deployment.

**Tech Stack:** Python 3.12, Zensical, HTML5/CSS3/JavaScript, GitHub Pages Actions.

**Spec:** `docs/superpowers/specs/2026-10-08-landing-page-and-guide-migration-design.md`

## Global Constraints

- Must support all 11 languages defined in `scripts/languages.py`: `en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`.
- Python-Markdown list spacing (MD032) must be preserved in all documentation files.
- All landing image assets must be referenced via root-relative path `/images/screenshots/...`.
- No additional runtime third-party dependencies (pure standard library Python for `build_landing.py`).
- 100% test pass rate for `node scripts/test_language_detector.js` and `python3 scripts/generate_configs.py --check`.

## Review Focus

1. **Root redirection loop or mismatch**: User visits `https://cmder.aitobox.com/` and must land on `/{lang}/` (landing page), never in an infinite loop or broken 404.
2. **Landing "User Guide" button cross-link**: On `/zh/` landing page, "User Guide" button must navigate to `/guide/zh/`, and on `/ja/` to `/guide/ja/`.
3. **Guide logo navigation**: Clicking ATBCmder logo inside `/guide/en/` must navigate back to `/en/`, not `/` or a dead link.
4. **Language switcher preservation**: Switching language inside `/guide/de/power_tools/` must navigate to `/guide/{target}/power_tools/` without losing the `/guide/` prefix.
5. **Image loading under deep paths**: All screenshots must load cleanly from `/images/screenshots/` on any landing page `/{lang}/`.

---

### Task 1: Language Detector Extension & Unit Tests

**Files:**
- Modify: `docs/en/javascripts/language-detector.js:95-115`
- Modify: `scripts/test_language_detector.js:120-170`
- Replicate to: `docs/{lang}/javascripts/language-detector.js` (for all 11 languages)

**Interfaces:**
- Consumes: URL pathname, e.g. `/guide/en/file_operations/` or `/zh/`
- Produces: `getCurrentPageLang(pathname) -> lang_code` (e.g. `'en'`, `'zh'`), `replaceLangInPath(pathname, fromLang, toLang) -> newPath`

- [ ] **Step 1: Write failing tests in `scripts/test_language_detector.js`**

Add tests for `/guide/{lang}/` path matching and path replacement:
```javascript
// In test 4:
{ path: '/guide/en/', expected: 'en' },
{ path: '/guide/zh/getting_started/', expected: 'zh' },
{ path: '/guide/ja/file_operations/', expected: 'ja' },
// In test 5:
{ path: '/guide/en/power_tools/', from: 'en', to: 'fr', expected: '/guide/fr/power_tools/' },
{ path: '/guide/zh/getting_started/', from: 'zh', to: 'ja', expected: '/guide/ja/getting_started/' }
```

- [ ] **Step 2: Run unit test to verify failure**

Run: `node scripts/test_language_detector.js`  
Expected: FAIL on path replacement preserving `/guide/` prefix or language extraction.

- [ ] **Step 3: Update `docs/en/javascripts/language-detector.js`**

Update `getCurrentPageLang(pathname)` and `replaceLangInPath(pathname, fromLang, toLang)` to support both `/guide/{lang}/` and `/{lang}/` paths cleanly while preserving any leading prefix.

- [ ] **Step 4: Sync `language-detector.js` to all languages and verify unit tests**

Copy `docs/en/javascripts/language-detector.js` to all `docs/{lang}/javascripts/language-detector.js`.  
Run: `node scripts/test_language_detector.js`  
Expected: PASS (All assertions passing).

- [ ] **Step 5: Commit changes**

```bash
git add docs/*/javascripts/language-detector.js scripts/test_language_detector.js
git commit -m "feat(i18n): support /guide/{lang}/ paths in language detector"
```

---

### Task 2: Zensical Config & Documentation Subpath Migration

**Files:**
- Modify: `scripts/generate_configs.py:80-110`
- Modify: `overrides/partials/source.html:15-30`
- Modify: `overrides/partials/header.html:10-15`
- Generate: `zensical.*.toml` (11 files)

**Interfaces:**
- Consumes: Language metadata in `scripts/languages.py`
- Produces: `site_dir = "site/guide/{code}"`, `site_url = "https://cmder.aitobox.com/guide/{code}/"`, `extra.homepage = "/{code}/"`

- [ ] **Step 1: Update `scripts/generate_configs.py`**

Modify `generate_config_content`:
- Change `site_url` to `f"https://cmder.aitobox.com/guide/{code}/"`
- Change `site_dir` to `f"site/guide/{code}"`
- Add `extra.homepage = f"/{code}/"` (or in `[extra]` section: `homepage = f"/{code}/"`)
- In `build_alternate_list`, change links to `f"/guide/{lang['code']}/"`

- [ ] **Step 2: Update header and source overrides**

In `overrides/partials/source.html`:
Change dropdown item links:
```html
<a href="/guide/{{ item_lang }}/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="{{ item_lang }}" role="menuitem">...</a>
```
In `overrides/partials/header.html`:
Ensure logo link uses `config.extra.homepage` or `/{{ config.theme.language }}/`.

- [ ] **Step 3: Regenerate configs and verify drift check**

Run: `python3 scripts/generate_configs.py`  
Run: `python3 scripts/generate_configs.py --check`  
Expected: PASS (All 11 config files updated and match).

- [ ] **Step 4: Commit changes**

```bash
git add scripts/generate_configs.py zensical.*.toml overrides/partials/
git commit -m "refactor(docs): migrate guide documentation output to /guide/{lang}/"
```

---

### Task 3: Landing Template & 11 Language Translation Dictionaries

**Files:**
- Create: `landing/template.html` (derived from `landing/index.html`)
- Create: `landing/i18n/en.json`
- Create: `landing/i18n/zh.json`
- Create: `landing/i18n/zh-hant.json`
- Create: `landing/i18n/ja.json`
- Create: `landing/i18n/de.json`
- Create: `landing/i18n/fr.json`
- Create: `landing/i18n/es.json`
- Create: `landing/i18n/pt.json`
- Create: `landing/i18n/ko.json`
- Create: `landing/i18n/ru.json`
- Create: `landing/i18n/it.json`

**Interfaces:**
- Consumes: `landing/index.html`, macOS terminology guidelines
- Produces: Complete translation dictionaries covering all sections of the landing page.

- [ ] **Step 1: Create `landing/template.html`**

Refactor `landing/index.html` into `landing/template.html`:
- Use absolute screenshot paths: `/images/screenshots/...`
- Add Language Switcher dropdown in header with click handler that saves to `localStorage.setItem('preferred_language', code)` and redirects to `/{code}/`.
- Bind "User Guide" links to `/guide/{{ lang }}/`.
- Replace all hardcoded texts with placeholders `{{ t.key_name }}`.

- [ ] **Step 2: Create master translation files `landing/i18n/zh.json` and `landing/i18n/en.json`**

Extract all keys from `landing/index.html` into `zh.json` (exact original copy).
Create `en.json` with idiomatic native macOS developer copy.

- [ ] **Step 3: Create translation files for remaining 9 languages**

Create `zh-hant.json`, `ja.json`, `de.json`, `fr.json`, `es.json`, `pt.json`, `ko.json`, `ru.json`, `it.json` ensuring 100% key parity with `en.json`.

- [ ] **Step 4: Verify key parity across all 11 JSON files**

Run a validation one-liner with Python:
`python3 -c "import json, glob; keys = [set(json.load(open(f)).keys()) for f in sorted(glob.glob('landing/i18n/*.json'))]; assert all(k == keys[0] for k in keys), 'Key mismatch'"`  
Expected: PASS with 0 mismatches.

- [ ] **Step 5: Commit changes**

```bash
git add landing/template.html landing/i18n/*.json
git commit -m "feat(landing): create master template and 11-language translation dictionaries"
```

---

### Task 4: Landing Builder Script (`scripts/build_landing.py`)

**Files:**
- Create: `scripts/build_landing.py`

**Interfaces:**
- Consumes: `landing/template.html`, `landing/i18n/{lang}.json`, `landing/images/`
- Produces: `site/{lang}/index.html` (all 11 languages), `site/images/`

- [ ] **Step 1: Write `scripts/build_landing.py`**

Implement `build_landing.py`:
- Read `landing/template.html` and `landing/i18n/*.json` for all languages in `scripts.languages.LANGUAGES`.
- Replace `{{ lang }}`, `{{ title }}`, `{{ meta_desc }}`, `{{ canonical }}`, and all `{{ t.<key> }}` strings.
- Inject active language styling and dropdown menu items.
- Write output to `site/{lang}/index.html` (and optionally `landing/{lang}/index.html`).
- Recursively copy `landing/images/` into `site/images/`.

- [ ] **Step 2: Run `build_landing.py` and verify generated HTML files**

Run: `python3 scripts/build_landing.py`  
Expected: 11 HTML files generated under `site/` with valid `<title>`, localized text, and images copied to `site/images/screenshots/`.

- [ ] **Step 3: Verify link and asset paths in generated HTML**

Inspect generated files to confirm:
- `<a href="/guide/zh/" ...>User Guide</a>` on Chinese page.
- `<a href="/guide/en/" ...>User Guide</a>` on English page.
- Image `src="/images/screenshots/dual_panel_list_and_thumbnails.png"`.

- [ ] **Step 4: Commit changes**

```bash
git add scripts/build_landing.py
git commit -m "feat(landing): implement landing builder script scripts/build_landing.py"
```

---

### Task 5: Pipeline & Local Preview Integration (`test.sh` & `deploy.yml`)

**Files:**
- Modify: `test.sh:180-260`
- Modify: `.github/workflows/deploy.yml:50-70`

**Interfaces:**
- Consumes: Zensical build, `scripts/build_landing.py`, `root_index.html`
- Produces: Complete working `site/` directory ready for preview or deployment.

- [ ] **Step 1: Update `test.sh`**

Integrate `python3 scripts/build_landing.py` after Zensical compilation.
Update the preview banner to display:
- Root URL: `http://localhost:${PORT}/`
- Landing pages: `http://localhost:${PORT}/${lang}/`
- User guides: `http://localhost:${PORT}/guide/${lang}/`

- [ ] **Step 2: Update `.github/workflows/deploy.yml`**

Add `python3 scripts/build_landing.py` step right after the Zensical build loop.

- [ ] **Step 3: Run full local build test (`./test.sh -b`)**

Run: `./test.sh -b`  
Expected: Static compilation completes with code 0, populating `site/` with `site/index.html`, `site/{lang}/index.html`, `site/guide/{lang}/`, and `site/images/`.

- [ ] **Step 4: Verify complete end-to-end site structure and link checks**

Verify with automated check script:
- All 11 landing pages exist: `test -f site/en/index.html && test -f site/zh/index.html` ...
- All 11 guide homepages exist: `test -f site/guide/en/index.html && test -f site/guide/zh/index.html` ...
- All screenshots present: `test -f site/images/screenshots/dual_panel_list_and_thumbnails.png` ...
- Root redirect exists: `test -f site/index.html` ...

- [ ] **Step 5: Commit changes**

```bash
git add test.sh .github/workflows/deploy.yml
git commit -m "feat(build): integrate landing page compilation into test.sh and deploy.yml"
```
