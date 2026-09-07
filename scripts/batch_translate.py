#!/usr/bin/env python3
"""
scripts/batch_translate.py - Translation pipeline for ATBCmder multilingual documentation.

Generates 1:1 localized documentation across 9 target languages:
  zh-hant, ja, de, fr, es, pt, ko, ru, it
benchmarked against docs/en/*.md (12 chapters).

Guarantees:
  1. Code blocks, inline code, <kbd> tags, image paths, and link URLs are protected.
  2. Apple macOS localized terminology alignment for each target language.
  3. 100% header hierarchy (H1, H2, H3) and image reference parity with docs/en/.
  4. Automatic list formatting (MD032 compliance).
  5. Disk-backed translation caching to avoid redundant API calls.

Usage:
  python3 scripts/batch_translate.py --all
  python3 scripts/batch_translate.py --lang ja,de,es
  python3 scripts/batch_translate.py --lang de --doc index.md
"""

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import sys
import threading
import time
from typing import Any, Dict, List, Optional, Tuple

# Ensure project root is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from scripts.languages import NAV_ORDER, get_language, get_language_codes
from scripts.format_markdown_lists import process_content as format_lists_content
from scripts.check_parity import check_file_parity

# Try importing opencc for zh-hant
try:
    from opencc import OpenCC
    HAVE_OPENCC = True
except ImportError:
    HAVE_OPENCC = False

# Try importing translators
try:
    import translators as ts
    HAVE_TRANSLATORS = True
except ImportError:
    HAVE_TRANSLATORS = False

TARGET_LANGUAGES = ["zh-hant", "ja", "de", "fr", "es", "pt", "ko", "ru", "it"]

CACHE_FILE = os.path.join(SCRIPT_DIR, ".translation_cache.json")
CACHE_LOCK = threading.Lock()
_CACHE: Dict[str, str] = {}

# macOS Localized Terminology Dictionary per Apple HIG / standard macOS locale
MACOS_TERMS: Dict[str, Dict[str, str]] = {
    "zh-hant": {
        "快速查看": "快速預覽",
        "快捷键": "快速鍵",
        "快捷鍵": "快速鍵",
        "回收站": "垃圾桶",
        "系统设置": "系統設定",
        "偏好设置": "偏好設定",
        "终端": "終端機",
        "菜单栏": "選單列",
        "文件管理器": "檔案管理器",
        "文件夹": "資料夾",
        "双栏": "雙欄",
        "Quick Look": "快速預覽",
    },
    "ja": {
        "Quick Look": "クイックルック",
        "クィックルック": "クイックルック",
        "Shortcuts": "ショートカット",
        "Trash": "ゴミ箱",
        "Menu bar": "メニューバー",
        "System Settings": "システム設定",
        "Preferences": "環境設定",
        "Terminal": "ターミナル",
        "Finder": "Finder",
        "デュアルパネル": "デュアルパネル",
    },
    "de": {
        "Quick Look": "Schnellübersicht",
        "Kurzer Blick": "Schnellübersicht",
        "Kurze Ansicht": "Schnellübersicht",
        "Trash": "Papierkorb",
        "Mülleimer": "Papierkorb",
        "System Settings": "Systemeinstellungen",
        "Menu bar": "Menüleiste",
        "Preferences": "Einstellungen",
        "Finder": "Finder",
        "Terminal": "Terminal",
        "Tastenkürzel": "Tastaturkurzbefehle",
    },
    "fr": {
        "Quick Look": "Coup d'œil",
        "Aperçu rapide": "Coup d'œil",
        "Trash": "Corbeille",
        "System Settings": "Réglages Système",
        "Menu bar": "Barre des menus",
        "Preferences": "Préférences",
        "Finder": "Finder",
        "Terminal": "Terminal",
        "Raccourcis": "Raccourcis clavier",
    },
    "es": {
        "Quick Look": "Vista rápida",
        "Vistazo rápido": "Vista rápida",
        "Trash": "Papelera",
        "System Settings": "Ajustes del Sistema",
        "Menu bar": "Barra de menús",
        "Preferences": "Preferencias",
        "Finder": "Finder",
        "Terminal": "Terminal",
    },
    "pt": {
        "Quick Look": "Visualização Rápida",
        "Olhar Rápido": "Visualização Rápida",
        "Trash": "Lixeira",
        "System Settings": "Ajustes do Sistema",
        "Menu bar": "Barra de menus",
        "Preferences": "Preferências",
        "Finder": "Finder",
        "Terminal": "Terminal",
    },
    "ko": {
        "Quick Look": "훑어보기",
        "빠른 보기": "훑어보기",
        "Trash": "휴지통",
        "System Settings": "시스템 설정",
        "Menu bar": "메뉴 막대",
        "Preferences": "환경설정",
        "Terminal": "터미널",
        "Finder": "Finder",
        "단축키": "단축키",
    },
    "ru": {
        "Quick Look": "Быстрый просмотр",
        "Trash": "Корзина",
        "System Settings": "Системные настройки",
        "Menu bar": "Строка меню",
        "Preferences": "Настройки",
        "Terminal": "Терминал",
        "Finder": "Finder",
        "Горячие клавиши": "Сочетания клавиш",
    },
    "it": {
        "Quick Look": "Visualizzazione rapida",
        "Sguardo rapido": "Visualizzazione rapida",
        "Trash": "Cestino",
        "System Settings": "Impostazioni di Sistema",
        "Menu bar": "Barra dei menu",
        "Preferences": "Preferenze",
        "Finder": "Finder",
        "Terminal": "Terminale",
    },
}


def load_cache() -> None:
    global _CACHE
    if os.path.isfile(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                _CACHE = json.load(f)
        except Exception:
            _CACHE = {}


def save_cache() -> None:
    with CACHE_LOCK:
        try:
            with open(CACHE_FILE, "w", encoding="utf-8") as f:
                json.dump(_CACHE, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[WARN] Failed to write translation cache: {e}")


def get_cache_key(text: str, to_lang: str, from_lang: str = "en") -> str:
    h = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    return f"{from_lang}->{to_lang}:{h}"


def translate_snippet(
    text: str,
    to_lang: str,
    from_lang: str = "en",
    engine: str = "google",
    use_cache: bool = True,
) -> str:
    """Translate a text snippet with caching and retry logic."""
    if not text.strip():
        return text

    cache_key = get_cache_key(text, to_lang, from_lang)
    if use_cache:
        with CACHE_LOCK:
            if cache_key in _CACHE:
                return _CACHE[cache_key]

    if not HAVE_TRANSLATORS:
        return text

    retries = 3
    last_err = None
    engines = [engine, "alibaba", "bing"] if engine == "google" else [engine, "google"]

    for cur_engine in engines:
        for attempt in range(retries):
            try:
                time.sleep(0.3 + attempt * 0.5)
                res = ts.translate_text(
                    text,
                    from_language=from_lang,
                    to_language=to_lang,
                    translator=cur_engine,
                    timeout=20,
                )
                if res and isinstance(res, str) and len(res.strip()) > 0:
                    with CACHE_LOCK:
                        _CACHE[cache_key] = res
                    return res
            except Exception as e:
                last_err = e
                time.sleep(0.8 + attempt * 0.8)

    print(f"[WARN] Translation failed for snippet ({from_lang}->{to_lang}): {last_err}")
    return text


def apply_terminology(text: str, target_lang: str) -> str:
    """Apply standard Apple macOS localized terminology substitutions outside code blocks."""
    terms = MACOS_TERMS.get(target_lang, {})
    if not terms:
        return text

    lines = text.splitlines(keepends=True)
    out: List[str] = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)
            continue

        mod_line = line
        for src_term, dst_term in terms.items():
            if src_term in mod_line:
                mod_line = mod_line.replace(src_term, dst_term)
        out.append(mod_line)

    return "".join(out)


def protect_section_body(body_text: str) -> Tuple[str, Dict[str, str]]:
    """
    Protects code blocks, inline code, HTML tags, images, and link URLs in a section body.
    Returns: (protected_text, placeholders_dict)
    """
    placeholders: Dict[str, str] = {}
    p_idx = 0

    def add_p(val: str, prefix: str) -> str:
        nonlocal p_idx
        k = f"__ATB_{prefix}_{p_idx:05d}__"
        placeholders[k] = val
        p_idx += 1
        return k

    # 1. Code blocks
    lines = body_text.splitlines(keepends=True)
    out: List[str] = []
    in_code = False
    code_buf: List[str] = []

    for l in lines:
        stripped = l.strip()
        if stripped.startswith("```"):
            if not in_code:
                in_code = True
                code_buf = [l]
            else:
                code_buf.append(l)
                in_code = False
                key = add_p("".join(code_buf), "CODE")
                out.append(key + "\n")
                code_buf = []
            continue
        if in_code:
            code_buf.append(l)
        else:
            out.append(l)

    if in_code and code_buf:
        key = add_p("".join(code_buf), "CODE")
        out.append(key + "\n")

    text = "".join(out)

    # 2. Badges [![alt](badge_url)](link_url)
    text = re.sub(
        r"\[!\[([^\]]*)\]\(([^)]+)\)\]\(([^)]+)\)",
        lambda m: add_p(m.group(0), "BDG"),
        text,
    )

    # 3. Standard Markdown images ![alt](url)
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        lambda m: add_p(m.group(0), "IMG"),
        text,
    )

    # 4. Comments <!-- ... -->
    text = re.sub(
        r"(<!--[\s\S]*?-->)",
        lambda m: add_p(m.group(0), "CMT"),
        text,
    )

    # 5. Keycaps <kbd>...</kbd>
    text = re.sub(
        r"(<kbd>[^<]*</kbd>)",
        lambda m: add_p(m.group(0), "KBD"),
        text,
    )

    # 6. General HTML tags
    text = re.sub(
        r"(<[^>]+>)",
        lambda m: add_p(m.group(0), "HTML"),
        text,
    )

    # 7. Inline code `...`
    text = re.sub(
        r"(`[^`]+`)",
        lambda m: add_p(m.group(0), "INL"),
        text,
    )

    # 8. Markdown link URLs [anchor](url) -> keep anchor translatable, protect URL
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f"[{m.group(1)}]({add_p(m.group(2), 'URL')})",
        text,
    )

    return text, placeholders


def restore_placeholders(text: str, placeholders: Dict[str, str]) -> str:
    """Restores protected placeholders with support for fuzzy whitespace around underscores."""
    for k, v in reversed(list(placeholders.items())):
        if k in text:
            text = text.replace(k, v)
        else:
            pat = re.escape(k).replace(r"\_", r"[\s_]*")
            text = re.sub(pat, lambda _: v, text)
    return text


def translate_markdown_document(
    content: str,
    target_lang: str,
    filename: str,
    engine: str = "google",
    use_cache: bool = True,
) -> str:
    """
    Translates an entire markdown document by sections.
    Guarantees:
      - 100% exact heading count and level structure
      - Untranslated code blocks
      - 100% identical image links and paths
      - Intact inline code, <kbd> tags, and link destinations
    """
    lang_info = get_language(target_lang)
    nav_title = lang_info["nav_titles"].get(filename, "") if lang_info else ""

    # Phase 1: Parse document into discrete sections outside code blocks
    lines = content.splitlines(keepends=True)
    sections: List[Dict[str, Any]] = []
    cur_sec: Dict[str, Any] = {"level": 0, "title": "", "lines": []}
    in_code = False

    for l in lines:
        stripped = l.strip()
        if stripped.startswith("```"):
            in_code = not in_code

        if not in_code:
            m = re.match(r"^([ ]{0,3})(#{1,6})\s+(.*)$", l)
            if m:
                if cur_sec["lines"] or cur_sec["title"] or cur_sec["level"] > 0:
                    sections.append(cur_sec)
                cur_sec = {
                    "level": len(m.group(2)),
                    "title": m.group(3).strip(),
                    "lines": [],
                }
                continue

        cur_sec["lines"].append(l)

    sections.append(cur_sec)

    # Phase 2: Translate and assemble sections
    doc_blocks: List[str] = []

    for sec in sections:
        level = sec["level"]
        title = sec["title"]
        body_raw = "".join(sec["lines"]).strip()

        # 1. Translate Section Header
        if level == 1:
            if nav_title:
                doc_blocks.append(f"# {nav_title}")
            else:
                doc_blocks.append(f"# {title}")
        elif level > 0 and title:
            # Protect inline code in title if present
            if "`" in title or "<kbd>" in title or "[" in title:
                t_prot, t_phs = protect_section_body(title)
                t_trans = translate_snippet(
                    t_prot, to_lang=target_lang, engine=engine, use_cache=use_cache
                )
                t_rest = restore_placeholders(t_trans, t_phs)
                doc_blocks.append(f"{'#' * level} {t_rest.strip()}")
            else:
                t_trans = translate_snippet(
                    title, to_lang=target_lang, engine=engine, use_cache=use_cache
                )
                doc_blocks.append(f"{'#' * level} {t_trans.strip()}")

        # 2. Translate Section Body
        if body_raw:
            prot_body, phs = protect_section_body(body_raw)

            # If body is small, translate directly; otherwise chunk by paragraphs
            if len(prot_body) <= 2200:
                trans_b = translate_snippet(
                    prot_body, to_lang=target_lang, engine=engine, use_cache=use_cache
                )
            else:
                paragraphs = prot_body.split("\n\n")
                chunks: List[str] = []
                cur_c: List[str] = []
                cur_l = 0

                for p in paragraphs:
                    if cur_l + len(p) > 2000 and cur_c:
                        chunks.append("\n\n".join(cur_c))
                        cur_c = [p]
                        cur_l = len(p)
                    else:
                        cur_c.append(p)
                        cur_l += len(p)
                if cur_c:
                    chunks.append("\n\n".join(cur_c))

                trans_chunks: List[str] = []
                for c in chunks:
                    if c.strip():
                        t_c = translate_snippet(
                            c, to_lang=target_lang, engine=engine, use_cache=use_cache
                        )
                        trans_chunks.append(t_c)
                    else:
                        trans_chunks.append(c)
                trans_b = "\n\n".join(trans_chunks)

            restored_b = restore_placeholders(trans_b, phs)
            doc_blocks.append(restored_b)

    full_text = "\n\n".join(doc_blocks)

    # Phase 3: Post-processing
    full_text = apply_terminology(full_text, target_lang)
    full_text = format_lists_content(full_text)

    return full_text


def translate_zh_hant_doc(zh_source_path: str, en_source_path: str, filename: str) -> str:
    """High-fidelity Traditional Chinese generation via OpenCC s2twp."""
    lang_info = get_language("zh-hant")
    nav_title = lang_info["nav_titles"].get(filename, "") if lang_info else ""

    if os.path.isfile(zh_source_path):
        with open(zh_source_path, "r", encoding="utf-8") as f:
            zh_content = f.read()
    else:
        with open(en_source_path, "r", encoding="utf-8") as f:
            zh_content = f.read()

    if HAVE_OPENCC:
        cc = OpenCC("s2twp")
        hant_content = cc.convert(zh_content)
    else:
        hant_content = zh_content

    if nav_title:
        hant_content = re.sub(
            r"^#\s+.*$", f"# {nav_title}", hant_content, count=1, flags=re.MULTILINE
        )

    hant_content = apply_terminology(hant_content, "zh-hant")
    hant_content = format_lists_content(hant_content)
    return hant_content


def init_language_assets(target_lang: str, docs_dir: str = "docs") -> None:
    """Ensure target language folder has images, stylesheets, and javascripts initialized."""
    lang_dir = os.path.join(docs_dir, target_lang)
    en_dir = os.path.join(docs_dir, "en")
    os.makedirs(lang_dir, exist_ok=True)

    # 1. Stylesheets
    tgt_css_dir = os.path.join(lang_dir, "stylesheets")
    src_css_dir = os.path.join(en_dir, "stylesheets")
    os.makedirs(tgt_css_dir, exist_ok=True)
    src_css = os.path.join(src_css_dir, "extra.css")
    tgt_css = os.path.join(tgt_css_dir, "extra.css")
    if os.path.isfile(src_css) and not os.path.isfile(tgt_css):
        shutil.copy2(src_css, tgt_css)

    # 2. Javascripts
    tgt_js_dir = os.path.join(lang_dir, "javascripts")
    src_js_dir = os.path.join(en_dir, "javascripts")
    os.makedirs(tgt_js_dir, exist_ok=True)
    if os.path.isdir(src_js_dir):
        for js_file in os.listdir(src_js_dir):
            if js_file.endswith(".js"):
                s_js = os.path.join(src_js_dir, js_file)
                t_js = os.path.join(tgt_js_dir, js_file)
                if not os.path.isfile(t_js):
                    shutil.copy2(s_js, t_js)

    # 3. Images - real files on disk to guarantee Zensical builds without missing asset errors
    tgt_img_dir = os.path.join(lang_dir, "images")
    src_img_dir = os.path.join(en_dir, "images")
    os.makedirs(tgt_img_dir, exist_ok=True)
    if os.path.isdir(src_img_dir):
        for img_file in os.listdir(src_img_dir):
            if img_file.endswith(".png") or img_file.endswith(".jpg") or img_file.endswith(".svg"):
                s_img = os.path.join(src_img_dir, img_file)
                t_img = os.path.join(tgt_img_dir, img_file)
                if not os.path.isfile(t_img):
                    try:
                        os.link(s_img, t_img)
                    except OSError:
                        shutil.copy2(s_img, t_img)


def process_single_doc(
    filename: str,
    target_lang: str,
    docs_dir: str = "docs",
    engine: str = "google",
    use_cache: bool = True,
) -> Tuple[bool, str]:
    """Translate, format, and write a single documentation file with parity validation."""
    en_path = os.path.join(docs_dir, "en", filename)
    zh_path = os.path.join(docs_dir, "zh", filename)
    target_path = os.path.join(docs_dir, target_lang, filename)

    if not os.path.isfile(en_path):
        return False, f"Source file {en_path} not found"

    try:
        t0 = time.time()
        if target_lang == "zh-hant":
            translated = translate_zh_hant_doc(zh_path, en_path, filename)
        else:
            with open(en_path, "r", encoding="utf-8") as f:
                en_content = f.read()
            translated = translate_markdown_document(
                en_content,
                target_lang=target_lang,
                filename=filename,
                engine=engine,
                use_cache=use_cache,
            )

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(translated)

        # Verify parity immediately
        is_ok, errs, stats = check_file_parity(
            filename, en_path, target_path, target_lang, docs_dir
        )
        dur = time.time() - t0

        if is_ok:
            return True, f"[{target_lang}] {filename:<34} PASS ({dur:.2f}s, H:{stats['target_header_count']}, Img:{stats['target_image_count']})"
        else:
            return False, f"[{target_lang}] {filename:<34} PARITY ERRORS: {'; '.join(errs)}"

    except Exception as e:
        return False, f"[{target_lang}] {filename:<34} EXCEPTION: {e}"


def translate_language(
    target_lang: str,
    docs: Optional[List[str]] = None,
    docs_dir: str = "docs",
    engine: str = "google",
    use_cache: bool = True,
    parallel: int = 1,
) -> int:
    """Translate all or specified documents for a single language."""
    init_language_assets(target_lang, docs_dir=docs_dir)
    target_docs = docs or NAV_ORDER
    lang_info = get_language(target_lang)
    lang_name = lang_info["name"] if lang_info else target_lang

    print(f"\nTranslating [{target_lang}] {lang_name} ({len(target_docs)} docs, parallel={parallel})...")

    errors = 0
    if parallel > 1 and target_lang != "zh-hant":
        with concurrent.futures.ThreadPoolExecutor(max_workers=parallel) as ex:
            futs = {
                ex.submit(
                    process_single_doc,
                    doc,
                    target_lang,
                    docs_dir,
                    engine,
                    use_cache,
                ): doc
                for doc in target_docs
            }
            for fut in concurrent.futures.as_completed(futs):
                ok, msg = fut.result()
                print(f"  {msg}")
                if not ok:
                    errors += 1
    else:
        for doc in target_docs:
            ok, msg = process_single_doc(
                doc, target_lang, docs_dir, engine, use_cache
            )
            print(f"  {msg}")
            if not ok:
                errors += 1

    save_cache()
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Batch translate ATBCmder documentation across target languages."
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Translate all 9 new languages (zh-hant, ja, de, fr, es, pt, ko, ru, it).",
    )
    parser.add_argument(
        "--lang",
        help="Comma-separated list of target language codes (e.g. 'ja,de,fr').",
    )
    parser.add_argument(
        "--doc",
        help="Specific document filename to translate (e.g. 'index.md'). Default: all 12 chapters.",
    )
    parser.add_argument(
        "--parallel",
        type=int,
        default=2,
        help="Parallel worker count for concurrent translation requests (default: 2).",
    )
    parser.add_argument(
        "--engine",
        default="google",
        help="Translation engine to use (default: 'google').",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="Do not use cached translations.",
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Documentation root directory (default: 'docs').",
    )

    args = parser.parse_args()

    if args.all:
        target_languages = TARGET_LANGUAGES
    elif args.lang:
        target_languages = [l.strip() for l in args.lang.split(",") if l.strip()]
    else:
        print("Error: Specify --all or --lang <code1,code2...>")
        return 1

    docs_to_translate = [args.doc] if args.doc else NAV_ORDER

    load_cache()
    print(f"Loaded {len(_CACHE)} cached translation entries.")
    print(f"Target languages: {', '.join(target_languages)}")
    print(f"Documents: {len(docs_to_translate)} chapter(s)")

    total_errors = 0
    t_start = time.time()

    for lang in target_languages:
        errs = translate_language(
            target_lang=lang,
            docs=docs_to_translate,
            docs_dir=args.docs_dir,
            engine=args.engine,
            use_cache=not args.no_cache,
            parallel=args.parallel,
        )
        total_errors += errs

    save_cache()
    dur = time.time() - t_start
    print(f"\nBatch translation completed in {dur:.2f}s with {total_errors} errors.")
    return 0 if total_errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
