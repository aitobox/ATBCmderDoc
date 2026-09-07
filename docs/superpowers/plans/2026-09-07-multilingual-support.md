# Multilingual Support (11 Languages) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand ATBCmder documentation from bilingual (EN/ZH) to 11 languages (`en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`) with 1:1 documentation parity, a native header dropdown switcher, intelligent browser language routing, and automated multi-site build workflows.

**Architecture:** A metadata-driven i18n system where `scripts/languages.py` serves as the single source of truth for all 11 languages. A Python generator synchronizes `zensical.<lang>.toml` to eliminate config drift. A semantic `<details>` dropdown in `overrides/partials/source.html` enables smooth language switching while preserving page subpaths. Updated `test.sh` and CI/CD compile and verify all 11 documentation sites.

**Tech Stack:** Python 3.12, Zensical (MkDocs Material engine), Vanilla HTML5/CSS3 (Material Theme Overrides), Vanilla JavaScript, Bash, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-09-07-multilingual-support-design.md`

## Global Constraints

- Must activate conda environment: `conda activate ATBCmderDoc` before executing commands.
- 1:1 documentation structure parity across all language folders (`docs/<lang>/` must have the exact same 12 core files).
- MD032 compliance: All Markdown list items must be preceded by an empty line in all translated files.
- Asset path invariant: All image links (`images/...` or `../images/...`) and code blocks must remain intact.
- Apple HIG / macOS localization standards: Standard localized macOS terminology for all 11 languages.
- Zero external frontend library dependencies: Pure HTML/CSS/JS for UI switcher and routing.

---

### Task 1: Language Metadata & Config Generator System

**Files:**
- Create: `scripts/languages.py`
- Create: `scripts/generate_configs.py`
- Test: `tests/test_generate_configs.py` or running `python3 scripts/generate_configs.py --check`

**Interfaces:**
- Consumes: `zensical.en.toml` (as the base layout and feature benchmark)
- Produces: `scripts/languages.py` exporting `LANGUAGES` list of dicts with keys: `code`, `name`, `english_name`, `description`, `theme_lang`, `browser_prefixes`, `nav_titles`
- Produces: `zensical.<lang>.toml` for all 11 languages (`en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`)

- [ ] **Step 1: Create language metadata single source of truth**

Write `scripts/languages.py` defining all 11 languages and their chapter title translations:

```python
"""
scripts/languages.py
Single Source of Truth for ATBCmder Documentation i18n metadata.
"""

LANGUAGES = [
    {
        "code": "en",
        "name": "English",
        "english_name": "English",
        "description": "The Dual-Panel File Manager for macOS",
        "theme_lang": "en",
        "browser_prefixes": ["en"],
        "nav_titles": {
            "index.md": "Welcome to ATBCmder",
            "getting_started.md": "Chapter 1: Fundamentals & macOS Setup",
            "navigation_and_tabs.md": "Chapter 2: Navigation & Folder Tabs",
            "file_operations.md": "Chapter 3: Daily File Operations & Background Queue",
            "viewers_and_editors.md": "Chapter 4: Universal Lister & Built-in Editors",
            "power_tools.md": "Chapter 5: Power Tools & Automation",
            "network_and_vfs.md": "Chapter 6: Virtual File Systems & Network",
            "preferences_and_customization.md": "Chapter 7: Preferences & Customization",
            "keyboard_shortcuts.md": "Chapter 8: Master Keyboard Shortcut Reference",
            "faq_howtos.md": "Chapter 9: Real-World Recipes & Troubleshooting",
            "download.md": "Chapter 10: Download & Installation",
            "privacy_policy.md": "Privacy Policy"
        }
    },
    {
        "code": "zh",
        "name": "简体中文",
        "english_name": "Simplified Chinese",
        "description": "macOS 双栏文件管理器与键盘流效率工具",
        "theme_lang": "zh",
        "browser_prefixes": ["zh-cn", "zh-sg", "zh-hans", "zh"],
        "nav_titles": {
            "index.md": "欢迎使用 ATBCmder",
            "getting_started.md": "第 1 章：基础概念与 macOS 系统配置",
            "navigation_and_tabs.md": "第 2 章：极速导航与多标签工作区",
            "file_operations.md": "第 3 章：日常文件操作与后台异步队列",
            "viewers_and_editors.md": "第 4 章：全能万用查看器与内置编辑器",
            "power_tools.md": "第 5 章：高阶生产力工具与自动化",
            "network_and_vfs.md": "第 6 章：虚拟文件系统与网络互联",
            "preferences_and_customization.md": "第 7 章：偏好设置与深度个性化定制",
            "keyboard_shortcuts.md": "第 8 章：终极快捷键全书",
            "faq_howtos.md": "第 9 章：实战场景解决方案与故障排查",
            "download.md": "第 10 章：软件下载与安装指南",
            "privacy_policy.md": "隐私政策"
        }
    },
    {
        "code": "zh-hant",
        "name": "繁體中文",
        "english_name": "Traditional Chinese",
        "description": "macOS 雙欄檔案管理器與鍵盤流效率工具",
        "theme_lang": "zh-TW",
        "browser_prefixes": ["zh-tw", "zh-hk", "zh-mo", "zh-hant"],
        "nav_titles": {
            "index.md": "歡迎使用 ATBCmder",
            "getting_started.md": "第 1 章：基礎概念與 macOS 系統配置",
            "navigation_and_tabs.md": "第 2 章：極速導覽與多分頁工作區",
            "file_operations.md": "第 3 章：日常檔案操作與後台異步隊列",
            "viewers_and_editors.md": "第 4 章：全能萬用檢視器與內建編輯器",
            "power_tools.md": "第 5 章：進階生產力工具與自動化",
            "network_and_vfs.md": "第 6 章：虛擬檔案系統與網路互連",
            "preferences_and_customization.md": "第 7 章：偏好設定與深度個性化自訂",
            "keyboard_shortcuts.md": "第 8 章：終極快速鍵全書",
            "faq_howtos.md": "第 9 章：實戰場景解決方案與疑難排解",
            "download.md": "第 10 章：軟體下載與安裝指南",
            "privacy_policy.md": "隱私政策"
        }
    },
    {
        "code": "ja",
        "name": "日本語",
        "english_name": "Japanese",
        "description": "macOS向けデュアルパネル・ファイルマネージャー",
        "theme_lang": "ja",
        "browser_prefixes": ["ja"],
        "nav_titles": {
            "index.md": "ATBCmder へようこそ",
            "getting_started.md": "第1章：基本概念と macOS の初期設定",
            "navigation_and_tabs.md": "第2章：高速ナビゲーションとフォルダータブ",
            "file_operations.md": "第3章：日常のファイル操作と非同期バックグラウンドキュー",
            "viewers_and_editors.md": "第4章：万能ビューアーと内蔵エディター",
            "power_tools.md": "第5章：高度なツールと自動化",
            "network_and_vfs.md": "第6章：仮想ファイルシステムとネットワーク",
            "preferences_and_customization.md": "第7章：環境設定とカスタマイズ",
            "keyboard_shortcuts.md": "第8章：マスターキーボードショートカット一覧",
            "faq_howtos.md": "第9章：実践レシピとトラブルシューティング",
            "download.md": "第10章：ダウンロードとインストール",
            "privacy_policy.md": "プライバシーポリシー"
        }
    },
    {
        "code": "de",
        "name": "Deutsch",
        "english_name": "German",
        "description": "Der Zwei-Fenster-Dateimanager für macOS",
        "theme_lang": "de",
        "browser_prefixes": ["de"],
        "nav_titles": {
            "index.md": "Willkommen bei ATBCmder",
            "getting_started.md": "Kapitel 1: Grundlagen & macOS-Einrichtung",
            "navigation_and_tabs.md": "Kapitel 2: Navigation & Ordner-Tabs",
            "file_operations.md": "Kapitel 3: Dateioperationen & Hintergrundwarteschlange",
            "viewers_and_editors.md": "Kapitel 4: Universeller Betrachter & Editoren",
            "power_tools.md": "Kapitel 5: Power-Tools & Automatisierung",
            "network_and_vfs.md": "Kapitel 6: Virtuelle Dateisysteme & Netzwerk",
            "preferences_and_customization.md": "Kapitel 7: Einstellungen & Anpassung",
            "keyboard_shortcuts.md": "Kapitel 8: Tastaturkurzbefehle-Referenz",
            "faq_howtos.md": "Kapitel 9: Praxislösungen & Fehlerbehebung",
            "download.md": "Kapitel 10: Download & Installation",
            "privacy_policy.md": "Datenschutzerklärung"
        }
    },
    {
        "code": "fr",
        "name": "Français",
        "english_name": "French",
        "description": "Le gestionnaire de fichiers à double panneau pour macOS",
        "theme_lang": "fr",
        "browser_prefixes": ["fr"],
        "nav_titles": {
            "index.md": "Bienvenue sur ATBCmder",
            "getting_started.md": "Chapitre 1: Notions de base et configuration macOS",
            "navigation_and_tabs.md": "Chapitre 2: Navigation et onglets de dossiers",
            "file_operations.md": "Chapitre 3: Opérations de fichiers et file d'attente en arrière-plan",
            "viewers_and_editors.md": "Chapitre 4: Visionneuse universelle et éditeurs intégrés",
            "power_tools.md": "Chapitre 5: Outils avancés et automatisation",
            "network_and_vfs.md": "Chapitre 6: Systèmes de fichiers virtuels et réseau",
            "preferences_and_customization.md": "Chapitre 7: Préférences et personnalisation",
            "keyboard_shortcuts.md": "Chapitre 8: Répertoire principal des raccourcis clavier",
            "faq_howtos.md": "Chapitre 9: Recettes pratiques et dépannage",
            "download.md": "Chapitre 10: Téléchargement et installation",
            "privacy_policy.md": "Politique de confidentialité"
        }
    },
    {
        "code": "es",
        "name": "Español",
        "english_name": "Spanish",
        "description": "El administrador de archivos de doble panel para macOS",
        "theme_lang": "es",
        "browser_prefixes": ["es"],
        "nav_titles": {
            "index.md": "Bienvenido a ATBCmder",
            "getting_started.md": "Capítulo 1: Fundamentos y configuración de macOS",
            "navigation_and_tabs.md": "Capítulo 2: Navegación y pestañas de carpetas",
            "file_operations.md": "Capítulo 3: Operaciones de archivos y cola en segundo plano",
            "viewers_and_editors.md": "Capítulo 4: Visor universal y editores integrados",
            "power_tools.md": "Capítulo 5: Herramientas avanzadas y automatización",
            "network_and_vfs.md": "Capítulo 6: Sistemas de archivos virtuales y red",
            "preferences_and_customization.md": "Capítulo 7: Preferencias y personalización",
            "keyboard_shortcuts.md": "Capítulo 8: Referencia maestra de atajos de teclado",
            "faq_howtos.md": "Capítulo 9: Soluciones prácticas y resolución de problemas",
            "download.md": "Capítulo 10: Descarga e instalación",
            "privacy_policy.md": "Política de privacidad"
        }
    },
    {
        "code": "pt",
        "name": "Português",
        "english_name": "Portuguese",
        "description": "O gerenciador de arquivos de painel duplo para macOS",
        "theme_lang": "pt",
        "browser_prefixes": ["pt", "pt-br", "pt-pt"],
        "nav_titles": {
            "index.md": "Bem-vindo ao ATBCmder",
            "getting_started.md": "Capítulo 1: Fundamentos e configuração do macOS",
            "navigation_and_tabs.md": "Capítulo 2: Navegação e abas de pastas",
            "file_operations.md": "Capítulo 3: Operações de arquivos e fila em segundo plano",
            "viewers_and_editors.md": "Capítulo 4: Visualizador universal e editores integrados",
            "power_tools.md": "Capítulo 5: Ferramentas avançadas e automação",
            "network_and_vfs.md": "Capítulo 6: Sistemas de arquivos virtuais e rede",
            "preferences_and_customization.md": "Capítulo 7: Preferências e personalização",
            "keyboard_shortcuts.md": "Capítulo 8: Referência mestre de atalhos de teclado",
            "faq_howtos.md": "Capítulo 9: Receitas práticas e solução de problemas",
            "download.md": "Capítulo 10: Download e instalação",
            "privacy_policy.md": "Política de privacidade"
        }
    },
    {
        "code": "ko",
        "name": "한국어",
        "english_name": "Korean",
        "description": "macOS용 듀얼 패널 파일 관리자",
        "theme_lang": "ko",
        "browser_prefixes": ["ko"],
        "nav_titles": {
            "index.md": "ATBCmder 에 오신 것을 환영합니다",
            "getting_started.md": "제1장: 기본 개념 및 macOS 설정",
            "navigation_and_tabs.md": "제2장: 내비게이션 및 폴더 탭",
            "file_operations.md": "제3장: 일상 파일 작업 및 백그라운드 큐",
            "viewers_and_editors.md": "제4장: 만능 뷰어 및 내장 편집기",
            "power_tools.md": "제5장: 고급 도구 및 자동화",
            "network_and_vfs.md": "제6장: 가상 파일 시스템 및 네트워크",
            "preferences_and_customization.md": "제7장: 환경설정 및 사용자 정의",
            "keyboard_shortcuts.md": "제8장: 마스터 키보드 단축키 레퍼런스",
            "faq_howtos.md": "제9장: 실전 문제 해결 및 레시피",
            "download.md": "제10장: 다운로드 및 설치 가이드",
            "privacy_policy.md": "개인정보 처리방침"
        }
    },
    {
        "code": "ru",
        "name": "Русский",
        "english_name": "Russian",
        "description": "Двухпанельный файловый менеджер для macOS",
        "theme_lang": "ru",
        "browser_prefixes": ["ru"],
        "nav_titles": {
            "index.md": "Добро пожаловать в ATBCmder",
            "getting_started.md": "Глава 1: Основные концепции и настройка macOS",
            "navigation_and_tabs.md": "Глава 2: Навигация и вкладки папок",
            "file_operations.md": "Глава 3: Операции с файлами и фоновая очередь",
            "viewers_and_editors.md": "Глава 4: Универсальный просмотрщик и редакторы",
            "power_tools.md": "Глава 5: Инструменты продуктивности и автоматизация",
            "network_and_vfs.md": "Глава 6: Виртуальные файловые системы и сеть",
            "preferences_and_customization.md": "Глава 7: Настройки и персонализация",
            "keyboard_shortcuts.md": "Глава 8: Справочник горячих клавиш",
            "faq_howtos.md": "Глава 9: Практические рецепты и устранение неполадок",
            "download.md": "Глава 10: Скачивание и установка",
            "privacy_policy.md": "Политика конфиденциальности"
        }
    },
    {
        "code": "it",
        "name": "Italiano",
        "english_name": "Italian",
        "description": "Il file manager a doppio pannello per macOS",
        "theme_lang": "it",
        "browser_prefixes": ["it"],
        "nav_titles": {
            "index.md": "Benvenuto in ATBCmder",
            "getting_started.md": "Capitolo 1: Concetti fondamentali e configurazione di macOS",
            "navigation_and_tabs.md": "Capitolo 2: Navigazione e schede delle cartelle",
            "file_operations.md": "Capitolo 3: Operazioni quotidiane sui file e coda in background",
            "viewers_and_editors.md": "Capitolo 4: Visualizzatore universale ed editor integrati",
            "power_tools.md": "Capitolo 5: Strumenti avanzati e automazione",
            "network_and_vfs.md": "Capitolo 6: File system virtuali e rete",
            "preferences_and_customization.md": "Capitolo 7: Preferenze e personalizzazione",
            "keyboard_shortcuts.md": "Capitolo 8: Guida rapida alle scorciatoie da tastiera",
            "faq_howtos.md": "Capitolo 9: Ricette pratiche e risoluzione dei problemi",
            "download.md": "Capitolo 10: Download e installazione",
            "privacy_policy.md": "Informativa sulla privacy"
        }
    }
]
```

- [ ] **Step 2: Create config generation and validation script**

Write `scripts/generate_configs.py` that generates `zensical.<lang>.toml` for all 11 languages, maintaining complete theme, palette, and plugin parity, with `--check` mode for CI verification.

- [ ] **Step 3: Run config generation and verify output**

Run: `python3 scripts/generate_configs.py`
Expected: Generates/updates 11 files `zensical.*.toml` without error.

- [ ] **Step 4: Commit Task 1**

```bash
git add scripts/languages.py scripts/generate_configs.py zensical.*.toml
git commit -m "feat(i18n): add language metadata and config generation system"
```

---

### Task 2: Top Navigation Dropdown UI & Stylesheet

**Files:**
- Modify: `overrides/partials/source.html`
- Modify: `docs/en/stylesheets/extra.css`
- Modify: `docs/zh/stylesheets/extra.css` (or ensure stylesheet sync)

**Interfaces:**
- Consumes: `page.url`, `config.extra.alternate` or `scripts/languages.py` language list
- Produces: `<details class="atb-lang-dropdown">` element in `.atb-header-actions`

- [ ] **Step 1: Update `overrides/partials/source.html` with dropdown markup**

Replace the 2-way toggle in `overrides/partials/source.html` with:
```jinja2
<div class="atb-header-actions">
  <a href="mailto:cmder@aitobox.com" title="Email Us" class="md-header__button atb-header-action">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M22 6c0-1.1-.9-2-2-2H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6zm-2 0l-8 5-8-5h16zm0 12H4V8l8 5 8-5v10z"/></svg>
    <span>Contact</span>
  </a>
  <a href="https://github.com/aitobox/ATBCmderDoc/discussions" title="Community Forum" class="md-header__button atb-header-action">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12 2C6.48 2 2 5.58 2 10c0 2.53 1.45 4.77 3.65 6.13A8.475 8.475 0 0 1 4 19.5c-.32.74.52 1.44 1.18 1.03 2.1-.87 4.1-2.12 5.76-3.48.35.03.7.05 1.06.05 5.52 0 10-3.58 10-8s-4.48-8-10-8z"/></svg>
    <span>Forum</span>
  </a>

  <details class="atb-lang-dropdown" id="atb-lang-switcher">
    <summary class="md-header__button atb-lang-summary" aria-label="Select Language" title="Select Language">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18" fill="currentColor"><path d="M12.87 15.07l-2.54-2.51.03-.03A17.52 17.52 0 0014.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2.1l1.1-3h4.7l1.1 3h2.1L18.5 10zm-2.62 7l1.62-4.41L19.12 17h-3.24z"/></svg>
      <span class="atb-lang-current" id="atb-lang-current-label">Language</span>
      <svg class="atb-lang-caret" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M7 10l5 5 5-5z"/></svg>
    </summary>
    <div class="atb-lang-menu" role="menu">
      <a href="/en/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="en" role="menuitem">English</a>
      <a href="/zh/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="zh" role="menuitem">简体中文</a>
      <a href="/zh-hant/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="zh-hant" role="menuitem">繁體中文</a>
      <a href="/ja/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="ja" role="menuitem">日本語</a>
      <a href="/de/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="de" role="menuitem">Deutsch</a>
      <a href="/fr/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="fr" role="menuitem">Français</a>
      <a href="/es/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="es" role="menuitem">Español</a>
      <a href="/pt/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="pt" role="menuitem">Português</a>
      <a href="/ko/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="ko" role="menuitem">한국어</a>
      <a href="/ru/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="ru" role="menuitem">Русский</a>
      <a href="/it/{{ page.url if page and page.url else '' }}" class="atb-lang-item" data-lang="it" role="menuitem">Italiano</a>
    </div>
  </details>
</div>
```

- [ ] **Step 2: Add dropdown styles to `extra.css`**

Add styling in `extra.css` for `.atb-lang-dropdown`, `.atb-lang-summary`, `.atb-lang-menu`, and `.atb-lang-item`:
- Floating menu with `position: absolute; right: 0; min-width: 150px; border-radius: 8px;`
- Elevation shadow `box-shadow: 0 4px 20px rgba(0,0,0,0.15);`
- Active item highlight and smooth hover states.
- Dark mode compatibility using Material CSS variables (`--md-default-bg-color`, `--md-typeset-color`).
- Mobile media queries so text doesn't overflow on small screens.

- [ ] **Step 3: Verify dropdown styles in browser build**

- [ ] **Step 4: Commit Task 2**

```bash
git add overrides/partials/source.html docs/*/stylesheets/extra.css
git commit -m "feat(ui): implement 11-language dropdown switcher in header"
```

---

### Task 3: Client-Side Routing & Language Detection

**Files:**
- Modify: `docs/en/javascripts/language-detector.js`
- Modify: `root_index.html`

**Interfaces:**
- Consumes: `window.location.pathname`, `navigator.languages`, `localStorage['preferred_language']`, URL query `?lang=<code>`
- Produces: Accurate redirection to `/<lang>/<path>` preserving deep links

- [ ] **Step 1: Update `docs/en/javascripts/language-detector.js`**

Update the script to support the full 11-language mapping table:
- Map `zh-tw`, `zh-hk`, `zh-mo`, `zh-hant` -> `zh-hant`
- Map `zh-cn`, `zh-sg`, `zh-hans`, `zh` -> `zh`
- Map `ja*` -> `ja`
- Map `de*` -> `de`
- Map `fr*` -> `fr`
- Map `es*` -> `es`
- Map `pt*` -> `pt`
- Map `ko*` -> `ko`
- Map `ru*` -> `ru`
- Map `it*` -> `it`
- Default fallback -> `en`
- Automatically highlight the active language item and update `#atb-lang-current-label` with the native name of the active language.
- Bind click events on `.atb-lang-item` to persist `preferred_language`.
- Close dropdown when clicking outside.

- [ ] **Step 2: Update `root_index.html`**

Update root redirection script to support the exact same 11-language detection priority and instantaneous redirect.

- [ ] **Step 3: Commit Task 3**

```bash
git add docs/*/javascripts/language-detector.js root_index.html
git commit -m "feat(router): add 11-language detection and deep routing"
```

---

### Task 4: Build Script & Parity Linter Enhancements

**Files:**
- Create: `scripts/check_parity.py`
- Modify: `scripts/format_markdown_lists.py`
- Modify: `test.sh`
- Modify: `.github/workflows/deploy.yml`

**Interfaces:**
- Produces:
  - `./test.sh` (builds all 11 languages into `site/`)
  - `./test.sh -b` (build all 11 static sites)
  - `./test.sh -s <lang>` (live preview any of the 11 languages)
  - `./test.sh -l` (lint lists across all 11 docs folders)
  - `./test.sh --fix-lists` (auto fix lists across all docs folders)
  - `./test.sh --check-parity` (verifies file inventory, headings, and images match `docs/en/`)

- [ ] **Step 1: Create `scripts/check_parity.py`**

Write a parity checker that:
- Reads all 12 files in `docs/en/`
- Verifies every file exists in each target language folder `docs/<lang>/`
- Compares markdown headings structure (H1, H2, H3 count)
- Verifies image path references match 1:1

- [ ] **Step 2: Update `scripts/format_markdown_lists.py`**

Ensure recursive traversal scans all language subfolders in `docs/` (`docs/en/`, `docs/zh/`, `docs/ja/`, etc.).

- [ ] **Step 3: Upgrade `test.sh`**

Modify `test.sh`:
- Dynamically detect languages from `scripts/languages.py` (all 11 languages).
- Build each language to `site/<lang>/`.
- Support `./test.sh -s <lang>` for any language (`ja`, `de`, `zh-hant`, `ko`, etc.).
- Support `--check-parity`.
- Print status and URLs for all languages.

- [ ] **Step 4: Update `.github/workflows/deploy.yml`**

Update GitHub Actions workflow to build all 11 sites in a loop or dynamic build step.

- [ ] **Step 5: Commit Task 4**

```bash
git add scripts/check_parity.py scripts/format_markdown_lists.py test.sh .github/workflows/deploy.yml
git commit -m "feat(build): enhance test.sh and CI/CD for 11-language compilation"
```

---

### Task 5: Translation Pipeline & Batch Documentation Generation

**Files:**
- Create: `scripts/batch_translate.py`
- Create folders and 108 files:
  - `docs/zh-hant/` (12 files)
  - `docs/ja/` (12 files)
  - `docs/de/` (12 files)
  - `docs/fr/` (12 files)
  - `docs/es/` (12 files)
  - `docs/pt/` (12 files)
  - `docs/ko/` (12 files)
  - `docs/ru/` (12 files)
  - `docs/it/` (12 files)

**Interfaces:**
- Consumes: 12 source files in `docs/en/*.md`
- Produces: High fidelity localized Markdown files in all 9 new language folders

- [ ] **Step 1: Create translation engine utility `scripts/batch_translate.py`**

Write a translation generation utility that:
- Reads `docs/en/<file>.md`
- Maintains exact code blocks, image URLs, keyboard shortcuts (`<kbd>...</kbd>`), and anchors.
- Applies standard macOS localization terms for `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`.

- [ ] **Step 2: Execute batch generation for all 9 languages**

Generate all 108 Markdown files.

- [ ] **Step 3: Run list formatting and parity checks**

Run:
```bash
python3 scripts/format_markdown_lists.py --fix
python3 scripts/check_parity.py
```
Expected: All 108 files formatted to MD032 list blank line standards; 100% parity reported.

- [ ] **Step 4: Commit Task 5**

```bash
git add docs/
git commit -m "feat(docs): generate 1:1 documentation for 9 new languages (108 docs)"
```

---

### Task 6: Multi-Site Build Verification & End-to-End Testing

**Files:**
- Verify build outputs in `site/`

- [ ] **Step 1: Run complete multi-language compilation**

Run:
```bash
./test.sh -b
```
Expected: All 11 language sites build successfully into `site/en`, `site/zh`, `site/zh-hant`, `site/ja`, `site/de`, `site/fr`, `site/es`, `site/pt`, `site/ko`, `site/ru`, `site/it`.

- [ ] **Step 2: Verify root redirect and CNAME**

Check:
```bash
test -f site/index.html && test -f site/CNAME
```
Expected: `site/index.html` and `site/CNAME` exist.

- [ ] **Step 3: Verify list formatting and parity passes cleanly**

Run:
```bash
./test.sh -l
./test.sh --check-parity
```
Expected: Exit code 0, all checks pass with zero warnings.

- [ ] **Step 4: Final commit and summary**

```bash
git commit --allow-empty -m "chore: complete 11-language documentation implementation"
```
