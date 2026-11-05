# Design Spec: ATBCmder v2.4.6 User Guide Screenshot Migration (English)

**Date:** 2026-11-05  
**Status:** In Review  
**Target Scope:** `docs/en/images/` and English User Guide Markdown files (`docs/en/*.md`)  
**Source Screenshot Directory:** `resource/screenshot/v2.4.6/`  

---

## 1. Executive Summary & Intent

ATBCmder has evolved significantly up to version 2.4.6, introducing comprehensive internal viewers, built-in editors, and dedicated system maintenance tools. While 16 core dual-panel and viewer screenshots were previously aligned with v2.4.6 captures, several documentation chapters remain visual "blind spots" (e.g. `system_tools.md` has 0 screenshots, and `viewers_and_editors.md` is missing visuals for Word, EPUB, SQLite, Markdown TOC, and Image Editor). Furthermore, legacy screenshots like `language_settings.png` still use low-resolution old UI crops.

The objective of this task is to:
1. Replace legacy screenshots in `docs/en/images/` where a modern v2.4.6 counterpart exists.
2. Import 14+ high-value v2.4.6 screenshots from `resource/screenshot/v2.4.6/` into `docs/en/images/`.
3. Update `docs/en/*.md` chapters with precise image embeds to showcase v2.4.6 capabilities.
4. Correct mismatched image references in the English documentation.

---

## 2. Goals, Non-Goals & Anti-Goals

### Goals
- **Corrected Screenshot Placement**:
  - `preferences_settings_dialog.png` captures the **Hotkeys Configuration** panel (`Hotkey Context: Main`, shortcut bindings). It will be added as a canonical screenshot to `docs/en/images/preferences_settings_dialog.png` and embedded into `docs/en/preferences_and_customization.md` Section 3 (*"Keyboard Shortcut Customization & Conflict Management"*), providing a real Retina UI visual where previously only an ASCII diagram existed.
  - `language_settings.png` will be retained as-is for the Language sections (`getting_started.md` Section 4 and `preferences_and_customization.md` Section 2) until a dedicated v2.4.6 Language tab capture is taken, preventing semantic mismatch.
- **Import v2.4.6 Feature Assets**: Copy 14 key screenshots from `resource/screenshot/v2.4.6/` into `docs/en/images/`:
  - `system_tools`: `system_resource_monitor.png`, `disk_usage_analyzer.png`, `system_cleaner.png`, `app_uninstaller.png`
  - `viewers_and_editors`: `epub_ebook_reader.png`, `word_document_viewer.png`, `sqlite_database_viewer.png`, `markdown_viewer_toc.png`, `markdown_source_editor.png`, `text_file_viewer.png`, `text_file_editor.png`, `image_editor.png`
  - `file_operations` & `navigation_and_tabs`: `calculate_directory_sizes.png`, `directory_history_dropdown.png`, `dual_panel_tree_views.png`, `preferences_settings_dialog.png`
- **Markdown Documentation Enrichment**:
  - Add image references in `docs/en/system_tools.md` for each major tool section.
  - Add image references in `docs/en/viewers_and_editors.md` for each viewer and editor type.
  - Add image reference in `docs/en/file_operations.md` for directory space calculation.
  - Add image reference in `docs/en/navigation_and_tabs.md` for history dropdown and both-panels tree view.
- **Reference Correction**:
  - Fix line 96 in `docs/en/navigation_and_tabs.md`: Remove the inaccurate `quick_access_paths.png` (which depicts Directory Hotlist Bookmarks) and replace it with a structured ASCII diagram illustrating `MacNativeTabBar` tab controls, close buttons, and active indicators.
- **Format & Build Quality**: Comply with Python-Markdown MD032 list blank spacing and verify clean build using `./test.sh -b`.

### Non-Goals
- **Re-capturing 8 Unmatched Legacy Screenshots**: Screenshots without v2.4.6 counterparts in `resource/screenshot/v2.4.6/` (`archive_pack_extract.png`, `driver_select.png`, `multi_rename_dialog.png`, `semantic_search_bar.png`, `archive_vfs.png`, `helpful_tooltips.png`, `middle_toolbar.png`, `semantic_command.png`) will remain as-is until new app screenshots are captured.
- **Other Language Directories**: Per user instruction, this task strictly focuses on `docs/en/images/` and English documentation. (Multilingual propagation will follow in a subsequent phase).
- **Landing Page Assets**: Modifying `landing/images/` is out of scope.

### Anti-Goals
- Do not introduce broken relative links in markdown documentation.
- Do not remove existing valid screenshots in `docs/en/images/`.

---

## 3. Approaches Considered

### Approach 1: Strict 1-to-1 Filename Replacement
- Only replace `docs/en/images/language_settings.png` with `preferences_settings_dialog.png`. Do not add new screenshots or touch other markdown files.
- **Pros**: Minimal diff.
- **Cons**: Leaves `system_tools.md` and major sections of `viewers_and_editors.md` without any visual screenshots despite high-quality v2.4.6 assets sitting ready in `resource/screenshot/v2.4.6`.

### Approach 2: Replace Legacy + Enrich Documentation with v2.4.6 Assets (Selected)
- Replace `language_settings.png` and copy 14 new v2.4.6 screenshots into `docs/en/images/`.
- Wire up the new screenshots in `system_tools.md`, `viewers_and_editors.md`, `file_operations.md`, and `navigation_and_tabs.md`.
- Correct mismatched image references.
- **Pros**: Delivers complete visual coverage of v2.4.6 features; high documentation value.
- **Cons**: Touches multiple markdown files in `docs/en/`. (Well-contained and verifiable via `./test.sh`).

### Approach 3: Full System Re-Capture
- Run the macOS application and re-capture all remaining 8 legacy dialogs before updating docs.
- **Pros**: 100% unified screenshot version across entire repo.
- **Cons**: Requires interactive desktop GUI execution environment, window setups, and mock data; out of scope for documentation repo.

---

## 4. Detailed Asset & Documentation Mapping

### 4.1 Asset Synchronization Plan

| Target in `docs/en/images/` | Source in `resource/screenshot/v2.4.6/` | Action |
| :--- | :--- | :--- |
| `preferences_settings_dialog.png` | `preferences_settings_dialog.png` | New Copy (Hotkeys Configuration Dialog) |
| `system_resource_monitor.png` | `system_resource_monitor.png` | New Copy |
| `disk_usage_analyzer.png` | `disk_usage_analyzer.png` | New Copy |
| `system_cleaner.png` | `system_cleaner.png` | New Copy |
| `app_uninstaller.png` | `app_uninstaller.png` | New Copy |
| `epub_ebook_reader.png` | `epub_ebook_reader.png` | New Copy |
| `word_document_viewer.png` | `word_document_viewer.png` | New Copy |
| `sqlite_database_viewer.png` | `sqlite_database_viewer.png` | New Copy |
| `markdown_viewer_toc.png` | `markdown_viewer_toc.png` | New Copy |
| `markdown_source_editor.png` | `markdown_source_editor.png` | New Copy |
| `text_file_viewer.png` | `text_file_viewer.png` | New Copy |
| `text_file_editor.png` | `text_file_editor.png` | New Copy |
| `image_editor.png` | `image_editor.png` | New Copy |
| `calculate_directory_sizes.png` | `calculate_directory_sizes.png` | New Copy |
| `directory_history_dropdown.png` | `directory_history_dropdown.png` | New Copy |
| `dual_panel_tree_views.png` | `dual_panel_tree_views.png` | New Copy |

### 4.2 Markdown Documentation Updates

1. **`docs/en/system_tools.md`**:
   - Section 3 (`## 3. System Status & Diagnostics`): Insert `![System Resource Monitor](images/system_resource_monitor.png)` above Section 3.1.
   - Section 4 (`## 4. Disk Usage Analyzer`): Insert `![Disk Usage Analyzer](images/disk_usage_analyzer.png)` above Section 4.1.
   - Section 5 (`## 5. System Cleaner`): Insert `![System Cleaner](images/system_cleaner.png)` above Section 5.1.
   - Section 6 (`## 6. Application Uninstaller`): Insert `![Application Uninstaller](images/app_uninstaller.png)` above Section 6.1.

2. **`docs/en/viewers_and_editors.md`**:
   - Section 3.1.1 (`#### 3.1.1 Word & Rich Text Documents`): Insert `![Word Document Viewer](images/word_document_viewer.png)`.
   - Section 3.1.4 (`#### 3.1.4 EPUB eBooks`): Insert `![EPUB eBook Reader](images/epub_ebook_reader.png)`.
   - Section 3.1.5 (`#### 3.1.5 Markdown Documents`): Insert `![Markdown Viewer with TOC Outline](images/markdown_viewer_toc.png)`.
   - Section 3.2.2 (`#### 3.2.2 SQLite Database Browser`): Insert `![SQLite Database Viewer](images/sqlite_database_viewer.png)`.
   - Section 3.2.4 (`#### 3.2.4 Code & Plain Text Viewing`): Insert `![Text File Viewer](images/text_file_viewer.png)`.
   - Section 4.1 (`### 4.1 Internal Code Editor`): Insert `![Code and Text File Editor](images/text_file_editor.png)` and `![Markdown Source Editor](images/markdown_source_editor.png)`.
   - Section 4.2 (`### 4.2 Dedicated Image Editor`): Insert `![Dedicated Image Editor](images/image_editor.png)`.

3. **`docs/en/file_operations.md`**:
   - Section 7.3 (`### 7.3 Occupied Space Calculation`): Insert `![Calculate Directory Sizes](images/calculate_directory_sizes.png)`.

4. **`docs/en/navigation_and_tabs.md`**:
   - Section 3 (Line 96): Replace inaccurate `images/quick_access_paths.png` embed with a clean ASCII diagram representing `MacNativeTabBar` active tabs, close buttons, and tab strip controls.
   - Section 6 (`### Navigation History`): Insert `![Directory History Dropdown](images/directory_history_dropdown.png)` under the `Directory History Popup` bullet.
   - Section 7.4 (`### 4. Tree View`): Insert `![Dual Panel Tree Views](images/dual_panel_tree_views.png)` under the `Tree View (Both Panels)` (`cm_TreeViewBoth`) bullet, complementing `vertical_split_tree_thumbnails.png`.

5. **`docs/en/preferences_and_customization.md`**:
   - Section 3 (`## 3. Keyboard Shortcut Customization & Conflict Management`): Insert `![Hotkey Configuration Page](images/preferences_settings_dialog.png)` right above the ASCII hotkey table diagram.
   - Section 2 (Language Settings): Retain `images/language_settings.png` without modification.

---

## 5. Verification & Quality Gates

1. **Asset File Verification**: Check existence, file permissions, and size of all newly copied files in `docs/en/images/`.
2. **Markdown Linting**: Run `./test.sh -l` to verify list blank spacing rules (MD032).
3. **Build Compilation**: Run `./test.sh -b` or `zensical build -f zensical.en.toml` to ensure 0 broken links and successful HTML asset generation.
4. **Git Diff Review**: Review full diff to confirm no unexpected deletions or regressions.
