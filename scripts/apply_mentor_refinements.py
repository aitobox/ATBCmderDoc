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
    Safely process markdown by strictly isolating fenced code blocks (```)
    from prose. Guarantees 0 headers or prose outside code blocks are touched.
    """
    parts = content.split("```")
    new_parts = []
    
    for i, part in enumerate(parts):
        if i % 2 == 0:
            # Prose outside code blocks
            part = fix_alerts(part)
            part = apply_terminology(part, lang)
            new_parts.append(part)
        else:
            # Code block (i // 2)
            block_index = i // 2
            if code_block_replacer:
                part = code_block_replacer(part, block_index, lang)
            new_parts.append(part)
            
    return "```".join(new_parts)

def replace_index_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in index.md by block index."""
    if block_index == 0 and lang in ASCII_DUAL_PANEL_INDEX:
        return f"\n{ASCII_DUAL_PANEL_INDEX[lang]}\n"
    elif block_index == 1 and lang in ASCII_LANDMARKS_INDEX:
        return f"\n{ASCII_LANDMARKS_INDEX[lang]}\n"
    return block_content

def replace_getting_started_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in getting_started.md by block index."""
    if block_index == 0 and lang in ASCII_FLOW_GETTING_STARTED:
        return f"\n{ASCII_FLOW_GETTING_STARTED[lang]}\n"
    elif block_index == 1 and lang in ASCII_ANATOMY_GETTING_STARTED:
        return f"\n{ASCII_ANATOMY_GETTING_STARTED[lang]}\n"
    return block_content

def replace_nav_tabs_block(block_content: str, block_index: int, lang: str) -> str:
    """Replace ASCII diagrams in navigation_and_tabs.md by block index."""
    if block_index == 0 and lang in ASCII_NAV_TABS:
        return f"\n{ASCII_NAV_TABS[lang]}\n"
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
    print("Batch 1 refinements applied successfully!")
