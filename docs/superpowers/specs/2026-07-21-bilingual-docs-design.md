# Design Spec: Bilingual (English & Chinese) Support for ATBCmder Documentation

**Date:** 2026-07-21  
**Status:** Approved  
**Target Domain:** `https://cmder.aitobox.com`

---

## 1. Overview

This design specification outlines the architecture, directory structure, configuration, and build pipeline required to introduce full bilingual support (English and Simplified Chinese) for the ATBCmder documentation site.

### Key Decisions
- **URL Structure:** Dual independent subpaths `/en/` and `/zh/`.
- **Default Language:** English (`/en/`). Root URL `https://cmder.aitobox.com/` automatically redirects to `/en/`.
- **Scope:** 1:1 parity across all 7 documentation pages in both English and Chinese.

---

## 2. Directory Structure & File Organization

The existing `docs/` folder will be reorganized into `docs/en/` and `docs/zh/`. Shared static assets (images and stylesheets) will remain shared at `docs/images/` and `docs/stylesheets/`.

```
docs/
├── en/
│   ├── index.md                # Welcome to ATBCmder
│   ├── getting_started.md      # Getting Started with ATBCmder
│   ├── navigation.md           # Navigation Guide
│   ├── file_management.md      # File Management Guide
│   ├── advanced_features.md    # Advanced Features (For Power Users)
│   ├── faq_howtos.md           # How-To Guides & FAQ
│   └── privacy_policy.md       # Privacy Policy
├── zh/
│   ├── index.md                # 欢迎使用 ATBCmder
│   ├── getting_started.md      # 快速入门
│   ├── navigation.md           # 导航指南
│   ├── file_management.md      # 文件管理指南
│   ├── advanced_features.md    # 高级功能（面向进阶用户）
│   ├── faq_howtos.md           # 操作指南与常见问题
│   └── privacy_policy.md       # 隐私政策
├── images/                     # Shared screenshot assets
└── stylesheets/                # Shared custom CSS
```

### Page Title Mapping

| English Title | Chinese Title (中文标题) | Target File Name |
| :--- | :--- | :--- |
| Welcome to ATBCmder | 欢迎使用 ATBCmder | `index.md` |
| Getting Started with ATBCmder | 快速入门 | `getting_started.md` |
| Navigation Guide | 导航指南 | `navigation.md` |
| File Management Guide | 文件管理指南 | `file_management.md` |
| Advanced Features (For Power Users) | 高级功能（面向进阶用户） | `advanced_features.md` |
| How-To Guides & FAQ | 操作指南与常见问题 | `faq_howtos.md` |
| Privacy Policy | 隐私政策 | `privacy_policy.md` |

---

## 3. Configuration & Language Switching UI

### 3.1 Zensical Configuration Files

Separate configuration files will manage language-specific navigation trees and site metadata:

1. **`zensical.en.toml`**:
   - `site_name = "ATBCmder"`
   - `docs_dir = "docs/en"`
   - English `nav` items.

2. **`zensical.zh.toml`**:
   - `site_name = "ATBCmder 文档"`
   - `docs_dir = "docs/zh"`
   - Chinese `nav` items.

### 3.2 Header UI (`overrides/partials/source.html`)

A language switcher button (🌐 icon + language label) will be placed in the top status bar header:
- On `/en/` pages: Shows `中文` button linking to the corresponding `/zh/` page (or root `/zh/`).
- On `/zh/` pages: Shows `English` button linking to the corresponding `/en/` page (or root `/en/`).
- Layout order: `[ Language Switcher (EN/中文) ]` | `[ Contact ]` | `[ Forum ]` | `[ GitHub Repository ]`

---

## 4. Root Redirection & Output Assembly

### 4.1 Root Redirect Page (`root_index.html`)

A static HTML file placed at `site/index.html` handles instant redirection for root traffic:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Redirecting to ATBCmder Documentation...</title>
  <meta http-equiv="refresh" content="0; url=/en/">
  <link rel="canonical" href="https://cmder.aitobox.com/en/">
</head>
<body>
  <p>Redirecting to <a href="/en/">English Documentation</a>...</p>
</body>
</html>
```

### 4.2 Output Directory Layout

```
site/
├── index.html          # Root redirect to /en/
├── CNAME               # cmder.aitobox.com
├── en/                 # English documentation build output
│   ├── index.html
│   └── ...
└── zh/                 # Chinese documentation build output
    ├── index.html
    └── ...
```

---

## 5. Build Pipeline & GitHub Actions (`deploy.yml`)

The CI/CD deployment script will execute dual Zensical builds and combine the outputs:

1. Clean build directory `site/`.
2. Build English: `zensical build -f zensical.en.toml -d site/en`
3. Build Chinese: `zensical build -f zensical.zh.toml -d site/zh`
4. Copy root redirect `index.html` to `site/index.html`.
5. Deploy `site/` directory to GitHub Pages.

---

## 6. Verification Plan

1. Verify local build executes cleanly for both `zensical.en.toml` and `zensical.zh.toml`.
2. Verify `/en/` and `/zh/` sites render with correct language navigation and titles.
3. Verify clicking the language switcher button smoothly toggles between English and Chinese versions.
4. Verify root `https://cmder.aitobox.com/` redirects to `https://cmder.aitobox.com/en/`.
5. Confirm CI/CD pipeline builds and deploys successfully.
