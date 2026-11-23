#!/usr/bin/env python3
"""
scripts/propagate_diff_i18n.py
Propagates v2.4.0–v2.9.0 new feature additions and diffs across foreign languages
(ja, de, fr, es, pt, ko, ru, it) while preserving existing localized ASCII
architecture diagrams and mentor polish.
"""

import argparse
import os
import re
import sys
import time
from typing import Dict, List, Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from scripts.batch_translate import (
    protect_section_body,
    restore_placeholders,
    translate_snippet,
    apply_terminology,
    save_cache,
    MACOS_TERMS,
)
from scripts.mentor_style_guide import TERMINOLOGY_REPLACEMENTS
from scripts.format_markdown_lists import process_content as format_lists_content
from scripts.check_parity import check_file_parity

TARGET_LANGUAGES = ["ja", "de", "fr", "es", "pt", "ko", "ru", "it"]


def trans_snippet(text: str, to_lang: str) -> str:
    """Translates text while protecting code, links, inline code, and HTML tags."""
    if not text.strip():
        return text
    prot, phs = protect_section_body(text)
    trans = translate_snippet(prot, to_lang=to_lang, engine="google", use_cache=True)
    restored = restore_placeholders(trans, phs)
    # Apply terminology
    restored = apply_terminology(restored, to_lang)
    mentor_terms = TERMINOLOGY_REPLACEMENTS.get(to_lang, {})
    for k, v in mentor_terms.items():
        if k in restored:
            restored = restored.replace(k, v)
    return restored


def propagate_file_operations(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "file_operations.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update space calculation shortcut to Alt+Shift+Return / ⌥⇧⏎
    content = content.replace("`Alt+Shift+Enter` / `⌥⇧⏎`", "`Alt+Shift+Return` / `⌥⇧⏎`")
    content = content.replace("`Alt+Shift+Enter`", "`Alt+Shift+Return`")

    # 2. Add collision-safe clipboard paste auto-rename in Section 4.1 if not present
    if "auto-rename" not in content and "自動名前変更" not in content and "auto-renommage" not in content and "自动重命名" not in content:
        en_paste = """- **Collision-Safe Paste Auto-Rename**: When pasting items into a directory that already contains identical filenames, ATBCmder automatically appends an incrementing counter (`file (1).ext`, `file (2).ext`) rather than triggering destructive overwrites, matching macOS Finder paste ergonomics."""
        trans_paste = trans_snippet(en_paste, lang)
        m = re.search(r"(?m)^-\s+.*?(?:Paste|Einfügen|Coller|Pegar|Colar|붙여넣기|Вставить|Incolla).*?$", content)
        if m:
            idx = m.end()
            content = content[:idx] + "\n" + trans_paste.strip() + content[idx:]

    # 3. Add Shift+Click range deselection in Section 5.1 if not present
    if "range deselect" not in content and "範囲選択解除" not in content and "deselección de rango" not in content and "反选" not in content:
        en_shift = """- **Shift+Click Range Deselection**: Hold `Shift` and click an already-selected range to cleanly invert or deselect specific spans without losing your broader multi-file selection state."""
        trans_shift = trans_snippet(en_shift, lang)
        m = re.search(r"(?m)^-\s+.*?(?:Shift\+Click|Shift).*?$", content[4000:])
        if m:
            idx = 4000 + m.end()
            content = content[:idx] + "\n" + trans_shift.strip() + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] file_operations.md updated.")
    return True


def propagate_power_tools(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "power_tools.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Search autofocus on pattern input and Enter debounce in Section 5.1
    if "autofocus" not in content and "フォーカス" not in content and "foco automático" not in content and "自动聚焦" not in content:
        en_focus = """- **Autofocus & Enter Debounce**: Opening the search dialog (`Alt+F7`) automatically focuses and highlights the pattern input field for instant typing. Pressing `Enter` is debounced to prevent duplicate search threads while maintaining responsive execution."""
        trans_focus = trans_snippet(en_focus, lang)
        m = re.search(r"(?m)^-\s+.*?(?:Alt\+F7|cm_FileSearch).*?$", content)
        if m:
            idx = m.end()
            content = content[:idx] + "\n" + trans_focus.strip() + content[idx:]

    # 2. Sandboxed terminal handoff callout in Section 10
    if "Terminal Handoff" not in content and "ターミナル" not in content[10000:] and "沙盒终端" not in content:
        en_term = """> [!TIP]
> **Sandboxed Terminal Handoff**
> In Mac App Store sandboxed builds where launching interactive shells inside the app sandbox is restricted by Apple security policies, pressing `Ctrl+J` (`F9` / `cm_RunTerm`) invokes macOS Terminal (`open -a Terminal <path>`) or iTerm2 directly at the active directory path, ensuring full interactive shell capabilities with zero sandbox friction."""
        trans_term = trans_snippet(en_term, lang)
        m = re.search(r"(?m)^## 10\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_term.strip() + "\n\n---\n\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] power_tools.md updated.")
    return True


def propagate_network_and_vfs(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "network_and_vfs.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Column sorting and bidirectional header sync in Section 4.3
    if "bidirectional" not in content and "双向同步" not in content and "双方向" not in content and "bidirektional" not in content:
        en_vfs_sort = """- **VFS Column Sorting & Bidirectional Sync**: Network and archive listings support full column sorting (Name, Size, Modified, Ext). Sorting preferences synchronize bidirectionally with local panel header states."""
        trans_vfs_sort = trans_snippet(en_vfs_sort, lang)
        m = re.search(r"(?m)^-\s+.*?(?:Sort|並べ替え|Trier|Ordenar|정렬|Сортировка).*?$", content[3000:])
        if m:
            idx = 3000 + m.end()
            content = content[:idx] + "\n" + trans_vfs_sort.strip() + content[idx:]

    # 2. On-Demand Authentication & Session Cache in Section 9.1
    if "VFSSessionCache" not in content and "NetworkPasswordDialog" not in content:
        en_auth = """- **On-Demand Authentication (`NetworkPasswordDialog`)**: When connecting to password-protected shares without pre-configured credentials, ATBCmder prompts with a native secure password sheet and caches authenticated sessions in memory (`VFSSessionCache`) during the application lifetime."""
        trans_auth = trans_snippet(en_auth, lang)
        m = re.search(r"(?m)^-\s+.*?(?:SFTP|SMB|FTP|Credentials|Authentification|認証).*?$", content[6000:])
        if m:
            idx = 6000 + m.end()
            content = content[:idx] + "\n" + trans_auth.strip() + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] network_and_vfs.md updated.")
    return True


def propagate_system_tools(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "system_tools.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # If already has 27 headers or cm_RecentChanges, skip
    if "cm_RecentChanges" in content:
        print(f"[{lang}] system_tools.md already contains cm_RecentChanges.")
        return True

    # 1. Add Section 3.2 before ## 4.
    en_sec32 = """### 3.2 Mac App Store Sandbox Mode (`Top Processes` + `Running Applications`)

In Mac App Store sandboxed builds, ATBCmder adapts its system telemetry to operate strictly within Apple's privacy boundaries without compromising diagnostics:

- **Current-User Process Inspection**: Rather than attempting global Mach kernel calls that require root permissions, ATBCmder queries Darwin kernel process structures (`sysctl KERN_PROC_UID`) and `proc_pidinfo` to measure CPU percentage, resident memory (RSS), virtual memory, and process thread counts for your user account.
- **Dual Tab Architecture**:
  - **Top Processes**: Displays real-time per-process CPU, memory, and state rankings sorted dynamically with configurable refresh intervals (default: 2.0 s).
  - **Running Applications**: Specifically identifies GUI applications running in user space with cached Retina dock icons, cleanly filtering out noise from background system daemons, launchd agents, and helper XPC services.
- **Sandbox-Safe Context Menu Actions**: Right-click any process entry to execute targeted actions: **Quit Process** (`SIGTERM`), **Force Quit** (`SIGKILL`), **Bring Window to Front**, **Show in Finder** (`open -R`), or **Inspect in Activity Monitor**."""
    trans_sec32 = trans_snippet(en_sec32, lang)
    trans_sec32 = re.sub(r"^(#+)\s*3\.2\b.*$", lambda m: f"### 3.2 {m.group(0).split('3.2', 1)[1].strip()}", trans_sec32, flags=re.MULTILINE)
    if not trans_sec32.startswith("### 3.2"):
        trans_sec32 = "### 3.2 " + trans_sec32.lstrip("# \t")

    m4 = re.search(r"(?m)^## 4\..*$", content)
    if m4:
        content = content[:m4.start()] + trans_sec32.strip() + "\n\n---\n\n" + content[m4.start():]

    # 2. Add Section 5: Recent File & Folder Changes before ## 5. (which is currently System Cleaner)
    en_sec5 = """## 5. Recent File & Folder Changes (`cm_RecentChanges`)

When tracking down where newly downloaded assets landed, finding modified code files across multiple projects, or verifying output from background build scripts, the **Recent Changes** tool scans your filesystem by last modification timestamp:

- **Launch Triggers**: Choose **Tools ➔ Recent Changes...** from the menu bar, or invoke `cm_RecentChanges` from the Command Palette.

---

### 5.1 Scope, Time Presets & Size Filtering

The filter bar provides targeted controls to narrow down large directories in seconds:

- **Search Path**: Defaults to the active panel directory, or enter any path (`/var/log`, `~/Library`, or external drive mounts).
- **Item Type Filtering**: Toggle between **Files & Folders**, **Files Only**, or **Folders Only**.
- **Time Presets**: Select quick lookback windows (**Past 1 Hour**, **Past 24 Hours**, **Past 7 Days**, **Past 30 Days**) or specify a custom calendar range.
- **Minimum Size Threshold**: Exclude trivial file touches (such as lockfiles or `.DS_Store`) by filtering for items larger than `0 B`, `1 KB`, `1 MB`, `10 MB`, or a custom threshold.

---

### 5.2 Fast Discovery & Instant Actions

Results populate asynchronously with real-time progress indicators:

- **Spotlight Pre-Seeding**: On local APFS/HFS+ volumes, ATBCmder queries the macOS Spotlight index (`mdfind`) for sub-second returns before falling back to POSIX directory traversal for network shares and non-indexed directories.
- **Context Actions**: Double-click any result or press `Enter` to open the file; press `Cmd+Enter` to locate and highlight it in the active panel, or drag results directly to external apps."""
    trans_sec5 = trans_snippet(en_sec5, lang)
    trans_sec5 = re.sub(r"^(#+)\s*5\.\s*(.+)$", lambda m: f"## 5. {m.group(2).strip()}", trans_sec5, flags=re.MULTILINE)
    trans_sec5 = re.sub(r"^(#+)\s*5\.\s*1\b.*$", lambda m: f"### 5.1 {re.split(r'5\.\s*1', m.group(0), maxsplit=1)[1].strip()}", trans_sec5, flags=re.MULTILINE)
    trans_sec5 = re.sub(r"^(#+)\s*5\.\s*2\b.*$", lambda m: f"### 5.2 {re.split(r'5\.\s*2', m.group(0), maxsplit=1)[1].strip()}", trans_sec5, flags=re.MULTILINE)

    # 3. Add Section 6.2 in System Cleaner and renumber sections
    m5 = re.search(r"(?m)^## 5\..*$", content)
    if m5:
        pre_content = content[:m5.start()]
        cleaner_and_after = content[m5.start():]

        en_sec62 = """### 6.2 Grouping Modes, Kept Sizes & Retention Transparency

To give power users complete confidence before purging data, ATBCmder structures results with granular risk controls and retention metrics:

- **Per-Application & Per-Domain Grouping**: Toggle between category-centric views (Caches, Logs, Trash) and application-centric grouping (Xcode, Docker, Node.js, Browsers) to inspect exact footprint per tool.
- **Kept Sizes & 10 Retention Reasons**: When safety rules prevent deleting an item (such as active socket files, open databases, locked caches, or whitelisted directories), ATBCmder displays the exact preserved byte size alongside localized explanations (e.g., *In Use by Active Process*, *System Protection Rule*, *Recently Modified Grace Period*)."""
        trans_sec62 = trans_snippet(en_sec62, lang)
        trans_sec62 = re.sub(r"^(#+)\s*6\.2\b.*$", lambda m: f"### 6.2 {m.group(0).split('6.2', 1)[1].strip()}", trans_sec62, flags=re.MULTILINE)
        if not trans_sec62.startswith("### 6.2"):
            trans_sec62 = "### 6.2 " + trans_sec62.lstrip("# \t")

        cleaner_and_after = re.sub(r"(?m)^## 8\.", "## 9.", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^## 7\.", "## 8.", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^## 6\.", "## 7.", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 6\.3\b", "### 7.3", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 6\.2\b", "### 7.2", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 6\.1\b", "### 7.1", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 5\.3\b", "### 6.4", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 5\.2\b", "### 6.3", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^### 5\.1\b", "### 6.1", cleaner_and_after)
        cleaner_and_after = re.sub(r"(?m)^## 5\.", "## 6.", cleaner_and_after)

        m63 = re.search(r"(?m)^### 6\.3\b.*$", cleaner_and_after)
        if m63:
            cleaner_and_after = cleaner_and_after[:m63.start()] + trans_sec62.strip() + "\n\n---\n\n" + cleaner_and_after[m63.start():]

        content = pre_content + trans_sec5.strip() + "\n\n---\n\n" + cleaner_and_after

    # Update Section 1 and Section 9 tables
    content = content.replace("`cm_DiskUsageAnalyzer` | `⌘⇧D` *(Cmd+Shift+D)*", "`cm_DiskUsageAnalyzer` | *(Menu: Tools ➔ Disk Usage Analyzer...)*")
    content = content.replace("`cm_DiskUsageAnalyzer` | `⌘⇧D`", "`cm_DiskUsageAnalyzer` | *(Menu: Tools ➔ Disk Usage Analyzer...)*")
    if "cm_RecentChanges" not in content[:3000]:
        en_tbl_row = "| `cm_RecentChanges` | View recently modified files/folders with time & size filters | *(Menu: Tools ➔ Recent Changes...)* | *(Menu: Tools ➔ Recent Changes...)* | Main |"
        trans_tbl_row = trans_snippet(en_tbl_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_DiskUsageAnalyzer`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tbl_row.strip() + "\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] system_tools.md updated.")
    return True


def propagate_preferences_and_customization(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "preferences_and_customization.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Fix leading whitespace on ### 4.6 if present
    content = re.sub(r"(?m)^[ \t]+### 4\.6\b", "### 4.6", content)

    # Add 4.7 and 4.8 if not present
    if "### 4.7" not in content and "view.panel_column_order" not in content:
        en_sec47_48 = """### 4.7 Customizable Column Visibility & Ordering (`view.panel_column_order`, `view.panel_column_visible`)

Under **Preferences ➔ File Views**, you can customize exactly which table columns appear across both file panels:

- **Column Visibility Toggles**: Check or uncheck secondary columns (`Ext`, `Size`, `Modified`, `Permissions`, `Owner`) according to your workflow needs. The primary `Name` column is always permanently pinned as the first column.
- **Drag-and-Drop Column Reordering**: Grab the `⠿` drag handle beside any column name in the list to reorder columns globally. Changes synchronize instantaneously across both panels.
- **Reset to Defaults**: Click **Reset to Defaults** at any time to restore the standard Commander column order.

---

### 4.8 macOS Finder Color Tags (`view.show_color_tags`, `view.color_tag_sync_interval_ms`)

ATBCmder reads and displays native macOS Finder extended attribute tags (`com.apple.metadata:_kMDItemUserTags`):

- **Enable Color Tags**: Check **Show macOS Finder color tags in file panel** (`view.show_color_tags`).
- **Visual Color Dots**: Files and folders with assigned Finder tags display crisp colored circular dots immediately to the left of their file icons, supporting all 7 macOS standard colors (Red, Orange, Yellow, Green, Blue, Purple, Gray) and custom tag labels.
- **Live Sync Interval**: Configure the background polling interval in seconds (`view.color_tag_sync_interval_ms`, default `30.0 s`; set to `0` to disable background polling and refresh on panel navigation)."""
        trans_sec47_48 = trans_snippet(en_sec47_48, lang)
        trans_sec47_48 = re.sub(r"^(#+)\s*4\.7\b.*$", lambda m: f"### 4.7 {m.group(0).split('4.7', 1)[1].strip()}", trans_sec47_48, flags=re.MULTILINE)
        trans_sec47_48 = re.sub(r"^(#+)\s*4\.8\b.*$", lambda m: f"### 4.8 {m.group(0).split('4.8', 1)[1].strip()}", trans_sec47_48, flags=re.MULTILINE)
        if not trans_sec47_48.startswith("### 4.7"):
            trans_sec47_48 = "### 4.7 " + trans_sec47_48.lstrip("# \t")

        m5 = re.search(r"(?m)^## 5\..*$", content)
        if m5:
            content = content[:m5.start()] + trans_sec47_48.strip() + "\n\n---\n\n" + content[m5.start():]

    # Check system tray in Section 3.5
    if "ui.minimize_to_tray" not in content and "RegisterEventHotKey" not in content:
        en_tray = """- **System Tray Residency (`ui.minimize_to_tray`)**: Check **Minimize to system tray (Requires Restart)** under **General** to tuck ATBCmder into the menu bar without Dock clutter.
- **Zero-Permission Carbon Global Hotkey (`Cmd+Opt+H` / `Ctrl+Alt+H`)**: Registered via native macOS Carbon `RegisterEventHotKey`, providing instant global toggling without requiring Accessibility permissions in System Settings."""
        trans_tray = trans_snippet(en_tray, lang)
        m35 = re.search(r"(?m)^### 3\.5\b.*?\n", content)
        if m35:
            idx = m35.end()
            content = content[:idx] + trans_tray.strip() + "\n\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] preferences_and_customization.md updated.")
    return True


def propagate_faq_howtos(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "faq_howtos.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if 2.9 is present
    if "### 2.9" not in content and "cm_EditPath" not in content:
        # Detect localized recipe prefix from 2.1
        m_r = re.search(r"(?m)^###\s+2\.1\s+(.*?1.*?):", content)
        r_prefix = "Recipe"
        if m_r:
            r_prefix = m_r.group(1).replace("1", "").strip()

        en_recipes = f"""### 2.9 {r_prefix} 9: Instant Path Editing & Direct File Jumping with "Enter Full Path and Go" (`⌘⇧G`)

When you copy a deep path from Terminal, Xcode, VS Code, or a message, you can jump straight into it—or directly highlight a specific file—without clicking up and down through folders:

1. **Activate Inline Path Editing**:
   - Click the pencil **Enter Full Path and Go** button (`btn_edit_path`) just left of the Parent Directory (`^`) button on either panel, double-click the empty space to the right of the breadcrumb segments, or press **`Cmd+Shift+G`** (`⌘⇧G` / `Ctrl+Shift+G` / `cm_EditPath`).
   - The current path is pre-filled and highlighted so you can immediately press **`Cmd+V`** (`⌘V`) to overwrite it.
2. **Paste Quoted Paths, Tildes, or File Paths**:
   - Press **`Enter`**. ATBCmder automatically trims whitespace, strips matching surrounding quotes (`"..."` / `'...'`), expands `~` and environment variables (`$VAR` / `%VAR%`), and preserves `vfs://` URIs.
   - If you pasted a path pointing directly to a **file** (e.g., `"/Users/brain/Projects/app/src/main.py"`), ATBCmder navigates to its parent directory (`src/`) and highlights `main.py` automatically.
3. **Recover Without Re-Pasting on Typos**:
   - If a path does not exist, the inline input stays open with a red border and a non-blocking status bar message so you can fix the typo directly and press `Enter` again.
   - Press `Esc`, click outside, or click the pencil button again at any time to cancel and return to breadcrumb buttons.

---

### 2.10 {r_prefix} 10: Staying Resident in the Background with System Tray & Global Hotkey (`⌘⌥H`)

If you switch into ATBCmder dozens of times a day to grab files, preview logs, or sync folders, keeping it resident in the macOS menu bar tray gives you instant sub-second access:

1. **Enable System Tray Residency**:
   - Press **`Cmd+,`** (`⌘,`) to open **Preferences ➔ General**.
   - Check **Minimize to system tray (Requires Restart)** (`ui.minimize_to_tray`).
   - Optionally customize **Show/Hide Window Hotkey** (`ui.global_hotkey`, default: `Ctrl+Alt+H` / `⌘⌥H` on macOS). Hotkey edits apply immediately without restarting.
   - Click **OK** and restart ATBCmder once to activate the tray icon.
2. **Zero-Permission macOS Carbon Global Hotkey**:
   - ATBCmder registers your global hotkey via macOS Carbon `RegisterEventHotKey`, so it works out of the box **without requiring Accessibility permissions** in System Settings, and Option-key (`⌥`) chords capture cleanly without accented dead-key conflicts.
3. **Toggle From Anywhere**:
   - Press **`Cmd+Option+H`** (`⌘⌥H`) inside any app or full-screen space to summon ATBCmder straight to the front with your exact window size and tabs, and press **`⌘⌥H`** again to tuck it back into the menu bar tray.

---

### 2.11 {r_prefix} 11: Customizing File Panel Columns & Viewing macOS Finder Color Tags

Tailor your file table to show only the columns you care about and inspect macOS Finder color tags right inside ATBCmder:

1. **Reorder or Hide Panel Columns**:
   - Open **Preferences ➔ File Views** (`Cmd+,`).
   - Under **Columns**, uncheck secondary columns (`Ext`, `Size`, `Modified`, `Permissions`, `Owner`) you want to hide (`Name` always remains first).
   - Drag the `⠿` handle beside any column to reorder columns globally across both panels, or click **Reset to Defaults** to restore standard ordering.
2. **Enable macOS Finder Color Tags**:
   - Scroll to **Color Tags (macOS)** on the same **File Views** page.
   - Check **Show macOS Finder color tags in file panel** (`view.show_color_tags`) and set your preferred **Live-sync interval** (default `30.0 s`, or `0` for Disabled).
   - Click **Apply** or **OK**. Both panels update immediately, showing crisp Finder tag dots with localized tooltips for all 7 standard Finder colors (`Red`, `Orange`, `Yellow`, `Green`, `Blue`, `Purple`, `Gray`) and any custom user tags."""
        trans_recipes = trans_snippet(en_recipes, lang)
        trans_recipes = re.sub(r"^(#+)\s*2\.9\b.*$", lambda m: f"### 2.9 {m.group(0).split('2.9', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)
        trans_recipes = re.sub(r"^(#+)\s*2\.10\b.*$", lambda m: f"### 2.10 {m.group(0).split('2.10', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)
        trans_recipes = re.sub(r"^(#+)\s*2\.11\b.*$", lambda m: f"### 2.11 {m.group(0).split('2.11', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)

        m3 = re.search(r"(?m)^## 3\..*$", content)
        if m3:
            content = content[:m3.start()] + trans_recipes.strip() + "\n\n---\n\n" + content[m3.start():]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] faq_howtos.md updated.")
    return True


def propagate_getting_started(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "getting_started.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if Tip 5 is present
    if "cm_Tutorial" not in content:
        m_tip = re.search(r"(?m)^###\s+(.*?(?:Tip|Tipp|ヒント|Conseil|Consejo|Dica|팁|Совет|Suggerimento)\s+4).*$", content)
        tip_prefix = "Tip"
        if m_tip:
            t4 = m_tip.group(1)
            tip_prefix = t4.replace("4", "").strip()

        en_tips = f"""### {tip_prefix} 5: Interactive Onboarding Tutorial (`cm_Tutorial`)

Want a guided hands-on tour directly inside the app? Choose **Help ➔ Interactive Tutorial...** from the menu bar to start ATBCmder's 32-step spotlighted tutorial. It walks you interactively through dual-panel switching, file operations, tab locking (`Cmd+K`), inline path bar jumping (`Cmd+Shift+G`), quick search, panel view modes, and the integrated system tools suite.

### {tip_prefix} 6: Background System Tray Residency & Permission-Free Global Hotkey (`⌘⌥H`)

For frequent daily switching, open **Preferences ➔ General** (`Cmd+,`), enable **Minimize to system tray (Requires Restart)** (`ui.minimize_to_tray`), and restart once. ATBCmder stays resident in your macOS menu bar tray with zero Dock clutter and can be summoned or hidden instantaneously from any application using the **Show/Hide Window Hotkey** (default `Cmd+Opt+H` / `⌘⌥H`) via permission-free macOS Carbon registration (no Accessibility permission prompt required)."""
        trans_tips = trans_snippet(en_tips, lang)
        lines = []
        for l in trans_tips.splitlines():
            if f"{tip_prefix} 5" in l:
                lines.append(f"### {tip_prefix} 5: " + l.split(f"{tip_prefix} 5", 1)[1].lstrip(": #\t"))
            elif f"{tip_prefix} 6" in l:
                lines.append(f"### {tip_prefix} 6: " + l.split(f"{tip_prefix} 6", 1)[1].lstrip(": #\t"))
            else:
                lines.append(l)
        trans_tips = "\n".join(lines)

        m6 = re.search(r"(?m)^## 6\..*$", content)
        if m6:
            content = content[:m6.start()] + trans_tips.strip() + "\n\n---\n\n" + content[m6.start():]

    # In section 7 table: add cm_ToggleLockTab and cm_EditPath
    if "cm_ToggleLockTab" not in content:
        en_tbl = """| **Lock / Unlock Tab** | `cm_ToggleLockTab` | `Cmd+K` | `Ctrl+K` | Toggles tab locking (`*`) on the active folder tab. |
| **Enter Full Path & Go** | `cm_EditPath` | `Cmd+Shift+G` | `Ctrl+Shift+G` | Switches path bar to inline text input and jumps directly. |"""
        trans_tbl = trans_snippet(en_tbl, lang)
        m = re.search(r"(?m)^\|\s*\*\*.*?\bcm_CloseTab\b.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tbl.strip() + "\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] getting_started.md updated.")
    return True


def propagate_keyboard_shortcuts(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "keyboard_shortcuts.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Navigation table: cm_EditPath, update cm_ConfigDirHotList
    if "cm_EditPath" not in content:
        en_row = "| `cm_EditPath` | Enter Full Path and Go (switch breadcrumb bar to inline text input) | `⇧⌘G` | `Ctrl+Shift+G` | Main |"
        trans_row = trans_snippet(en_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_DirHotList`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_row.strip() + "\n" + content[idx:]
        content = re.sub(r"(\|\s*`cm_ConfigDirHotList`\s*\|.*?\|)\s*`⇧⌘D`\s*\|", r"\1 `⌥⌘D` |", content)

    # 2. Tabs table: cm_ToggleLockTab, cm_SaveFavoriteTabs
    if "cm_ToggleLockTab" not in content:
        en_tab_row = "| `cm_ToggleLockTab` | Instant toggle tab lock state (`*` badge) | `⌘K` | `Ctrl+K` | Main |"
        trans_tab_row = trans_snippet(en_tab_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_CloseTab`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tab_row.strip() + "\n" + content[idx:]

    if "cm_SaveFavoriteTabs" not in content:
        en_fav_row = "| `cm_SaveFavoriteTabs` | Save all open tabs across both panels as a new favorite tabs set | `⇧⌘D` | `Ctrl+Shift+D` | Main |"
        trans_fav_row = trans_snippet(en_fav_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_LoadTab`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_fav_row.strip() + "\n" + content[idx:]

    # 3. System Tools table: cm_DiskUsageAnalyzer to menu, add cm_RecentChanges
    content = re.sub(r"(\|\s*`cm_DiskUsageAnalyzer`\s*\|.*?\|)\s*`⌘⇧D`.*?\s*\|", r"\1 *(Menu: Tools ➔ Disk Usage Analyzer...)* |", content)
    if "cm_RecentChanges" not in content:
        en_rec_row = "| `cm_RecentChanges` | Open Recent File & Folder Changes tool | *(Menu: Tools ➔ Recent Changes...)* | *(Menu: Tools ➔ Recent Changes...)* | Main |"
        trans_rec_row = trans_snippet(en_rec_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_DiskUsageAnalyzer`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_rec_row.strip() + "\n" + content[idx:]

    # 4. Help & System table: cm_Tutorial, Global hotkey
    if "cm_Tutorial" not in content:
        en_tut_row = """| `cm_Tutorial` | Launch 32-step interactive onboarding tutorial | *(Menu: Help ➔ Interactive Tutorial...)* | *(Menu: Help ➔ Interactive Tutorial...)* | Main |
| `*(Global Hotkey)*` | Summon / hide main window (toggle from menu bar system tray) | `⌘⌥H` | `Ctrl+Alt+H` | System (Carbon) |"""
        trans_tut_row = trans_snippet(en_tut_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_HelpContents`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tut_row.strip() + "\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] keyboard_shortcuts.md updated.")
    return True


def propagate_navigation_and_tabs(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "navigation_and_tabs.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Cheat sheet table: Add cm_EditPath, cm_ToggleLockTab, update hotlist / favorite tabs
    if "cm_EditPath" not in content[:3000]:
        en_rows = """| **Enter Full Path & Go** | `Cmd+Shift+G` / `⌘⇧G` | `Ctrl+Shift+G` | `cm_EditPath` | Switch path bar to inline text input and jump directly. |
| **Lock / Unlock Tab** | `Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab` | Instant toggle tab lock state (`*` badge). |"""
        trans_rows = trans_snippet(en_rows, lang)
        m = re.search(r"(?m)^\|\s*\*\*.*?\bcm_DirHotList\b.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_rows.strip() + "\n" + content[idx:]
        content = re.sub(r"(\|\s*\*\*.*?\bcm_ConfigDirHotList\b.*?\|)\s*`Cmd\+Shift\+D`\s*\|", r"\1 `Option+Cmd+D` / `⌥⌘D` |", content)
        content = re.sub(r"(\|\s*\*\*.*?\bcm_SaveFavoriteTabs\b.*?\|)\s*—\s*\|", r"\1 `Cmd+Shift+D` / `⌘⇧D` |", content)

    # 2. Section 2.4: update to Enter Full Path and Go
    if "btn_edit_path" not in content:
        en_p = """- **Enter Full Path and Go (`BreadcrumbLineEdit` / `cm_EditPath`)**: Click the pencil icon button (`btn_edit_path`) immediately to the left of the Parent Directory (`^`) button, double-click the empty space to the right of the breadcrumb chain, or press **`Cmd+Shift+G`** (`⌘⇧G` / `Ctrl+Shift+G`). Type or paste any path (quotes, `~`, `$VAR`, or `vfs://` URIs are normalized automatically; pasting a local file path opens its parent directory and highlights that file), and fix invalid paths effortlessly with red-border inline error retention."""
        trans_p = trans_snippet(en_p, lang)
        pattern = r"(?m)^-\s+.*?(?:BreadcrumbLineEdit|Direct Path Editing|Direkte Pfadbearbeitung|Modification directe).*?$"
        content = re.sub(pattern, trans_p.strip(), content, count=1)

    # 3. Section 7.1: Columns & Finder tags
    if "view.show_color_tags" not in content and "view.panel_column_order" not in content:
        en_cols = """- **Customizable Columns & Finder Color Tags**: Configure which columns (`Ext`, `Size`, `Modified`, `Permissions`, `Owner`) are visible and drag-reorder them in **Preferences ➔ File Views**, or enable localized **Finder Color Tags** dots alongside filenames."""
        trans_cols = trans_snippet(en_cols, lang)
        m = re.search(r"(?m)^-\s+.*?(?:Full Details|詳細|Détails|Detaillierte).*?$", content[10000:])
        if m:
            idx = 10000 + m.end()
            content = content[:idx] + "\n" + trans_cols.strip() + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] navigation_and_tabs.md updated.")
    return True


def propagate_index(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "index.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Landmark items in Overview
    if "btn_edit_path" not in content:
        en_l3 = """3. **Interactive Breadcrumb Path Bar (`[3]`)**: Click any directory segment in the path to jump directly up the hierarchy, click the chevron to browse sibling folders, or click the pencil **Enter Full Path and Go** button (`btn_edit_path` / `Cmd+Shift+G` / `cm_EditPath`) to paste and jump straight to any folder or file."""
        trans_l3 = trans_snippet(en_l3, lang)
        pattern = r"(?m)^3\.\s*\*\*.*?\n"
        content = re.sub(pattern, trans_l3.strip() + "\n", content, count=1)

    if "cm_ToggleLockTab" not in content:
        en_l4 = """4. **Folder Tabs & Workspaces (`[4]`)**: Open adjacent tabs (`Cmd+T`), close tabs (`Cmd+W`), toggle tab locking with `Cmd+K` (`cm_ToggleLockTab` with `*` badge) alongside visible macOS context menu shortcuts, and save entire dual-panel tab workspaces (`cm_SaveFavoriteTabs` / `Cmd+Shift+D`)."""
        trans_l4 = trans_snippet(en_l4, lang)
        pattern = r"(?m)^4\.\s*\*\*.*?\n"
        content = re.sub(pattern, trans_l4.strip() + "\n", content, count=1)

    # Track A interactive tutorial link
    if "cm_Tutorial" not in content:
        en_tut = """Launch the built-in 32-step **Interactive Tutorial** (**Help ➔ Interactive Tutorial...** / `cm_Tutorial`) right inside the app, or follow our guides—once you learn the core patterns, you will never want to go back to dragging files across scattered windows:"""
        trans_tut = trans_snippet(en_tut, lang)
        pattern = r"(?m)^If you are coming from Finder.*?\n"
        if not re.search(pattern, content):
            pattern = r"(?m)^.*?(?:Finder|访达|訪達).*?(?:unfamiliar|étrangers|desconocidos|낯설|непривыч).*?\n"
        content = re.sub(pattern, trans_tut.strip() + "\n", content, count=1)

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] index.md updated.")
    return True


def propagate_language(lang: str, doc_name: str = "all") -> bool:
    print(f"\n==========================================")
    print(f"  Propagating updates to [{lang}]...")
    print(f"==========================================")

    handlers = {
        "system_tools.md": propagate_system_tools,
        "preferences_and_customization.md": propagate_preferences_and_customization,
        "faq_howtos.md": propagate_faq_howtos,
        "getting_started.md": propagate_getting_started,
        "keyboard_shortcuts.md": propagate_keyboard_shortcuts,
        "navigation_and_tabs.md": propagate_navigation_and_tabs,
        "file_operations.md": propagate_file_operations,
        "power_tools.md": propagate_power_tools,
        "network_and_vfs.md": propagate_network_and_vfs,
        "index.md": propagate_index,
    }

    if doc_name != "all":
        if doc_name in handlers:
            handlers[doc_name](lang)
        else:
            print(f"[ERR] Unknown document: {doc_name}")
            return False
    else:
        for name, fn in handlers.items():
            try:
                fn(lang)
            except Exception as e:
                print(f"[ERR] Failed {name} for {lang}: {e}")

    save_cache()
    return True


def main():
    parser = argparse.ArgumentParser(description="Propagate v2.4.0–v2.9.0 diffs across foreign languages.")
    parser.add_argument("--lang", default="all", help="Target language (ja, de, fr, etc. or 'all')")
    parser.add_argument("--doc", default="all", help="Specific doc name or 'all'")
    args = parser.parse_args()

    langs = TARGET_LANGUAGES if args.lang == "all" else [l.strip() for l in args.lang.split(",")]

    for l in langs:
        propagate_language(l, args.doc)

    print("\nAll done! Verifying parity...")


if __name__ == "__main__":
    main()
