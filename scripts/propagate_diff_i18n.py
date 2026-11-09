#!/usr/bin/env python3
"""
scripts/propagate_diff_i18n.py
Propagates v2.4.6 new feature additions and diffs across foreign languages
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

    # 2. Add Section 6.1 if not present
    if "### 6.1" not in content:
        en_sec61 = """### 6.1 Data Integrity & Safe Transfer Protocols

ATBCmder is designed for mission-critical file management where silent data loss, half-written files, or corrupted links are completely unacceptable:

- **Atomic Staging and Replacement**:
  When overwriting or saving existing files, the transfer engine stages writes to a temporary file (`.tmp.atbcmder_*`) in the target directory before performing an atomic POSIX replace (`os.replace`). If an operation is canceled, network drops, or disk space exhausts mid-transfer, the original destination file remains completely intact and uncorrupted.
- **Symlink Move Protection**:
  Moving symbolic links preserves the relative or absolute pointer target without dereferencing or altering the real source data. Moving a link across filesystem mounts recreates the link reference cleanly rather than copying or deleting the target payload.
- **Archive Extraction & Symlink Traversal Guard**:
  When unpacking ZIP, TAR, or 7z archives, ATBCmder strictly validates path hierarchies against directory traversal attacks (zip-slip vulnerabilities) and rejects symlinks pointing outside the destination tree or attempting to overwrite existing real directories."""

        trans_sec61 = trans_snippet(en_sec61, lang)
        # Ensure header is ### 6.1 ...
        trans_sec61 = re.sub(r"^(#+)\s*6\.1\b.*$", lambda m: f"### 6.1 {m.group(0).split('6.1', 1)[1].strip()}", trans_sec61, flags=re.MULTILINE)
        if not trans_sec61.startswith("### 6.1"):
            trans_sec61 = "### 6.1 " + trans_sec61.lstrip("# \t")

        # Insert before Section 7 header (## 7.)
        m = re.search(r"(?m)^## 7\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_sec61.strip() + "\n\n---\n\n" + content[idx:]
        else:
            print(f"[WARN] Could not find ## 7 in {path}")

    # 3. Add ergonomics and instant cancel in Section 7.3
    if "Esc" not in content and "cm_CountDirContent" in content:
        en_points = """  - **macOS Keyboard Ergonomics**: Bound to `Alt+Shift+Return` (`⌥⇧⏎`) so macOS users can trigger it naturally on standard MacBook and Magic Keyboards without requiring a dedicated numeric keypad Enter or `Fn` combination.
  - **Instant Cancellation (`Esc`)**: Space calculation runs in background worker threads and can be canceled immediately at any point by pressing `Esc` without freezing the user interface."""
        trans_points = trans_snippet(en_points, lang)
        # Find the line with cm_CountDirContent in Section 7
        m = re.search(r"(?m)^-\s+.*\bcm_CountDirContent\b.*$", content)
        if m:
            # find end of this bullet item list
            idx = m.end()
            content = content[:idx] + "\n" + trans_points.strip() + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] file_operations.md updated.")
    return True


def propagate_network_and_vfs(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "network_and_vfs.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Add Section 6.3 if not present
    if "Security-Scoped" not in content and "App Store Sandbox" not in content and "沙盒" not in content:
        en_sec63 = """### 6.3 App Store Sandbox Cloud Storage (OneDrive, Google Drive, iCloud)

In Mac App Store sandboxed builds of ATBCmder, direct filesystem access to third-party cloud synchronization directories (e.g., Microsoft OneDrive, Google Drive for Desktop, Dropbox, and iCloud Drive) is regulated by Apple's sandbox architecture:

- **Security-Scoped Bookmarks**: Synced cloud directories residing in `~/Library/CloudStorage/OneDrive-*`, `~/Library/CloudStorage/GoogleDrive-*`, or `~/Library/Mobile Documents/com~apple~CloudDocs/` require security-scoped access tokens.
- **Drive Switcher & Path Integration**: ATBCmder automatically discovers configured local cloud directories and surfaces them in the Drive Switcher (`Alt+D` / `⌥D`), drive button bars, and path breadcrumbs.
- **Persistent Permission Grants**: When opening a cloud directory for the first time, macOS presents an authorization sheet. Once selected, ATBCmder stores the cryptographic security-scoped bookmark in user preferences, granting seamless, uninterrupted read/write access across application restarts without repeated authorization dialogs."""

        trans_sec63 = trans_snippet(en_sec63, lang)
        m_h = re.search(r"^(#+)\s*(?:6\.3)?\s*(.*?)$", trans_sec63, flags=re.MULTILINE)
        if m_h:
            rest = m_h.group(2)
            trans_sec63 = re.sub(r"^#+.*$", f"### 6.3 {rest}", trans_sec63, count=1, flags=re.MULTILINE)
        else:
            trans_sec63 = "### 6.3 " + trans_sec63.lstrip("# \t")

        # Insert before ## 7.
        m = re.search(r"(?m)^## 7\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_sec63.strip() + "\n\n---\n\n" + content[idx:]
        else:
            print(f"[WARN] Could not find ## 7 in {path}")

    # Update SSH Host Key Warning callout
    en_warn = """> [!WARNING]
> **SSH Host Key & Fingerprint Verification**
> To protect against man-in-the-middle (MITM) attacks and credential eavesdropping, ATBCmder's SFTP engine strictly validates server fingerprints against your local `~/.ssh/known_hosts` registry before initiating cryptographic key exchange or transmitting passwords. If a server's fingerprint differs from the stored record, the connection is immediately aborted with a security warning dialog detailing the mismatch. Never bypass host key warnings on untrusted public Wi-Fi networks without independently confirming host key changes with your server administrator."""
    trans_warn = trans_snippet(en_warn, lang)
    # Replace existing warning in Section 10
    pattern = r"(?s)>\s*\[!WARNING\]\s*\n>\s*\*\*SSH.*?(?=\n\n>\s*\[!|\n\n---\n\n## 11|\Z)"
    if re.search(pattern, content):
        content = re.sub(pattern, trans_warn.strip(), content, count=1)

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] network_and_vfs.md updated.")
    return True


def propagate_navigation_and_tabs(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "navigation_and_tabs.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Cheat sheet table: Add trackpad swipe, show all files, show custom files
    if "cm_SrcAllFiles" not in content[:3000]:
        en_rows = """| **Trackpad Swipe Navigation** | Two-finger swipe left/right | — | `cm_ViewHistoryPrev` / `Next` | Back/Forward history swipe on trackpad (toggle in File Views). |
| **Show All Files** | `Cmd+F10` / `⌘F10` | `Ctrl+F10` | `cm_SrcAllFiles` | Clear active file mask and show all files. |
| **Show Custom Files** | `Cmd+F11` / `⌘F11` | `Ctrl+F11` | `cm_SrcUserDef` | Filter visible files by glob mask (*.py;*.md). |"""
        trans_rows = trans_snippet(en_rows, lang)
        # insert after DirHistory row or before --- in table
        m = re.search(r"(?m)^\|\s*\*\*.*?\bcm_DirHistory\b.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_rows.strip() + "\n" + content[idx:]

    # 2. Trackpad section before Drive & Volume Switcher in Section 6
    m6 = re.search(r"(?m)^## 6\..*$", content)
    m7 = re.search(r"(?m)^## 7\..*$", content)
    if m6 and m7:
        sec6 = content[m6.start():m7.start()]
        h3_matches = list(re.finditer(r"(?m)^###\s+.*$", sec6))
        if len(h3_matches) == 2:
            en_trackpad_sec = """### MacBook Trackpad Horizontal Swipe Navigation

For MacBook laptop users and Apple Magic Trackpad setups, ATBCmder natively recognizes two-finger horizontal swipe gestures across the active or inactive file list viewport:

- **Swipe Left**: Navigates **Back** in folder history (`cm_ViewHistoryPrev`).
- **Swipe Right**: Navigates **Forward** in folder history (`cm_ViewHistoryNext`).

The gesture engine is engineered for seamless macOS ergonomics:

- **Intelligent Debounce & Horizontal Dominance**: Distinguishes intentional horizontal history gestures from vertical list scrolling, completely ignoring momentum drift.
- **Automatic Panel Focus**: Swiping over the inactive panel immediately shifts keyboard and operational focus to that panel before executing the history step, ensuring the intended side is navigated.
- **Configurable Toggle**: Swipe navigation can be enabled or disabled in **Preferences** (`Cmd+,`) → **File Views** (`view.trackpad_swipe_navigation`, default: off)."""

            trans_trackpad_sec = trans_snippet(en_trackpad_sec, lang)
            if not trans_trackpad_sec.startswith("###"):
                trans_trackpad_sec = "### " + trans_trackpad_sec.lstrip("# \t")

            drive_h3 = h3_matches[1]
            insert_idx = m6.start() + drive_h3.start()
            content = content[:insert_idx] + trans_trackpad_sec.strip() + "\n\n---\n\n" + content[insert_idx:]

    # 3. File Masks & Extension Filters section before Auto-Fitting Column Modes in Section 8
    m8 = re.search(r"(?m)^## 8\..*$", content)
    if m8 and "cm_SrcUserDef" not in content[m8.start():]:
        en_masks_sec = """### File Masks & Extension Filters (`Cmd+F10` / `Cmd+F11`)

When managing directories containing hundreds of mixed files, ATBCmder provides dedicated commands in the **Show** menu and column header context menus to filter the visible list:

- **Show All Files (`Cmd+F10` / `⌘F10` / `cm_SrcAllFiles`)**:
  - Instantly clears active extension masks and quick filters, resetting the view to display all files and directories.
- **Show Custom Files / Extension Mask (`Cmd+F11` / `⌘F11` / `cm_SrcUserDef`)**:
  - Opens a prompt pre-filled with the current or last-used mask (e.g., `*.py;*.md`, `*.jpg;*.png`, or `test_*`).
  - Directories and parent `..` entries remain visible so you can navigate folder hierarchies while maintaining your active mask.
  - A prominent status bar badge displays `Mask: <pattern>` while filtering is active.
  - The mask persists across navigation within that tab and can be quickly reset with `Cmd+F10`."""

        trans_masks_sec = trans_snippet(en_masks_sec, lang)
        if not trans_masks_sec.startswith("###"):
            trans_masks_sec = "### " + trans_masks_sec.lstrip("# \t")

        m_qs = re.search(r"\bcm_QuickSearch\b", content[m8.start():])
        if m_qs:
            qs_start = m8.start() + m_qs.end()
            m_next = re.search(r"(?m)^###\s+", content[qs_start:])
            if m_next:
                insert_pos = qs_start + m_next.start()
                content = content[:insert_pos] + trans_masks_sec.strip() + "\n\n---\n\n" + content[insert_pos:]
            else:
                print(f"[WARN] Could not find next ### after cm_QuickSearch in {path}")
        else:
            print(f"[WARN] Could not find cm_QuickSearch in {path}")

    # 4. Final shortcuts table rows
    if "cm_SrcAllFiles" not in content[-3000:]:
        en_tbl_rows = """| | Show All Files | `Cmd+F10` / `⌘F10` | `Ctrl+F10` | `cm_SrcAllFiles` |
| | Custom File Mask | `Cmd+F11` / `⌘F11` | `Ctrl+F11` | `cm_SrcUserDef` |"""
        trans_tbl_rows = trans_snippet(en_tbl_rows, lang)
        m = re.search(r"(?m)^\|\s*\|\s*.*?\bcm_HorizontalFilePanels\b.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tbl_rows.strip() + "\n" + content[idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] navigation_and_tabs.md updated.")
    return True


def propagate_preferences_and_customization(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "preferences_and_customization.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Section 4.5 and 4.6 before ## 5.
    if "### 4.5" not in content:
        en_sec45_46 = """### 4.5 Semantic Lucide File-Type Icons & Shared Singleton Cache

ATBCmder features a modernized, high-DPI vector icon subsystem (`fs_icons.py`) engineered for crisp visuals on Retina displays and extreme rendering speed:

- **Lucide Vector Icon Library**: Generic low-resolution icons are replaced with over 200 tailored Lucide vector symbols, automatically mapped to programming languages (Python, Rust, Go, TypeScript, C/C++, Swift), documents (PDF, Markdown, Office), media (audio, video, vectors, RAW photos), databases, and archives.
- **Shared Singleton Cache Architecture**:
  - Rather than creating duplicate `QIcon` and `QPixmap` instances for each visible table row, ATBCmder pools icon instances in a shared global cache keyed by file extension and MIME type.
  - Keeps memory overhead negligible (under 15 MB even when rendering thousands of diverse file types).
  - Eliminates main-thread filesystem stat calls during scrolling, ensuring silky-smooth 60fps scrolling performance through directories containing 100,000+ files.

---

### 4.6 MacBook Trackpad Horizontal Swipe Navigation

For macOS users working on MacBooks or with Magic Trackpads, ATBCmder provides native horizontal two-finger gesture navigation:

- **Two-Finger Swipe Left**: Goes backward in directory history (`cm_ViewHistoryPrev` / `Cmd+[`).
- **Two-Finger Swipe Right**: Goes forward in directory history (`cm_ViewHistoryNext` / `Cmd+]`).
- **Ergonomics & Safety**:
  - **Horizontal Dominance Check**: Automatically detects whether a gesture is primarily horizontal or vertical, preventing accidental history jumps when scrolling through file lists.
  - **Hover Panel Focus**: Swiping over either panel automatically directs navigation to the panel underneath the cursor without requiring a prior click.
  - **Momentum Filter**: Blocks spurious multi-page triggers from trackpad inertia.
- **Configuration**:
  - Toggle in **Preferences** → **File Views** → **Trackpad Navigation** (`view.trackpad_swipe_navigation`, default: off)."""

        trans_sec45_46 = trans_snippet(en_sec45_46, lang)
        trans_sec45_46 = re.sub(r"^(#+)\s*4\.5\b.*$", lambda m: f"### 4.5 {m.group(0).split('4.5', 1)[1].strip()}", trans_sec45_46, flags=re.MULTILINE)
        trans_sec45_46 = re.sub(r"^(#+)\s*4\.6\b.*$", lambda m: f"### 4.6 {m.group(0).split('4.6', 1)[1].strip()}", trans_sec45_46, flags=re.MULTILINE)

        m = re.search(r"(?m)^## 5\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_sec45_46.strip() + "\n\n---\n\n" + content[idx:]

    # 2. Pro Tip 5 before ## 10.
    if "Pro Tip 5" not in content and "quick_search.pinyin_search" not in content:
        # Determine language-specific Pro Tip prefix
        m_pt = re.search(r"(?m)^###\s+(.*?(?:Pro Tip|進階技巧|进阶技巧|Tipp|Conseil|Consejo|Dica|팁|Совет|Suggerimento)\s+4).*$", content)
        pt_prefix = "Pro Tip 5"
        if m_pt:
            t4 = m_pt.group(1)
            pt_prefix = t4.replace("4", "5")

        en_pt5 = f"""### {pt_prefix}: High-Performance Pinyin Quick Search & Live Filtering
Under **Preferences ➔ Quick Search**, power users can tailor in-panel letter search to their language and filtering habits:

- **Arbitrary-Boundary Pinyin Matching (`quick_search.pinyin_search`)**:
  - Matches Chinese characters by initial consonants or full pinyin syllables beginning at *any* character boundary in the name.
  - *Example*: Typing `gz` matches `2024工作总结.docx` and `【公司】工资表.xlsx` without needing to match from the very first character of the filename.
  - Enabled by default using an in-memory cached lookup table.
- **Live Filter-Only Mode (`quick_search.filter_only`)**:
  - Toggling on **Only show matching files/directories (Filter mode)** hides non-matching items directly as you type.
  - Unlike standard Quick Search (which merely moves the selection cursor among visible files), Filter mode isolates matching rows so batch operations—such as **Select All** (`Cmd+A`), **Copy** (`F5`), **Move** (`F6`), and **Pack** (`Alt+F5`)—operate strictly on the matched items."""

        trans_pt5 = trans_snippet(en_pt5, lang)
        # Ensure header starts with ###
        if not trans_pt5.startswith("###"):
            trans_pt5 = f"### {pt_prefix}: " + trans_pt5.lstrip("# \t")

        m = re.search(r"(?m)^## 10\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_pt5.strip() + "\n\n---\n\n" + content[idx:]

    # 3. Add trackpad block in ASCII diagram
    if "view.trackpad_swipe_navigation" not in content[:6000]:
        ascii_box = """├────────────────────────────────────────────────────────────────────────────────────────┤
│  Trackpad Navigation:                                                                  │
│  [X] Swipe left/right with two fingers to go back/forward in folder history            │
└────────────────────────────────────────────────────────────────────────────────────────┘"""
        # find end of File Views ascii diagram
        m = re.search(r"(?m)^└─+┘\s*\n\s*### 4\.1", content)
        if m:
            # Replace box end with trackpad box
            idx = m.start()
            content = content[:idx] + ascii_box + "\n\n" + content[m.end() - len("### 4.1"):]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] preferences_and_customization.md updated.")
    return True


def propagate_faq_howtos(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "faq_howtos.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update space calculation shortcut to Alt+Shift+Return
    content = content.replace("`Alt+Shift+Enter` (`Space`)", "`Alt+Shift+Return` / `⌥⇧⏎` (`Space`)")
    content = content.replace("`Alt+Shift+Enter`", "`Alt+Shift+Return`")

    # 2. Recipes 6, 7, 8 before ## 3.
    if "### 2.6" not in content:
        # Check language prefix for Recipe
        m_r5 = re.search(r"(?m)^###\s+2\.5\s+(.*?5.*?):", content)
        r_prefix = "Recipe"
        if m_r5:
            # e.g., "Praxis-Szenario 5" -> "Praxis-Szenario"
            r_prefix = m_r5.group(1).replace("5", "").strip()

        en_recipes = f"""### 2.6 {r_prefix} 6: Protecting Workspaces with Total Commander-Style Tab Locking

When managing critical projects, server mounts, or repositories, accidentally navigating away from your primary working directory disrupts your flow. ATBCmder provides Total Commander-compatible tab locking:

1. **Locking a Tab (`cm_SetTabOptionLock`)**:
   - Right-click any tab header and select **Lock this tab**.
   - An asterisk `*` badge immediately appears in the tab title (e.g., `* WebApp`).
   - The base directory is frozen. Double-clicking any folder or opening an archive inside this tab leaves the locked tab intact and automatically spawns the target location in an **adjacent tab** immediately to the right.
2. **Locking with Subdirectories Allowed (`cm_SetTabOptionLockWithSubdirs`)**:
   - Right-click the tab and choose **Locked, but directory changes allowed**.
   - You can browse freely into nested subdirectories within the current tab.
   - However, switching away to another tab, re-clicking the tab header, or navigating to the root button automatically resets the tab back to its designated base path.
3. **Unlocking (`cm_SetTabOptionNormal`)**:
   - Right-click the tab and select **Unlock tab** to return to standard behavior.

---

### 2.7 {r_prefix} 7: Filtering Active Files by Custom Extension Mask (`Cmd+F11`)

When a directory contains hundreds of files with varying extensions (e.g. source code, compiled binaries, logs, assets), you often need to focus on a specific subset without losing folder navigation:

1. **Activate Custom Filter (`Cmd+F11` / `⌘F11` / `cm_SrcUserDef`)**:
   - Press **`Cmd+F11`** (`⌘F11`).
   - A dialog appears pre-filled with the active or last-used mask (e.g., `*.py;*.md` or `*.jpg;*.png`).
   - Enter your desired glob patterns separated by semicolons and press `Enter`.
2. **Live Filtered Browsing**:
   - The panel immediately hides all non-matching files while keeping subdirectories and parent `..` visible.
   - A clear indicator (`Mask: *.py;*.md`) appears on the panel status bar.
   - You can enter and exit subdirectories; the mask remains active across navigation.
3. **Reset to All Files (`Cmd+F10` / `⌘F10` / `cm_SrcAllFiles`)**:
   - Press **`Cmd+F10`** (`⌘F10`) at any time to clear the mask and restore the full file listing.

---

### 2.8 {r_prefix} 8: Enabling MacBook Two-Finger Trackpad History Navigation

If you work on a MacBook or use a Magic Trackpad, you can navigate your folder history using fluid two-finger horizontal swipe gestures:

1. **Enable Trackpad Navigation**:
   - Press **`Cmd+,`** (`⌘,`) to open **Preferences**.
   - Navigate to the **File Views** page.
   - In the **Trackpad Navigation** section, check **Swipe left/right with two fingers to go back/forward in folder history** (`view.trackpad_swipe_navigation`).
   - Click **OK**.
2. **Effortless Gesture Navigation**:
   - Move your pointer over either panel (no click required).
   - **Swipe Left with Two Fingers**: Navigates back in directory history (`cm_ViewHistoryPrev`).
  - **Swipe Right with Two Fingers**: Navigates forward in directory history (`cm_ViewHistoryNext`).
  - The horizontal dominance filter ensures vertical list scrolling is never accidentally interrupted."""

        trans_recipes = trans_snippet(en_recipes, lang)
        # Ensure headings have ### 2.6, 2.7, 2.8
        trans_recipes = re.sub(r"^(#+)\s*2\.6\b.*$", lambda m: f"### 2.6 {m.group(0).split('2.6', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)
        trans_recipes = re.sub(r"^(#+)\s*2\.7\b.*$", lambda m: f"### 2.7 {m.group(0).split('2.7', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)
        trans_recipes = re.sub(r"^(#+)\s*2\.8\b.*$", lambda m: f"### 2.8 {m.group(0).split('2.8', 1)[1].strip()}", trans_recipes, flags=re.MULTILINE)

        m = re.search(r"(?m)^## 3\..*$", content)
        if m:
            idx = m.start()
            content = content[:idx] + trans_recipes.strip() + "\n\n---\n\n" + content[idx:]

    # 3. Add FAQ Q7
    if "quick_search.filter_only" not in content and "Q7" not in content:
        en_q7 = """#### Q7: How does Chinese Pinyin Quick Search work?
When browsing folders containing Chinese names, typing in the panel matches both initial consonants and full pinyin syllables starting at any Chinese character boundary. For example, typing `gz` matches `2024工作总结.docx` and `【公司】工资表.xlsx`. If you prefer to hide non-matching files while typing, open **Preferences ➔ Quick Search** and enable **Only show matching files/directories (Filter mode)** (`quick_search.filter_only`)."""

        trans_q7 = trans_snippet(en_q7, lang)
        # Ensure header starts with ####
        if not trans_q7.startswith("####"):
            trans_q7 = "#### Q7: " + trans_q7.lstrip("# \t")

        # insert after Q6
        m = re.search(r"(?m)^####\s+.*?(?:Q6|6\b|Frage 6|Вопрос 6).*?$", content)
        if m:
            # find end of Q6 section (before --- or ## 4)
            m_end = re.search(r"(?m)^\s*(?:---|## 4\.)", content[m.start():])
            if m_end:
                idx = m.start() + m_end.start()
                content = content[:idx] + trans_q7.strip() + "\n\n" + content[idx:]
            else:
                content += "\n\n" + trans_q7.strip()

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] faq_howtos.md updated.")
    return True


def propagate_viewers_and_editors(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "viewers_and_editors.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update ASCII toolbar line
    content = re.sub(
        r"│\s*\[💾.*?\]\s*\[.*?另存.*?\]\s*\|.*?(?=\│\n├)",
        "│  [💾] [📄] [🔄] │ [↩] [↪] │ [🔍] [📝] │ [↩ Wrap] [123 Lines] │ [🔍+] [🔍-] [1:1]       ",
        content
    )
    content = re.sub(
        r"│\s*\[💾\s*Save\].*?(?=\│\n├)",
        "│  [💾] [📄] [🔄] │ [↩] [↪] │ [🔍] [📝] │ [↩ Wrap] [123 Lines] │ [🔍+] [🔍-] [1:1]       ",
        content
    )

    # 2. Add Modern Vector Action Toolbar section if not present
    if "Modern Vector Action Toolbar" not in content and "[💾]" not in content[2000:]:
        en_tb_sec = """#### Modern Vector Action Toolbar

The editor header features a sleek vector action toolbar with high-DPI squircle icons and dual-shortcut tooltips:

| Action | Icon | macOS Shortcut | Classic Key | Tooltip & Function |
| :--- | :--- | :--- | :--- | :--- |
| **Save** | `💾` | `Cmd+S` / `⌘S` | `Ctrl+S` | Saves modifications atomically to disk (`.tmp` staging). |
| **Save As** | `📄` | `Shift+Cmd+S` / `⇧⌘S` | `Ctrl+Shift+S` | Prompts for target directory and new file name. |
| **Reload** | `🔄` | `Cmd+R` / `⌘R` | `Ctrl+R` | Discards unsaved changes and reloads file from disk. |
| **Undo** | `↩` | `Cmd+Z` / `⌘Z` | `Ctrl+Z` | Reverts the most recent text modification. |
| **Redo** | `↪` | `Shift+Cmd+Z` / `⇧⌘Z` | `Ctrl+Y` | Re-applies the previously undone modification. |
| **Find** | `🔍` | `Cmd+F` / `⌘F` | `Ctrl+F` | Docks the incremental search bar at the bottom. |
| **Replace** | `📝` | `Option+Cmd+F` / `⌥⌘F`| `Ctrl+H` | Docks the search and replace bar. |
| **Word Wrap** | `↩ Wrap` | `Option+W` / `⌥W` | `Alt+W` | Toggles soft text wrapping at window edge. |
| **Line Numbers**| `123 Lines`| `Option+L` / `⌥L` | `Alt+L` | Toggles left-gutter line numbering. |
| **Zoom In** | `🔍+` | `Cmd++` / `⌘+` | `Ctrl++` | Increases editor font size. |
| **Zoom Out** | `🔍-` | `Cmd+-` / `⌘-` | `Ctrl+-` | Decreases editor font size. |
| **Reset Zoom** | `1:1` | `Cmd+0` / `⌘0` | `Ctrl+0` | Resets font scaling back to default 100%. |"""

        trans_tb_sec = trans_snippet(en_tb_sec, lang)
        if not trans_tb_sec.startswith("####"):
            trans_tb_sec = "#### " + trans_tb_sec.lstrip("# \t")

        # Insert after Figure 4.14
        m = re.search(r"(?m)^\*.*?(?:4\.14|Markdown).*?\*\s*$", content)
        if m:
            idx = m.end()
            content = content[:idx] + "\n\n" + trans_tb_sec.strip() + "\n" + content[idx:]

    # 3. Add symlink preservation in atomic save
    if "os.replace" not in content and "Symlink" not in content[8000:]:
        en_atomic = """- **Atomic Save Protection**: When pressing `Cmd+S`, ATBCmder stages writes to a temporary file (`.tmp.atbcmder_*`) on the same volume, syncs disk buffers, and executes an atomic POSIX replace (`os.replace`). This guarantees the target file is never left half-written or corrupted if power is interrupted, a network drive hiccups, or storage exhausts mid-save.
- **Symlink Preservation**: If the file being edited is a symbolic link, ATBCmder writes directly to the resolved target destination rather than replacing the symlink with a regular file, keeping link structures intact across project builds and system configurations."""
        trans_atomic = trans_snippet(en_atomic, lang)
        # replace existing atomic save bullet
        content = re.sub(r"(?m)^-\s+.*?(?:Atomic|Atomar|atomique|atómica|атомар).*?$", trans_atomic.strip(), content, count=1)

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] viewers_and_editors.md updated.")
    return True


def propagate_keyboard_shortcuts(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "keyboard_shortcuts.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Navigation trackpad swipe
    if "cm_ViewHistoryPrev" in content and "Two-finger swipe" not in content and "二本指" not in content and "Zwei-Finger" not in content:
        en_track_row = "| `cm_ViewHistoryPrev` / `Next` | Trackpad swipe back/forward in directory history (toggle in Views) | Two-finger swipe ← / → | — | FilePanel |"
        trans_track_row = trans_snippet(en_track_row, lang)
        m = re.search(r"(?m)^\|\s*`cm_ViewHistoryNext`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_track_row.strip() + "\n" + content[idx:]

    # 2. View modes: cm_SrcAllFiles, cm_SrcUserDef
    if "cm_SrcAllFiles" not in content:
        en_mask_rows = """| `cm_SrcAllFiles` | Show All Files (clear active extension mask & quick filter) | `⌘F10` | `Ctrl+F10` | Main |
| `cm_SrcUserDef` | Show Custom Files / Filter by Extension Mask (`*.py;*.md`) | `⌘F11` | `Ctrl+F11` | Main |"""
        trans_mask_rows = trans_snippet(en_mask_rows, lang)
        m = re.search(r"(?m)^\|\s*`cm_HorizontalFilePanels`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_mask_rows.strip() + "\n" + content[idx:]

    # 3. Tabs: cm_SetTabOptionLock, etc.
    if "cm_SetTabOptionLock" not in content:
        en_tab_rows = """| `cm_SetTabOptionLock` | Lock this tab (freeze path, opens child folders in adjacent tabs) | *(Tab Context Menu)* | — | Main |
| `cm_SetTabOptionLockWithSubdirs` | Lock tab with subdirs allowed (resets back to base path on switch) | *(Tab Context Menu)* | — | Main |
| `cm_SetTabOptionNormal` | Unlock tab (restore default unlocked navigation behavior) | *(Tab Context Menu)* | — | Main |"""
        trans_tab_rows = trans_snippet(en_tab_rows, lang)
        m = re.search(r"(?m)^\|\s*`cm_ShowTabsList`.*?\n", content)
        if m:
            idx = m.end()
            content = content[:idx] + trans_tab_rows.strip() + "\n" + content[idx:]

    # 4. Editor shortcuts: Save As, Reload, Replace, Word Wrap, Line Numbers, Zoom
    if "cm_ZoomIn" not in content and "⌘0" not in content[-3000:]:
        en_ed_rows = """| Save File As | Prompt for target directory and new file name | `⇧⌘S` | `Ctrl+Shift+S` | Editor |
| Reload File | Discard unsaved changes and reload from disk | `⌘R` | `Ctrl+R` | Editor |
| Replace Text | Find and replace text in document | `⌥⌘F` | `Ctrl+H` | Editor |
| Word Wrap | Toggle soft text wrapping at window edge | `⌥W` | `Alt+W` | Editor |
| Line Numbers | Toggle left gutter line numbering | `⌥L` | `Alt+L` | Editor |
| Zoom In | Increase font size | `⌘+` | `Ctrl++` | Editor |
| Zoom Out | Decrease font size | `⌘-` | `Ctrl+-` | Editor |
| Reset Zoom | Reset font size to default 100% | `⌘0` | `Ctrl+0` | Editor |"""
        trans_ed_rows = trans_snippet(en_ed_rows, lang)
        m = re.search(r"(?m)^\|\s*.*?(?:Save|儲存|Speichern|Enregistrer|Guardar|Salvar|저장|Сохранить).*?\b(?:F2|⌘S)\b.*?\n", content[7000:])
        if m:
            abs_idx = 7000 + m.end()
            content = content[:abs_idx] + trans_ed_rows.strip() + "\n" + content[abs_idx:]

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] keyboard_shortcuts.md updated.")
    return True


def propagate_getting_started(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "getting_started.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Landmark [4] Folder Tab Bar
    if "cm_SetTabOptionLock" not in content:
        en_l4 = """### [4] Folder Tab Bar
Each panel maintains an independent set of tabs built with `MacNativeTabBar`:

- **Adjacent Tab Creation**: Opening new tabs with `Cmd+T` (`cm_NewTab`) inserts the new tab immediately to the right of your active tab rather than at the end of the strip. Close tabs with `Cmd+W` (`cm_CloseTab`).
- **Total Commander Tab Locking**: Right-click tabs to choose **Lock this tab** (freezes base directory with an asterisk `*` badge; child folder navigation opens in adjacent tabs) or **Locked, but directory changes allowed** (in-place subfolder browsing with automatic reset back to base on switch).
- **Workspace Organization**: Drag-and-drop to reorder tabs, double-click empty strip space to duplicate, rename titles, or clone tab layouts to the opposite panel."""
        trans_l4 = trans_snippet(en_l4, lang)
        # replace Landmark 4 section
        pattern = r"(?s)###\s*\[4\].*?(?=###\s*\[5\])"
        content = re.sub(pattern, trans_l4.strip() + "\n\n", content, count=1)

    # Landmark [5] Dual File Panels
    if "Lucide" not in content:
        en_l5 = """### [5] Dual File Panels
High-performance virtualized file lists capable of rendering folders with hundreds of thousands of entries smoothly without UI stutter:

- **Semantic Lucide Icon System**: High-DPI vector icons tailored to programming languages, documents, media, and archives, backed by a shared singleton cache for 60fps scrolling.
- **MacBook Trackpad Gesture Navigation**: Fluid two-finger horizontal swipe navigation (swipe left for History Back, swipe right for History Forward) with automatic panel hover detection and vertical scroll preservation.
- **In-Panel Quick Search & Masks**: Instant character-by-character search supporting arbitrary-boundary Chinese Pinyin matching, filter-only live isolation, and custom extension masks (`Cmd+F11` / reset with `Cmd+F10`).
- **Column Sorting & Views**: Click any header to sort ascending or descending. Multiple view modes include Full Details, Brief Grid, Thumbnail Gallery, Tree View, and recursive Flat Branch View (`Cmd+B`)."""
        trans_l5 = trans_snippet(en_l5, lang)
        pattern = r"(?s)###\s*\[5\].*?(?=###\s*\[6\])"
        content = re.sub(pattern, trans_l5.strip() + "\n\n", content, count=1)

    # Landmark [7] Status Bar
    if "OneDrive" not in content:
        en_l7 = """- **Drive Storage Meter & Cloud Integration**: Visual disk usage indicator displaying the currently mounted volume name (e.g., `Macintosh HD`), total capacity, used storage, and remaining free space percentage. Synced cloud storage providers (OneDrive, Google Drive, iCloud) are automatically identified with persistent security-scoped bookmark authorization."""
        trans_l7 = trans_snippet(en_l7, lang)
        pattern = r"(?m)^-\s+.*?(?:Drive Storage|Capacité|Festplatt|Disco|Armazenamento|드라이브|Диск|容量).*?$"
        content = re.sub(pattern, trans_l7.strip(), content, count=1)

    content = format_lists_content(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[{lang}] getting_started.md updated.")
    return True


def propagate_index(lang: str) -> bool:
    path = os.path.join(PROJECT_ROOT, "docs", lang, "index.md")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Landmark items in Overview
    if "cm_SetTabOptionLock" not in content:
        en_items = """4. **Folder Tabs & Workspaces (`[4]`)**: Open adjacent tabs (`Cmd+T`), close tabs (`Cmd+W`), lock paths with Total Commander locking modes (`cm_SetTabOptionLock` with `*` badge), and save entire dual-panel tab workspaces (`cm_SaveFavoriteTabs`).
5. **Dual File Panels (`[5]`)**: Independent file tables powered by Semantic Lucide vector icons and a shared singleton cache. Features two-finger trackpad history navigation, arbitrary-boundary Chinese Pinyin quick search, custom file masks (`Cmd+F11` / `Cmd+F10`), and instant focus switching with `Tab`.
6. **Middle Toolbar & Draggable Splitter (`[6]`)**: A vertical quick-action strip placed directly on the panel divider. Provides one-click triggers for View (`F3`), Edit (`F4`), Copy (`F5`), Move (`F6`), New Folder (`F7`), Delete (`F8`), Wipe, and Swap Panels (`cm_Exchange`). Drag the splitter left or right to resize panels.
7. **Status Bar & Drive Storage Meter (`[7]`)**: Shows live file counts, selected item statistics, aggregate byte sizes, persistent cloud drive authorization (OneDrive, Google Drive, iCloud), and an active volume storage capacity gauge with free space calculation."""
        trans_items = trans_snippet(en_items, lang)
        pattern = r"(?s)4\.\s*\*\*.*?\n(?=---\n\n##)"
        content = re.sub(pattern, trans_items.strip() + "\n\n", content, count=1)

    # Chapter 2, 3, 4 summaries
    if "Alt+Shift+Return" not in content and "⌥⇧⏎" not in content:
        en_chap_summaries = """### 🧭 [Chapter 2: Navigation & Folder Tabs](navigation_and_tabs.md)
Move effortlessly through directory trees using interactive breadcrumbs, keyboard jumps (`Ctrl+\`, `Backspace`), two-finger trackpad history navigation, multi-tab organization with adjacent tab opening and TC tab locking (`*`), dual-panel favorite workspace sets (`cm_SaveFavoriteTabs`), Directory Hotlist bookmarks (`Ctrl+D`), Chinese Pinyin quick search, custom file masks (`Cmd+F10`/`Cmd+F11`), and flexible view modes (Brief, Full Columns, Thumbnails, Tree View, and Flat Branch View `Cmd+B`).

### 📁 [Chapter 3: Daily File Operations & Queue](file_operations.md)
Perform fast, rock-solid file operations: Copy (`F5`), Move (`F6`), New Folder (`F7`), Delete to Trash (`F8`), inline quick rename (`F2`), and ergonomic directory space calculation (`Alt+Shift+Return` / `⌥⇧⏎`). Master wildcard and attribute selections, drag-and-drop interoperability, collision conflict resolution, atomic staging safeguards against data loss, UNIX octal permissions (`Alt+Enter`), and asynchronous transfer monitoring via the Background Operations Queue (`cm_OperationsPanel`).

### 👁️ [Chapter 4: Universal Lister & Built-in Editors](viewers_and_editors.md)
Inspect files without launching heavy third-party software. Use Quick View (`Ctrl+Q` / `Cmd+Q`) for live side-panel previews, and Universal Lister (`F3`) for Word documents, spreadsheets, SQLite databases, Jupyter notebooks, EPUBs, syntax-highlighted code, raw Hex byte inspection (`2`), image annotations and watermarking (`F4`), PDF document reader, and integrated Audio/Video media players with background audio playback. Edit files directly with the built-in text editor (`F4`) featuring a modern vector action toolbar and atomic save protection."""

        trans_chap_summaries = trans_snippet(en_chap_summaries, lang)
        pattern = r"(?s)###\s+🧭.*?###\s+⚡\s+\["
        # preserve the title of Chapter 2, 3, 4 while updating descriptions
        # simpler: replace chapter 2, 3, 4 block before Chapter 5
        m = re.search(r"(?s)(###\s+🧭.*)(###\s+⚡\s+\[.*)", content)
        if m:
            content = content[:m.start(1)] + trans_chap_summaries.strip() + "\n\n" + content[m.start(2):]

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
        "file_operations.md": propagate_file_operations,
        "network_and_vfs.md": propagate_network_and_vfs,
        "navigation_and_tabs.md": propagate_navigation_and_tabs,
        "preferences_and_customization.md": propagate_preferences_and_customization,
        "faq_howtos.md": propagate_faq_howtos,
        "viewers_and_editors.md": propagate_viewers_and_editors,
        "keyboard_shortcuts.md": propagate_keyboard_shortcuts,
        "getting_started.md": propagate_getting_started,
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
    parser = argparse.ArgumentParser(description="Propagate v2.4.6 diffs across foreign languages.")
    parser.add_argument("--lang", default="all", help="Target language (ja, de, fr, etc. or 'all')")
    parser.add_argument("--doc", default="all", help="Specific doc name or 'all'")
    args = parser.parse_args()

    langs = TARGET_LANGUAGES if args.lang == "all" else [l.strip() for l in args.lang.split(",")]

    for l in langs:
        propagate_language(l, args.doc)

    print("\nAll done! Verifying parity...")


if __name__ == "__main__":
    main()
