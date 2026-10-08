# Design Spec: Multilingual Landing Pages & User Guide Migration for ATBCmder

**Date:** 2026-10-08  
**Status:** In Review  
**Target Domain:** `https://cmder.aitobox.com`  
**Reference File:** `landing/index.html`, `landing/images/`

---

## 1. Executive Summary & Goals

ATBCmder currently serves its MkDocs/Zensical-based User Guide at the root locale path (`https://cmder.aitobox.com/{lang}/`), with automatic root redirection via `root_index.html`. To deliver a premium, high-converting product marketing presence while retaining comprehensive technical documentation, we are restructuring the site:

1. **New Multilingual Landing Page as Site Entry:**
   - Elevate `landing/index.html` into a fully localized product showcase across all 11 supported languages (`en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`).
   - The root URL (`https://cmder.aitobox.com/`) will automatically route visitors based on browser locale or saved preference to their respective landing page (`/{lang}/`).
   - Each landing page includes a glassmorphic multi-language switcher dropdown, instant workflow tabs with retina screenshots, specifications matrix, and direct call-to-actions.

2. **User Guide Relocation to Secondary Subpath:**
   - Move the complete 11-language documentation guide under the secondary URL hierarchy: `https://cmder.aitobox.com/guide/{lang}/`.
   - Update all Guide header navigation elements (ATBCmder brand logo links back to `/{lang}/`; language switcher navigates between `/guide/{lang}/...`).
   - All "User Guide" buttons across landing pages link directly to the corresponding language's documentation (`/guide/{lang}/`).

3. **Template-Driven Build & Continuous Deployment:**
   - Abstract `landing/index.html` into `landing/template.html` and 11 translation dictionaries (`landing/i18n/{lang}.json`).
   - Create `scripts/build_landing.py` to compile landing pages and synchronize shared screenshot assets into `site/`.
   - Update `scripts/generate_configs.py`, `test.sh`, and `.github/workflows/deploy.yml` for unified, one-command compilation.

---

## 2. Target URL Routing & Directory Architecture

### 2.1 URL Routing Specifications

| URL Pattern | Destination File | Role & Behavior |
| :--- | :--- | :--- |
| `https://cmder.aitobox.com/` | `site/index.html` | **Root Gateway**: Evaluates query param `?lang=<code>`, `localStorage.preferred_language`, and `navigator.languages`. Instantly redirects to `/{lang}/`. |
| `https://cmder.aitobox.com/{lang}/` | `site/{lang}/index.html` | **Localized Landing Page**: Product showcase for language `<lang>`. Contains 11-language switcher, feature tabs, and Guide CTA (`/guide/{lang}/`). |
| `https://cmder.aitobox.com/guide/{lang}/` | `site/guide/{lang}/index.html` | **Localized User Guide**: Full MkDocs/Zensical documentation for `<lang>`. Logo links to `/{lang}/`, switcher switches within `/guide/{lang}/`. |
| `https://cmder.aitobox.com/images/screenshots/*` | `site/images/screenshots/*` | **Global Screenshot Assets**: Shared assets referenced by all landing pages via absolute path `/images/screenshots/...`. |

### 2.2 Output Directory Tree (`site/`)

```
site/
├── index.html                      # Root locale detector & redirector (from root_index.html)
├── CNAME                           # GitHub Pages custom domain
├── images/                         # Landing page screenshots (from landing/images/)
│   └── screenshots/
│       ├── dual_panel_list_and_thumbnails.png
│       └── ... (33 screenshots)
├── en/                             # English Landing Page
│   └── index.html
├── zh/                             # Simplified Chinese Landing Page
│   └── index.html
├── zh-hant/ ... ja/ ... de/ ...    # Remaining 9 language Landing Pages
└── guide/                          # Documentation guides (compiled by Zensical)
    ├── en/                         # English User Guide
    ├── zh/                         # Simplified Chinese User Guide
    └── (9 other languages)...
```

---

## 3. Landing Page Templating & i18n Architecture

### 3.1 Source Directory Layout (`landing/`)

```
landing/
├── template.html                   # Master HTML template (styles, layout, DOM, Lightbox, scripts)
├── images/                         # Screenshot assets
│   └── screenshots/*.png
├── i18n/                           # Localized translation dictionaries
│   ├── en.json                     # English master copy
│   ├── zh.json                     # Simplified Chinese master copy
│   ├── zh-hant.json                # Traditional Chinese
│   ├── ja.json                     # Japanese
│   ├── de.json                     # German
│   ├── fr.json                     # French
│   ├── es.json                     # Spanish
│   ├── pt.json                     # Portuguese
│   ├── ko.json                     # Korean
│   ├── ru.json                     # Russian
│   └── it.json                     # Italian
└── {lang}/                         # Optional mirror directory for direct source inspection
```

### 3.2 Master Template Design (`landing/template.html`)

1. **Asset Path Normalization**:
   - Convert all screenshot references from relative `images/screenshots/...` to absolute `/images/screenshots/...`.
2. **Top Navigation & Language Switcher**:
   - Modern glassmorphic header bar matching the User Guide's design language.
   - Includes:
     - ATBCmder brand logo with macOS Native badge.
     - Anchor navigation items: `#dual-panel`, `#universal-preview`, `#remote-vfs`, `#system-tools`, `#instant-search`.
     - Mac App Store direct download button.
     - Localized "User Guide" button pointing to `/guide/{lang}/`.
     - Contact link (`mailto:cmder@aitobox.com`).
     - **Language Switcher Dropdown**:
       - Displays the current language's native name and a globe icon.
       - Expanding the dropdown reveals all 11 supported languages.
       - Selecting a language updates `localStorage.setItem('preferred_language', code)` and redirects to `/{code}/`.
3. **Core Workflow Sections**:
   - Hero section with dual-panel showcase.
   - 5 workflow tabs with real-time image swapping:
     - Dual-Panel File Management
     - Universal File Viewer (30+ formats)
     - Remote VFS & Cloud Connections (SMB, SFTP, FTP)
     - Deep System & Disk Maintenance Tools
     - Instant File & Semantic Search
   - Hardware & System Specification Matrix (Apple Silicon, macOS 12-15+, Sandboxing, Dual Hotkey Paradigm).
   - High-contrast conversion banner and footer.

### 3.3 Translation Dictionaries (`landing/i18n/*.json`)

Every language JSON file maps exact keys for all headings, descriptions, badge highlights, button labels, and tab names. Translations adhere strictly to established macOS localized terminology:
- English: Finder, Apple Silicon, Dual-panel, Tab switcher, Quick View
- Simplified Chinese: 访达, 视网膜, 双面板, 穿透模式, 快速预览
- Traditional Chinese: 訪達, 雙欄, 穿透模式, 快速預覽
- Japanese: デュアルパネル, クイックプレビュー, フラット表示
- German, French, Spanish, Portuguese, Korean, Russian, Italian: High-standard localized terms.

---

## 4. Zensical & Guide Migration Architecture

### 4.1 Zensical Configuration Synchronization (`scripts/generate_configs.py`)

1. **`site_dir`**: Updated from `site/{code}` to `site/guide/{code}`.
2. **`site_url`**: Updated from `https://cmder.aitobox.com/{code}/` to `https://cmder.aitobox.com/guide/{code}/`.
3. **`extra.homepage`**: Configured as `/{code}/` so clicking the top logo returns to that language's landing page.
4. **Alternate Links (`build_alternate_list`)**: Updated links to `/guide/{code}/`.
5. Run `python3 scripts/generate_configs.py` to regenerate all 11 `zensical.<lang>.toml` files.

### 4.2 Theme Overrides (`overrides/`)

1. **`overrides/partials/source.html`**:
   - Update multi-language switcher links from `/{lang}/{{ page.url }}` to `/guide/{lang}/{{ page.url }}`.
2. **`overrides/partials/header.html`**:
   - Preserve Mac App Store and Product Hunt badges.
   - Logo navigation connects to `config.extra.homepage` (`/{lang}/`).

### 4.3 Client-Side Language Detector (`javascripts/language-detector.js`)

1. Update `getCurrentPageLang(pathname)`:
   - Accurately parse language code whether under `/guide/{lang}/...` or `/{lang}/...`.
2. Update `replaceLangInPath(pathname, fromLang, toLang)`:
   - Correctly swap language prefixes while preserving `/guide/` (e.g., `/guide/en/power_tools/` -> `/guide/de/power_tools/`).
3. Ensure internal navigation protection respects switching between Landing and Guide without unexpected redirect loops.

---

## 5. Build Pipeline & Tooling

### 5.1 Landing Builder Script (`scripts/build_landing.py`)

- Reads `landing/template.html` and `landing/i18n/{lang}.json` for each language defined in `scripts/languages.py`.
- Injects localized strings, SEO `<title>`, `<meta description>`, OpenGraph tags, canonical link, and language switcher DOM.
- Writes compiled HTML files to `site/{lang}/index.html`.
- Recursively copies `landing/images/` to `site/images/`.

### 5.2 Local Preview Script (`test.sh`)

1. Step 1: Pre-build checks (Markdown lists formatting and config validation).
2. Step 2: Build Guide documentation for all 11 languages via Zensical (`site/guide/{lang}/`).
3. Step 3: Run `python3 scripts/build_landing.py` to compile landing pages (`site/{lang}/`).
4. Step 4: Copy `root_index.html` to `site/index.html` and `CNAME` to `site/CNAME`.
5. Step 5: Start preview server with comprehensive CLI status output:
   - Root URL: `http://localhost:8000/` (Redirects to landing)
   - Landing Pages: `http://localhost:8000/zh/`, `http://localhost:8000/en/`, etc.
   - User Guides: `http://localhost:8000/guide/zh/`, `http://localhost:8000/guide/en/`, etc.

### 5.3 CI/CD GitHub Actions (`.github/workflows/deploy.yml`)

Add `python3 scripts/build_landing.py` into the deployment pipeline immediately following the Zensical documentation build.

---

## 6. Verification & Quality Assurance

1. **Unit Tests**:
   - `node scripts/test_language_detector.js`: Verify path parsing and language replacement for `/guide/{lang}/` and `/{lang}/`.
2. **Configuration Integrity**:
   - `python3 scripts/generate_configs.py --check`: Ensure all 11 `zensical.<lang>.toml` match specifications with zero drift.
3. **Build Execution**:
   - `./test.sh -b`: Static compilation passes with 0 errors across all 11 landing pages and 11 guide sites.
4. **Navigation Flow Checks**:
   - Root `/` detects browser locale and lands on `/{lang}/`.
   - Landing page "User Guide" links lead to `/guide/{lang}/`.
   - Guide page ATBCmder logo returns to `/{lang}/`.
   - Language switchers on both Landing and Guide properly switch language while staying in context.
