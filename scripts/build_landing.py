#!/usr/bin/env python3
"""
scripts/build_landing.py
Compiles template-driven multilingual landing pages across all 11 supported languages.
Synchronizes static assets to site/ and guarantees 1:1 key parity and link integrity.
"""

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List

# Ensure scripts dir is in sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DIR.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from languages import DEFAULT_LANGUAGE, LANGUAGES, get_language_codes

TEMPLATE_PATH = PROJECT_ROOT / "landing" / "template.html"
I18N_DIR = PROJECT_ROOT / "landing" / "i18n"
IMAGES_DIR = PROJECT_ROOT / "landing" / "images"
SITE_DIR = PROJECT_ROOT / "site"


def load_translation(code: str) -> Dict[str, str]:
    """Load translation JSON for a language code, falling back to en.json."""
    lang_file = I18N_DIR / f"{code}.json"
    en_file = I18N_DIR / "en.json"
    
    translations: Dict[str, str] = {}
    if en_file.exists():
        with open(en_file, "r", encoding="utf-8") as f:
            translations.update(json.load(f))
            
    if lang_file.exists():
        with open(lang_file, "r", encoding="utf-8") as f:
            translations.update(json.load(f))
            
    return translations


def check_key_parity() -> bool:
    """Check that all 11 languages have identical keys to en.json."""
    en_file = I18N_DIR / "en.json"
    if not en_file.exists():
        print(f"ERROR: Base English dictionary not found at {en_file}")
        return False
        
    with open(en_file, "r", encoding="utf-8") as f:
        en_keys = set(json.load(f).keys())
        
    all_ok = True
    codes = get_language_codes()
    for code in codes:
        lang_file = I18N_DIR / f"{code}.json"
        if not lang_file.exists():
            print(f"  [MISSING] {lang_file}")
            all_ok = False
            continue
            
        with open(lang_file, "r", encoding="utf-8") as f:
            keys = set(json.load(f).keys())
            
        missing = en_keys - keys
        extra = keys - en_keys
        if missing or extra:
            print(f"  [PARITY MISMATCH] {code}: missing {len(missing)}, extra {len(extra)}")
            if missing:
                print(f"    Missing keys: {list(missing)[:5]}...")
            all_ok = False
        else:
            print(f"  [PARITY OK] {code} ({len(keys)} keys)")
            
    return all_ok


def generate_language_dropdown(current_code: str) -> str:
    """Generate dropdown HTML for the landing page language switcher."""
    items: List[str] = []
    for lang in LANGUAGES:
        code = lang["code"]
        name = lang["name"]
        active_class = " active" if code == current_code else ""
        items.append(
            f'        <a href="/{code}/" class="lang-item{active_class}" data-lang="{code}">'
            f'<span>{name}</span>'
            f'</a>'
        )
    return "\n".join(items)


def render_landing_page(lang_meta: Dict[str, Any], template: str) -> str:
    """Render a single language landing page from template and translation dict."""
    code = lang_meta["code"]
    name = lang_meta["name"]
    theme_lang = lang_meta["theme_lang"]
    
    translations = load_translation(code)
    dropdown_html = generate_language_dropdown(code)
    
    html = template
    html = html.replace("{{ lang }}", code)
    html = html.replace("{{ lang_html }}", theme_lang)
    html = html.replace("{{ current_lang_name }}", name)
    html = html.replace("{{ lang_menu_items }}", dropdown_html)
    
    # Replace all {{ t.<key> }}
    def replace_key(match: re.Match) -> str:
        key = match.group(1)
        return translations.get(key, f"MISSING_{key}")
        
    html = re.sub(r"\{\{\s*t\.([a-zA-Z0-9_]+)\s*\}\}", replace_key, html)
    return html


def build_all_landing_pages(
    site_output: Path = SITE_DIR,
    landing_output: Path = PROJECT_ROOT / "landing"
) -> None:
    """Compile all 11 landing pages and copy screenshot assets."""
    if not TEMPLATE_PATH.exists():
        raise FileNotFoundError(f"Landing template not found: {TEMPLATE_PATH}")
        
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()
        
    print(f"Compiling Landing Pages for {len(LANGUAGES)} languages...")
    
    for lang in LANGUAGES:
        code = lang["code"]
        name = lang["name"]
        rendered_html = render_landing_page(lang, template)
        
        # 1. Output to site/{code}/index.html
        site_target_dir = site_output / code
        site_target_dir.mkdir(parents=True, exist_ok=True)
        site_target_file = site_target_dir / "index.html"
        with open(site_target_file, "w", encoding="utf-8") as f:
            f.write(rendered_html)
            
        # 2. Output to landing/{code}/index.html (for source repository inspection)
        landing_target_dir = landing_output / code
        landing_target_dir.mkdir(parents=True, exist_ok=True)
        landing_target_file = landing_target_dir / "index.html"
        with open(landing_target_file, "w", encoding="utf-8") as f:
            f.write(rendered_html)
            
        print(f"  [OK] Generated {code} ({name}) -> {site_target_file.relative_to(PROJECT_ROOT)}")
        
    # Copy shared screenshot assets to site/images/
    if IMAGES_DIR.exists():
        site_images_dir = site_output / "images"
        print(f"Synchronizing landing images to {site_images_dir.relative_to(PROJECT_ROOT)}...")
        shutil.copytree(IMAGES_DIR, site_images_dir, dirs_exist_ok=True)
        print("  [OK] Image assets synchronized.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build ATBCmder multilingual landing pages.")
    parser.add_argument("--check", action="store_true", help="Check translation key parity.")
    args = parser.parse_args()
    
    if args.check:
        print("Checking landing page translation parity...")
        ok = check_key_parity()
        sys.exit(0 if ok else 1)
        
    build_all_landing_pages()
    print("Done! All landing pages compiled successfully.")


if __name__ == "__main__":
    main()
