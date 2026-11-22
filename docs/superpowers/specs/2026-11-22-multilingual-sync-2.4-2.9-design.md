# Design Spec: Multilingual Documentation Synchronization (v2.4.0 – v2.9.0 Updates)

**Date:** 2026-11-22  
**Status:** In Review  
**Target Scope:** Synchronize 10 updated chapters from `docs/en/` benchmark into Simplified Chinese (`docs/zh/`), Traditional Chinese (`docs/zh-hant/`), and 8 foreign languages (`docs/{ja,de,fr,es,pt,ko,ru,it}/`).  
**Selected Approach:** Approach 1 (Phased Delivery: High-Standard Idiomatic Simplified Chinese Localization ➔ OpenCC / Apple HIG Traditional Chinese Alignment ➔ Batch Diff Propagation for 8 Foreign Languages ➔ End-to-End Parity & Zensical Build Validation).

---

## 1. Executive Summary & Intent

Between v2.4.0 and v2.9.0, ATBCmder introduced major features and UX enhancements:
- Direct inline path editing button (`btn_edit_path` / `⌘⇧G` / `cm_EditPath`) with smart normalization and direct file jumping.
- Instant tab lock toggling (`⌘K` / `cm_ToggleLockTab`) and dynamic context menu shortcut synchronization.
- Menu bar tray residency (`ui.minimize_to_tray`) paired with permission-free macOS Carbon global hotkey (`⌘⌥H` / `ui.global_hotkey`).
- Customizable panel column visibility/drag-reordering (`view.panel_column_order`, `view.panel_column_visible`) and macOS Finder color tags column (`view.show_color_tags`).
- New "Recent Changes" diagnostic tool (`cm_RecentChanges`) with Spotlight pre-seeding and minimum size filtering.
- Dual-mode App Sandbox system status inspection (current-user process ranking, Running Applications tab, sandbox-safe process context menu).
- Enhanced System Cleaner with per-application tree grouping, accurate kept-size metrics, and localized retention reasons.
- Collision-safe clipboard auto-rename, `Shift+Click` range deselection, search autofocus, sandboxed terminal handoff, and remote VFS column sorting / on-demand credential caching.
- 32-step interactive onboarding tutorial (`cm_Tutorial`).

These enhancements have been integrated into 10 English documentation chapters in `docs/en/` without version badges. The goal of this project is to propagate these updates into all other language versions in `docs/`, prioritizing high-craft, idiomatic Chinese technical writing that avoids stiff, mechanical translation.

---

## 2. Goals, Non-Goals & Anti-Goals

### Goals
- **Phase 1: High-Craft Simplified Chinese (`docs/zh/`) Localization**:
  - Manually translate and synchronize the 10 modified chapters into natural, vivid, accurate Chinese adhering to Apple macOS HIG terminology (访达, 废纸篓, 快捷键, 隔空投送, 标签页, 菜单栏, 状态栏) and classic Commander conventions.
  - Avoid literal or robotic translation (e.g. avoid translating "Enter Full Path and Go" literally; use "输入完整路径并跳转"; avoid translating "collision-safe paste auto-rename" awkwardly; use "同名冲突自动重命名").
  - Preserve all ASCII UI diagrams, table layouts, Markdown formatting, and `<kbd>` tags.
- **Phase 1: Traditional Chinese (`docs/zh-hant/`) Alignment**:
  - Transform `docs/zh/` updates to `docs/zh-hant/` using OpenCC `s2twp` with Apple Taiwan/HK localization terms (分頁, 偏好設定, 垃圾桶, 快速鍵, 檔案, 剪貼簿).
- **Phase 2: 8 International Languages (`ja, de, fr, es, pt, ko, ru, it`) Synchronization**:
  - Propagate section-level diffs, new recipes, and shortcut rows to all 8 foreign languages using targeted diff propagation (`scripts/propagate_diff_i18n.py`) while preserving existing localized diagrams and `mentor_style_guide.py` terminology.
- **Validation**:
  - Pass `python3 scripts/check_parity.py` with 0 errors across all 10 target languages (resolving all 40 current parity failures).
  - Pass markdown list blank spacing checks (`./test.sh -l` / `python3 scripts/format_markdown_lists.py --check`).
  - Pass static site compilation across all languages (`./test.sh -b`).

### Non-Goals
- Modifying `download.md` or `privacy_policy.md` (which were untouched in `docs/en/`).
- Adding or altering image assets in `docs/images/`.
- Changing web landing page assets (`landing/`).
- Introducing version badge callouts (`> [!NOTE] Available since v2.9.0` or `(since v2.8.0)`).

### Anti-Goals
- Never alter Commander Command IDs (`cm_*`), configuration keys (e.g., `view.panel_column_order`), or keyboard symbols (`⌘`, `⌥`, `⇧`, `⌃`).
- Never allow mechanical/untranslated English placeholders in `docs/zh/` or `docs/zh-hant/`.
- Never break table column alignments or Markdown list blank spacing (MD032).

---

## 3. Approaches Considered

### Approach 1: Phased Delivery (Selected)
- **Phase 1**: Dedicated hand-crafted translation of the 10 chapters in `docs/zh/`, ensuring high readability and technical accuracy, followed by OpenCC `s2twp` conversion for `docs/zh-hant/`.
- **Phase 2**: Automated diff propagation script for the 8 foreign languages (`ja, de, fr, es, pt, ko, ru, it`) with protected placeholders, followed by list formatting and parity verification.
- **Why Selected**: Respects the user's explicit preference for vivid, non-literal translation in Chinese first, while keeping the full multilingual repository 100% compliant with CI parity checks.

### Approach 2: Monolithic Machine Translation for All Languages Simultaneously
- Run full automated translation scripts across all languages directly from English.
- **Why Rejected**: Machine translation produces robotic, literal Chinese phrasing (e.g. "回车完整路径并去", "碰撞安全粘贴自动重命名"), violating the user's explicit requirement ("要求翻译简洁生动准确，避免生翻硬翻").

### Approach 3: Chinese-Only Synchronization
- Only update `docs/zh/` and `docs/zh-hant/`, ignoring foreign languages.
- **Why Rejected**: Leaves 40 parity errors failing across `ja`, `de`, `fr`, `es`, `pt`, `ko`, `ru`, `it`, breaking repository test checks and CI builds.

---

## 4. Detailed Chapter-by-Chapter Technical Specifications

### 4.1 `navigation_and_tabs.md`
- **Section 1 (Cheat Sheet) & Section 11 (Master Table)**:
  - Add `输入完整路径并跳转` (`Cmd+Shift+G` / `⌘⇧G` | `Ctrl+Shift+G` | `cm_EditPath`).
  - Add `锁定 / 解锁当前标签页` (`Cmd+K` / `⌘K` | `Ctrl+K` | `cm_ToggleLockTab`).
  - Update `cm_ConfigDirHotList` to `Option+Cmd+D` / `⌥⌘D` | `Ctrl+Alt+D`.
  - Update `cm_SaveFavoriteTabs` to `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D`.
- **Section 2 (Breadcrumbs & Direct Path Editing)**:
  - Update Section 2.4 to "输入完整路径并跳转 (`BreadcrumbLineEdit` / `cm_EditPath`)":
    - 3 entry points: 点击路径栏左侧铅笔图标按钮 (`btn_edit_path`)、双击面包屑右侧空白区域、按下快捷键 `Cmd+Shift+G`（或菜单栏“命令 ➔ 输入完整路径并跳转”）。
    - 自动预填并全选当前路径，支持 `⌘V` 瞬间覆写。
    - 智能路径规范化：自动剥离首尾空格与包裹引号（`"..."` 或 `'...'`），自动展开家目录波浪号 `~`、`$VAR` 及 `%VAR%` 环境变量，支持相对路径解析，保持 `vfs://` 归档路径原样。
    - 直接定位文件：若输入的路径指向具体文件，自动跳转至其父目录并在面板中高亮聚焦该文件。
    - 红框错误保持：路径不存在或加载失败时，输入框保持展开并呈现红色警示边框，状态栏提示错误原因，按 `Esc` 或再次点击铅笔按钮取消。
- **Section 3 (Folder Tabs) & Section 4/5 (Favorites/Hotlists)**:
  - 标签锁定快捷键：`Cmd+K`（`⌘K` / `Ctrl+K` / `cm_ToggleLockTab`）在未锁定与“锁定此标签页”之间快速切换。
  - 右键菜单动态同步：macOS 标签右键菜单与“标签页”顶栏菜单均显示右对齐快捷键（`⌘T`、`⌘W`、`⌘K` 等），动态指示当前操作。
- **Section 6 (Trackpad Swipe Navigation)**:
  - 增强描述：全面支持 MacBook 内置触控板与 Apple 妙控板 (Magic Trackpad) 的双指左右滑动手势。
- **Section 7.1 (Full Columns View)**:
  - 自定义列显示与排序：在“偏好设置 ➔ 文件视图 ➔ 列设置”中勾选/隐藏扩展名、大小、修改时间、权限及所有者，拖拽 `⠿` 手柄调整显示顺序（`名称` 列始终固定在最前）。
  - macOS 访达颜色标签列：开启“在文件面板中显示 macOS 访达颜色标签”，呈现 7 种原生标签圆点（红、橙、黄、绿、蓝、紫、灰）与本地化浮动提示，并支持自定义标签。

### 4.2 `preferences_and_customization.md`
- **Section 3.5 (System Tray & Carbon Global Hotkey)**:
  - 菜单栏托盘驻留：勾选“最小化到系统托盘（需要重启）”（`ui.minimize_to_tray`），重启后常驻 macOS 顶部菜单栏，彻底告别 Dock 栏堆积。
  - Carbon 免权限全局快捷键：设置“显示/隐藏窗口快捷键”（`ui.global_hotkey`，默认 `Ctrl+Alt+H` / `⌘⌥H`），立即生效且带“重置”按钮。
  - 底层原生实现：采用 macOS Carbon `RegisterEventHotKey` API，**无需在 macOS 系统设置中授予辅助功能 (Accessibility) 权限**即可全局呼出；配备 Option 键虚键规范化 (`_MacAwareKeySequenceEdit`)，杜绝变音符号冲突。
- **Section 4 (File Views, Columns & Tags)**:
  - ASCII 示意图加入 `[ 列设置 ]` 与 `[ 颜色标签 (macOS) ]`。
  - 新增 4.7 节“自定义列可见性与排序 (`view.panel_column_order`, `view.panel_column_visible`)”。
  - 新增 4.8 节“macOS 访达颜色标签 (`view.show_color_tags`, `view.color_tag_sync_interval_ms`)”，支持 0~300 秒刷新间隔调整。
- **Section 11 (Master Reference Table)**:
  - 同步更新快捷键表中的托盘全局快捷键、常用标签组与书签热键。

### 4.3 `system_tools.md`
- **Chapter Overview & Section 1**:
  - 工具数量由 4 款更新为 **5 款核心系统维护与诊断工具**（加入“最近修改文件与文件夹”）。
  - ASCII 架构图与快速矩阵加入 `[4] 最近修改文件与文件夹 (cm_RecentChanges)`。
  - 移除 `Disk Usage Analyzer` 过时的 `⌘⇧D` 绑定，标明为菜单入口 `Tools ➔ Disk Usage Analyzer...`。
- **Section 2 & 3 (StatusPopup & SystemStatusPanel)**:
  - App Sandbox 双模式：在 Mac App Store 沙盒环境下，借助 Darwin 底层进程 API (`sysctl KERN_PROC_UID` + `proc_pidinfo`) 统计当前用户进程与内存，显示“当前用户进程（App 沙盒）”。
  - 底部双分页：默认展示“Top 进程”，第二分页展示“正在运行的应用程序”（缓存主线程应用图标，自动过滤后台小组件与 XPC 干扰）。
  - 沙盒合规右键操作：提供“退出”、“强制退出”、“前置窗口”、“在访达中显示”以及“在活动监视器中查看…”。
- **新增 Section 5: 最近修改文件与文件夹 (`cm_RecentChanges`)**:
  - 菜单入口：`工具 ➔ 查看最近修改的文件/文件夹...`。
  - 核心功能：路径选择、类型过滤（文件、文件夹）、时间预设（过去 1 小时、过去 1 天、过去 1 周、自定义时间范围）、最小体积过滤（忽略小于 1 KB、1 MB、10 MB 或自定义大小）。
  - 引擎与结果：预先集成 macOS 聚焦 (Spotlight) 候选加速检索，支持文件夹体积动态计算（`≥` 标识部分下限），提供实时过滤输入框。
  - 操作动作：双击或“在访达中显示”、“在 ATBCmder 面板中打开”、“移到废纸篓”。
- **Section 6 (重写为原 5 节的系统清理工具)**:
  - 按应用程序树状视图：支持在“按类别分组”与“按应用程序分组”之间自由切换。
  - 真实保留体积度量：受保护或不可清理项展示实际度量体积（或 `≥` 标识），混合组在“大小”列仅显示可清理字节（与“可回收总计”严密匹配），状态栏显示 `+<体积> 已保留`。
  - 精准本地化保留原因：列举 10 大保留原因（如“应用程序正在运行”、“包含数据库”、“被进程占用”、“包含符号链接”、“权限不足”等）。
  - 快速定位按钮：“在访达中显示”与“在 ATBCmder 面板中打开”。
- **Section 9 (主命令表)**:
  - 重新顺畅编号（1~9 节），全面收录 Recent Changes 与 System Cleaner 的新动作。

### 4.4 `file_operations.md`
- **Section 2.1 (剪贴板复制粘贴)**:
  - 新增“同名冲突自动重命名”说明：使用 `cm_PasteFromClipboard` 粘贴遇到目标路径存在同名文件时，自动追加递增数字后缀（如 `report (1).pdf`），绝不静默覆盖。
- **Section 4.3 (连续范围选择)**:
  - 新增 `Shift+Click` 反选机制说明：在已选中项目上按住 `Shift` 单击，可精准反向取消该连续区间的选择，而不影响区间之外的其余已选项目。

### 4.5 `power_tools.md`
- **Section 5.1 (高级搜索对话框)**:
  - 唤出搜索（`Cmd+F` / `Alt+F7`）时光标自动聚焦并全选“文件名模式”输入框，支持零点击即时键入；同时增加按键防抖，防止误按 `Enter` 意外取消搜索。
- **Section 7.5 (内嵌终端交接)**:
  - 沙盒构建终端接力：在 Mac App Store 沙盒版本中从底部命令行执行命令时，自动在解析后的工作目录下启动外部终端，将完整命令行复制到系统剪贴板，并提示用户按下 `⌘V` 和回车即可干净执行。

### 4.6 `network_and_vfs.md`
- **Section 2.2 (网络 VFS 排序与表头同步)**:
  - 远程网络面板支持点击表头或快捷键（`⌃F3`–`⌃F6`）对名称、扩展名、大小、修改时间进行排序，目录始终置顶，表头箭头与“排序”菜单严格双向同步。
- **Section 7 & 8 (按需网络凭据认证与会话缓存)**:
  - 弹出 `NetworkPasswordDialog` 支持密码明暗切换与“记住密码（存入系统钥匙串）”复选框；若未勾选保存，凭据自动保存在当前会话内存缓存 (`VFSSessionCache`) 中，在连接管理器中修改配置后仍无需重复输入密码。

### 4.7 `keyboard_shortcuts.md`
- **4.3 节 面板导航与书签**: 补全 `cm_EditPath` (`⇧⌘G` / `Ctrl+Shift+G`)；更新 `cm_ConfigDirHotList` 为 `⌥⌘D` / `Ctrl+Alt+D`。
- **4.5 节 标签页与窗口管理**: 补全 `cm_ToggleLockTab` (`⌘K` / `Ctrl+K`)；补全 `cm_SaveFavoriteTabs` (`⇧⌘D` / `Ctrl+Shift+D`)。
- **4.6 节 高级工具**: 将 `cm_CalculateChecksum` 快捷键修正为单一 `⌃X`，剥离 `⌘K`。
- **4.7 节 集成系统工具**: `cm_DiskUsageAnalyzer` 修正为菜单项；新增 `cm_RecentChanges`。
- **4.8 节 系统设置与帮助**: 补全 `cm_Tutorial`（32 步交互式新手引导）与全局托盘快捷键 `⌘⌥H`。

### 4.8 `faq_howtos.md`
- **2.6 节 (Recipe 6: 标签页锁定)**: 补充 `Cmd+K` 单键快速锁定/解锁与右键菜单快捷键同步。
- **新增 2.9 节 (Recipe 9: 路径快速编辑与文件直达)**: 详解 `⌘⇧G` 快速跳转、带引号/环境变量路径智能剥离、直接定位高亮文件、错误红框保持。
- **新增 2.10 节 (Recipe 10: 菜单栏托盘常驻与全局快捷键)**: 详解 `ui.minimize_to_tray` 与免辅助功能权限的 Carbon 全局热键 `⌘⌥H`。
- **新增 2.11 节 (Recipe 11: 自定义文件面板列与 macOS 访达颜色标签)**: 详解列排序/勾选与 7 色访达标签的使用。

### 4.9 `getting_started.md` & `index.md`
- **getting_started.md**:
  - 界面地标 `[3]` 路径面包屑栏补充铅笔编辑按钮；`[4]` 标签栏补充 `Cmd+K` 锁定；`[5]` 面板补充自定义列与颜色标签。
  - 新增进阶技巧 5：32 步交互式新手引导教程 (`cm_Tutorial`)。
  - 新增进阶技巧 6：后台托盘常驻与免权限全局热键 (`⌘⌥H`)。
  - 核心快捷键表格补充 `cm_EditPath` 与 `cm_ToggleLockTab`。
- **index.md**:
  - 地标速查对应同步铅笔按钮、`Cmd+K` 与自定义列/标签。
  - Track A 新手路线推荐体验交互式教程。
  - 主目录 (Master TOC) 第 2、7、8 章导读摘要同步更新。

---

## 5. Terminology & Copywriting Quality Standards

| 英文原词 | 简体中文 (`zh`) 推荐用语 | 繁体中文 (`zh-hant`) 推荐用语 | 禁忌生硬翻法 (Anti-Patterns) |
| :--- | :--- | :--- | :--- |
| Enter Full Path and Go | 输入完整路径并跳转 | 輸入完整路徑並前往 | 回车完整路径并去、进入全路径并走 |
| Breadcrumb Bar | 路径面包屑栏 | 路徑麵包屑列 | 面包屑条、面包屑条栏 |
| Lock this tab | 锁定此标签页 | 鎖定此分頁 | 锁住这个标签、锁定本卡片 |
| Minimize to system tray | 最小化到系统托盘 | 最小化至系統匣 / 系統選單列 | 最小化到托盘系统 |
| Global hotkey | 全局快捷键 | 全域快速鍵 | 外部热键、全局热键 |
| Accessibility permissions | 辅助功能权限 | 輔助使用權限 | 可访问性权限、无障碍权限 |
| Finder color tags | 访达颜色标签 | Finder 顏色標籤 | 查找器颜色标签、Finder 色标 |
| Recent Changes | 最近修改文件/文件夹 | 最近修改檔案/資料夾 | 近期变化、近期改动 |
| System Cleaner | 系统清理工具 | 系統清理工具 | 电脑清道夫 |
| Group by application | 按应用程序分组 | 依應用程式分組 | 按应用成组 |
| Reclaimable | 可回收 | 可回收 / 可釋放 | 可重新获得 |
| Interactive Tutorial | 交互式新手教程 | 互動式新手教學 | 交互指导书 |
| Collision-safe paste auto-rename | 同名冲突自动重命名 | 檔名衝突自動重新命名 | 碰撞安全粘贴自动重命名 |

---

## 6. Verification Criteria & Test Plan

1. **Structural Parity Check**:
   - 运行 `python3 scripts/check_parity.py`，全库 10 个语言目录针对 `docs/en` 基准校验，错误数必须归零（0 errors across 10 languages）。
2. **Markdown List Spacing (MD032)**:
   - 运行 `./test.sh -l` 或 `python3 scripts/format_markdown_lists.py --check`，全库检查通过，无列表紧凑粘连问题。
3. **Static Build Verification**:
   - 运行 `./test.sh -b`，完成所有语言站点静态编译，无 Markdown 解析死链或模板渲染警告。
4. **Copywriting Inspection**:
   - 检查 `docs/zh/`，确保语句通顺、语法准确、语气沉稳精炼、术语百分百符合 macOS 与 Commander 习惯。

---

## 7. What's Left to the Builder

- 确认是否需要在实施前先将 `docs/en/` 的未提交修改生成独立的 Git commit。
- 具体的批量同步脚本执行微调与文件保存顺序。
