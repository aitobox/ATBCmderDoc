# ATBCmder Official Website — Design Spec

**Date:** 2026-07-19  
**Status:** Approved  
**Scope:** Zensical-based product website + documentation, deployed to GitHub Pages from the `ATBCmderDoc` repository.

---

## 1. Goals

Build an official website for ATBCmder (a dual-panel macOS file manager) that:

- Presents the product with a polished Landing Page that highlights core features
- Hosts the existing help documentation (5 Markdown files + screenshots)
- Deploys automatically to GitHub Pages via GitHub Actions on every push to `main`
- Uses English as the primary language (additional languages to be added later)
- Links to the Mac App Store (placeholder URL until the app is published)

---

## 2. Tool Stack

| Layer | Choice | Rationale |
|---|---|---|
| Site generator | **Zensical** | MkDocs successor by Material for MkDocs team; `zensical.toml` config; `zensical build` / `zensical serve` |
| Theme | **Material** | Ships with Zensical; supports dark/light mode, search, responsive layout |
| Deployment | **GitHub Actions → `gh-pages` branch** | Standard, zero-cost, automatic on push |

---

## 3. Repository Structure

```
ATBCmderDoc/
├── zensical.toml              # Main site configuration
├── docs/
│   ├── index.md               # Home page trigger (content rendered by home.html)
│   ├── 01_getting_started.md  # Existing docs — unchanged
│   ├── 02_navigation.md
│   ├── 03_file_management.md
│   ├── 04_advanced_features.md
│   ├── 05_faq_howtos.md
│   └── images/                # Existing screenshots — unchanged
├── overrides/
│   ├── home.html              # Custom Landing Page Jinja2 template
│   └── stylesheets/
│       └── extra.css          # Landing page custom styles
└── .github/
    └── workflows/
        └── deploy.yml         # GitHub Actions CI/CD
```

No existing files are moved or renamed. All new files are additive.

---

## 4. Zensical Configuration (`zensical.toml`)

Key settings:

```toml
[project]
site_name    = "ATBCmder"
site_url     = "https://<github-username>.github.io/ATBCmderDoc/"
site_description = "The Dual-Panel File Manager for macOS"
repo_url     = "https://github.com/<github-username>/ATBCmderDoc"
repo_name    = "ATBCmderDoc"

[theme]
name        = "material"
custom_dir  = "overrides"
palette     = [
  { scheme = "default", primary = "indigo", accent = "deep-purple", media = "(prefers-color-scheme: light)" },
  { scheme = "slate",   primary = "indigo", accent = "deep-purple", media = "(prefers-color-scheme: dark)" }
]
font        = { text = "Roboto", code = "Roboto Mono" }
features    = [
  "navigation.tabs",
  "navigation.top",
  "search.highlight",
  "content.code.copy"
]

[extra]
app_store_url = "https://apps.apple.com/app/atbcmder/idXXXXXXXX"  # placeholder

[extra_css]
files = ["overrides/stylesheets/extra.css"]
```

---

## 5. Navigation Structure

### Top Navigation Tabs

```
ATBCmder    [Home]    [Documentation ▾]    [GitHub ↗]
```

`Documentation` tab reveals the sidebar with the 5 doc pages.

### Left Sidebar (documentation pages)

| File | Display Title |
|---|---|
| `01_getting_started.md` | Getting Started |
| `02_navigation.md` | Navigating Like a Pro |
| `03_file_management.md` | Working With Files |
| `04_advanced_features.md` | Advanced Features |
| `05_faq_howtos.md` | FAQ & How-Tos |

---

## 6. Landing Page Design (`overrides/home.html`)

The template extends Material's `base.html` and replaces the `content` block entirely for `index.md` only.

### Section 1 — Hero

- Full-width dark gradient background (indigo → deep-purple)
- Large product name: **ATBCmder**
- Tagline: *"The Dual-Panel File Manager for macOS"*
- Subtitle: *"Navigate, manage, and transform your files with the speed and power of a professional tool."*
- Mac App Store badge (official SVG) — links to `extra.app_store_url`; annotated "Coming soon · Stay tuned" until published

### Section 2 — Features Grid (2 rows × 3 columns)

| Icon | Title | Description |
|---|---|---|
| 🗂 | Dual Panel | View and manage two directories side-by-side simultaneously |
| 🌐 | Network VFS | FTP, SFTP, WebDAV & Samba — remote files feel local |
| 📦 | Archive VFS | Browse and edit ZIP, TAR, 7z without extracting |
| ✨ | Semantic Command | Natural language file search powered by macOS Spotlight |
| 🌿 | Branch View | See all nested files in a single flat list instantly |
| 🌍 | 30+ Languages | Automatically follows your system language |

Cards use a subtle glassmorphism border, hover lift animation, icon + bold title + short description.

### Section 3 — Screenshots

Three screenshots displayed in sequence (horizontal on desktop, stacked on mobile):

1. `images/semantic_command.png` — highest visual impact
2. `images/branch_view.png` — showcases core browsing capability
3. `images/middle_toolbar.png` — showcases UI layout

Each screenshot has a short caption below it.

### Section 4 — Get Started CTA

- Centered section with a brief line: *"Ready to explore ATBCmder?"*
- Primary button: **Read the Documentation →** (links to `getting-started/`)

---

## 7. Styling (`overrides/stylesheets/extra.css`)

- Hero gradient and typography overrides
- Feature card grid layout (CSS Grid, responsive)
- Screenshot section layout (flexbox, responsive)
- CTA section centering and button styles
- All landing page styles scoped under `.atb-*` class prefix to avoid conflicts with Material's doc styles

---

## 8. Deployment (`deploy.yml`)

GitHub Actions workflow triggered on push to `main`:

1. Checkout repository
2. Set up Python
3. Install Zensical: `pip install zensical`
4. Build: `zensical build`
5. Deploy `site/` directory to `gh-pages` branch using `peaceiris/actions-gh-pages`

GitHub Pages source must be set to the `gh-pages` branch in repository Settings → Pages.

---

## 9. Out of Scope

- Multilingual support (deferred to a future phase)
- Blog or changelog section
- Custom domain (can be added later via `CNAME` file)
- Analytics (can be added later via `extra.analytics` in config)

---

## 10. Success Criteria

- `zensical serve` runs locally without errors
- Landing page renders correctly in light and dark mode
- All 5 documentation pages are accessible via the sidebar
- Screenshots load correctly from `docs/images/`
- GitHub Actions workflow deploys successfully on push to `main`
- Mac App Store link is present (placeholder until app is live)
