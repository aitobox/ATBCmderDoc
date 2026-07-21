# AGENTS.md — Agent & Developer Guide for ATBCmder Documentation

Welcome to **ATBCmderDoc**, the official repository for the ATBCmder documentation website. This document provides an overview of the project background, architecture, documentation setup, build workflows, and contribution guidelines for AI agents and developers working on this codebase.

---

## 1. Project Overview

- **Product Name:** ATBCmder — The Ultimate Keyboard-Driven File Manager for macOS
- **Repository:** [`aitobox/ATBCmderDoc`](https://github.com/aitobox/ATBCmderDoc)
- **Live Documentation Domain:** [https://cmder.aitobox.com](https://cmder.aitobox.com)
- **Mac App Store URL:** [https://apps.apple.com/app/atbcmder/6792398333](https://apps.apple.com/app/atbcmder/6792398333)

### About ATBCmder
ATBCmder resurrects the classic dual-panel file management paradigm and supercharges it for macOS. Designed for software engineers, system administrators, and Vim enthusiasts, it enables a mouse-free, keyboard-native workflow with high efficiency and performance.

### Core Product Features
1. **100% Keyboard-Native Workflow:** Complete file operations (navigate, copy, move, delete, batch rename) using hotkeys.
2. **Local AI Semantic Search:** Privacy-first, on-device AI natural language search without cloud API dependencies.
3. **Instant Quick Search:** Type-ahead filtering on active panel to lock cursor onto target files instantly.
4. **Branch View (Flat Directory):** Flattens deeply nested folder hierarchies into a single unified list.
5. **Built-In Geek PDF Reader:** Distraction-free, high-speed PDF reading with Vim keybindings (`j`/`k`).
6. **Asynchronous I/O Queue:** Background task management for heavy file transfers without UI freezing.

---

## 2. Documentation Architecture & Bilingual Setup

The documentation is published as a static website hosted on GitHub Pages with full bilingual support (**English** and **Simplified Chinese**).

### Site Structure & URL Layout
- **Root URL (`/`):** Redirects automatically via `root_index.html` (meta-refresh) to `/en/`.
- **English Documentation (`/en/`):** Primary language output.
- **Chinese Documentation (`/zh/`):** Simplified Chinese output.

### Folder Structure
```
ATBCmderDoc/
├── docs/
│   ├── en/                       # English documentation source files
│   │   ├── index.md              # Welcome to ATBCmder
│   │   ├── getting_started.md    # Getting Started with ATBCmder
│   │   ├── navigation.md         # Navigation Guide
│   │   ├── file_management.md    # File Management Guide
│   │   ├── advanced_features.md  # Advanced Features (For Power Users)
│   │   ├── faq_howtos.md         # How-To Guides & FAQ
│   │   └── privacy_policy.md     # Privacy Policy
│   ├── zh/                       # Chinese documentation source files
│   │   ├── index.md              # 欢迎使用 ATBCmder
│   │   ├── getting_started.md    # 快速入门
│   │   ├── navigation.md         # 导航指南
│   │   ├── file_management.md    # 文件管理指南
│   │   ├── advanced_features.md  # 高级功能（面向进阶用户）
│   │   ├── faq_howtos.md         # 操作指南与常见问题
│   │   └── privacy_policy.md     # 隐私政策
│   ├── images/                   # Shared screenshot assets
│   ├── stylesheets/              # Shared custom CSS (extra.css)
│   └── superpowers/              # Design specs & implementation plans
│       ├── specs/                # Architectural spec files
│       └── plans/                # Execution plan files
├── overrides/                    # Jinja2 theme overrides for Material header/partials
│   ├── main.html                 # Layout extension script hooks
│   └── partials/
│       ├── header.html           # Header bar with Mac App Store link
│       └── source.html           # Header items: Contact email, Forum link, EN/ZH Switcher
├── site/                         # Build output directory (generated, ignored by git)
│   ├── index.html                # Copied from root_index.html
│   ├── CNAME                     # Custom domain definition
│   ├── en/                       # Built HTML for English site
│   └── zh/                       # Built HTML for Chinese site
├── .github/
│   └── workflows/
│       └── deploy.yml            # CI/CD deployment pipeline for GitHub Pages
├── CNAME                         # Domain file: cmder.aitobox.com
├── Readme.md                     # Project overview and repository summary
├── root_index.html               # 0-second redirect template for root URL
├── zensical.en.toml              # Zensical config for English site
└── zensical.zh.toml              # Zensical config for Chinese site
```

---

## 3. Technology Stack & Tooling

- **Static Site Generator:** [Zensical](https://github.com/zensical) (MkDocs Material theme compatible engine).
- **Configuration Format:** TOML (`zensical.en.toml`, `zensical.zh.toml`).
- **Styling:** Material theme with custom overrides in `overrides/` and custom styles in `docs/stylesheets/extra.css`.
- **Hosting / CI/CD:** GitHub Pages deployed automatically via GitHub Actions (`.github/workflows/deploy.yml`).

---

## 4. Key Customizations

### 1. Bilingual Language Switcher (`overrides/partials/source.html`)
- Header includes a dynamic language switcher button:
  - On `/en/` pages, displays a `中文` button linking to the corresponding `/zh/` page.
  - On `/zh/` pages, displays an `English` button linking to the corresponding `/en/` page.
- Also includes header links for **Contact** (`mailto:aitoboxinc@gmail.com`) and **Forum** (GitHub Discussions).

### 2. Mac App Store Button (`overrides/partials/header.html`)
- Displays a dedicated Mac App Store button in the top navigation bar linking to the ATBCmder app listing.

### 3. Root Redirection (`root_index.html`)
- Built into `site/index.html` during CI/CD to handle root traffic redirecting to `/en/`.

---

## 5. Development & Build Commands

### Prerequisites
- Python 3.12+
- Zensical installed (`pip install zensical`)

### Local Server & Live Preview
Run local development server for testing documentation changes:

- **Preview English Site:**
  ```bash
  zensical serve -f zensical.en.toml
  ```
- **Preview Chinese Site:**
  ```bash
  zensical serve -f zensical.zh.toml
  ```

### Local Build Execution
To build static assets locally:

- **Build English Documentation:**
  ```bash
  zensical build -f zensical.en.toml
  ```
- **Build Chinese Documentation:**
  ```bash
  zensical build -f zensical.zh.toml
  ```

---

## 6. Guidelines for AI Agents & Contributors

When working on this repository, ensure compliance with the following rules:

1. **Content Parity:**
   Always maintain 1:1 page and structural parity between `docs/en/` and `docs/zh/`. If adding, editing, or reordering sections in English docs, apply equivalent changes to Chinese docs.

2. **Preserve Overrides & Header UI:**
   Do not overwrite or remove custom partials in `overrides/partials/header.html` or `overrides/partials/source.html` unless explicitly updating top navigation header elements.

3. **Verify Build Output:**
   Always run `zensical build` on both configuration files (`zensical.en.toml` and `zensical.zh.toml`) to ensure no broken links or template syntax errors before submitting PRs or finalizing tasks.

4. **Target Branch:**
   Follow repository workflow conventions (commit to feature branches or target branch as configured).
