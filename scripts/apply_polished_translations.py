#!/usr/bin/env python3
"""
scripts/apply_polished_translations.py
Applies human-crafted, vivid, and idiomatic translations across all languages for the landing page.
Ensures zero robotic phrasing, perfect macOS terminology, and 100% key parity with en.json.
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
I18N_DIR = os.path.join(PROJECT_ROOT, "landing", "i18n")

# Load master English dictionary to verify key parity
with open(os.path.join(I18N_DIR, "en.json"), "r", encoding="utf-8") as f:
    EN_KEYS = list(json.load(f).keys())

def save_and_verify(lang_code: str, data: dict):
    # Verify all keys are present
    missing = set(EN_KEYS) - set(data.keys())
    extra = set(data.keys()) - set(EN_KEYS)
    assert not missing, f"Missing keys in {lang_code}: {missing}"
    assert not extra, f"Extra keys in {lang_code}: {extra}"
    
    # Save ordered by EN_KEYS
    ordered = {k: data[k] for k in EN_KEYS}
    path = os.path.join(I18N_DIR, f"{lang_code}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
    print(f"✓ Successfully polished {lang_code}.json ({len(ordered)} keys)")

print("Applying polished translations...")
