#!/usr/bin/env python3
"""
scripts/translate_landing_i18n.py
Fast, multi-threaded translation of landing/i18n/en.json into ja, de, fr, es, pt, ko, ru, it.
Applies Apple macOS localized terminology and translation caching.
"""

import concurrent.futures
import hashlib
import json
import os
import sys
import threading
import time
from typing import Dict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

import translators as ts
from scripts.batch_translate import MACOS_TERMS

EN_JSON_PATH = os.path.join(PROJECT_ROOT, "landing", "i18n", "en.json")
I18N_DIR = os.path.join(PROJECT_ROOT, "landing", "i18n")
CACHE_FILE = os.path.join(SCRIPT_DIR, ".translation_cache.json")

TARGET_LANGS = ["ja", "de", "fr", "es", "pt", "ko", "ru", "it"]

LANG_MAP = {
    "ja": "ja",
    "de": "de",
    "fr": "fr",
    "es": "es",
    "pt": "pt",
    "ko": "ko",
    "ru": "ru",
    "it": "it"
}

CACHE_LOCK = threading.Lock()
_CACHE: Dict[str, str] = {}
if os.path.exists(CACHE_FILE):
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            _CACHE = json.load(f)
    except Exception:
        _CACHE = {}


def get_cache_key(text: str, to_lang: str) -> str:
    h = hashlib.sha256(f"en:{to_lang}:{text}".encode("utf-8")).hexdigest()
    return f"en_{to_lang}_{h}"


def save_cache() -> None:
    with CACHE_LOCK:
        try:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(_CACHE, f, ensure_ascii=False, indent=2)
        except Exception:
            pass


def translate_snippet(key: str, text: str, target_lang: str) -> tuple[str, str]:
    if key == "version_pill":
        return key, "macOS Native"
    if key == "footer_copyright":
        return key, "© 2026 ATBCmder. All rights reserved."

    ck = get_cache_key(text, target_lang)
    with CACHE_LOCK:
        if ck in _CACHE:
            return key, _CACHE[ck]

    tl = LANG_MAP[target_lang]
    engines = ["bing", "google", "alibaba"]
    
    for engine in engines:
        for attempt in range(2):
            try:
                res = ts.translate_text(
                    text,
                    from_language="en",
                    to_language=tl,
                    translator=engine,
                    timeout=10
                )
                if res and isinstance(res, str) and res.strip():
                    res = res.strip()
                    terms = MACOS_TERMS.get(target_lang, {})
                    for orig, localized in terms.items():
                        res = res.replace(orig, localized)
                    with CACHE_LOCK:
                        _CACHE[ck] = res
                    return key, res
            except Exception:
                time.sleep(0.3)
                
    return key, text


def translate_language(target_lang: str, en_dict: Dict[str, str]) -> None:
    target_file = os.path.join(I18N_DIR, f"{target_lang}.json")
    print(f"--> Translating {target_lang} ({len(en_dict)} keys)...", flush=True)

    existing = {}
    if os.path.exists(target_file):
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = {}

    to_translate = {k: v for k, v in en_dict.items() if k not in existing or not existing[k]}
    results = dict(existing)

    if to_translate:
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            futures = [
                executor.submit(translate_snippet, k, v, target_lang)
                for k, v in to_translate.items()
            ]
            for f in concurrent.futures.as_completed(futures):
                k, res = f.result()
                results[k] = res

    # Ensure all keys in en_dict order
    final_dict = {k: results.get(k, en_dict[k]) for k in en_dict.keys()}
    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(final_dict, f, ensure_ascii=False, indent=2)

    save_cache()
    print(f"✓ Completed and saved {target_file}", flush=True)


def main() -> None:
    with open(EN_JSON_PATH, "r", encoding="utf-8") as f:
        en_dict = json.load(f)

    for target_lang in TARGET_LANGS:
        translate_language(target_lang, en_dict)

    print("\nAll target language dictionaries completed!", flush=True)


if __name__ == "__main__":
    main()
