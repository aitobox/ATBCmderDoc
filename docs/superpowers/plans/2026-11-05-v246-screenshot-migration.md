# ATBCmder v2.4.6 User Guide Screenshot Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Synchronize 16 v2.4.6 application screenshots into `docs/en/images/` and update English user documentation chapters with accurate UI visuals and corrected references.

**Architecture:** Copy canonical PNG Retina captures from `resource/screenshot/v2.4.6/` into `docs/en/images/`. Update targeted Markdown documentation files (`system_tools.md`, `viewers_and_editors.md`, `file_operations.md`, `navigation_and_tabs.md`, and `preferences_and_customization.md`) with clean Markdown image embeds following Python-Markdown MD032 spacing rules. Validate using `./test.sh -l` and `./test.sh -b`.

**Tech Stack:** Markdown, Python-Markdown, Zensical (MkDocs Material engine), Shell/Bash.

**Spec:** [`docs/superpowers/specs/2026-11-05-v246-screenshot-migration-design.md`](file:///Users/brainzhang/work/aitobox/ATBCmderDoc/docs/superpowers/specs/2026-11-05-v246-screenshot-migration-design.md)

## Global Constraints

- Scope: Strictly limited to `docs/en/images/` and English documentation markdown files in `docs/en/`.
- Markdown List Spacing (MD032): Every markdown list (`-`, `*`, `1.`) must have a preceding blank line separating it from preceding paragraphs or images.
- Non-Destructive Assets: Existing valid screenshots in `docs/en/images/` must not be removed.
- Path Integrity: All image references must use relative paths in the form `images/<filename>.png`.

## Review Focus

1. Image file permissions and existence: ensure all 16 copied images exist in `docs/en/images/` and are readable (non-empty).
2. Correct image-to-section semantic alignment: `preferences_settings_dialog.png` goes to Hotkeys (Section 3), NOT Language Settings.
3. MD032 list spacing integrity: inserting an image before a list must not collapse the list items into an inline paragraph.
4. Broken image links: Zensical build (`./test.sh -b`) must complete with 0 missing asset warnings and exit code 0.
5. Removal of mismatched line 96 in `navigation_and_tabs.md`: replaced with native tab bar ASCII representation.

---

### Task 1: Synchronize v2.4.6 Screenshot Assets into `docs/en/images/`

**Files:**
- Create/Copy:
  - `docs/en/images/preferences_settings_dialog.png`
  - `docs/en/images/system_resource_monitor.png`
  - `docs/en/images/disk_usage_analyzer.png`
  - `docs/en/images/system_cleaner.png`
  - `docs/en/images/app_uninstaller.png`
  - `docs/en/images/epub_ebook_reader.png`
  - `docs/en/images/word_document_viewer.png`
  - `docs/en/images/sqlite_database_viewer.png`
  - `docs/en/images/markdown_viewer_toc.png`
  - `docs/en/images/markdown_source_editor.png`
  - `docs/en/images/text_file_viewer.png`
  - `docs/en/images/text_file_editor.png`
  - `docs/en/images/image_editor.png`
  - `docs/en/images/calculate_directory_sizes.png`
  - `docs/en/images/directory_history_dropdown.png`
  - `docs/en/images/dual_panel_tree_views.png`

**Interfaces:**
- Consumes: PNG files located in `resource/screenshot/v2.4.6/`
- Produces: 16 readable, verified PNG assets in `docs/en/images/`

- [ ] **Step 1: Copy 16 screenshot assets from `resource/screenshot/v2.4.6/` to `docs/en/images/`**

Run shell command:
```bash
for img in preferences_settings_dialog.png system_resource_monitor.png disk_usage_analyzer.png \
           system_cleaner.png app_uninstaller.png epub_ebook_reader.png word_document_viewer.png \
           sqlite_database_viewer.png markdown_viewer_toc.png markdown_source_editor.png \
           text_file_viewer.png text_file_editor.png image_editor.png calculate_directory_sizes.png \
           directory_history_dropdown.png dual_panel_tree_views.png; do
  cp "resource/screenshot/v2.4.6/$img" "docs/en/images/$img"
  chmod 644 "docs/en/images/$img"
done
```

- [ ] **Step 2: Verify all 16 copied images exist and have non-zero byte size**

Run verification check:
```bash
python3 -c "
import os
names = ['preferences_settings_dialog.png', 'system_resource_monitor.png', 'disk_usage_analyzer.png',
         'system_cleaner.png', 'app_uninstaller.png', 'epub_ebook_reader.png', 'word_document_viewer.png',
         'sqlite_database_viewer.png', 'markdown_viewer_toc.png', 'markdown_source_editor.png',
         'text_file_viewer.png', 'text_file_editor.png', 'image_editor.png', 'calculate_directory_sizes.png',
         'directory_history_dropdown.png', 'dual_panel_tree_views.png']
for name in names:
    p = os.path.join('docs/en/images', name)
    assert os.path.isfile(p) and os.path.getsize(p) > 0, f'Missing {p}'
print('All 16 screenshot assets verified successfully.')
"
```
Expected: PASS with "All 16 screenshot assets verified successfully."

- [ ] **Step 3: Commit asset synchronization**

```bash
git add docs/en/images/*.png
git commit -m "docs: import v2.4.6 application screenshot assets into docs/en/images"
```

---

### Task 2: Enrich `docs/en/system_tools.md` with System Maintenance Screenshots

**Files:**
- Modify: `docs/en/system_tools.md`

**Interfaces:**
- Consumes:
  - `images/system_resource_monitor.png`
  - `images/disk_usage_analyzer.png`
  - `images/system_cleaner.png`
  - `images/app_uninstaller.png`
- Produces: Visual documentation for Chapter 7 system maintenance tools

- [ ] **Step 1: Insert System Status screenshot into Section 3**

In `docs/en/system_tools.md`, under `## 3. System Status & Diagnostics (cm_SystemStatus / ⌘⇧M)` right before `### 3.1 Diagnostic Features & Metric Sections`, insert:
```markdown
![System Resource Monitor](images/system_resource_monitor.png)  
*Figure 7.1: Real-time System Status & Diagnostics dashboard displaying CPU, RAM, disk I/O, and top processes.*

```

- [ ] **Step 2: Insert Disk Usage Analyzer screenshot into Section 4**

Under `## 4. Disk Usage Analyzer (cm_DiskUsageAnalyzer / ⌘⇧D)` right before `### 4.1 Key Architecture & Capabilities`, insert:
```markdown
![Disk Usage Analyzer](images/disk_usage_analyzer.png)  
*Figure 7.2: Disk Usage Analyzer scanning local volumes with categorized space breakdown and treemap navigation.*

```

- [ ] **Step 3: Insert System Cleaner screenshot into Section 5**

Under `## 5. System Cleaner (cm_CleanSystem / ⌘⇧C)` right before `### 5.1 The Two-Stage Safety Architecture`, insert:
```markdown
![System Cleaner](images/system_cleaner.png)  
*Figure 7.3: System Cleaner safe scanning interface showing cache, log, and temporary junk file recovery estimates.*

```

- [ ] **Step 4: Insert Application Uninstaller screenshot into Section 6**

Under `## 6. Application Uninstaller (cm_UninstallApp / ⌘⇧U)` right before `### 6.1 Remnant Discovery Locations`, insert:
```markdown
![Application Uninstaller](images/app_uninstaller.png)  
*Figure 7.4: Application Uninstaller performing deep remnant scanning across Application Support, Caches, and Preferences.*

```

- [ ] **Step 5: Verify formatting and MD032 compliance in `system_tools.md`**

Run:
```bash
./test.sh -l
```
Expected: PASS with 0 MD032 violations in `docs/en/system_tools.md`.

- [ ] **Step 6: Commit changes to `system_tools.md`**

```bash
git add docs/en/system_tools.md
git commit -m "docs(en): embed v2.4.6 system tool screenshots in system_tools.md"
```

---

### Task 3: Enrich `docs/en/viewers_and_editors.md` with Lister & Editor Screenshots

**Files:**
- Modify: `docs/en/viewers_and_editors.md`

**Interfaces:**
- Consumes:
  - `images/word_document_viewer.png`
  - `images/epub_ebook_reader.png`
  - `images/markdown_viewer_toc.png`
  - `images/sqlite_database_viewer.png`
  - `images/text_file_viewer.png`
  - `images/text_file_editor.png`
  - `images/markdown_source_editor.png`
  - `images/image_editor.png`
- Produces: Visual documentation for Chapter 4 Universal Lister and internal editors

- [ ] **Step 1: Insert Document and Book Viewer screenshots**

In `docs/en/viewers_and_editors.md`:
- Under `#### 3.1.1 Word & Rich Text Documents (DocumentPanel)`:
  Insert:
  ```markdown
  ![Word Document Viewer](images/word_document_viewer.png)  
  *Figure 4.2: Built-in Word and rich text document viewer with multi-page navigation and zoom.*
  ```
- Under `#### 3.1.4 EPUB eBooks (EpubPanel)`:
  Insert:
  ```markdown
  ![EPUB eBook Reader](images/epub_ebook_reader.png)  
  *Figure 4.3: Built-in EPUB eBook reader with chapter navigation and adjustable typography.*
  ```
- Under `#### 3.1.5 Markdown Documents (MarkdownPanel)`:
  Insert:
  ```markdown
  ![Markdown Viewer with TOC Outline](images/markdown_viewer_toc.png)  
  *Figure 4.4: Markdown reader displaying rendered content alongside interactive Outline Table of Contents.*
  ```

- [ ] **Step 2: Insert Data, Database & Text Viewer screenshots**

- Under `#### 3.2.2 SQLite Database Browser (SqlitePanel)`:
  Insert:
  ```markdown
  ![SQLite Database Viewer](images/sqlite_database_viewer.png)  
  *Figure 4.5: SQLite database inspector browsing table schema, row records, and indices.*
  ```
- Under `#### 3.2.4 Code & Plain Text Viewing (TextPanel)`:
  Insert:
  ```markdown
  ![Text File Viewer](images/text_file_viewer.png)  
  *Figure 4.6: High-performance plain text and source code viewer with syntax highlighting.*
  ```

- [ ] **Step 3: Insert Internal Editor screenshots**

- Under `### 4.1 Internal Code Editor (EditorWindow)` (above `#### Core Code Editor Capabilities`):
  Insert:
  ```markdown
  ![Code and Text File Editor](images/text_file_editor.png)  
  *Figure 4.7: Dedicated internal text editor featuring search/replace bar and line numbering.*

  ![Markdown Source Editor](images/markdown_source_editor.png)  
  *Figure 4.8: Internal editor editing Markdown files with live syntax highlighting and quick tools.*
  ```
- Under `### 4.2 Dedicated Image Editor (ImageEditorDialog)` (above `#### Interactive Canvas & Transforms`):
  Insert:
  ```markdown
  ![Dedicated Image Editor](images/image_editor.png)  
  *Figure 4.9: Built-in Image Editor with crop aspect ratios, canvas rotation, and transformation controls.*
  ```

- [ ] **Step 4: Verify formatting and MD032 compliance in `viewers_and_editors.md`**

Run:
```bash
./test.sh -l
```
Expected: PASS with 0 MD032 violations in `docs/en/viewers_and_editors.md`.

- [ ] **Step 5: Commit changes to `viewers_and_editors.md`**

```bash
git add docs/en/viewers_and_editors.md
git commit -m "docs(en): embed v2.4.6 lister and editor screenshots in viewers_and_editors.md"
```

---

### Task 4: Update `file_operations.md` and `navigation_and_tabs.md`

**Files:**
- Modify: `docs/en/file_operations.md`
- Modify: `docs/en/navigation_and_tabs.md`

**Interfaces:**
- Consumes:
  - `images/calculate_directory_sizes.png`
  - `images/directory_history_dropdown.png`
  - `images/dual_panel_tree_views.png`
- Produces: Corrected tab diagram, space calculation screenshot, history dropdown screenshot, and tree view screenshot

- [ ] **Step 1: Insert space calculation screenshot into `file_operations.md`**

In `docs/en/file_operations.md`, under `### 7.3 Occupied Space Calculation (cm_CountDirContent / cm_CalculateSpace / Space)` right before `- Single Folder Size`:
Insert:
```markdown
![Calculate Directory Sizes](images/calculate_directory_sizes.png)  
*Figure 3.2: Asynchronous directory space calculation replacing <DIR> with exact recursive byte footprints.*

```

- [ ] **Step 2: Correct Line 96 in `navigation_and_tabs.md`**

In `docs/en/navigation_and_tabs.md`, replace line 96:
```markdown
![Folder Tabs and Splitters](images/quick_access_paths.png)  
*Multi-tab management and quick navigation in ATBCmder*
```
with a dedicated ASCII structure diagram of `MacNativeTabBar`:
```markdown
```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ [📁 Documents ✕] [📁 Downloads ✕] [📁 Projects ✕]   +                                   │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ [/dev/disk3s3s1] /Users/brainzhang/Projects                     428.5 GB free of 994.7 GB│
└─────────────────────────────────────────────────────────────────────────────────────────┘
```
*Figure 2.1: Native macOS tab bar (`MacNativeTabBar`) providing independent tab stacks per panel.*
```

- [ ] **Step 3: Insert Directory History Dropdown screenshot into `navigation_and_tabs.md`**

In `docs/en/navigation_and_tabs.md`, under `### Navigation History` under bullet `- Directory History Popup`:
Insert:
```markdown
![Directory History Dropdown](images/directory_history_dropdown.png)  
*Figure 2.2: Directory History dropdown menu (`Alt+F8` / `Ctrl+Down`) displaying recently visited folder paths.*

```

- [ ] **Step 4: Insert Dual Tree Views screenshot into `navigation_and_tabs.md`**

In `docs/en/navigation_and_tabs.md`, under `### 4. Tree View (cm_TreeView, cm_TreeViewSplit, cm_TreeViewBoth)` right after the `- Tree View (Both Panels)` bullet point:
Insert:
```markdown
![Dual Panel Tree Views](images/dual_panel_tree_views.png)  
*Figure 2.3: Dual Tree Views mode (`cm_TreeViewBoth`) providing simultaneous folder hierarchy navigation on both panels.*

```

- [ ] **Step 5: Verify formatting and MD032 compliance**

Run:
```bash
./test.sh -l
```
Expected: PASS with 0 MD032 violations.

- [ ] **Step 6: Commit changes to `file_operations.md` and `navigation_and_tabs.md`**

```bash
git add docs/en/file_operations.md docs/en/navigation_and_tabs.md
git commit -m "docs(en): embed space calculation, history dropdown, and tree view screenshots"
```

---

### Task 5: Update `preferences_and_customization.md` with Hotkeys Dialog Screenshot

**Files:**
- Modify: `docs/en/preferences_and_customization.md`

**Interfaces:**
- Consumes: `images/preferences_settings_dialog.png`
- Produces: Real UI screenshot for Section 3 Hotkey Configuration

- [ ] **Step 1: Insert Hotkey Configuration screenshot into Section 3**

In `docs/en/preferences_and_customization.md`, under `## 3. Keyboard Shortcut Customization & Conflict Management`, immediately above the existing ASCII diagram (`┌───────────────────────────┐`), insert:
```markdown
![Hotkey Configuration Page](images/preferences_settings_dialog.png)  
*Figure 7.2: ATBCmder Hotkey Configuration page showing context filtering, command search, and collision prevention.*

```

- [ ] **Step 2: Verify `language_settings.png` in Section 2 remains untouched**

Ensure Section 2 still links to `images/language_settings.png`.

- [ ] **Step 3: Verify formatting and MD032 compliance**

Run:
```bash
./test.sh -l
```
Expected: PASS with 0 MD032 violations.

- [ ] **Step 4: Commit changes to `preferences_and_customization.md`**

```bash
git add docs/en/preferences_and_customization.md
git commit -m "docs(en): embed hotkey configuration screenshot in preferences_and_customization.md"
```

---

### Task 6: Full Validation & Build Verification

**Files:**
- Test/Verification scripts: `./test.sh`

- [ ] **Step 1: Run Markdown list blank spacing linter**

Run:
```bash
./test.sh -l
```
Expected output: `[OK] All Markdown files adhere to list blank line rules (MD032).`

- [ ] **Step 2: Execute full site build to verify assets and navigation**

Run:
```bash
./test.sh -b
```
Expected output:
- Compiles both English and Chinese documentation without errors.
- Exit code: 0.

- [ ] **Step 3: Review full git diff to ensure pristine repository state**

Run:
```bash
git status
git log -n 5 --oneline
```
Expected output: Clean working tree on branch main, clean commit history.
