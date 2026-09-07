#!/usr/bin/env python3
"""
check_parity.py - Validates 1:1 documentation parity across language directories.

Benchmark: docs/en/ (12 chapters defined in NAV_ORDER)
Validates:
  1. File inventory: All 12 files in docs/en/ exist in docs/<lang>/.
  2. Header hierarchy: H1, H2, H3 counts and structural nesting order match docs/en/.
  3. Image references: Counts, local image filenames, and existence of image assets on disk.

Usage:
  python3 scripts/check_parity.py [--target-lang <lang>] [--all] [--verbose]
"""

import argparse
import os
import re
import sys
from typing import Any, Dict, List, Optional, Tuple

# Ensure project root is in sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from scripts.languages import NAV_ORDER, get_language, get_language_codes

# ANSI colors
USE_COLOR = sys.stdout.isatty() and "NO_COLOR" not in os.environ
GREEN = "\033[92m" if USE_COLOR else ""
RED = "\033[91m" if USE_COLOR else ""
YELLOW = "\033[93m" if USE_COLOR else ""
CYAN = "\033[96m" if USE_COLOR else ""
BOLD = "\033[1m" if USE_COLOR else ""
RESET = "\033[0m" if USE_COLOR else ""


def strip_code_blocks(text: str) -> str:
    """Strip fenced code blocks to ignore comments that look like headings."""
    lines = []
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if not in_code:
            lines.append(line)
    return "\n".join(lines)


def extract_headers(text: str) -> List[Tuple[int, str, int]]:
    """
    Extract H1, H2, and H3 headers outside code blocks.
    Returns: List of (level, title, line_number)
    """
    clean_text = strip_code_blocks(text)
    headers = []
    for line_no, line in enumerate(clean_text.splitlines(), start=1):
        m = re.match(r"^[ ]{0,3}(#{1,3})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            headers.append((level, title, line_no))
    return headers


def extract_image_references(text: str) -> List[Dict[str, Any]]:
    """
    Extract markdown image references outside code blocks.
    Returns: List of image dicts with alt, clean_url, is_local, basename.
    """
    clean_text = strip_code_blocks(text)
    raw_matches = re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", clean_text)
    images = []
    for m in raw_matches:
        alt = m.group(1).strip()
        raw_target = m.group(2).strip()
        clean_url = raw_target.split()[0].strip()
        # Clean any trailing markdown attributes or quotes
        clean_url = re.sub(r"[\"'].*$", "", clean_url).strip()
        is_local = (
            clean_url.startswith("images/")
            or clean_url.startswith("../images/")
            or "/images/" in clean_url
        ) and not clean_url.startswith("http")
        images.append(
            {
                "alt": alt,
                "url": clean_url,
                "is_local": is_local,
                "basename": os.path.basename(clean_url) if is_local else None,
            }
        )
    return images


def check_file_parity(
    rel_path: str,
    en_file_path: str,
    target_file_path: str,
    target_lang: str,
    docs_dir: str,
) -> Tuple[bool, List[str], Dict[str, Any]]:
    """
    Check parity between benchmark file (en) and target language file.
    Returns: (is_ok, errors, stats)
    """
    errors = []
    stats = {}

    if not os.path.isfile(target_file_path):
        errors.append(f"Missing file: {target_file_path}")
        return False, errors, stats

    with open(en_file_path, "r", encoding="utf-8") as f:
        en_content = f.read()

    with open(target_file_path, "r", encoding="utf-8") as f:
        target_content = f.read()

    # 1. Header checks
    en_headers = extract_headers(en_content)
    target_headers = extract_headers(target_content)

    stats["en_header_count"] = len(en_headers)
    stats["target_header_count"] = len(target_headers)
    stats["h1_count"] = sum(1 for h in target_headers if h[0] == 1)
    stats["h2_count"] = sum(1 for h in target_headers if h[0] == 2)
    stats["h3_count"] = sum(1 for h in target_headers if h[0] == 3)

    if len(en_headers) != len(target_headers):
        errors.append(
            f"Header count mismatch: expected {len(en_headers)} headers, found {len(target_headers)}"
        )
    else:
        for idx, (en_h, tgt_h) in enumerate(zip(en_headers, target_headers)):
            if en_h[0] != tgt_h[0]:
                errors.append(
                    f"Header structure mismatch at index #{idx + 1}: expected H{en_h[0]} ('{en_h[1]}'), found H{tgt_h[0]} ('{tgt_h[1]}')"
                )
                break

    # 2. Image checks
    en_images = extract_image_references(en_content)
    target_images = extract_image_references(target_content)

    stats["en_image_count"] = len(en_images)
    stats["target_image_count"] = len(target_images)

    en_local_basenames = [img["basename"] for img in en_images if img["is_local"]]
    target_local_basenames = [
        img["basename"] for img in target_images if img["is_local"]
    ]
    stats["local_image_count"] = len(target_local_basenames)

    if len(en_images) != len(target_images):
        errors.append(
            f"Image count mismatch: expected {len(en_images)} images, found {len(target_images)}"
        )

    if en_local_basenames != target_local_basenames:
        errors.append(
            f"Local image mismatch: expected {en_local_basenames}, found {target_local_basenames}"
        )

    # Check local image existence on disk
    target_dir = os.path.dirname(target_file_path)
    for img in target_images:
        if img["is_local"]:
            local_rel = img["url"]
            # Possible paths: relative to target file or in docs/<lang>/images/ or docs/en/images/
            possible_paths = [
                os.path.normpath(os.path.join(target_dir, local_rel)),
                os.path.normpath(os.path.join(docs_dir, target_lang, "images", img["basename"])),
                os.path.normpath(os.path.join(docs_dir, "en", "images", img["basename"])),
                os.path.normpath(os.path.join(docs_dir, "images", img["basename"])),
            ]
            if not any(os.path.isfile(p) for p in possible_paths):
                errors.append(
                    f"Image asset missing on disk: '{img['url']}' (basename: '{img['basename']}')"
                )

    return (len(errors) == 0, errors, stats)


def check_language_parity(
    target_lang: str,
    docs_dir: str = "docs",
    benchmark_lang: str = "en",
    verbose: bool = False,
) -> Tuple[bool, int, List[str]]:
    """
    Check parity for a given target language against benchmark.
    Returns: (is_ok, total_errors, log_lines)
    """
    lang_info = get_language(target_lang)
    lang_name = lang_info["name"] if lang_info else target_lang
    target_dir = os.path.join(docs_dir, target_lang)
    benchmark_dir = os.path.join(docs_dir, benchmark_lang)

    logs = []
    logs.append(
        f"\n{BOLD}Checking Parity: [{target_lang}] {lang_name} vs [{benchmark_lang}] Benchmark{RESET}"
    )
    logs.append("-" * 72)

    if not os.path.isdir(target_dir):
        msg = f"Target directory '{target_dir}' does not exist."
        logs.append(f"  {RED}[FAIL]{RESET} {msg}")
        return False, 12, logs

    total_errors = 0
    passed_files = 0

    for fname in NAV_ORDER:
        en_path = os.path.join(benchmark_dir, fname)
        target_path = os.path.join(target_dir, fname)

        if not os.path.isfile(en_path):
            logs.append(f"  {RED}[FAIL]{RESET} Benchmark file missing: {en_path}")
            total_errors += 1
            continue

        is_ok, errors, stats = check_file_parity(
            fname, en_path, target_path, target_lang, docs_dir
        )

        if is_ok:
            passed_files += 1
            h_str = f"H:{stats['target_header_count']} [H1:{stats['h1_count']} H2:{stats['h2_count']} H3:{stats['h3_count']}]"
            img_str = f"Img:{stats['target_image_count']} ({stats['local_image_count']} local)"
            logs.append(
                f"  {GREEN}[PASS]{RESET} {fname:<34} {h_str:<28} {img_str}"
            )
        else:
            total_errors += len(errors)
            logs.append(f"  {RED}[FAIL]{RESET} {fname:<34} ({len(errors)} errors)")
            for err in errors:
                logs.append(f"         {YELLOW}↳ {err}{RESET}")

    logs.append("-" * 72)
    if total_errors == 0:
        logs.append(
            f"  {GREEN}✓ [{target_lang}] All {passed_files}/{len(NAV_ORDER)} files passed 1:1 parity checks.{RESET}"
        )
    else:
        logs.append(
            f"  {RED}✗ [{target_lang}] Found {total_errors} parity errors across {len(NAV_ORDER)} files.{RESET}"
        )

    return (total_errors == 0, total_errors, logs)


def main():
    parser = argparse.ArgumentParser(
        description="Verify 1:1 documentation parity against English benchmark."
    )
    parser.add_argument(
        "--target-lang",
        dest="target_lang",
        help="Specific target language code to check (e.g. 'zh', 'ja', 'de').",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Require and check all configured languages in scripts/languages.py.",
    )
    parser.add_argument(
        "--docs-dir",
        default="docs",
        help="Documentation root directory (default: 'docs').",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Show verbose output.",
    )

    args = parser.parse_args()

    # Validate benchmark
    benchmark_dir = os.path.join(args.docs_dir, "en")
    if not os.path.isdir(benchmark_dir):
        print(f"{RED}Error: Benchmark directory '{benchmark_dir}' not found.{RESET}")
        sys.exit(1)

    configured_codes = get_language_codes()
    all_target_codes = [c for c in configured_codes if c != "en"]

    if args.target_lang:
        if args.target_lang not in configured_codes:
            print(
                f"{RED}Error: Unknown language '{args.target_lang}'. Configured: {all_target_codes}{RESET}"
            )
            sys.exit(1)
        if args.target_lang == "en":
            print(f"{YELLOW}Warning: 'en' is the benchmark language. Checking parity against itself is trivial.{RESET}")
            targets_to_check = ["en"]
        else:
            targets_to_check = [args.target_lang]
    else:
        if args.all:
            targets_to_check = all_target_codes
        else:
            # Check configured languages that have directories on disk
            available = [
                c for c in all_target_codes if os.path.isdir(os.path.join(args.docs_dir, c))
            ]
            skipped = [
                c for c in all_target_codes if not os.path.isdir(os.path.join(args.docs_dir, c))
            ]
            if skipped:
                print(
                    f"{CYAN}[INFO] Languages not yet initialized in '{args.docs_dir}/' (skipped): {', '.join(skipped)}{RESET}"
                )
                print(
                    f"{CYAN}[INFO] Use --all to enforce that all configured languages must exist.{RESET}"
                )
            targets_to_check = available

    if not targets_to_check:
        print(f"{YELLOW}No target languages found to check.{RESET}")
        sys.exit(0)

    print(f"{BOLD}========================================================================{RESET}")
    print(f"{BOLD}             ATBCmder Documentation Parity Linter                     {RESET}")
    print(f"{BOLD}========================================================================{RESET}")
    print(f"Benchmark:   {args.docs_dir}/en ({len(NAV_ORDER)} chapters)")
    print(f"Target(s):   {', '.join(targets_to_check)}")

    overall_success = True
    total_errors_all = 0

    for lang in targets_to_check:
        is_ok, err_count, logs = check_language_parity(
            target_lang=lang,
            docs_dir=args.docs_dir,
            benchmark_lang="en",
            verbose=args.verbose,
        )
        for line in logs:
            print(line)
        if not is_ok:
            overall_success = False
            total_errors_all += err_count

    print(f"\n{BOLD}========================================================================{RESET}")
    if overall_success:
        print(
            f"{GREEN}✓ ALL PARITY CHECKS PASSED: Verified {len(targets_to_check)} language(s) with 0 errors.{RESET}"
        )
        print(f"{BOLD}========================================================================{RESET}")
        sys.exit(0)
    else:
        print(
            f"{RED}✗ PARITY CHECK FAILED: Found {total_errors_all} errors across {len(targets_to_check)} language(s).{RESET}"
        )
        print(f"{BOLD}========================================================================{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
