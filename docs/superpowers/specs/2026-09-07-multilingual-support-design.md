# Design Spec: Comprehensive Multilingual Support (11 Languages) for ATBCmder Documentation

**Date:** 2026-09-07  
**Status:** Approved  
**Target Domain:** `https://cmder.aitobox.com`  
**Base Benchmark:** English (`docs/en/`)

---

## 1. Executive Summary & Goals

ATBCmder is a keyboard-driven, dual-panel file manager for macOS designed for software engineers, power users, and system administrators worldwide. While the initial documentation provided bilingual support for English (`en`) and Simplified Chinese (`zh`), global demand requires localized documentation across key international macOS and developer markets.

This specification outlines the architecture, metadata modeling, UI components, routing mechanisms, build pipelines, and translation verification systems to support **11 languages** simultaneously with 1:1 documentation parity.

### Supported Language Roster

| Language Code (`<lang>`) | Native Display Name | English Name | Target Market / Locale Focus | URL Path |
| :--- | :--- | :--- | :--- | :--- |
| `en` | English | English | Global Default / Primary Reference | `/en/` |
| `zh` | 简体中文 | Simplified Chinese | Mainland China, Singapore | `/zh/` |
| `zh-hant` | 繁體中文 | Traditional Chinese | Taiwan, Hong Kong, Macao, Overseas Chinese | `/zh-hant/` |
| `ja` | 日本語 | Japanese | Japan (High macOS & Vim penetration) | `/ja/` |
| `de` | Deutsch | German | Germany, Austria, Switzerland | `/de/` |
| `fr` | Français | French | France, Canada, Belgium, Francophone regions | `/fr/` |
| `es` | Español | Spanish | Spain, Latin America | `/es/` |
| `pt` | Português | Portuguese | Portugal, Brazil | `/pt/` |
| `ko` | 한국어 | Korean | South Korea | `/ko/` |
| `ru` | Русский | Russian | Eastern Europe, Central Asia | `/ru/` |
| `it` | Italiano | Italian | Italy, Switzerland | `/it/` |

---

## 2. Directory Structure & Documentation Parity

Each language directory under `docs/` must contain the complete set of 12 core documentation chapters, maintaining exact 1:1 file and structural parity with `docs/en/`:

```
ATBCmderDoc/
├── docs/
│   ├── en/                       # English documentation source (Master Benchmark)
│   ├── zh/                       # Simplified Chinese (Existing)
│   ├── zh-hant/                  # Traditional Chinese (12 docs)
│   ├── ja/                       # Japanese (12 docs)
│   ├── de/                       # German (12 docs)
│   ├── fr/                       # French (12 docs)
│   ├── es/                       # Spanish (12 docs)
│   ├── pt/                       # Portuguese (12 docs)
│   ├── ko/                       # Korean (12 docs)
│   ├── ru/                       # Russian (12 docs)
│   ├── it/                       # Italian (12 docs)
│   ├── images/                   # Shared screenshot & diagram assets
│   ├── stylesheets/              # Shared extra.css styles
│   └── javascripts/              # Shared client-side scripts
├── overrides/                    # Jinja2 theme overrides
│   ├── main.html                 # Extra script loading
│   └── partials/
│       ├── header.html           # Header bar with AppStore & Search
│       └── source.html           # Header items: Contact, Forum, Multi-language Dropdown
├── scripts/
│   ├── languages.py              # Single Source of Truth metadata for all 11 languages
│   ├── generate_configs.py       # Synchronizes zensical.<lang>.toml for all languages
│   ├── format_markdown_lists.py  # MD032 list blank line auto-formatter
│   ├── check_parity.py           # Validates 1:1 chapter and image parity
│   └── batch_translate.py        # Automated translation pipeline from docs/en/
├── test.sh                       # Local build, lint, and preview CLI
├── root_index.html               # Language detection redirect for root URL '/'
├── zensical.*.toml               # Individual configs (zensical.en.toml, zensical.ja.toml, ...)
└── .github/workflows/deploy.yml  # Multi-site CI/CD build & Pages deployment
```

### Document Inventory (12 Core Chapters per Language)

1. `index.md` — Welcome & Product Overview
2. `getting_started.md` — Chapter 1: Fundamentals & macOS Setup
3. `navigation_and_tabs.md` — Chapter 2: Navigation & Folder Tabs
4. `file_operations.md` — Chapter 3: Daily File Operations & Background Queue
5. `viewers_and_editors.md` — Chapter 4: Universal Lister & Built-in Editors
6. `power_tools.md` — Chapter 5: Power Tools & Automation
7. `network_and_vfs.md` — Chapter 6: Virtual File Systems & Network
8. `preferences_and_customization.md` — Chapter 7: Preferences & Customization
9. `keyboard_shortcuts.md` — Chapter 8: Master Keyboard Shortcut Reference
10. `faq_howtos.md` — Chapter 9: Real-World Recipes & Troubleshooting
11. `download.md` — Chapter 10: Download & Installation
12. `privacy_policy.md` — Privacy Policy

---

## 3. Metadata & Configuration Management

To prevent configuration drift across 11 languages, `scripts/languages.py` acts as the single source of truth.

### Metadata Schema
```python
LANGUAGES = [
    {
        "code": "en",
        "name": "English",
        "english_name": "English",
        "description": "The Dual-Panel File Manager for macOS",
        "browser_prefixes": ["en"],
        "nav_titles": {
            "index.md": "Welcome to ATBCmder",
            "getting_started.md": "Chapter 1: Fundamentals & macOS Setup",
            # ...
        }
    },
    # 10 other languages defined identically
]
```

### Configuration Synchronizer (`scripts/generate_configs.py`)
- Reads global defaults (Material theme palette, fonts, plugins, search, custom overrides directory `overrides`).
- Emits or verifies `zensical.<lang>.toml` for all 11 languages.
- Configures `alternate` array in each TOML file listing all 11 languages to power Material's i18n metadata.
- Sets appropriate `theme.language` (e.g., `ja`, `de`, `zh`, `en`, `fr`, etc.) for native search stemming and UI labels.

---

## 4. Header UI Language Switcher (`overrides/partials/source.html`)

The previous 2-way toggle link is replaced with an accessible, native-feeling language dropdown menu.

### Structural Design
- **Markup**: Pure semantic HTML using `<details class="atb-lang-dropdown">` and `<summary>` without third-party framework dependencies.
- **Trigger Button**:
  - Global translation SVG icon.
  - Active language's native name (e.g. `日本語`, `Deutsch`, `English`).
  - Dropdown chevron indicator SVG.
- **Dropdown List**:
  - Popover card styled with Material surface elevation, rounded corners (`8px`), and theme-aware borders.
  - Displays all 11 languages in their native script.
  - Active language highlighted with distinct background and checkmark.
  - Preserves current page path: `/en/file_operations/` -> `/ja/file_operations/`.
  - Attaches click listener writing `localStorage.setItem('preferred_language', '<lang>')`.
- **Responsive Handling**:
  - Desktop: Positioned neatly between Forum link and Search bar.
  - Mobile: Gracefully shrinks text or shows icon-only on narrow viewports to avoid overlapping App Store and search triggers.
  - Dark Mode: Uses Material's `--md-default-bg-color` and `--md-shadow-z2` variables for seamless theme harmony.

---

## 5. Client-Side Routing & Language Detection

### Browser Language Matching Table (`language-detector.js` & `root_index.html`)

When a user visits the root `/` or enters without explicit language selection:

```javascript
const LANG_PREFIX_MAP = [
  { prefix: 'zh-tw', code: 'zh-hant' },
  { prefix: 'zh-hk', code: 'zh-hant' },
  { prefix: 'zh-mo', code: 'zh-hant' },
  { prefix: 'zh-hant', code: 'zh-hant' },
  { prefix: 'zh', code: 'zh' },
  { prefix: 'ja', code: 'ja' },
  { prefix: 'de', code: 'de' },
  { prefix: 'fr', code: 'fr' },
  { prefix: 'es', code: 'es' },
  { prefix: 'pt', code: 'pt' },
  { prefix: 'ko', code: 'ko' },
  { prefix: 'ru', code: 'ru' },
  { prefix: 'it', code: 'it' }
];
// Fallback: 'en'
```

### Routing Rules
1. **Query Parameter (`?lang=<code>`)**: Explicitly overrides and stores preference.
2. **Local Storage (`preferred_language`)**: If present and valid, routes user to their chosen language.
3. **Internal Navigation Protection**: If `document.referrer` is on the same host, the user's current browsing language is preserved and written to preference.
4. **Browser Language Detection**: Evaluates `navigator.languages` against the matching table.
5. **Default Fallback**: Routes to English (`/en/`).
6. **Path Preservation**: If a user is on `/<lang1>/power_tools/` and switches to `<lang2>`, the URL resolves directly to `/<lang2>/power_tools/`.

---

## 6. Build Pipeline & Developer Tooling

### `test.sh` Capabilities
1. `./test.sh`
   - Checks MD032 list blank line formatting.
   - Compiles all 11 language sites into `site/<lang>/`.
   - Copies `root_index.html` -> `site/index.html` and `CNAME` -> `site/CNAME`.
   - Starts local multi-language preview HTTP server and opens browser.
2. `./test.sh -b` (`--build-only`): Compiles all 11 static sites without running a server.
3. `./test.sh -s <lang>`: Launches `zensical serve -f zensical.<lang>.toml` for instant single-language live reloading during editing.
4. `./test.sh -l` (`--lint`): Verifies Markdown list blank lines across all `docs/*/*.md`.
5. `./test.sh --fix-lists`: Automatically fixes list blank spacing in place.
6. `./test.sh --check-parity`: Verifies all 12 core files exist across all 11 language folders and checks image link parity.

### CI/CD Deployment (`.github/workflows/deploy.yml`)
- Triggered on `push` to `main`.
- Sets up Python 3.12, installs Zensical.
- Runs list spacing check and config synchronization check.
- Builds all 11 language sites via loop.
- Sets up Pages artifact and deploys to GitHub Pages (`https://cmder.aitobox.com`).

---

## 7. Content Translation Standards & Parity Assurance

### Preservation Invariants
1. **Asset Paths**: All relative image references (`images/...` or `../images/...`) remain unchanged.
2. **Keybindings**: All `<kbd>` elements, symbol sequences (`<kbd>⌘</kbd><kbd>C</kbd>`), and function keys (`<kbd>F1</kbd>`-`<kbd>F10</kbd>`) are strictly preserved.
3. **Code Blocks & Config**: Commands (`brew install ...`), TOML keys, and directory paths (`~/.config/atbcmder/`) remain untranslated.
4. **Markdown List Blank Spacing (MD032)**: Every list item block must have an empty line preceding it to prevent Python-Markdown inline collapse.

### Terminology Alignment
Each language adheres to standard Apple macOS localized terminology:
- `ja`: Finder, クイックルック (Quick Look), ショートカット (Shortcuts), ゴミ箱 (Trash), メニューバー (Menu bar).
- `zh-hant`: 檔案管理員, 快速預覽 (Quick Look), 快速鍵, 終端機, 偏好設定.
- `de`: Finder, Schnellübersicht (Quick Look), Tastaturkurzbefehle, Papierkorb.
- `fr`: Finder, Coup d'œil (Quick Look), Raccourcis clavier, Corbeille.
- `es`: Finder, Vista rápida (Quick Look), Atajos de teclado, Papelera.
- `pt`: Finder, Visualização Rápida (Quick Look), Atalhos de teclado, Lixeira.
- `ko`: Finder, 훑어보기 (Quick Look), 단축키, 휴지통, 시스템 설정.
- `ru`: Finder, Быстрый просмотр (Quick Look), Сочетания клавиш, Корзина.
- `it`: Finder, Visualizzazione rapida (Quick Look), Scorciatoie da tastiera, Cestino.

---

## 8. Rollout Plan

- **Phase 1**: Implement metadata source (`scripts/languages.py`), config generator (`scripts/generate_configs.py`), header dropdown UI (`overrides/partials/source.html`, CSS), and routing detection (`language-detector.js`, `root_index.html`).
- **Phase 2**: Upgrade `test.sh`, `scripts/format_markdown_lists.py`, `scripts/check_parity.py`, and `.github/workflows/deploy.yml`.
- **Phase 3**: Batch translate and verify all 9 new languages (108 documentation files) from `docs/en/` master copy.
- **Phase 4**: Full build verification (`./test.sh -b`), lint check (`./test.sh -l`), parity check (`./test.sh --check-parity`), and local preview testing.
