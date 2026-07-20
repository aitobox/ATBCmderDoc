# Bilingual (English & Chinese) Support Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the ATBCmder documentation site into a bilingual (English and Chinese) website with `/en/` and `/zh/` subpaths, a header language switcher button, and a root redirect.

**Architecture:** Split `docs/` into `docs/en/` and `docs/zh/`, build two target trees with `zensical.en.toml` and `zensical.zh.toml` into `site/en/` and `site/zh/`, and copy a root redirect `index.html` to `site/index.html`.

**Tech Stack:** Zensical (MkDocs Material), Jinja2 HTML overrides, GitHub Actions CI/CD.

## Global Constraints

- Primary domain: `https://cmder.aitobox.com`
- Default language: English (`/en/`)
- Root redirect target: `https://cmder.aitobox.com/en/`
- Parity: Exactly 7 documentation pages in both English and Chinese (`index.md`, `getting_started.md`, `navigation.md`, `file_management.md`, `advanced_features.md`, `faq_howtos.md`, `privacy_policy.md`).

---

### Task 1: Reorganize Markdown files into `docs/en/` and `docs/zh/`

**Files:**
- Modify: `docs/en/index.md` (moved from `docs/index.md`)
- Modify: `docs/en/getting_started.md` (moved from `docs/getting_started.md`)
- Modify: `docs/en/navigation.md` (moved from `docs/navigation.md`)
- Modify: `docs/en/file_management.md` (moved from `docs/file_management.md`)
- Modify: `docs/en/advanced_features.md` (moved from `docs/advanced_features.md`)
- Modify: `docs/en/faq_howtos.md` (moved from `docs/faq_howtos.md`)
- Modify: `docs/en/privacy_policy.md` (moved from `docs/privacy_policy.md`)
- Create: `docs/zh/index.md`
- Create: `docs/zh/getting_started.md`
- Create: `docs/zh/navigation.md`
- Create: `docs/zh/file_management.md`
- Create: `docs/zh/advanced_features.md`
- Create: `docs/zh/faq_howtos.md`
- Create: `docs/zh/privacy_policy.md`

**Interfaces:**
- Consumes: Existing English markdown files in `docs/`
- Produces: `docs/en/*.md` and `docs/zh/*.md` files for Zensical builds

- [ ] **Step 1: Move existing English markdown files into `docs/en/`**

Run:
```bash
mkdir -p docs/en docs/zh
git mv docs/index.md docs/en/index.md
git mv docs/getting_started.md docs/en/getting_started.md
git mv docs/navigation.md docs/en/navigation.md
git mv docs/file_management.md docs/en/file_management.md
git mv docs/advanced_features.md docs/en/advanced_features.md
git mv docs/faq_howtos.md docs/en/faq_howtos.md
git mv docs/privacy_policy.md docs/en/privacy_policy.md
```

- [ ] **Step 2: Create Chinese translation `docs/zh/index.md`**

Create `docs/zh/index.md` with translated content for Welcome to ATBCmder.

- [ ] **Step 3: Create Chinese translation `docs/zh/getting_started.md`**

Create `docs/zh/getting_started.md` with translated content for Getting Started.

- [ ] **Step 4: Create Chinese translation `docs/zh/navigation.md`**

Create `docs/zh/navigation.md` with translated content for Navigation Guide.

- [ ] **Step 5: Create Chinese translation `docs/zh/file_management.md`**

Create `docs/zh/file_management.md` with translated content for File Management Guide.

- [ ] **Step 6: Create Chinese translation `docs/zh/advanced_features.md`**

Create `docs/zh/advanced_features.md` with translated content for Advanced Features.

- [ ] **Step 7: Create Chinese translation `docs/zh/faq_howtos.md`**

Create `docs/zh/faq_howtos.md` with translated content for FAQ & How-Tos.

- [ ] **Step 8: Create Chinese translation `docs/zh/privacy_policy.md`**

Create `docs/zh/privacy_policy.md` with translated content for Privacy Policy.

- [ ] **Step 9: Commit markdown file restructuring and translations**

Run:
```bash
git add docs/en/ docs/zh/
git commit -m "docs: restructure markdown files into docs/en and docs/zh"
```

---

### Task 2: Create Zensical configuration files `zensical.en.toml` & `zensical.zh.toml`

**Files:**
- Create: `zensical.en.toml`
- Create: `zensical.zh.toml`
- Remove: `zensical.toml`

- [ ] **Step 1: Create `zensical.en.toml`**

Create `zensical.en.toml` with English site configuration.

- [ ] **Step 2: Create `zensical.zh.toml`**

Create `zensical.zh.toml` with Chinese site configuration (`language = "zh"`).

- [ ] **Step 3: Remove old `zensical.toml`**

Run:
```bash
git rm zensical.toml
```

- [ ] **Step 4: Commit config changes**

Run:
```bash
git add zensical.en.toml zensical.zh.toml
git commit -m "config: add zensical.en.toml and zensical.zh.toml, remove zensical.toml"
```

---

### Task 3: Update Header template for Language Switcher

**Files:**
- Modify: `overrides/partials/source.html`

- [ ] **Step 1: Update `overrides/partials/source.html` with Language Switcher**

Add language switcher button to the header layout.

- [ ] **Step 2: Commit header template changes**

Run:
```bash
git add overrides/partials/source.html
git commit -m "docs: add language switcher button to header template"
```

---

### Task 4: Root Redirection Page & Local Build Verification

**Files:**
- Create: `root_index.html`

- [ ] **Step 1: Create `root_index.html`**

Create `root_index.html` redirecting to `/en/`.

- [ ] **Step 2: Local build and test script**

Run:
```bash
rm -rf site/
zensical build -f zensical.en.toml -d site/en
zensical build -f zensical.zh.toml -d site/zh
cp root_index.html site/index.html
```

- [ ] **Step 3: Commit `root_index.html`**

Run:
```bash
git add root_index.html
git commit -m "docs: add root index.html redirecting to /en/"
```

---

### Task 5: Update GitHub Actions Workflow (`.github/workflows/deploy.yml`)

**Files:**
- Modify: `.github/workflows/deploy.yml`

- [ ] **Step 1: Update `.github/workflows/deploy.yml`**

Update `.github/workflows/deploy.yml` to run dual Zensical builds.

- [ ] **Step 2: Test full build workflow locally**

Run:
```bash
zensical build -f zensical.en.toml -d site/en && zensical build -f zensical.zh.toml -d site/zh && cp root_index.html site/index.html
```

- [ ] **Step 3: Commit and push deployment workflow**

Run:
```bash
git add .github/workflows/deploy.yml
git commit -m "ci: update deploy.yml workflow for dual language build"
git push origin main
```
