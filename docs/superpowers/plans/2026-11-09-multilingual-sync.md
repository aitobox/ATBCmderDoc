# Multilingual Documentation Synchronization (v2.4.6 Feature Updates) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Synchronize the 9 newly updated English documentation chapters across all 10 non-English languages (`zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`) with 100% header parity, Apple localized terminology, zero MD032 list formatting errors, and clean static site compilation.

**Architecture:** A quality-first phased pipeline: clean benchmark formatting in `docs/en/`, perform human-grade technical localization for Simplified Chinese (`docs/zh/`), generate Traditional Chinese (`docs/zh-hant/`) via OpenCC with Apple Taiwan HIG terminology (`分頁`, `預設`, `快速鍵`), propagate incremental section/table-row diffs to the 8 foreign languages while strictly preserving localized ASCII architecture diagrams, and validate the whole suite through `check_parity.py`, `format_markdown_lists.py`, and `./test.sh -b`.

**Tech Stack:** Python 3.12, Conda (`ATBCmderDoc`), OpenCC (`s2twp`), `translators` (Google / Bing / Alibaba engine fallback), Zensical (MkDocs Material engine), Bash.

**Spec:** [docs/superpowers/specs/2026-11-09-multilingual-sync-design.md](file:///Users/brainzhang/work/aitobox/ATBCmderDoc/docs/superpowers/specs/2026-11-09-multilingual-sync-design.md)

## Global Constraints

- All commands must be executed in the `ATBCmderDoc` conda environment (`conda run -n ATBCmderDoc ...`).
- Python-Markdown list blank line spacing rule (MD032) must be strictly maintained for every list item across all files.
- Commander Command IDs (`cm_*`), config keys (`quick_search.pinyin_search`, `quick_search.filter_only`, `view.trackpad_swipe_navigation`), keyboard glyphs (`⌘`, `⌥`, `⇧`, `⌃`), and image asset paths (`images/*.png`) must remain verbatim.
- Traditional Chinese documentation (`zh-hant`) must adhere to Apple Taiwan HIG terminology (e.g. `分頁`, `預設`, `快速鍵`, `檔案管理器`, `資料夾`, `垃圾桶`).
- Existing localized ASCII architecture diagrams and mentor refinements in `docs/{ja,de,fr,es,pt,ko,ru,it}/` must NOT be overwritten with raw English blocks.

## Review Focus

- Header count or nesting hierarchy mismatch between `docs/en/` benchmark and target language files — verify with `scripts/check_parity.py`.
- MD032 list spacing collapse caused by missing blank lines before lists — verify with `scripts/format_markdown_lists.py --check`.
- Traditional Chinese terminology regression (using `標籤頁` instead of `分頁`, or `默認` instead of `預設`).
- Overwriting localized ASCII art blocks in foreign languages with English diagrams during batch propagation.
- Static site compilation failures across any of the 11 `zensical.<lang>.toml` configs — verify with `./test.sh -b`.

---

### Task 1: Benchmark Lint & Formatting Cleanup

**Files:**
- Modify: `docs/en/navigation_and_tabs.md:115-125`

**Interfaces:**
- Produces: 100% MD032-clean English benchmark for all subsequent translations.

- [ ] **Step 1: Check existing MD032 list spacing errors**

Run: `conda run -n ATBCmderDoc python scripts/format_markdown_lists.py --check`  
Expected: FAIL indicating missing blank line before list in `docs/en/navigation_and_tabs.md`.

- [ ] **Step 2: Fix missing blank line in `docs/en/navigation_and_tabs.md`**

Add preceding blank line before list items in `docs/en/navigation_and_tabs.md` around lines 118–122.

- [ ] **Step 3: Verify clean markdown list lint**

Run: `conda run -n ATBCmderDoc python scripts/format_markdown_lists.py --check`  
Expected: PASS with 0 files failing.

- [ ] **Step 4: Commit benchmark fix**

```bash
git add docs/en/navigation_and_tabs.md
git commit -m "docs(en): fix MD032 list blank line spacing in navigation_and_tabs.md"
```

---

### Task 2: Simplified Chinese Localization (`docs/zh/`) - Part 1: Core Navigation & File Operations

**Files:**
- Modify: `docs/zh/navigation_and_tabs.md`
- Modify: `docs/zh/file_operations.md`

**Interfaces:**
- Consumes: `docs/en/navigation_and_tabs.md`, `docs/en/file_operations.md`
- Produces: Fully synchronized Chinese chapters with exact H1/H2/H3 header hierarchy (38 headers in navigation, 38 headers in file operations).

- [ ] **Step 1: Synchronize `docs/zh/navigation_and_tabs.md`**

Translate and inject:
- Navigation cheat sheet new rows: `cm_ViewHistoryPrev / Next` (触控板横向滑动手势), `cm_QuickSearch` (支持拼音与Filter模式说明), `cm_SrcAllFiles` (`Cmd+F10`), `cm_SrcUserDef` (`Cmd+F11`).
- Adjacent tab creation: `MacNativeTabBar` 新标签页在当前激活标签右侧邻近插入说明.
- Folder tabs table new commands: `cm_SetTabOptionLock` (锁定此标签页), `cm_SetTabOptionLockWithSubdirs` (锁定但允许进入子目录), `cm_SetTabOptionNormal` (解锁标签页).
- Section `### 标签页锁定模式（Total Commander 标准）`: 详细说明 `*` 标识、冻结根目录与双击子目录在邻近标签打开机制、允许进入子目录并在切换/点击根目录自动重置机制.
- Section 5: 拼音任意边界快速搜索 (`quick_search.pinyin_search`) 与 Filter 模式 (`quick_search.filter_only`) 详细说明与示例 (`gz` 匹配 `2024工作总结.docx`、`【公司】工资表.xlsx`).
- Section `### 文件掩码与扩展名过滤（Cmd+F10 / Cmd+F11）`: 详细说明交互输入通配符掩码、状态栏 `Mask: <pattern>` 指示及 `Cmd+F10` 一键复位.
- Master shortcuts table: 补充所有新命令行.

- [ ] **Step 2: Synchronize `docs/zh/file_operations.md`**

Translate and inject:
- Cheat sheet and Section 7 shortcuts: 更新目录空间计算快捷键为 `Alt+Shift+Return` (`⌥⇧⏎` / `cm_CountDirContent`)，标注适配 Mac 键盘回车键、后台异步扫描与 `Esc` 瞬时取消.
- Section 6.1 `### 6.1 数据完整性与安全传输协议`:
  - 原子暂存与替换写入：临时文件暂存 (`.tmp.atbcmder_*`) + POSIX 原子重命名 (`os.replace`) 防止断电损坏.
  - 符号链接移动保护：跨卷移动重建链接指针，保护源数据实体.
  - 解压 Zip-Slip / 路径穿越防护：拦截跳出目标目录的恶意符号链接与相对路径.

- [ ] **Step 3: Verify parity for `navigation_and_tabs.md` and `file_operations.md` in `zh`**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py --target-lang zh`  
Expected: `navigation_and_tabs.md` and `file_operations.md` show `[PASS]` (38 headers each).

- [ ] **Step 4: Commit Chinese navigation and file operations**

```bash
git add docs/zh/navigation_and_tabs.md docs/zh/file_operations.md
git commit -m "docs(zh): synchronize navigation_and_tabs and file_operations to v2.4.6"
```

---

### Task 3: Simplified Chinese Localization (`docs/zh/`) - Part 2: Editors, Network & Preferences

**Files:**
- Modify: `docs/zh/viewers_and_editors.md`
- Modify: `docs/zh/network_and_vfs.md`
- Modify: `docs/zh/preferences_and_customization.md`

**Interfaces:**
- Consumes: `docs/en/viewers_and_editors.md`, `docs/en/network_and_vfs.md`, `docs/en/preferences_and_customization.md`
- Produces: Synchronized Chinese chapters with exact H1/H2/H3 header hierarchy (30 headers in viewers, 32 headers in network, 45 headers in preferences).

- [ ] **Step 1: Synchronize `docs/zh/viewers_and_editors.md`**

- Update ASCII diagram in section 4 to the modern vector action toolbar:
  `[💾] [📄] [🔄] │ [↩] [↪] │ [🔍] [📝] │ [↩ 自动换行] [123 行号] │ [🔍+] [🔍-] [1:1]`
- Add Section `#### 全新现代矢量操作工具栏`: 包含保存 `⌘S`、另存为 `⇧⌘S`、重新载入 `⌘R`、撤销 `⌘Z`、重做 `⇧⌘Z`、查找 `⌘F`、替换 `⌥⌘F`、自动换行 `⌥W`、行号 `⌥L`、缩放 `⌘+`/`⌘-`/`⌘0` 完整动作对照表.
- Update Status Bar & Atomic Save Protection: 补充编码选择器 (`UTF-8`, `GBK`, `ISO-8859-1`)、临时文件原子替换 (`.tmp.atbcmder_*` + `os.replace`) 以及符号链接保护（写入目标实体保留链接本体）.

- [ ] **Step 2: Synchronize `docs/zh/network_and_vfs.md`**

- Add Section `### 6.3 App Store 沙盒云存储（OneDrive、Google Drive、iCloud）`: 详细说明 Security-Scoped Bookmarks 安全书签机制、盘符切换器 (`⌥D`) 自动发现与授权持久化.
- Section 10 SFTP Warning: 更新基于 `~/.ssh/known_hosts` 的严格主机指纹核验与中间人攻击告警拦截.

- [ ] **Step 3: Synchronize `docs/zh/preferences_and_customization.md`**

- Page table updates: General (Lucide 矢量图标与共享单例缓存), File Views (触控板横向滑动手势 `view.trackpad_swipe_navigation`), Quick Search (拼音快速搜索 `quick_search.pinyin_search` 与 Filter 模式 `quick_search.filter_only`).
- ASCII diagram update: File Views 添加触控板导航选项.
- Add Section `### 4.5 语义化 Lucide 矢量文件图标体系与单例共享缓存`: 200+ 专属矢量文件图标映射，全局单例缓存架构与 10 万+ 文件列表 60fps 流畅滚动.
- Add Section `### 4.6 MacBook 触控板横向滑动历史导航`: 双指左滑后退 (`⌘[` / `cm_ViewHistoryPrev`)，双指右滑前进 (`⌘]` / `cm_ViewHistoryNext`)，横向主导识别与惯性滤波.
- Add Section `### Pro Tip 5: 高性能拼音快速搜索与实时过滤模式`: 拼音任意字符边界匹配原理解析与 Filter 模式批处理特性 (`Cmd+A`, `F5`, `F6`, `Alt+F5`).

- [ ] **Step 4: Verify parity for `viewers_and_editors.md`, `network_and_vfs.md`, `preferences_and_customization.md` in `zh`**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py --target-lang zh`  
Expected: `viewers_and_editors.md` (30 headers), `network_and_vfs.md` (32 headers), `preferences_and_customization.md` (45 headers) show `[PASS]`.

- [ ] **Step 5: Commit Chinese viewers, network, and preferences**

```bash
git add docs/zh/viewers_and_editors.md docs/zh/network_and_vfs.md docs/zh/preferences_and_customization.md
git commit -m "docs(zh): synchronize viewers_and_editors, network_and_vfs, preferences_and_customization to v2.4.6"
```

---

### Task 4: Simplified Chinese Localization (`docs/zh/`) - Part 3: Shortcuts, FAQ, Getting Started & Index

**Files:**
- Modify: `docs/zh/keyboard_shortcuts.md`
- Modify: `docs/zh/faq_howtos.md`
- Modify: `docs/zh/getting_started.md`
- Modify: `docs/zh/index.md`

**Interfaces:**
- Consumes: `docs/en/keyboard_shortcuts.md`, `docs/en/faq_howtos.md`, `docs/en/getting_started.md`, `docs/en/index.md`
- Produces: 100% `[PASS]` on parity check for `docs/zh/` across all 13 chapters.

- [ ] **Step 1: Synchronize `docs/zh/keyboard_shortcuts.md`**

- Navigation section: 补充 `cm_ViewHistoryPrev / Next` 双指触控板手势快捷键行.
- Views & Filters: 补充 `cm_SrcAllFiles` (`⌘F10`)、`cm_SrcUserDef` (`⌘F11`).
- Tabs section: 补充 `cm_SetTabOptionLock`、`cm_SetTabOptionLockWithSubdirs`、`cm_SetTabOptionNormal`.
- Editor context table: 补充另存为 `⇧⌘S`、重新载入 `⌘R`、替换 `⌥⌘F`、自动换行 `⌥W`、行号 `⌥L`、缩放 `⌘+`/`⌘-`/`⌘0`.

- [ ] **Step 2: Synchronize `docs/zh/faq_howtos.md`**

- Matrix table: 更新目录空间计算快捷键为 `Alt+Shift+Return` / `⌥⇧⏎`.
- Add Section `### 2.6 操作秘笈 6：使用 Total Commander 风格标签页锁定保护工作区`: 详细讲解三种模式及 `*` 标识.
- Add Section `### 2.7 操作秘笈 7：使用自定义扩展名掩码过滤面板（Cmd+F11）`: 详细讲解掩码输入、保留子目录导航与 `Cmd+F10` 一键复位.
- Add Section `### 2.8 操作秘笈 8：启用 MacBook 双指触控板横向滑动历史导航`: 偏好设置开启步骤与免点击悬停面板导航.
- Add Section `#### Q7: 中文拼音快速搜索的工作原理是什么？`: 拼音任意字符边界匹配与 Filter 模式工作机制说明.

- [ ] **Step 3: Synchronize `docs/zh/getting_started.md` & `docs/zh/index.md`**

- `getting_started.md`:
  - Section 4 标签栏：补充邻近标签创建与 TC 标签锁定说明.
  - Section 5 双栏面板：补充 Lucide 图标体系、触控板手势导航、拼音快速搜索与掩码过滤.
  - Section 7 状态栏：补充沙盒云存储书签集成.
- `index.md`:
  - 核心架构导览条目 4、5、7 同步更新.
  - 第 2、3、4 章章节导读摘要同步更新.

- [ ] **Step 4: Run parity check on `zh`**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py --target-lang zh`  
Expected: All 13 chapters report `[PASS]` (0 errors).

- [ ] **Step 5: Commit Chinese shortcuts, FAQ, and introductory chapters**

```bash
git add docs/zh/keyboard_shortcuts.md docs/zh/faq_howtos.md docs/zh/getting_started.md docs/zh/index.md
git commit -m "docs(zh): complete Chinese synchronization for shortcuts, FAQ, getting_started, index"
```

---

### Task 5: Traditional Chinese (`docs/zh-hant/`) Generation & Taiwan HIG Terminology Alignment

**Files:**
- Modify: `docs/zh-hant/{navigation_and_tabs,file_operations,viewers_and_editors,network_and_vfs,preferences_and_customization,keyboard_shortcuts,faq_howtos,getting_started,index}.md`

**Interfaces:**
- Consumes: Updated `docs/zh/*.md`
- Produces: 100% `[PASS]` on parity check for `docs/zh-hant/` with Apple Taiwan HIG terminology (`分頁`, `預設`, `快速鍵`, `檔案管理器`, `資料夾`, `垃圾桶`).

- [ ] **Step 1: Check existing `zh-hant` parity errors**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py --target-lang zh-hant`  
Expected: Flags 5 files with header count mismatch.

- [ ] **Step 2: Generate Traditional Chinese files with OpenCC and enhanced Taiwan HIG terms**

Execute script using OpenCC `s2twp` and enhanced `MACOS_TERMS` + `TERMINOLOGY_REPLACEMENTS["zh-hant"]` to generate the 9 modified files from `docs/zh/`, ensuring `標籤頁` ➔ `分頁`, `默認` ➔ `預設`, `拖拽` ➔ `拖曳`, `快捷鍵` ➔ `快速鍵` and preserving localized ASCII diagrams.

- [ ] **Step 3: Run parity check and markdown list check on `zh-hant`**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py --target-lang zh-hant`  
Expected: All 13 chapters report `[PASS]` (0 errors).

- [ ] **Step 4: Commit Traditional Chinese documentation**

```bash
git add docs/zh-hant/
git commit -m "docs(zh-hant): synchronize all 9 chapters to v2.4.6 with Apple Taiwan HIG terms"
```

---

### Task 6: Incremental Diff Propagation for 8 Foreign Languages (`ja, de, fr, es, pt, ko, ru, it`)

**Files:**
- Modify: `docs/{ja,de,fr,es,pt,ko,ru,it}/{navigation_and_tabs,file_operations,viewers_and_editors,network_and_vfs,preferences_and_customization,keyboard_shortcuts,faq_howtos,getting_started,index}.md` (72 files)

**Interfaces:**
- Consumes: `docs/en/*.md`
- Produces: 100% header, code, and image parity across all 8 foreign languages without overwriting existing localized ASCII architecture diagrams.

- [ ] **Step 1: Verify failing parity in 8 foreign languages**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py`  
Expected: 40 parity errors (5 files × 8 languages).

- [ ] **Step 2: Execute incremental diff propagation script**

Run a dedicated incremental sync script (e.g. `scripts/sync_v246_diffs.py` or enhanced section-level translator) to:
1. Translate newly added H3/H4 sections from `docs/en/` into each of the 8 languages using `translate_snippet` (with macOS term replacement).
2. Splicing translated sections into the exact corresponding header locations in `docs/{ja,de,fr,es,pt,ko,ru,it}/`.
3. Updating modified tables (cheat sheets, shortcuts tables) with the new feature rows.
4. Updating the F4 code editor ASCII toolbar in `viewers_and_editors.md` to the vector icon format.
5. Strictly preserving all existing localized ASCII architecture diagrams in `index.md`, `getting_started.md`, `navigation_and_tabs.md`, `file_operations.md`, and `viewers_and_editors.md`.

- [ ] **Step 3: Run parity check across all languages**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py`  
Expected: `PARITY CHECK PASSED: 0 errors across 10 language(s)`.

- [ ] **Step 4: Commit 8 foreign languages synchronization**

```bash
git add docs/{ja,de,fr,es,pt,ko,ru,it}/
git commit -m "docs(i18n): incrementally propagate v2.4.6 feature documentation across 8 languages"
```

---

### Task 7: Global List Formatting, Full Parity Linter & Static Site Build Verification

**Files:**
- Check/Format: Entire `docs/` tree across all 11 languages

**Interfaces:**
- Produces: Clean markdown list formatting (MD032), 100% parity across all 11 languages, and successful static site compilation into `site/`.

- [ ] **Step 1: Auto-fix markdown list spacing across docs/**

Run: `conda run -n ATBCmderDoc python scripts/format_markdown_lists.py --fix`  
Expected: Output shows any formatted files or 0 changes needed.

- [ ] **Step 2: Verify zero MD032 list spacing errors**

Run: `conda run -n ATBCmderDoc python scripts/format_markdown_lists.py --check`  
Expected: PASS with 0 errors.

- [ ] **Step 3: Verify 100% parity across all 10 target languages**

Run: `conda run -n ATBCmderDoc python scripts/check_parity.py`  
Expected: 0 errors across all 10 languages (all chapters `[PASS]`).

- [ ] **Step 4: Execute multilingual static build**

Run: `./test.sh -b`  
Expected: Builds `en`, `zh`, `zh-hant`, `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it` documentation and landing pages successfully with `✓ Static site compiled successfully into site/!`.

- [ ] **Step 5: Final commit if formatting adjustments were made**

```bash
git add docs/
git commit -m "chore(docs): ensure MD032 list spacing compliance and build validation across all languages" || true
```
