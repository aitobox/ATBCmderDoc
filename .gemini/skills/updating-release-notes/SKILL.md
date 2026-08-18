---
name: updating-release-notes
description: Use when adding, updating, or managing release notes and changelogs in the documentation
---

# Updating Release Notes

## Overview
This skill provides standard procedures for updating version release notes across bilingual documentation, building static sites, and committing changes to Git.

## When to Use
- Adding a new app version release note
- Updating existing changelog entries in the download documentation

## Core Requirements

1. **Read & Parse User Input**: Extract version numbers, release dates, and feature/fix bullet points provided by the user.
2. **Reverse Chronological Order**: The newest release version MUST be inserted at the very top of the Release Notes section (immediately below `## Release Notes` in `docs/en/download.md` and `## 更新日志 (Release Notes)` in `docs/zh/download.md`).
3. **Bilingual Parity**: 
   - Update both `docs/en/download.md` and `docs/zh/download.md` in the same turn.
   - Proactively translate English entries to natural Simplified Chinese (and vice versa) so both documents remain 1:1 aligned.
4. **Verification**: Run `zensical build` on both configuration files (`zensical.en.toml` and `zensical.zh.toml`) to verify site build integrity.
5. **Git Commit & Push**: Commit the updated documentation files and push them to the remote repository.

## Red Flags - STOP and Fix

- Placing new release notes at the bottom of the section instead of the top.
- Updating `docs/en/download.md` while leaving `docs/zh/download.md` outdated.
- Skipping `git push` when the task requests publishing updates.

## Step-by-Step Procedure

```bash
# 1. Update docs/en/download.md and docs/zh/download.md (Newest version first)

# 2. Verify static site build
zensical build -f zensical.en.toml && zensical build -f zensical.zh.toml

# 3. Commit and push changes
git add docs/en/download.md docs/zh/download.md
git commit -m "docs: add X.Y.Z release notes (en & zh)"
git push
```
