# Custom Domain Binding Design Spec

## Overview
This document specifies the design for adapting the current GitHub Actions automated build and deployment process for ATBCmderDoc to bind the custom domain `cmder.aitobox.com`.

## Goals
- Automate the generation of the `CNAME` file required by GitHub Pages.
- Update the project configuration to reflect the new primary URL so internal links and canonical URLs remain correct.

## Design Decisions

### 1. GitHub Actions Deployment Update (Approach A)
We will leverage the native `cname` parameter within the `peaceiris/actions-gh-pages@v4` action in `.github/workflows/deploy.yml`. 
This is the recommended approach as it ensures that the `CNAME` file is predictably and reliably injected into the root of the published site without requiring manual file management in the static assets.

**Changes required:**
- Append `cname: cmder.aitobox.com` to the `with` block of the "Deploy to GitHub Pages" step.

### 2. Project Configuration Update
To ensure SEO metrics and internal references remain accurate, the static site generator's base URL must match the new domain.

**Changes required:**
- In `zensical.toml`, update `site_url` from `https://aitobox.github.io/ATBCmderDoc/` to `https://cmder.aitobox.com/`.

## Affected Files
1. `.github/workflows/deploy.yml`
2. `zensical.toml`

## Dependencies / Prerequisites
- The user must configure DNS settings (A/CNAME records) on their domain registrar for `cmder.aitobox.com` pointing to GitHub Pages. (Out of scope for this codebase).
