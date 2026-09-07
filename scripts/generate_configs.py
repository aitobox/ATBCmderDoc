#!/usr/bin/env python3
"""
scripts/generate_configs.py
Synchronizes and verifies zensical.<lang>.toml configuration files for all 11 supported languages.
Prevents configuration drift across multilingual documentation builds.
"""

import argparse
import difflib
import sys
import tomllib
from pathlib import Path
from typing import Any, Dict, List

# Ensure scripts dir is in sys.path
SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from languages import DEFAULT_LANGUAGE, LANGUAGES, NAV_ORDER, get_language_codes

PROJECT_ROOT = SCRIPTS_DIR.parent

# Global defaults across all documentation sites
SITE_NAME = "ATBCmder"
REPO_URL = "https://github.com/aitobox/ATBCmderDoc"
REPO_NAME = "ATBCmderDoc"
APP_STORE_URL = "https://apps.apple.com/app/atbcmder/id6792398333"

EXTRA_JAVASCRIPT = [
    "javascripts/language-detector.js",
    "javascripts/ascii-diagram.js",
]
EXTRA_CSS = ["stylesheets/extra.css"]

THEME_NAME = "material"
THEME_CUSTOM_DIR = "overrides"
THEME_PALETTE = [
    {
        "scheme": "default",
        "primary": "light-blue",
        "accent": "cyan",
        "media": "(prefers-color-scheme: light)",
    },
    {
        "scheme": "slate",
        "primary": "light-blue",
        "accent": "cyan",
        "media": "(prefers-color-scheme: dark)",
    },
]
THEME_FONT = {"text": "Inter", "code": "JetBrains Mono"}
THEME_FEATURES = [
    "navigation.top",
    "search.highlight",
    "content.code.copy",
]


def build_alternate_list() -> List[Dict[str, str]]:
    """Build list of all 11 alternate language links."""
    return [
        {"name": lang["name"], "link": f"/{lang['code']}/", "lang": lang["code"]}
        for lang in LANGUAGES
    ]


def generate_config_content(lang: Dict[str, Any]) -> str:
    """Generate the complete TOML content for a single language."""
    code = lang["code"]
    description = lang["description"]
    theme_lang = lang["theme_lang"]
    nav_titles = lang["nav_titles"]

    lines: List[str] = []
    lines.append("[project]")
    lines.append(f'site_name    = "{SITE_NAME}"')
    lines.append(f'site_url     = "https://cmder.aitobox.com/{code}/"')
    lines.append(f'site_description = "{description}"')
    lines.append(f'repo_url     = "{REPO_URL}"')
    lines.append(f'repo_name    = "{REPO_NAME}"')
    lines.append(f'docs_dir     = "docs/{code}"')
    lines.append(f'site_dir     = "site/{code}"')
    lines.append("")
    lines.append("extra_javascript = [")
    for i, js in enumerate(EXTRA_JAVASCRIPT):
        comma = "," if i < len(EXTRA_JAVASCRIPT) - 1 else ""
        lines.append(f'  "{js}"{comma}')
    lines.append("]")
    lines.append(f'extra_css        = ["{EXTRA_CSS[0]}"]')
    lines.append("")
    lines.append("nav = [")
    for i, filename in enumerate(NAV_ORDER):
        title = nav_titles.get(filename, filename)
        escaped_title = title.replace('"', '\\"')
        comma = "," if i < len(NAV_ORDER) - 1 else ""
        lines.append(f'  {{ "{escaped_title}" = "{filename}" }}{comma}')
    lines.append("]")
    lines.append("")
    lines.append("[project.theme]")
    lines.append(f'name        = "{THEME_NAME}"')
    lines.append(f'custom_dir  = "{THEME_CUSTOM_DIR}"')
    lines.append(f'language    = "{theme_lang}"')
    lines.append("palette     = [")
    for i, p in enumerate(THEME_PALETTE):
        comma = "," if i < len(THEME_PALETTE) - 1 else ""
        lines.append(
            f'  {{ scheme = "{p["scheme"]}", primary = "{p["primary"]}", '
            f'accent = "{p["accent"]}", media = "{p["media"]}" }}{comma}'
        )
    lines.append("]")
    lines.append(
        f'font        = {{ text = "{THEME_FONT["text"]}", code = "{THEME_FONT["code"]}" }}'
    )
    lines.append("features    = [")
    for i, feat in enumerate(THEME_FEATURES):
        comma = "," if i < len(THEME_FEATURES) - 1 else ""
        lines.append(f'  "{feat}"{comma}')
    lines.append("]")
    lines.append("")
    lines.append("[project.extra]")
    lines.append(f'app_store_url = "{APP_STORE_URL}"')
    lines.append("alternate = [")
    alternates = build_alternate_list()
    for i, alt in enumerate(alternates):
        comma = "," if i < len(alternates) - 1 else ""
        lines.append(
            f'  {{ name = "{alt["name"]}", link = "{alt["link"]}", lang = "{alt["lang"]}" }}{comma}'
        )
    lines.append("]")
    lines.append("")

    return "\n".join(lines)


def validate_toml(content: str, filename: str) -> None:
    """Validate that the generated content is valid TOML syntax."""
    try:
        tomllib.loads(content)
    except Exception as e:
        raise ValueError(f"Generated invalid TOML for {filename}: {e}") from e


def generate_all_configs(project_root: Path = PROJECT_ROOT) -> None:
    """Generate or update zensical.<lang>.toml for all 11 languages."""
    print(f"Generating Zensical configurations for {len(LANGUAGES)} languages...")
    for lang in LANGUAGES:
        code = lang["code"]
        config_path = project_root / f"zensical.{code}.toml"
        content = generate_config_content(lang)
        validate_toml(content, config_path.name)
        config_path.write_text(content, encoding="utf-8")
        print(f"  [OK] Generated {config_path.name}")
    print("Done! All 11 configurations generated successfully.")


def check_configs(project_root: Path = PROJECT_ROOT, show_diff: bool = True) -> bool:
    """Check whether current zensical.<lang>.toml files match generated configs."""
    drift_found = False
    print(f"Checking {len(LANGUAGES)} Zensical configurations for drift...")

    for lang in LANGUAGES:
        code = lang["code"]
        config_path = project_root / f"zensical.{code}.toml"
        expected_content = generate_config_content(lang)
        validate_toml(expected_content, config_path.name)

        if not config_path.exists():
            print(f"  [MISSING] {config_path.name} does not exist!")
            drift_found = True
            continue

        actual_content = config_path.read_text(encoding="utf-8")
        if actual_content != expected_content:
            print(f"  [DRIFT] {config_path.name} does not match expected configuration!")
            drift_found = True
            if show_diff:
                diff = difflib.unified_diff(
                    actual_content.splitlines(keepends=True),
                    expected_content.splitlines(keepends=True),
                    fromfile=f"actual/{config_path.name}",
                    tofile=f"expected/{config_path.name}",
                )
                sys.stdout.writelines(diff)
        else:
            print(f"  [SYNCED] {config_path.name}")

    if drift_found:
        print("\nERROR: Configuration drift detected!")
        print("Run `python3 scripts/generate_configs.py` to re-synchronize all configs.")
        return False

    print("\nSUCCESS: All 11 configuration files are perfectly synchronized.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate and verify zensical.<lang>.toml for 11 documentation languages."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Check for configuration drift without modifying files (exit 0 if synced, 1 if drift).",
    )
    parser.add_argument(
        "--no-diff",
        action="store_true",
        help="Do not display diff when checking for drift.",
    )
    args = parser.parse_args()

    if args.check:
        success = check_configs(project_root=PROJECT_ROOT, show_diff=not args.no_diff)
        return 0 if success else 1
    else:
        generate_all_configs(project_root=PROJECT_ROOT)
        return 0


if __name__ == "__main__":
    sys.exit(main())
