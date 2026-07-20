# Custom Domain Binding Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bind the custom domain `cmder.aitobox.com` to the GitHub Pages deployment.

**Architecture:** Use the `cname` parameter in the `actions-gh-pages` GitHub Action and update the static site generator's `site_url` to ensure correct internal links.

**Tech Stack:** GitHub Actions, Zensical (MkDocs-based config).

## Global Constraints

- Domain name must be exactly `cmder.aitobox.com`
- Primary URL scheme must be `https://`

---

### Task 1: Update zensical.toml

**Files:**
- Modify: `zensical.toml:2-4`

**Interfaces:**
- Consumes: N/A
- Produces: Updated base URL in Zensical config

- [ ] **Step 1: Write the update**

```toml
[project]
site_name    = "ATBCmder"
site_url     = "https://cmder.aitobox.com/"
site_description = "The Dual-Panel File Manager for macOS"
```

- [ ] **Step 2: Commit**

```bash
git add zensical.toml
git commit -m "chore: update site_url to custom domain"
```

### Task 2: Update deploy.yml

**Files:**
- Modify: `.github/workflows/deploy.yml:26-32`

**Interfaces:**
- Consumes: N/A
- Produces: Updated GitHub Actions deployment with `cname` parameter

- [ ] **Step 1: Write the update**

```yaml
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          publish_branch: gh-pages
          cname: cmder.aitobox.com
```

- [ ] **Step 2: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: add cname parameter for github pages deployment"
```
