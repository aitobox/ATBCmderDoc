#!/usr/bin/env python3
"""
scripts/apply_mentor_refinements.py
Applies mentor-style phrasing, localized ASCII diagrams, canonical alerts,
and macOS keybinding standards across documentation files.
"""

import glob
import os
import re
import sys
from pathlib import Path

from mentor_style_guide import (
    ALERT_CANONICAL_MAP,
    TERMINOLOGY_REPLACEMENTS,
    ASCII_DUAL_PANEL_INDEX,
    ASCII_LANDMARKS_INDEX,
    ASCII_FLOW_GETTING_STARTED,
    ASCII_ANATOMY_GETTING_STARTED,
    ASCII_NAV_TABS
)

from mentor_style_guide_batch2 import (
    ASCII_FILE_OPS_TRANSFER,
    ASCII_VIEWERS_QUICK_VIEW,
    ASCII_POWER_TOOLS_MAP
)

from mentor_style_guide_batch3 import (
    ASCII_KEYBOARD_ENGINE,
    ASCII_KEYBOARD_SCOPES
)

LANGUAGES = ["zh", "zh-hant", "ja", "de", "fr", "es", "pt", "ko", "ru", "it"]

def fix_alerts(content: str) -> str:
    """Normalize localized alert tags to canonical GitHub markdown alerts."""
    for localized, canonical in ALERT_CANONICAL_MAP.items():
        pattern = r'> \[!' + re.escape(localized) + r'\]'
        replacement = f'> [!{canonical}]'
        content = re.sub(pattern, replacement, content)
    return content

def apply_terminology(content: str, lang: str) -> str:
    """Replace machine translation artifacts with native mentor expressions."""
    if lang not in TERMINOLOGY_REPLACEMENTS:
        return content
    
    replacements = TERMINOLOGY_REPLACEMENTS[lang]
    for bad_term, good_term in replacements.items():
        if bad_term in content:
            content = content.replace(bad_term, good_term)
    return content

def process_markdown_file(content: str, lang: str, code_block_replacer) -> str:
    """
    Safely process markdown using line-based parsing. Strictly isolates
    fenced code blocks (``` at line start) from prose, guaranteeing 0 headers
    or text outside code blocks are swallowed or modified.
    """
    lines = content.splitlines(keepends=True)
    sections = []
    current = []
    in_code = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if not in_code:
                if current:
                    sections.append((False, "".join(current)))
                    current = []
                in_code = True
                current.append(line)
            else:
                current.append(line)
                sections.append((True, "".join(current)))
                current = []
                in_code = False
        else:
            current.append(line)

    if current:
        sections.append((in_code, "".join(current)))

    new_sections = []
    block_index = 0
    for is_code, text in sections:
        if not is_code:
            text = fix_alerts(text)
            text = apply_terminology(text, lang)
            new_sections.append(text)
        else:
            if code_block_replacer:
                text = code_block_replacer(text, block_index, lang)
            new_sections.append(text)
            block_index += 1

    return "".join(new_sections)

# --- Batch 1 Replacers ---

def replace_index_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in index.md by block index."""
    if block_index == 0 and lang in ASCII_DUAL_PANEL_INDEX:
        return f"```\n{ASCII_DUAL_PANEL_INDEX[lang]}\n```\n"
    elif block_index == 1 and lang in ASCII_LANDMARKS_INDEX:
        return f"```\n{ASCII_LANDMARKS_INDEX[lang]}\n```\n"
    return block_content

def replace_getting_started_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in getting_started.md by block index."""
    if block_index == 0 and lang in ASCII_FLOW_GETTING_STARTED:
        return f"```\n{ASCII_FLOW_GETTING_STARTED[lang]}\n```\n"
    elif block_index == 1 and lang in ASCII_ANATOMY_GETTING_STARTED:
        return f"```\n{ASCII_ANATOMY_GETTING_STARTED[lang]}\n```\n"
    return block_content

def replace_nav_tabs_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in navigation_and_tabs.md by block index."""
    if block_index == 0 and lang in ASCII_NAV_TABS:
        return f"```\n{ASCII_NAV_TABS[lang]}\n```\n"
    return block_content

# --- Batch 2 Replacers ---

def replace_file_operations_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in file_operations.md by block index."""
    if block_index == 0 and lang in ASCII_FILE_OPS_TRANSFER:
        return f"```\n{ASCII_FILE_OPS_TRANSFER[lang]}\n```\n"
    return block_content

def replace_viewers_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in viewers_and_editors.md by block index."""
    if block_index == 0 and lang in ASCII_VIEWERS_QUICK_VIEW:
        return f"```\n{ASCII_VIEWERS_QUICK_VIEW[lang]}\n```\n"
    return block_content

def replace_power_tools_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in power_tools.md by block index."""
    if block_index == 0 and lang in ASCII_POWER_TOOLS_MAP:
        return f"```\n{ASCII_POWER_TOOLS_MAP[lang]}\n```\n"
    return block_content

# --- Batch 3 Replacers ---

def replace_keyboard_shortcuts_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in keyboard_shortcuts.md by block index."""
    if block_index == 0 and lang in ASCII_KEYBOARD_ENGINE:
        return f"```\n{ASCII_KEYBOARD_ENGINE[lang]}\n```\n"
    elif block_index == 1 and lang in ASCII_KEYBOARD_SCOPES:
        return f"```\n{ASCII_KEYBOARD_SCOPES[lang]}\n```\n"
    return block_content

def refine_batch_1():
    """Process Batch 1 files: index.md, getting_started.md, navigation_and_tabs.md."""
    print("=== Refining Batch 1: Core Foundation Trilogy (index.md, getting_started.md, navigation_and_tabs.md) ===")
    
    for lang in LANGUAGES:
        lang_dir = Path("docs") / lang
        if not lang_dir.is_dir():
            continue
        
        # 1. index.md
        index_file = lang_dir / "index.md"
        if index_file.is_file():
            content = index_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_index_block)
            index_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished index.md")
        
        # 2. getting_started.md
        gs_file = lang_dir / "getting_started.md"
        if gs_file.is_file():
            content = gs_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_getting_started_block)
            gs_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished getting_started.md")
        
        # 3. navigation_and_tabs.md
        nav_file = lang_dir / "navigation_and_tabs.md"
        if nav_file.is_file():
            content = nav_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_nav_tabs_block)
            nav_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished navigation_and_tabs.md")

def refine_batch_2():
    """Process Batch 2 files: file_operations.md, viewers_and_editors.md, power_tools.md."""
    print("=== Refining Batch 2: Core Workflows & Utilities (file_operations.md, viewers_and_editors.md, power_tools.md) ===")
    
    for lang in LANGUAGES:
        lang_dir = Path("docs") / lang
        if not lang_dir.is_dir():
            continue
        
        # 1. file_operations.md
        fops_file = lang_dir / "file_operations.md"
        if fops_file.is_file():
            content = fops_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_file_operations_block)
            fops_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished file_operations.md")
        
        # 2. viewers_and_editors.md
        viewers_file = lang_dir / "viewers_and_editors.md"
        if viewers_file.is_file():
            content = viewers_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_viewers_block)
            viewers_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished viewers_and_editors.md")
        
        # 3. power_tools.md
        power_file = lang_dir / "power_tools.md"
        if power_file.is_file():
            content = power_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_power_tools_block)
            power_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished power_tools.md")

def refine_batch_3():
    """Process Batch 3 files: network_and_vfs.md, preferences_and_customization.md, keyboard_shortcuts.md."""
    print("=== Refining Batch 3: System & Customization (network_and_vfs.md, preferences_and_customization.md, keyboard_shortcuts.md) ===")
    
    for lang in LANGUAGES:
        lang_dir = Path("docs") / lang
        if not lang_dir.is_dir():
            continue
        
        # 1. network_and_vfs.md
        vfs_file = lang_dir / "network_and_vfs.md"
        if vfs_file.is_file():
            content = vfs_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, None)
            vfs_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished network_and_vfs.md")
        
        # 2. preferences_and_customization.md
        pref_file = lang_dir / "preferences_and_customization.md"
        if pref_file.is_file():
            content = pref_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, None)
            pref_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished preferences_and_customization.md")
        
        # 3. keyboard_shortcuts.md
        keys_file = lang_dir / "keyboard_shortcuts.md"
        if keys_file.is_file():
            content = keys_file.read_text(encoding="utf-8")
            content = process_markdown_file(content, lang, replace_keyboard_shortcuts_block)
            keys_file.write_text(content, encoding="utf-8")
            print(f"[{lang}] Polished keyboard_shortcuts.md")

def refine_all_alerts():
    """Ensure all alert tags across all chapters in all languages are canonical."""
    for lang in LANGUAGES:
        for fpath in glob.glob(f"docs/{lang}/*.md"):
            p = Path(fpath)
            content = p.read_text(encoding="utf-8")
            fixed = fix_alerts(content)
            if fixed != content:
                p.write_text(fixed, encoding="utf-8")

if __name__ == "__main__":
    refine_all_alerts()
    refine_batch_1()
    refine_batch_2()
    refine_batch_3()
    print("Batch 1, 2 & 3 refinements applied successfully!")
