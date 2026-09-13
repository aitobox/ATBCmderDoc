# Zensical Theme Starter Local Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Package our current Zensical customizations—including the Glacier & Ocean Tech theme, Apple glassmorphic UI, extended Markdown syntax plugins, templates, ASCII diagram alignment, and preview tooling—into a reusable local skill under `.agents/skills/zensical-theme-starter/` capable of transforming any blank Zensical project with a single command or guided workflow.

**Architecture:** The skill consists of a standardized `SKILL.md` reference guide, a curated `templates/` directory (containing modular `zensical.toml`, `extra.css`, `ascii-diagram.js`, `overrides/`, and `test.sh`), and an automated CLI generator `scripts/apply.py`. When invoked in a blank or existing project, the skill can either be applied automatically via `apply.py` or manually step-by-step to inject all configurations, assets, and dependencies.

**Tech Stack:** Python 3.12+, Zensical 0.0.46, PyMdown Extensions, Pygments, markdown-gfm-admonition, Jinja2, HTML5/CSS3.

**Spec:** Local workspace specifications derived from `zensical.en.toml`, `docs/en/stylesheets/extra.css`, `overrides/`, and `docs/en/javascripts/ascii-diagram.js`.

## Global Constraints

- **Location:** Place the skill strictly in `.agents/skills/zensical-theme-starter/`, and ensure compatibility with `.agents/skill/` via a symbolic link. Do not publish to global skill locations (`~/.gemini/...` or `~/.agents/...`).
- **Dependencies:** Standardize dependencies on `zensical`, `pymdown-extensions`, `Pygments`, and `markdown-gfm-admonition`.
- **Zero Hallucination:** All templates and configurations must be tested and confirmed working with the current `zensical` version (`0.0.46`) in the `ATBCmderDoc` conda environment.
- **Python-Markdown Compliance (MD032):** Include `format_markdown_lists.py` and `test.sh` linting logic to prevent list collapsing bugs.

---

### Task 1: Initialize Local Skill Directory & Compatibility Symlink

**Files:**
- Create: `.agents/skills/zensical-theme-starter/`
- Create: `.agents/skills/zensical-theme-starter/templates/`
- Create: `.agents/skills/zensical-theme-starter/scripts/`
- Symlink: `.agents/skill` -> `.agents/skills` (if `.agents/skill` does not already exist)

**Interfaces:**
- Consumes: Target filesystem structure
- Produces: Base directory hierarchy for local skill assets and scripts

- [ ] **Step 1: Check existing directories and establish symlink**

Create `.agents/skills/zensical-theme-starter` directory hierarchy and ensure `.agents/skill` points to `.agents/skills` for seamless cross-referencing.

```bash
mkdir -p .agents/skills/zensical-theme-starter/templates/overrides/partials
mkdir -p .agents/skills/zensical-theme-starter/templates/assets/stylesheets
mkdir -p .agents/skills/zensical-theme-starter/templates/assets/javascripts
mkdir -p .agents/skills/zensical-theme-starter/templates/scripts
mkdir -p .agents/skills/zensical-theme-starter/scripts
mkdir -p .agents/skills/zensical-theme-starter/tests

if [ ! -e ".agents/skill" ]; then
  ln -s skills .agents/skill
fi
```

- [ ] **Step 2: Verify directory structure**

Run: `ls -ld .agents/skill .agents/skills/zensical-theme-starter`
Expected: Symlink and directory properly created.

- [ ] **Step 3: Commit initial structure**

```bash
git add .agents/skills/zensical-theme-starter .agents/skill
git commit -m "chore: scaffold zensical-theme-starter local skill structure"
```

---

### Task 2: Extract & Modularize Reusable Templates

**Files:**
- Create: `.agents/skills/zensical-theme-starter/templates/requirements.txt`
- Create: `.agents/skills/zensical-theme-starter/templates/zensical.toml`
- Create: `.agents/skills/zensical-theme-starter/templates/zensical.multilingual.toml`
- Create: `.agents/skills/zensical-theme-starter/templates/overrides/main.html`
- Create: `.agents/skills/zensical-theme-starter/templates/overrides/partials/header.html`
- Create: `.agents/skills/zensical-theme-starter/templates/overrides/partials/source.html`
- Create: `.agents/skills/zensical-theme-starter/templates/overrides/partials/copyright.html`
- Create: `.agents/skills/zensical-theme-starter/templates/assets/stylesheets/extra.css`
- Create: `.agents/skills/zensical-theme-starter/templates/assets/javascripts/ascii-diagram.js`
- Create: `.agents/skills/zensical-theme-starter/templates/assets/javascripts/language-detector.js`
- Create: `.agents/skills/zensical-theme-starter/templates/test.sh`
- Create: `.agents/skills/zensical-theme-starter/templates/scripts/format_markdown_lists.py`
- Create: `.agents/skills/zensical-theme-starter/templates/root_index.html`

**Interfaces:**
- Consumes: Production configuration from `zensical.en.toml`, `docs/en/stylesheets/extra.css`, `overrides/`, `scripts/format_markdown_lists.py`, `test.sh`
- Produces: Generalized, parameterized templates free of hardcoded project-specific assumptions (or with clear parameter placeholders like `{{SITE_NAME}}`)

- [ ] **Step 1: Create `templates/requirements.txt`**

Define core dependencies needed for Zensical + all plugins:
```
zensical>=0.0.46
pymdown-extensions>=10.0
Pygments>=2.16.0
markdown-gfm-admonition>=0.3.0
```

- [ ] **Step 2: Create parameterized `templates/zensical.toml`**

Include all 23 markdown extensions, Glacier & Ocean theme palette (light `default`, dark `slate`), Inter/JetBrains Mono typography, `overrides/` custom directory, and asset links.

- [ ] **Step 3: Create `templates/overrides/` Jinja2 files**

Provide modular `main.html`, `partials/header.html`, `partials/source.html`, and `partials/copyright.html` with customizable branding hooks.

- [ ] **Step 4: Create `templates/assets/` stylesheets and scripts**

Copy and generalize `extra.css` (Glacier & Ocean blue design system), `ascii-diagram.js` (CJK ASCII monospace normalizer), and `language-detector.js` (for multilingual projects).

- [ ] **Step 5: Create `templates/test.sh` and `templates/scripts/format_markdown_lists.py`**

Provide one-click dev/preview and Markdown blank line linting tools.

- [ ] **Step 6: Verify all template files are present and valid**

Run: `ls -la .agents/skills/zensical-theme-starter/templates/`
Expected: All template files created.

- [ ] **Step 7: Commit templates**

```bash
git add .agents/skills/zensical-theme-starter/templates
git commit -m "feat(skill): add zensical-theme-starter reusable templates"
```

---

### Task 3: Implement Automated Setup Tool (`scripts/apply.py`)

**Files:**
- Create: `.agents/skills/zensical-theme-starter/scripts/apply.py`
- Create: `.agents/skills/zensical-theme-starter/tests/test_apply.py`

**Interfaces:**
- Consumes: Target directory path, optional flags (`--site-name`, `--multilingual`, `--skip-install`)
- Produces: Fully configured Zensical project ready to build and run

- [ ] **Step 1: Write the failing test for `apply.py`**

Write `tests/test_apply.py` using `pytest` or `unittest` to test running `apply.py` against a temporary blank directory:
1. Verifies that `zensical.toml`, `overrides/`, `docs/stylesheets/extra.css`, `docs/javascripts/ascii-diagram.js`, `test.sh`, and `docs/index.md` are correctly populated.
2. Verifies that running `zensical build` on the populated directory succeeds with exit code 0.

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest .agents/skills/zensical-theme-starter/tests/test_apply.py`
Expected: FAIL (`apply.py` not yet implemented).

- [ ] **Step 3: Implement `scripts/apply.py`**

Implement CLI script handling:
- Argument parsing: `--target` (default: current dir), `--site-name`, `--site-desc`, `--repo-url`, `--multilingual`.
- Directory structure scaffolding: `docs/`, `docs/stylesheets/`, `docs/javascripts/`, `overrides/`, `scripts/`.
- File rendering/copying with variable substitution (`{{SITE_NAME}}`, etc.).
- Creating sample `docs/index.md` demonstrating all rich components (callouts, tabs, keyboard shortcuts, code highlighting, tables, mermaid).
- Setting executable permissions on `test.sh`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python -m pytest .agents/skills/zensical-theme-starter/tests/test_apply.py -v`
Expected: PASS.

- [ ] **Step 5: Commit `apply.py` and test**

```bash
git add .agents/skills/zensical-theme-starter/scripts .agents/skills/zensical-theme-starter/tests
git commit -m "feat(skill): implement automated zensical project generator script"
```

---

### Task 4: Author the Skill Document (`SKILL.md`)

**Files:**
- Create: `.agents/skills/zensical-theme-starter/SKILL.md`

**Interfaces:**
- Consumes: Skill usage specifications and template details
- Produces: Comprehensive agent-ready instruction document following standard skill discovery and TDD guidelines

- [ ] **Step 1: Write `SKILL.md` frontmatter and overview**

- YAML frontmatter with `name: zensical-theme-starter` and rich `description` answering when to use.
- Core principles: Glacier & Ocean design language, Apple glassmorphic elements, rich Markdown extensions, CJK ASCII box normalizer.

- [ ] **Step 2: Document Quick Start & Automated Usage**

Provide clear instructions on how an agent can transform any blank project with `python .agents/skills/zensical-theme-starter/scripts/apply.py --target <path>`.

- [ ] **Step 3: Document Manual Step-by-Step Architecture**

Detail each subsystem:
1. Environment & Dependencies (`requirements.txt`).
2. Markdown Plugins Configuration (`zensical.toml` syntax).
3. Apple Glassmorphic Header & Overrides (`overrides/`).
4. Glacier & Ocean Theme CSS (`extra.css`).
5. CJK ASCII Diagram Monospace Normalizer (`ascii-diagram.js`).
6. Python-Markdown List Formatting & Local Preview Tool (`test.sh`).

- [ ] **Step 4: Document Component Showcase & Markdown Syntax Guide**

Include copy-pasteable Markdown recipes for:
- Admonitions (Note, Tip, Warning, Important, Caution)
- Content Tabs (`=== "Tab 1"`)
- Keyboard Keycaps (`++cmd+k++` / `<kbd>Cmd</kbd>`)
- Mermaid Diagrams (` ```mermaid `)
- Code blocks with line highlighting and annotations
- Math formulas (KaTeX / Arithmatex)
- Task lists with checkboxes

- [ ] **Step 5: Commit `SKILL.md`**

```bash
git add .agents/skills/zensical-theme-starter/SKILL.md
git commit -m "docs(skill): author zensical-theme-starter SKILL.md guide"
```

---

### Task 5: End-to-End Verification in a Mock Blank Workspace

**Files:**
- Test target: Temporary isolated directory `/tmp/test-zensical-project`

**Interfaces:**
- Consumes: The newly created skill `.agents/skills/zensical-theme-starter`
- Produces: Verified working static documentation site generated by Zensical

- [ ] **Step 1: Create clean test directory**

```bash
mkdir -p /tmp/test-zensical-project
cd /tmp/test-zensical-project
```

- [ ] **Step 2: Run skill script `apply.py` against mock project**

```bash
python /Users/brainzhang/work/aitobox/ATBCmderDoc/.agents/skills/zensical-theme-starter/scripts/apply.py \
  --target /tmp/test-zensical-project \
  --site-name "Mock Demo Docs"
```

- [ ] **Step 3: Test build in conda environment**

```bash
cd /tmp/test-zensical-project
zensical build
```
Expected: Site builds into `site/` with 0 warnings/errors.

- [ ] **Step 4: Verify generated HTML artifacts**

Check that `site/index.html` contains:
- Glacier & Ocean primary colors (`#0284c7`)
- Inter and JetBrains Mono font declarations
- `stylesheets/extra.css` link
- `javascripts/ascii-diagram.js` script tag
- Rendered admonition, tabs, and keyboard shortcuts

- [ ] **Step 5: Clean up temporary test directory**

```bash
rm -rf /tmp/test-zensical-project
```

---

## Self-Review Checklist

1. **Spec coverage:** Does the plan cover theme beautification (Glacier/Ocean tech theme, glassmorphic header, typography, cards, kbd, tables)? Yes. Does it cover extended markdown extensions? Yes (all 23 extensions). Does it include current templates? Yes (overrides, extra.css, scripts, test.sh). Does it place the skill in `.agents/skills/` without touching global skills? Yes.
2. **Placeholder scan:** No "TBD" or "TODO". All paths, file names, and steps are concrete.
3. **Type and command consistency:** Paths are consistent across tasks.
