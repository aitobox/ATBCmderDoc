---
name: writing-bilingual-docs
description: Use when creating, updating, or modifying any user-facing documentation or release notes in this project
---

# Writing Bilingual Documentation

## Overview
This project maintains strict 1:1 parity between English and Simplified Chinese documentation. Every documentation change must be applied symmetrically to both languages and written in simple, user-friendly language.

## When to Use
- Adding new feature descriptions to the manual
- Updating release notes or changelogs
- Modifying navigation menus or site configuration
- Fixing typos or outdated information in the docs

## Core Requirements

1. **Strict Bilingual Parity**: Every edit made to a file in `docs/en/` MUST have an equivalent edit in `docs/zh/` (and vice versa).
2. **Translate Proactively**: If the user provides content in only one language, it is YOUR responsibility to translate it into the other language before applying the change.
3. **Configuration Symmetry**: If you add a new page, you MUST update both `zensical.en.toml` and `zensical.zh.toml`.
4. **User-Friendly Tone**: Write for end-users, not developers. 
   - Use clear, simple language.
   - Explain features in terms of user benefits.
   - Avoid internal architecture jargon unless it is necessary for power users.

## Red Flags - STOP and Fix

- "The user only provided the English text, so I only updated the English file."
- "I updated `docs/zh/navigation.md` but forgot `docs/en/navigation.md`."
- "I added a new markdown file but didn't link it in the `zensical.*.toml` config."
- Using overly technical phrasing like "The IPC socket polling mechanism" instead of "Background processing".

**All of these mean: Stop. Translate the content, update the missing counterpart, and simplify the language.**

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "The user only asked me to add this text, they didn't ask for a translation." | Bilingual parity is a strict project constraint. You must proactively translate and update both. |
| "I'll just add the Chinese version later." | Do it in the same tool call or turn to prevent desync. |
| "The technical details are important for accuracy." | End-users need to know how to use it, not how it's coded. Keep it simple and focus on the UI/UX. |

## Verification Check

Before concluding your task, always verify:
1. Did I edit both `docs/zh/XYZ.md` and `docs/en/XYZ.md`?
2. Are the translations natural and easy to read?
3. If a new page was added, are both TOML navigation files updated?
