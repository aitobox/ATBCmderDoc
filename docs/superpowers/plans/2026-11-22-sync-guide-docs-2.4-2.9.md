# Sync Major Feature Updates (v2.4.0 – v2.9.0) to English User Guide Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Seamlessly integrate all 10 major feature areas added between v2.4.0 and v2.9.0 into the 10 thematic Markdown chapters under `docs/guide/en/`, updating prose, ASCII diagrams, configuration tables, dual-matrix keyboard shortcut references, and practical FAQ recipes without adding version callout badges.

**Architecture:** Follow the existing Progressive Tiered Manual architecture across `docs/guide/en/`. Each thematic chapter absorbs its corresponding features directly into primary walkthroughs, visual diagrams, settings descriptions, and Dual-Matrix shortcut tables, followed by cross-file shortcut alignment and end-to-end link/badge verification.

**Tech Stack:** GitHub-Flavored Markdown (`> [!NOTE]` / `> [!TIP]` / `> [!IMPORTANT]` / `> [!WARNING]` / `> [!CAUTION]`), ASCII UI diagrams, Dual-Matrix shortcut tables (`macOS Shortcut` | `Classic Commander Key` | `Command ID`), ATBCmder Python/Qt6 command & config reference (`src/atbcmder/`).

**Spec:** `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md`

## Global Constraints
- Modify only the 10 specified guide files under `docs/guide/en/` (`navigation_and_tabs.md`, `preferences_and_customization.md`, `system_tools.md`, `file_operations.md`, `power_tools.md`, `network_and_vfs.md`, `getting_started.md`, `index.md`, `keyboard_shortcuts.md`, `faq_howtos.md`). Do NOT modify `download.md` or `privacy_policy.md`.
- STRICTLY DO NOT add version callout badges or inline version labels (e.g., `> [!NOTE] Available since v2.9.0` or `(since v2.8.0)`). Every document must read as a unified, current guide.
- Every `cm_*` command ID, configuration section/key, menu path, UI label, and default shortcut must match the `src/atbcmder/` codebase verbatim.
- Preserve existing Markdown formatting conventions, table column layouts, ASCII box-drawing alignments, and cross-chapter navigation footers.

## Review Focus
- Zero version callout badges or inline version tags (`since v2.`, `Available since`, `v2.8`, `v2.9`) anywhere in the 10 modified `docs/guide/en/*.md` files.
- Cross-file shortcut consistency after resolving legacy collisions: `cm_EditPath` (`⇧⌘G` / `Ctrl+Shift+G`), `cm_FocusCmdLine` (`Shift+F2`), `cm_ToggleLockTab` (`⌘K` / `Ctrl+K`), `cm_CalculateChecksum` (`⌃X` / `Ctrl+X`, with `/ ⌘K` removed), `cm_SaveFavoriteTabs` (`⇧⌘D` / `Ctrl+Shift+D`), `cm_ConfigDirHotList` (`⌥⌘D` / `Ctrl+Alt+D`), and `cm_DiskUsageAnalyzer` (Menu only, removing stale `⌘⇧D`).
- Verbatim config keys and UI labels: `view.panel_column_order`, `view.panel_column_visible`, `view.show_color_tags`, `view.color_tag_sync_interval_ms`, `view.trackpad_swipe_navigation`, `ui.minimize_to_tray`, `ui.global_hotkey`, `Group by category`, `Group by application`, `Current user processes`, `Current user processes (App Sandbox)`, `Enter Full Path and Go`.
- Section numbering and internal anchor links remain consistent after inserting the `Recent Changes` section in `system_tools.md` and Recipes 9–11 in `faq_howtos.md`.
- All relative links to `.md` files and `images/*.png` assets under `docs/guide/en/` resolve to existing files on disk.

---

### Task 1: Update Path Editing (`cm_EditPath`), Tab Locking (`⌘K`), Trackpad Swipe, Customizable Columns & Finder Color Tags in `docs/guide/en/navigation_and_tabs.md`

**Files:**
- Modify: `docs/guide/en/navigation_and_tabs.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Section 4.1)
- Produces: Updated `docs/guide/en/navigation_and_tabs.md` with verified path-bar edit workflow (`btn_edit_path` / `⌘⇧G` / `cm_EditPath`), `⌘K` tab lock toggle & context menu shortcuts, tuned trackpad swipe navigation, customizable panel columns, Finder color tags, and corrected shortcut rows.

- [x] **Step 1: Update Section 1 Dual-Matrix Navigation Cheat Sheet**
  - In `docs/guide/en/navigation_and_tabs.md` Section 1 table (`Dual-Matrix Navigation Cheat Sheet`):
    - Add row for **Enter Full Path & Go**: `Cmd+Shift+G` / `⌘⇧G` | `Ctrl+Shift+G` | `cm_EditPath` | Switch path bar to inline text input and jump directly.
    - Add row for **Lock / Unlock Tab**: `Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab` | Toggle lock state (`*`) on the active folder tab.
    - Verify `Trackpad Swipe Navigation` row remains intact.

- [x] **Step 2: Update Section 2 Breadcrumb ASCII & Item 4 ("Direct Path Text Editing")**
  - Update the breadcrumb ASCII diagram or Section 2 item 4 (`Direct Path Text Editing`):
    - Remove the inaccurate `(or press Shift+F2)` trigger (`Shift+F2` is `cm_FocusCmdLine`).
    - Document all three verified entry points:
      1. Click the pencil icon button (**Enter Full Path and Go**, `btn_edit_path`) positioned immediately to the left of the Parent Directory (`btn_up`) button.
      2. Double-click the blank space to the right of the breadcrumb chain.
      3. Press **`Cmd+Shift+G`** (`⌘⇧G` / `Ctrl+Shift+G`), or choose **Commands ➔ Enter Full Path and Go** (`cm_EditPath`).
    - Document full path submission semantics:
      - Pre-fills and selects the active path so pasting with `⌘V` replaces it immediately.
      - Input normalization: trims leading/trailing whitespace, strips matching outer quotes (`"..."` or `'...'`), expands `~`, `$VAR`, and `%VAR%`, resolves relative local paths against the current directory, and preserves `vfs://` URIs verbatim.
      - **Direct File Jumping**: If the entered path points to an existing local file, ATBCmder navigates to its parent folder and highlights/focuses that file in the panel.
      - **Inline Error Retention**: If the path does not exist or fails to load, the editor stays open with a red error border and a non-blocking status bar message so you can fix typos without re-pasting; typing clears the red border, and pressing `Esc`, clicking outside, or clicking `btn_edit_path` again cancels and restores breadcrumbs.

- [x] **Step 3: Update Section 3 ("Folder Tabs"), Section 4 ("Favorite Tabs"), and Section 5 ("Directory Hotlists")**
  - In Section 3 (`Tab Operations & Hotkeys` table and `Tab Locking Modes`):
    - Add row `Lock / Unlock Tab` | `Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab` | Toggle active tab between normal and locked (`*`).
    - Update `Save Favorite Tabs` description in Section 4 to include `Cmd+Shift+D` (`⌘⇧D` / `Ctrl+Shift+D` / `cm_SaveFavoriteTabs`).
    - Document in `Tab Locking Modes` that:
      - `Cmd+K` (`⌘K` / `Ctrl+K` / `cm_ToggleLockTab`) provides instant single-chord toggling between unlocked and **Lock this tab** (and unlocks **Locked, but directory changes allowed** / `cm_SetTabOptionLockNoNavigation`).
      - Both the top **Tabs** menu and the macOS tab bar right-click context menu display right-aligned shortcuts (`⌘T`, `⌘W`, `⌘K`, `⇧⌘D`, etc.) synchronized with `HotkeyManager`, dynamically showing `⌘K` next to whichever lock/unlock action executes next.
  - In Section 5 (`Hotlist Configuration` heading):
    - Update `Ctrl+Shift+D` / `⌃⇧D` to `Option+Cmd+D` / `⌥⌘D` (or `Ctrl+Alt+D`) for `cm_ConfigDirHotList`, keeping `⌘⇧D` dedicated to `cm_SaveFavoriteTabs`.

- [x] **Step 4: Update Section 6 ("MacBook Trackpad Horizontal Swipe Navigation")**
  - Expand the bullet list under `MacBook Trackpad Horizontal Swipe Navigation` to reflect tuned gesture sensitivity and broad hardware compatibility across built-in MacBook trackpads and Apple Magic Trackpads, noting its equivalence to `Option+Left` / `Option+Right` (`cm_ViewHistoryPrev` / `cm_ViewHistoryNext`) and configuration under **Preferences** (`Cmd+,`) → **File Views** (`view.trackpad_swipe_navigation`).

- [x] **Step 5: Update Section 7.1 ("Full Columns View") with Customizable Columns & Finder Color Tags**
  - Under Section 7.1 (`Full Columns View`), add two concise notes/bullets:
    - **Customizable Column Visibility & Order**: Configure which secondary columns (`Ext`, `Size`, `Modified`, `Permissions`, `Owner`) are visible and drag them into any display order globally across both panels in **Preferences ➔ File Views ➔ Columns** (`view.panel_column_order`, `view.panel_column_visible`); the `Name` column always remains first.
    - **macOS Finder Color Tags (`color_tag`)**: Enable **Show macOS Finder color tags in file panel** (`view.show_color_tags`) in **Preferences ➔ File Views** to display a dedicated tag dot column with localized tooltips for all 7 standard Finder colors (`Red`, `Orange`, `Yellow`, `Green`, `Blue`, `Purple`, `Gray`) across all 31 UI languages alongside custom user tags.

- [x] **Step 6: Update Section 11 ("Dual-Matrix Keyboard Reference Table")**
  - Add `Enter Full Path and Go` (`Cmd+Shift+G` / `⌘⇧G` | `Ctrl+Shift+G` | `cm_EditPath`) under **Directory Navigation**.
  - Add `Lock / Unlock Active Tab` (`Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab`) under **Folder Tabs**, and note context-menu shortcut visibility.
  - Update `Save Favorite Tabs` under **Favorite Tabs** to `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_SaveFavoriteTabs`.
  - Update `Configure Hotlist` under **Hotlists & History** to `Option+Cmd+D` / `⌥⌘D` | `Ctrl+Alt+D` | `cm_ConfigDirHotList`.

- [x] **Step 7: Verify `docs/guide/en/navigation_and_tabs.md`**
  - Run: `grep -n -E "Shift\+F2|Available since|v2\." docs/guide/en/navigation_and_tabs.md`
  - Expected: 0 matches (no stale `Shift+F2` for breadcrumb edit and 0 version badges).

- [x] **Step 8: Commit Task 1**
  ```bash
  git add docs/guide/en/navigation_and_tabs.md
  git commit -m "docs(guide): document path bar edit button, Cmd+K tab lock, trackpad tuning, and custom columns in navigation_and_tabs.md"
  ```

---

### Task 2: Update System Tray Residency, Carbon Global Hotkey (`⌘⌥H`), Customizable Columns & Color Tags in `docs/guide/en/preferences_and_customization.md`

**Files:**
- Modify: `docs/guide/en/preferences_and_customization.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Section 4.2)
- Produces: Updated `docs/guide/en/preferences_and_customization.md` covering high-frequency tray residency + Carbon permission-free global hotkeys (`⌘⌥H`), customizable panel column visibility/drag-ordering, macOS Finder color tags configuration, and corrected hotkey table entries.

- [x] **Step 1: Update Section 1 Cheat Sheet & Section 2.2 Table**
  - In Section 1 (`Dual-Matrix Preferences & Customization Cheat Sheet`):
    - Update `Directory Hotlist Setup` (`cm_ConfigDirHotList`) shortcut to `Option+Cmd+D` / `⌥⌘D` | `Ctrl+Alt+D`.
  - In Section 2.2 (`Comprehensive Configuration Page Directory`):
    - Update the `File Views` row to explicitly include **customizable column visibility and drag-to-reorder** (`view.panel_column_order`, `view.panel_column_visible`) and **macOS Finder color tags** (`view.show_color_tags`, `view.color_tag_sync_interval_ms`).

- [x] **Step 2: Expand Section 3.5 ("Global Show/Hide Window Hotkey (`Cmd+Opt+H` / `Ctrl+Alt+H`)")**
  - Rewrite Section 3.5 to cover the full high-frequency background residency workflow:
    - Step-by-step setup in **Preferences ➔ General**: check **Minimize to system tray (Requires Restart)** (`ui.minimize_to_tray`) and restart ATBCmder once so the tray menu bar icon activates.
    - Explain tray behavior: minimizing or hiding sends ATBCmder to the macOS menu bar tray (`Show Main Window`, `Options`, `Exit`) so it stays resident in memory with zero Dock clutter while preserving open tabs and active panels.
    - Explain the **Show/Hide Window Hotkey** (`ui.global_hotkey`, default `Ctrl+Alt+H` / `⌘⌥H` on macOS, takes effect immediately without restart, includes a **Reset** button): pressing the global chord from any app or full-screen space restores and raises the window to its exact previous geometry/maximized state, or hides it back to the tray if currently active.
    - Highlight macOS native implementation details: uses native macOS Carbon `RegisterEventHotKey` APIs so global hotkeys work **out of the box without requiring Accessibility permissions** in macOS System Settings, and uses Option-key (`⌥`) virtual-key normalization (`_MacAwareKeySequenceEdit`) to prevent dead-key/diacritic capture conflicts.

- [x] **Step 3: Update Section 4 ("File Views, Column Modes & Thumbnail Management")**
  - Update the Section 4 ASCII wireframe (`FILE VIEWS CONFIGURATION`) to include the top `[ Columns ]` group (`⠿ [X] Ext`, `⠿ [X] Size`, `⠿ [X] Modified`, `⠿ [X] Permissions`, `⠿ [X] Owner`, `[ Reset to Defaults ]`) and the `[ Color Tags (macOS) ]` group (`[X] Show macOS Finder color tags in file panel`, `Live-sync interval: [ 30.0 s ]`).
  - Add subsection **4.7 Customizable Column Visibility & Ordering (`view.panel_column_order`, `view.panel_column_visible`)**:
    - Document toggling checkboxes to show/hide `Ext`, `Size`, `Modified`, `Permissions`, and `Owner` globally for both panels (`Name` always remains first).
    - Document dragging the `⠿` handle to reorder columns, clicking **Reset to Defaults**, immediate effect on **Apply**/**OK**, and interaction with Brief View (Brief View always shows Name-only while preserving your custom column layout when switching back to Full Columns View).
  - Add subsection **4.8 macOS Finder Color Tags (`view.show_color_tags`, `view.color_tag_sync_interval_ms`)**:
    - Document enabling **Show macOS Finder color tags in file panel** and adjusting **Live-sync interval** (`0` = Disabled up to `300 s`, default `30.0 s`).
    - Explain canonicalized 7-color Finder tag rendering (`Red`, `Orange`, `Yellow`, `Green`, `Blue`, `Purple`, `Gray`) with 31-language localized tooltips plus verbatim display of custom user tags.

- [x] **Step 4: Update Section 11 ("Master Dual-Matrix Customization & Preferences Command Reference")**
  - Update `Directory Hotlist Manager` (`cm_ConfigDirHotList`) to `Option+Cmd+D` / `⌥⌘D` | `Ctrl+Alt+D`.
  - Update `Save Current Tabs as Favorite Set` (`cm_SaveFavoriteTabs`) to `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D`.

- [x] **Step 5: Verify `docs/guide/en/preferences_and_customization.md`**
  - Run: `grep -n -E "Available since|since v2\." docs/guide/en/preferences_and_customization.md`
  - Expected: 0 matches.

- [x] **Step 6: Commit Task 2**
  ```bash
  git add docs/guide/en/preferences_and_customization.md
  git commit -m "docs(guide): document tray residency, Carbon global hotkeys, custom columns, and Finder color tags in preferences_and_customization.md"
  ```

---

### Task 3: Add `Recent Changes` (`cm_RecentChanges`), Sandbox Dual-Mode `System Status`, and Per-App `System Cleaner` with Kept Sizes/Reasons in `docs/guide/en/system_tools.md`

**Files:**
- Modify: `docs/guide/en/system_tools.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Section 4.3)
- Produces: Updated `docs/guide/en/system_tools.md` covering all 5 system tools (`System Status`, `Disk Usage Analyzer`, `Recent Changes`, `System Cleaner`, `Application Uninstaller`), renumbered cleanly with updated diagrams, shortcut tables, and sandbox/cleaner details.

- [x] **Step 1: Update Chapter Intro & Section 1 ("Visual Quickstart: System Tools & Status HUD")**
  - Update intro copy from "four specialized system maintenance and diagnostic tools" to **five integrated system maintenance and diagnostic tools**.
  - Update the Section 1 ASCII summary card (`ATBCMDER SYSTEM TOOLS SUITE`) to include `[4] Recent File & Folder Changes (cm_RecentChanges)` (renumbering System Cleaner and Application Uninstaller to `[5]` and `[6]` alongside Status Capsule `[1]`).
  - Update `Dual-Matrix System Tools Shortcut Matrix`:
    - Change `Disk Usage Analyzer` shortcut columns to `*(Menu: Tools ➔ Disk Usage Analyzer...)*` | — | `cm_DiskUsageAnalyzer` | **Tools ➔ Disk Usage Analyzer...** (removing the obsolete `⌘⇧D` / `Ctrl+Shift+D` binding).
    - Add `Recent Changes` | `*(Menu: Tools ➔ View Recently Modified Files/Folders...)*` | — | `cm_RecentChanges` | **Tools ➔ View Recently Modified Files/Folders...**.

- [x] **Step 2: Update Section 2 (`StatusPopup`) and Section 3 (`SystemStatusPanel`) for Sandbox Dual-Mode & Top Processes**
  - In Section 2.2 (`Interactive Popover (StatusPopup)`):
    - Explain that **Top 5 Processes** ranks live processes by both CPU % and memory footprint out of the box even inside Mac App Store sandboxed builds, displaying the `Current user processes` scope indicator when sandboxed.
  - In Section 3 (`System Status & Diagnostics`):
    - Add a dedicated subsection **3.2 Mac App Store Sandbox Mode (`Top Processes` + `Running Applications`)**:
      - Explain native Darwin process collection (`sysctl KERN_PROC_UID` + `proc_pidinfo`) surfacing current-user apps, CLI tools, language servers, and helper processes with `Current user processes (App Sandbox)`.
      - Document the dual-tab bottom pane hosting **Top Processes** (default tab) and **Running Applications** (second tab, displaying regular & menu-bar accessory apps with cached main-thread icons and filtering out background widget/XPC noise).
      - Document sandbox-compliant context menu actions on process rows: **Quit**, **Force Quit**, **Bring to Front**, and **Reveal in Finder** (when the PID corresponds to a GUI app) plus **View in Activity Monitor…**, without offering `SIGTERM`/`SIGKILL`.

- [x] **Step 3: Insert Section 5 — "Recent File & Folder Changes (`cm_RecentChanges`)" (after Disk Usage Analyzer, renumbering System Cleaner to Section 6, Application Uninstaller to Section 7, Alerts to Section 8, Master Table to Section 9)**
  - Document **Tools ➔ View Recently Modified Files/Folders...** (`cm_RecentChanges`):
    - Purpose & ASCII layout showing path input (`Browse...`), type filters (`Files`, `Folders`), time presets (`Last hour`, `Last day`, `Last week`, `Custom time range` with start/end timestamps), and minimum size filter (`Ignore files smaller than`: `1 KB`, `1 MB`, `10 MB`, or `Custom size` in `B`/`KB`/`MB`/`GB`).
    - Search engine & results table (`Name`, `Type`, `Size on disk`, `Matched modification time`, `Path`, `Status`): seeds fresh searches with macOS Spotlight candidates for instant responsiveness while computing folder disk usage (`≥` prefix for lower-bound partial results).
    - Interactive filter & actions: real-time case-insensitive name/path filter box, double-click or **Reveal in Finder**, **Open in ATBCmder Panel**, and **Move to Trash**.

- [x] **Step 4: Rewrite Section 6 ("System Cleaner (`cm_CleanSystem` / `⌘⇧C`)") for Per-Application Tree View, Kept Sizes & Precise Reasons**
  - Replace the outdated category-only ASCII diagram with the modern **System Cleaner** tree layout showing the **Group by application** / **Group by category** selector, live **Search...** filter, `Size` + `Status` + `Path` columns, mixed-group `+<size> kept` indicators, greyed-out kept entries with real measured sizes (or `≥` lower-bound prefix), and bottom **Reveal in Finder** / **Open in ATBCmder Panel** buttons.
  - Document:
    - **Dual Grouping Views**: Switch seamlessly between **Group by category** and **Group by application** to review and clean caches, logs, and browser profiles per app without losing selections.
    - **Real Kept Sizes & Tiered Size Sorting**: Kept items display actual read-only measured footprints (or `≥` lower bounds when hitting traversal/permission limits) instead of `Unknown`; mixed groups display only cleanable bytes in `Size` (matching `Total Reclaimable`) and `+<size> kept` in `Status`; sorting by `Size` ranks cleanable groups ahead of kept-only groups.
    - **Precise Localized Retention Reasons & Scan Completeness**: List the retention reasons (`Application is running`, `Application state is unknown`, `Contains database`, `In use by a process`, `Cannot verify if in use`, `Contains symbolic link`, `Too many files`, `No write permission`, `Excluded by whitelist`, `Protected data`) and explain the bottom scan status summary (`Scan completed (%1 item(s) could not be fully verified). Select items to clean.`).
    - **Quick Navigation**: Double-clicking a row or clicking **Reveal in Finder** / **Open in ATBCmder Panel** opens the target path directly.

- [x] **Step 5: Update Renumbered Section 9 ("Master Dual-Matrix System Tools Reference Table")**
  - Update `Disk Analyzer` open shortcut from `Cmd+Shift+D` / `⌘⇧D` to `*(Menu: Tools ➔ Disk Usage Analyzer...)*`.
  - Add `Recent Changes` rows (`Open Recent Changes Tool` via `Menu: Tools ➔ View Recently Modified Files/Folders...` / `cm_RecentChanges`, `Filter Recent Results`, `Reveal in Finder`, `Open in ATBCmder Panel`, `Move to Trash`).
  - Add `System Cleaner` rows for `Switch Grouping (Category / App)`, `Reveal in Finder`, and `Open in ATBCmder Panel`.

- [x] **Step 6: Verify `docs/guide/en/system_tools.md`**
  - Verify section heading hierarchy (`## 1.` through `## 9.`) is strictly sequential and run: `grep -n -E "⌘⇧D|Ctrl\+Shift\+D|Available since|v2\." docs/guide/en/system_tools.md`
  - Expected: 0 matches.

- [x] **Step 7: Commit Task 3**
  ```bash
  git add docs/guide/en/system_tools.md
  git commit -m "docs(guide): add Recent Changes, sandbox Top Processes dual-tabs, and per-app System Cleaner details to system_tools.md"
  ```

---

### Task 4: Update Clipboard Auto-Rename, `Shift+Click` Deselect, Search Focus, Sandboxed Terminal Handoff, and Network VFS Auth/Sorting in `file_operations.md`, `power_tools.md`, and `network_and_vfs.md`

**Files:**
- Modify: `docs/guide/en/file_operations.md`
- Modify: `docs/guide/en/power_tools.md`
- Modify: `docs/guide/en/network_and_vfs.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Sections 4.4, 4.5, 4.6)
- Produces: Synchronized `file_operations.md`, `power_tools.md`, and `network_and_vfs.md`.

- [x] **Step 1: Update `docs/guide/en/file_operations.md`**
  - In Section 2.1 (`Standard macOS Clipboard (Cmd+C ➔ Cmd+V)`): add a note explaining **Collision-Safe Paste Auto-Rename** (`cm_PasteFromClipboard`): pasting items whose names already exist in the destination automatically appends incremental numeric suffixes (e.g., `report (1).pdf`, `report (2).pdf`) so existing files are never silently overwritten.
  - In Section 4.3 (`Range and Point Selection` -> `Mouse & Trackpad`): clarify that `Shift+Click` extends a contiguous selection from the anchor row—and when `Shift+Click`ing on an already-selected item, batch-deselects that contiguous range without losing remaining selections outside the range.

- [x] **Step 2: Update `docs/guide/en/power_tools.md`**
  - In Section 5.1 (`Launching Search`): note that opening the Search dialog (`Cmd+F` / `Alt+F7`) focuses and selects the **File Names Pattern** input immediately for zero-click typing, and safely guards against accidental search cancellation caused by `Enter` double-triggering.
  - In Section 7.5 (`Embedded System Terminal`): document the two macOS execution behaviors when launching external shell commands from the bottom command bar (`MainWindow.cmd_edit`) or terminal launcher:
    - Standard builds launch your configured terminal (`Terminal.app`, `iTerm2`, etc.) in the active panel directory with the command pre-filled.
    - Mac App Store sandboxed builds open the configured terminal at the resolved working directory, copy the exact command text to the system clipboard, and display a status bar prompt guiding you to press `⌘V` and `Return` to run it cleanly outside the sandbox.

- [x] **Step 3: Update `docs/guide/en/network_and_vfs.md`**
  - In Section 2.2 (`Seamless Dual-Panel Integration`): add a bullet on **Network VFS Column Sorting & Header Sync** explaining that remote network panels (`VfsTableModel`) support sorting by `Name`, `Ext`, `Size`, `Date Modified`, and `Attributes` via column header clicks or sort hotkeys (`⌃F3`–`⌃F6`), always keeping directories pinned at the top and keeping header sort arrows synchronized bidirectionally with the **Sort** menu.
  - In Section 7 (`Quick Connect vs. Connection Manager`) and Section 8 (`Credential Safety & Keychain Integration`): document **On-Demand Network Authentication (`NetworkPasswordDialog`)** and **Session Credential Persistence (`VFSSessionCache`)**:
    - Navigating to an unremembered SFTP, FTP/FTPS, SMB, or WebDAV connection automatically prompts via `NetworkPasswordDialog` (with username edit, password show/hide toggle, and optional **Remember password (stored in system keychain)** checkbox); canceling rolls back navigation cleanly.
    - Credentials entered without saving in Keychain remain cached in memory (`VFSSessionCache`) for the current application session and survive profile edits in Connection Manager without requiring re-entry.

- [x] **Step 4: Verify `file_operations.md`, `power_tools.md`, and `network_and_vfs.md`**
  - Run: `grep -n -E "Available since|since v2\." docs/guide/en/file_operations.md docs/guide/en/power_tools.md docs/guide/en/network_and_vfs.md`
  - Expected: 0 matches.

- [x] **Step 5: Commit Task 4**
  ```bash
  git add docs/guide/en/file_operations.md docs/guide/en/power_tools.md docs/guide/en/network_and_vfs.md
  git commit -m "docs(guide): update clipboard auto-rename, Shift+Click deselect, sandbox terminal handoff, and network VFS auth/sorting"
  ```

---

### Task 5: Update Master Shortcut Tables in `docs/guide/en/keyboard_shortcuts.md` and Add Practical Recipes in `docs/guide/en/faq_howtos.md`

**Files:**
- Modify: `docs/guide/en/keyboard_shortcuts.md`
- Modify: `docs/guide/en/faq_howtos.md`

**Interfaces:**
- Consumes: Tasks 1–4 and `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Sections 4.8, 4.9)
- Produces: Conflict-free master shortcut reference (`keyboard_shortcuts.md`) and updated step-by-step recipes (`faq_howtos.md`).

- [x] **Step 1: Update `docs/guide/en/keyboard_shortcuts.md`**
  - **Section 4.3 (`Panel Navigation & Bookmarks`)**:
    - Add `cm_EditPath` | Enter full path and go (switch path bar to inline text input) | `⇧⌘G` | `Ctrl+Shift+G` | `Main`.
    - Update `cm_ConfigDirHotList` shortcut columns from `⇧⌘D` / `Ctrl+Shift+D` to `⌥⌘D` / `Ctrl+Alt+D`.
  - **Section 4.5 (`Tabs & Window Management`)**:
    - Add `cm_ToggleLockTab` | Lock / unlock active folder tab (`*` indicator) | `⌘K` | `Ctrl+K` | `Main`.
    - Add `cm_SaveFavoriteTabs` | Save current tabs to a New Favorite Tabs | `⇧⌘D` | `Ctrl+Shift+D` | `Main`.
    - Update `cm_SetTabOptionLock`, `cm_SetTabOptionLockWithSubdirs`, and `cm_SetTabOptionNormal` descriptions to note macOS tab context menu shortcut visibility and dynamic `⌘K` hint.
  - **Section 4.6 (`Power Tools & Utilities`)**:
    - Update `cm_CalculateChecksum` shortcut from `` `⌃X` / `⌘K` `` to `` `⌃X` `` so `⌘K` belongs exclusively to `cm_ToggleLockTab`.
  - **Section 4.7 (`Integrated System Tools`)**:
    - Update `cm_DiskUsageAnalyzer` shortcut columns to `*(Menu: Tools ➔ Disk Usage Analyzer...)*` | `*(Menu: Tools ➔ Disk Usage Analyzer...)*` (removing stale `⌘⇧D` / `Ctrl+Shift+D`).
    - Add `cm_RecentChanges` | Open Recent File & Folder Changes Tool | `*(Menu: Tools ➔ View Recently Modified Files/Folders...)*` | `*(Menu: Tools ➔ View Recently Modified Files/Folders...)*` | `Main`.
  - **Section 4.8 (`System, Configuration & Help`)**:
    - Add `cm_Tutorial` | Launch 32-step Interactive Onboarding Tutorial | `*(Menu: Help ➔ Interactive Tutorial...)*` | `*(Menu: Help ➔ Interactive Tutorial...)*` | `Main`.
    - Add `*(Global System Hotkey)*` | Show / hide ATBCmder window from system tray (`ui.global_hotkey`) | `⌘⌥H` | `Ctrl+Alt+H` | `System (Carbon)`.

- [x] **Step 2: Update `docs/guide/en/faq_howtos.md`**
  - Update **Section 2.6 ("Recipe 6: Protecting Workspaces with Total Commander-Style Tab Locking")**:
    - Include **`Cmd+K`** (`⌘K` / `Ctrl+K` / `cm_ToggleLockTab`) for instant locking/unlocking and mention visible right-aligned shortcuts in the macOS tab bar right-click menu.
  - Add **Section 2.9 ("Recipe 9: Instant Path Editing & Direct File Jumping with 'Enter Full Path and Go' (`⌘⇧G`)")**:
    - Walk through clicking the pencil button (`btn_edit_path`), double-clicking empty breadcrumb space, or pressing `Cmd+Shift+G` (`⌘⇧G`), pasting quoted paths or `~`/env paths, automatic parent jump + file highlight when pasting a file path, and red-border error retention on typos.
  - Add **Section 2.10 ("Recipe 10: Staying Resident in the Background with System Tray & Global Hotkey (`⌘⌥H`)")**:
    - Walk through checking **Minimize to system tray (Requires Restart)** in **Preferences ➔ General**, restarting once, customizing **Show/Hide Window Hotkey** (default `Cmd+Option+H` / `⌘⌥H`) using permission-free Carbon `RegisterEventHotKey` (zero Accessibility permissions needed), and toggling ATBCmder instantaneously from anywhere.
  - Add **Section 2.11 ("Recipe 11: Customizing File Panel Columns & Viewing macOS Finder Color Tags")**:
    - Walk through opening **Preferences ➔ File Views**, toggling and drag-reordering columns (`Ext`, `Size`, `Modified`, `Permissions`, `Owner`), and enabling localized macOS **Finder Color Tags** with configurable live-sync interval.

- [x] **Step 3: Verify `keyboard_shortcuts.md` and `faq_howtos.md`**
  - Run: `grep -n -E "⌘K.*Checksum|⌘⇧D.*Disk|Available since|since v2\." docs/guide/en/keyboard_shortcuts.md docs/guide/en/faq_howtos.md`
  - Expected: 0 matches.

- [x] **Step 4: Commit Task 5**
  ```bash
  git add docs/guide/en/keyboard_shortcuts.md docs/guide/en/faq_howtos.md
  git commit -m "docs(guide): sync master keyboard shortcuts and add FAQ recipes for path bar, tray hotkey, and custom columns"
  ```

---

### Task 6: Update Interactive Tutorial (`cm_Tutorial`), Landmarks & Overviews in `getting_started.md` and `index.md`, and Run End-to-End Doc Audit

**Files:**
- Modify: `docs/guide/en/getting_started.md`
- Modify: `docs/guide/en/index.md`

**Interfaces:**
- Consumes: Tasks 1–5 and `docs/superpowers/specs/2026-11-22-sync-guide-docs-2.4-2.9-design.md` (Section 4.7)
- Produces: Synchronized `getting_started.md` and `index.md` entry portals plus verified `docs/guide/en/` documentation suite.

- [x] **Step 1: Update `docs/guide/en/getting_started.md`**
  - In Section 2 (`Interface Anatomy & Landmark Tour`):
    - `[3] Finder-Style Interactive Breadcrumb Bar`: Replace outdated double-click-only note with all three triggers including the pencil **Enter Full Path and Go** button (`btn_edit_path` / `⌘⇧G` / `cm_EditPath`), quote/tilde normalization, direct file-path highlight, and red-border error retention.
    - `[4] Folder Tab Bar`: Mention **`Cmd+K`** (`⌘K` / `cm_ToggleLockTab`) for instant tab lock toggling and visible right-aligned keyboard shortcuts in macOS tab context menus.
    - `[5] Dual File Panels`: Mention customizable column visibility and drag-to-reorder (`Preferences ➔ File Views`) plus optional macOS Finder color tags.
  - Under Section 5 (`Pro Tips & Advanced Layout Configurations`):
    - Add **Tip 5: Interactive Onboarding Tutorial (`cm_Tutorial`)** explaining **Help ➔ Interactive Tutorial...** (32 spotlighted interactive & observation steps).
    - Add **Tip 6: Background System Tray Residency & Permission-Free Global Hotkey (`⌘⌥H`)** summarizing the fast-toggle residency workflow.
  - In Section 7 (`Dual-Matrix Essential Shortcuts Quick Reference`):
    - Add `Enter Full Path & Go` (`cm_EditPath`, `⌘⇧G`, `Ctrl+Shift+G`) and `Lock / Unlock Tab` (`cm_ToggleLockTab`, `⌘K`, `Ctrl+K`).

- [x] **Step 2: Update `docs/guide/en/index.md`**
  - In `UI Landmark Reference`:
    - `[3]`: Mention the **Enter Full Path and Go** button (`btn_edit_path` / `⌘⇧G`) alongside clickable breadcrumb segments.
    - `[4]`: Mention **`Cmd+K`** (`cm_ToggleLockTab`) lock toggling and visible tab context menu shortcuts.
    - `[5]`: Mention customizable panel columns and macOS Finder color tags alongside Lucide icons, trackpad swipe, pinyin quick search, and extension masks.
  - In `Track A: New to Dual-Panel File Managers?`:
    - Mention launching the 32-step **Interactive Tutorial** (**Help ➔ Interactive Tutorial...** / `cm_Tutorial`) as a guided hands-on first step.
  - In `Master Table of Contents`:
    - Chapter 2: mention **Enter Full Path and Go (`Cmd+Shift+G`)** and **`Cmd+K` tab locking**.
    - Chapter 7: list all 5 integrated system tools, adding **Recent Changes** (`cm_RecentChanges`) and per-application **System Cleaner** with transparent kept-size metrics.
    - Chapter 8: mention customizable panel columns, Finder color tags, and background system tray residency with permission-free global hotkeys (`Cmd+Opt+H`).

- [x] **Step 3: Run End-to-End Verification Audit Across All `docs/guide/en/*.md` Files**
  - Verify zero prohibited version badges or inline version tags exist across all 10 modified chapters:
    - Run: `grep -rn -i -E "available since|since v2\.|added in v2\.|\(v2\.[4-9]" docs/guide/en/ --exclude=download.md`
    - Expected: 0 matches.
  - Verify zero stale shortcut conflicts remain across `docs/guide/en/`:
    - Run: `grep -rn -E "Shift\+F2.*breadcrumb|breadcrumb.*Shift\+F2|⌘K.*Checksum|Checksum.*⌘K|DiskUsage.*⌘⇧D|⌘⇧D.*Disk" docs/guide/en/`
    - Expected: 0 matches.
  - Verify all markdown links (`[...](*.md)` and `![...](images/*)`) in `docs/guide/en/` resolve to existing files using a quick Python one-liner via `conda run -n ATBCmder python -c "..."`.
  - Expected: All links valid, exit code 0.

- [x] **Step 4: Commit Task 6**
  ```bash
  git add docs/guide/en/getting_started.md docs/guide/en/index.md
  git commit -m "docs(guide): update getting_started and index portals for interactive tutorial and 2.4-2.9 parity"
  ```
