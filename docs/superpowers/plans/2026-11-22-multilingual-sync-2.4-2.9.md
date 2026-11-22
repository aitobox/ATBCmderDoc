# Multilingual Documentation Synchronization (v2.4.0 – v2.9.0) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Synchronize the 10 English documentation chapters updated for v2.4.0–v2.9.0 into Simplified Chinese (`docs/zh/`), Traditional Chinese (`docs/zh-hant/`), and 8 foreign languages (`ja, de, fr, es, pt, ko, ru, it`), delivering high-craft, idiomatic Chinese technical writing that avoids literal machine translation, resolving all 40 parity errors, and passing all static site builds.

**Architecture:** Two-phase execution. Phase 1 performs high-standard, hand-crafted Simplified Chinese (`docs/zh/`) translation and OpenCC (`s2twp`) Traditional Chinese (`docs/zh-hant/`) alignment across the 10 chapters. Phase 2 propagates the structural diffs into the 8 foreign languages using an automated propagation pipeline, followed by markdown list formatting (`./test.sh -l`), parity validation (`scripts/check_parity.py`), and full static site compilation (`./test.sh -b`).

**Tech Stack:** Python 3.12+, Zensical, OpenCC (`s2twp`), GitHub-Flavored Markdown, `scripts/check_parity.py`, `scripts/format_markdown_lists.py`, `scripts/propagate_diff_i18n.py`.

**Spec:** `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md`

## Global Constraints

- Never introduce version badges or inline version labels (e.g., `> [!NOTE] Available since v2.9.0` or `(since v2.8.0)`).
- Every Commander Command ID (`cm_*`), configuration key (e.g., `view.panel_column_order`, `ui.minimize_to_tray`, `ui.global_hotkey`), and shortcut symbol (`⌘`, `⌥`, `⇧`, `⌃`) must be preserved verbatim.
- Simplified Chinese (`docs/zh/`) must strictly adhere to Apple macOS HIG terminology (访达, 废纸篓, 快捷键, 偏好设置, 菜单栏, 状态栏) and vivid, professional technical prose without mechanical/literal translations.
- Traditional Chinese (`docs/zh-hant/`) must use Apple Taiwan/HK localization terms (分頁, 偏好設定, 垃圾桶, 快速鍵, 檔案, 剪貼簿).
- Every Markdown list must have a preceding blank line (MD032 compliance).
- All 10 target languages must achieve 100% header hierarchy (H1, H2, H3), image reference, and table structure parity with the `docs/en/` benchmark (`python3 scripts/check_parity.py`).

## Review Focus

- Header count parity across all languages on the four restructured files: `system_tools.md` (27 headers), `getting_started.md` (32 headers), `preferences_and_customization.md` (47 headers), `faq_howtos.md` (23 headers).
- Natural, idiomatic Chinese translations of new key terms: "输入完整路径并跳转" (`cm_EditPath`), "锁定此标签页" / "解锁" (`cm_ToggleLockTab`), "同名冲突自动重命名", "按应用程序分组", "免辅助功能权限的全局快捷键".
- Conflict-free shortcut table synchronization: `cm_ConfigDirHotList` (`⌥⌘D` / `Ctrl+Alt+D`), `cm_SaveFavoriteTabs` (`⇧⌘D` / `Ctrl+Shift+D`), `cm_CalculateChecksum` (`⌃X`), `cm_DiskUsageAnalyzer` (Menu only).
- Consistent ASCII UI diagrams: breadcrumb bar with `[✎]` button, tab strip with `[* Source]`, System Status dual tabs, and System Cleaner per-app tree layout.
- Static site build health: zero broken links, zero markdown formatting errors, clean compilation with `./test.sh -b`.

---

### Task 1: Sync `navigation_and_tabs.md` and `preferences_and_customization.md` to Simplified & Traditional Chinese

**Files:**
- Modify: `docs/zh/navigation_and_tabs.md`
- Modify: `docs/zh-hant/navigation_and_tabs.md`
- Modify: `docs/zh/preferences_and_customization.md`
- Modify: `docs/zh-hant/preferences_and_customization.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md` (Sections 4.1 & 4.2)
- Produces: Updated Chinese navigation and preferences documentation matching English benchmark structure (H:38 and H:47).

- [ ] **Step 1: Translate and update `docs/zh/navigation_and_tabs.md`**
  - In Section 1 cheat sheet: add `输入完整路径并跳转` (`Cmd+Shift+G` / `⌘⇧G` | `Ctrl+Shift+G` | `cm_EditPath`) and `锁定 / 解锁当前标签页` (`Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab`).
  - In Section 2 breadcrumb ASCII & item 4: update diagram with `[✎]` button; rewrite item 4 as "输入完整路径并跳转 (`BreadcrumbLineEdit` / `cm_EditPath`)", detailing the 3 entry points (pencil button, blank space double-click, `Cmd+Shift+G`), input pre-filling, smart normalization (whitespace/quotes trimming, `~` and `$VAR` expansion, relative paths, `vfs://` preservation), direct file jumping with highlight, and inline red-border error retention.
  - In Section 3 & 4: add `Cmd+K` tab locking toggle and context menu dynamic shortcut sync; update `cm_SaveFavoriteTabs` shortcut to `Cmd+Shift+D` (`⌘⇧D`).
  - In Section 5: update `cm_ConfigDirHotList` shortcut to `Option+Cmd+D` (`⌥⌘D` / `Ctrl+Alt+D`).
  - In Section 6: mention broad trackpad compatibility (built-in MacBook and Magic Trackpad).
  - In Section 7.1: add customizable columns (`view.panel_column_order`, `view.panel_column_visible`) and macOS Finder 7 color tags (`view.show_color_tags`) with localized tooltips.
  - In Section 11 master table: add `cm_EditPath` and `cm_ToggleLockTab`; update hotlist and favorite tab shortcuts.

- [ ] **Step 2: Generate Traditional Chinese `docs/zh-hant/navigation_and_tabs.md`**
  - Run OpenCC `s2twp` conversion on `docs/zh/navigation_and_tabs.md`, ensuring Taiwan/HK macOS terms (分頁, 快速鍵, 偏好設定, 標籤 ➔ 顏色標記/標籤, 拖曳).
  - Verify ASCII box-drawing characters and tables remain perfectly aligned.

- [ ] **Step 3: Translate and update `docs/zh/preferences_and_customization.md`**
  - In Section 1 & 2.2: update hotlist shortcut to `Option+Cmd+D` (`⌥⌘D`), add custom columns and color tags to File Views summary row.
  - In Section 3.5: expand "全局显示/隐藏窗口快捷键 (`Cmd+Opt+H` / `Ctrl+Alt+H`)" to document menu bar system tray residency (`ui.minimize_to_tray`, requires restart once, menu bar items), permission-free Carbon `RegisterEventHotKey` API (zero Accessibility permissions needed in macOS System Settings), and Option key normalization (`_MacAwareKeySequenceEdit`).
  - In Section 4: update ASCII diagram with `[ 列设置 ]` and `[ 颜色标签 (macOS) ]`; add subsection 4.7 "自定义列可见性与排序 (`view.panel_column_order`, `view.panel_column_visible`)" and subsection 4.8 "macOS 访达颜色标签 (`view.show_color_tags`, `view.color_tag_sync_interval_ms`)".
  - In Section 11 master table: update `cm_ConfigDirHotList` (`⌥⌘D`), `cm_SaveFavoriteTabs` (`⇧⌘D`), and add global hotkey row.

- [ ] **Step 4: Generate Traditional Chinese `docs/zh-hant/preferences_and_customization.md`**
  - Run OpenCC `s2twp` conversion on `docs/zh/preferences_and_customization.md`, applying Apple Taiwan terms (系統選單列, 全域快速鍵, 輔助使用權限, 偏好設定).

- [ ] **Step 5: Verify parity and list spacing for Task 1 files**
  - Run: `python3 scripts/check_parity.py --lang zh,zh-hant`
  - Expected: `navigation_and_tabs.md` and `preferences_and_customization.md` both [PASS] for `zh` and `zh-hant`.
  - Run: `./test.sh -l`
  - Expected: PASS.

- [ ] **Step 6: Commit Task 1**
  ```bash
  git add docs/zh/navigation_and_tabs.md docs/zh-hant/navigation_and_tabs.md docs/zh/preferences_and_customization.md docs/zh-hant/preferences_and_customization.md
  git commit -m "docs(zh): sync navigation_and_tabs and preferences_and_customization to zh and zh-hant"
  ```

---

### Task 2: Sync `system_tools.md` to Simplified & Traditional Chinese

**Files:**
- Modify: `docs/zh/system_tools.md`
- Modify: `docs/zh-hant/system_tools.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md` (Section 4.3)
- Produces: Updated Chinese system tools documentation matching English benchmark structure (H:27, 5 integrated tools, renumbered sections 1–9).

- [ ] **Step 1: Translate and update `docs/zh/system_tools.md`**
  - In intro & Section 1: update tool count from 4 to 5 tools; update ASCII summary card to include `[4] 最近修改文件与文件夹 (cm_RecentChanges)`; update shortcut matrix: change Disk Usage Analyzer to Menu only, add `cm_RecentChanges`.
  - In Section 2.2 & 3: add subsection 3.2 "Mac App Store 沙盒模式 (Top 进程 + 正在运行的应用程序)", documenting Darwin `sysctl KERN_PROC_UID` + `proc_pidinfo` process collection, dual-tab bottom pane (Top 进程, 正在运行的应用程序 with cached icons and noise filtering), and sandbox-compliant context menu actions (退出, 强制退出, 前置窗口, 在访达中显示, 在活动监视器中查看…).
  - Insert Section 5: "最近修改文件与文件夹 (`cm_RecentChanges`)" (placed after Disk Usage Analyzer):
    - Document menu path (`工具 ➔ 查看最近修改的文件/文件夹...`).
    - Document UI layout ASCII diagram (path input, type filters, time presets, minimum size filter with `B`/`KB`/`MB`/`GB`).
    - Document Spotlight search pre-seeding, recursive directory calculation with `≥` lower bound, real-time filter box, and action buttons (在访达中显示, 在 ATBCmder 面板中打开, 移到废纸篓).
  - Rewrite Section 6 (formerly Section 5, "系统清理工具 (`cm_CleanSystem` / `⌘⇧C`)"):
    - Update ASCII wireframe to tree view with `Group by application` / `Group by category` selector, Search filter, Size/Status/Path columns, mixed-group `+<size> 已保留` indicators, greyed-out kept rows with real measured sizes (or `≥` prefix), and bottom action buttons.
    - Document dual grouping views ("按应用程序分组" 与 "按类别分组").
    - Document real kept sizes and tiered sorting (cleanable groups sort ahead of kept-only groups).
    - Document precise localized retention reasons (应用程序正在运行, 应用程序状态未知, 包含数据库, 被进程占用, 包含符号链接, 文件数量过多, 权限不足, 白名单排除, 受保护数据) and scan status summary.
  - Renumber remaining sections cleanly: Section 7 (应用程序卸载工具), Section 8 (安全提示), Section 9 (主命令速查表).
  - In Section 9 master table: update `cm_DiskUsageAnalyzer` to Menu only, add `cm_RecentChanges` rows, and add System Cleaner grouping/navigation rows.

- [ ] **Step 2: Generate Traditional Chinese `docs/zh-hant/system_tools.md`**
  - Run OpenCC `s2twp` conversion on `docs/zh/system_tools.md`, ensuring Taiwan/HK terms (應用程式, 垃圾桶, 處理程序, 資源庫, 磁碟).
  - Verify ASCII box-drawing lines and table columns align properly.

- [ ] **Step 3: Verify parity and list spacing for Task 2 files**
  - Run: `python3 scripts/check_parity.py --lang zh,zh-hant`
  - Expected: `system_tools.md` [PASS] with 27 headers for both `zh` and `zh-hant`.
  - Run: `./test.sh -l`
  - Expected: PASS.

- [ ] **Step 4: Commit Task 2**
  ```bash
  git add docs/zh/system_tools.md docs/zh-hant/system_tools.md
  git commit -m "docs(zh): sync system_tools with Recent Changes and per-app cleaner to zh and zh-hant"
  ```

---

### Task 3: Sync `file_operations.md`, `power_tools.md`, and `network_and_vfs.md` to Simplified & Traditional Chinese

**Files:**
- Modify: `docs/zh/file_operations.md`
- Modify: `docs/zh-hant/file_operations.md`
- Modify: `docs/zh/power_tools.md`
- Modify: `docs/zh-hant/power_tools.md`
- Modify: `docs/zh/network_and_vfs.md`
- Modify: `docs/zh-hant/network_and_vfs.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md` (Sections 4.4, 4.5, 4.6)
- Produces: Updated Chinese file operations, power tools, and network VFS documentation matching English benchmark structure.

- [ ] **Step 1: Translate and update `docs/zh/file_operations.md`**
  - In Section 2.1: add note explaining **同名冲突自动重命名** (`cm_PasteFromClipboard`): pasting conflicting files automatically appends incremental numeric suffixes (e.g., `report (1).pdf`).
  - In Section 4.3: clarify that `Shift+Click` on an already-selected item batch-deselects that contiguous range without affecting remaining selections outside the range.

- [ ] **Step 2: Translate and update `docs/zh/power_tools.md`**
  - In Section 5.1: note that opening Search (`Cmd+F` / `Alt+F7`) automatically focuses and selects "文件名模式" input for zero-click typing, and guards against Enter double-trigger cancellation.
  - In Section 7.5: document sandboxed terminal handoff (Terminal.app launches at working directory, copies command to clipboard, prompts user to press `⌘V` and Return).

- [ ] **Step 3: Translate and update `docs/zh/network_and_vfs.md`**
  - In Section 2.2: add bullet on remote VFS column sorting & header sync (`VfsTableModel`), supporting Name, Ext, Size, Date Modified, Attributes sorting via header clicks or `⌃F3`–`⌃F6`, dirs pinned on top, sort arrows bidirectionally synchronized with Sort menu.
  - In Section 7 & 8: document on-demand network authentication (`NetworkPasswordDialog`) with password visibility toggle and Keychain checkbox, and in-memory session credential persistence (`VFSSessionCache`) surviving profile edits.

- [ ] **Step 4: Generate Traditional Chinese versions for Task 3 files**
  - Run OpenCC `s2twp` conversion for `file_operations.md`, `power_tools.md`, and `network_and_vfs.md`.
  - Apply Taiwan/HK terms (檔案, 剪貼簿, 終端機, 認證).

- [ ] **Step 5: Verify parity and list spacing for Task 3 files**
  - Run: `python3 scripts/check_parity.py --lang zh,zh-hant`
  - Expected: `file_operations.md`, `power_tools.md`, `network_and_vfs.md` [PASS] for `zh` and `zh-hant`.
  - Run: `./test.sh -l`
  - Expected: PASS.

- [ ] **Step 6: Commit Task 3**
  ```bash
  git add docs/zh/file_operations.md docs/zh-hant/file_operations.md docs/zh/power_tools.md docs/zh-hant/power_tools.md docs/zh/network_and_vfs.md docs/zh-hant/network_and_vfs.md
  git commit -m "docs(zh): sync file_operations, power_tools, and network_and_vfs to zh and zh-hant"
  ```

---

### Task 4: Sync `keyboard_shortcuts.md`, `faq_howtos.md`, `getting_started.md`, and `index.md` to Simplified & Traditional Chinese

**Files:**
- Modify: `docs/zh/keyboard_shortcuts.md`
- Modify: `docs/zh-hant/keyboard_shortcuts.md`
- Modify: `docs/zh/faq_howtos.md`
- Modify: `docs/zh-hant/faq_howtos.md`
- Modify: `docs/zh/getting_started.md`
- Modify: `docs/zh-hant/getting_started.md`
- Modify: `docs/zh/index.md`
- Modify: `docs/zh-hant/index.md`

**Interfaces:**
- Consumes: Tasks 1–3 and `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md` (Sections 4.7, 4.8, 4.9)
- Produces: 100% synchronized Simplified and Traditional Chinese documentation suites passing all parity checks.

- [ ] **Step 1: Translate and update `docs/zh/keyboard_shortcuts.md`**
  - Section 4.3: add `cm_EditPath` (`⇧⌘G` / `Ctrl+Shift+G`); update `cm_ConfigDirHotList` to `⌥⌘D` / `Ctrl+Alt+D`.
  - Section 4.5: add `cm_ToggleLockTab` (`⌘K` / `Ctrl+K`); add `cm_SaveFavoriteTabs` (`⇧⌘D` / `Ctrl+Shift+D`); update lock command descriptions for tab context menu shortcut visibility.
  - Section 4.6: update `cm_CalculateChecksum` to `⌃X` (removing `/ ⌘K`).
  - Section 4.7: update `cm_DiskUsageAnalyzer` to Menu only; add `cm_RecentChanges` row.
  - Section 4.8: add `cm_Tutorial` (32 步交互式新手引导教程) and global system hotkey (`⌘⌥H` / `Ctrl+Alt+H` / `System (Carbon)`).

- [ ] **Step 2: Translate and update `docs/zh/faq_howtos.md`**
  - Section 2.6 (Recipe 6): add `Cmd+K` (`⌘K` / `Ctrl+K` / `cm_ToggleLockTab`) for instant tab locking and right-aligned context menu shortcut hints.
  - Add Section 2.9 (Recipe 9: "配方 9：使用‘输入完整路径并跳转’快速编辑路径与文件直达 (`⌘⇧G`)").
  - Add Section 2.10 (Recipe 10: "配方 10：使用系统托盘常驻与免权限全局快捷键唤出窗口 (`⌘⌥H`)").
  - Add Section 2.11 (Recipe 11: "配方 11：自定义文件面板分栏与查看 macOS 访达颜色标签").

- [ ] **Step 3: Translate and update `docs/zh/getting_started.md` and `docs/zh/index.md`**
  - `getting_started.md`:
    - Interface landmarks: update breadcrumb bar with pencil button (`btn_edit_path` / `⌘⇧G`), tab bar with `Cmd+K` tab locking, and file panels with customizable columns and Finder color tags.
    - Pro tips: add Tip 5 "交互式新手引导教程 (`cm_Tutorial`)" and Tip 6 "后台系统托盘常驻与免权限全局快捷键 (`⌘⌥H`)".
    - Essential shortcuts table: add `cm_EditPath` and `cm_ToggleLockTab`.
  - `index.md`:
    - Landmarks: update pencil button, `Cmd+K`, and custom columns/tags.
    - Track A: recommend 32-step interactive tutorial (`cm_Tutorial`).
    - Master TOC: update Chapter 2, 7, and 8 summary blurbs.

- [ ] **Step 4: Generate Traditional Chinese versions for Task 4 files**
  - Run OpenCC `s2twp` conversion for `keyboard_shortcuts.md`, `faq_howtos.md`, `getting_started.md`, and `index.md`.
  - Apply Taiwan/HK terms (快速鍵, 偏好設定, 互動式教學, 系統選單列).

- [ ] **Step 5: Verify 100% parity across `zh` and `zh-hant`**
  - Run: `python3 scripts/check_parity.py --lang zh,zh-hant`
  - Expected: ALL 13 chapters [PASS] for `zh` and `zh-hant` (0 errors).
  - Run: `./test.sh -l`
  - Expected: PASS.

- [ ] **Step 6: Commit Task 4**
  ```bash
  git add docs/zh/ docs/zh-hant/
  git commit -m "docs(zh): complete Chinese and Traditional Chinese synchronization across all 10 chapters"
  ```

---

### Task 5: Extend Diff Propagation Script and Synchronize 8 Foreign Languages

**Files:**
- Modify: `scripts/propagate_diff_i18n.py`
- Modify: `docs/{ja,de,fr,es,pt,ko,ru,it}/*.md` (10 files per language = 80 files)

**Interfaces:**
- Consumes: Synchronized `docs/en/` benchmark and `docs/superpowers/specs/2026-11-22-multilingual-sync-2.4-2.9-design.md`
- Produces: 100% structural parity across all 8 international languages (`ja, de, fr, es, pt, ko, ru, it`).

- [ ] **Step 1: Extend `scripts/propagate_diff_i18n.py` for v2.4–v2.9 diff propagation**
  - Implement handlers for:
    - `getting_started.md`: add landmark updates, insert Tips 5 & 6, and update shortcut table.
    - `navigation_and_tabs.md`: add `cm_EditPath`, `cm_ToggleLockTab`, pencil button workflow, custom columns, color tags, and hotlist shortcuts.
    - `preferences_and_customization.md`: add tray residency, Carbon hotkey, ASCII diagram, and subsections 4.7 & 4.8.
    - `system_tools.md`: update to 5 tools, add Section 3.2 sandbox mode, insert Section 5 `Recent Changes`, update Section 6 System Cleaner to per-app layout with kept sizes and reasons, renumber sections to 1–9, and update master table.
    - `file_operations.md`: add paste auto-rename and Shift+Click deselect.
    - `power_tools.md`: add search focus and sandboxed terminal handoff.
    - `network_and_vfs.md`: add remote VFS column sorting and on-demand auth / session cache.
    - `keyboard_shortcuts.md`: add `cm_EditPath`, `cm_ToggleLockTab`, `cm_SaveFavoriteTabs`, `cm_RecentChanges`, `cm_Tutorial`, Global Hotkey; update `cm_ConfigDirHotList`, `cm_CalculateChecksum`, and `cm_DiskUsageAnalyzer`.
    - `faq_howtos.md`: update Recipe 6, append Recipes 9, 10, 11.
    - `index.md`: update landmarks, Track A interactive tutorial blurb, and TOC chapter blurbs.

- [ ] **Step 2: Run propagation across all 8 target languages**
  - Run: `python3 scripts/propagate_diff_i18n.py --all`
  - Verify that code blocks, command IDs (`cm_*`), config keys, and shortcut symbols remain protected.

- [ ] **Step 3: Run parity check across all 10 languages**
  - Run: `python3 scripts/check_parity.py`
  - Expected: ALL 10 languages pass with 0 errors across all 13 chapters!

- [ ] **Step 4: Commit Task 5**
  ```bash
  git add scripts/propagate_diff_i18n.py docs/ja/ docs/de/ docs/fr/ docs/es/ docs/pt/ docs/ko/ docs/ru/ docs/it/
  git commit -m "docs(i18n): propagate v2.4-v2.9 updates across ja, de, fr, es, pt, ko, ru, it"
  ```

---

### Task 6: Repository-Wide Format Check, Linting, and Static Build Verification

**Files:**
- Modify: Any files with formatting or list spacing adjustments across `docs/`

**Interfaces:**
- Consumes: Fully synchronized multilingual documentation suite (11 languages total).
- Produces: Production-ready documentation repository with zero lint errors and clean builds.

- [ ] **Step 1: Format Markdown lists across all languages**
  - Run: `python3 scripts/format_markdown_lists.py --fix`
  - Run: `./test.sh -l`
  - Expected: `[PASS] All Markdown lists have proper blank line spacing.`

- [ ] **Step 2: Verify 100% parity across all 10 languages**
  - Run: `python3 scripts/check_parity.py`
  - Expected: `✓ 100% PARITY ACHIEVED: All 10 language(s) pass benchmark verification.` (0 errors).

- [ ] **Step 3: Run full static build for all documentation sites**
  - Run: `./test.sh -b`
  - Expected: All 11 language sites (`en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`) build successfully into `site/` with return code 0.

- [ ] **Step 4: Final verification and commit**
  - Run: `git status`
  - Commit any remaining list formatting fixes:
    ```bash
    git add -u docs/
    git commit -m "docs: finalize multilingual list formatting and parity verification"
    ```
