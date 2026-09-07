# 第 8 章：快捷键速查掌中宝

ATBCmder 是一款为**纯键盘高效操作**而生的双面板文件管理器。无论是日常文件复制移动、跨目录跳转、视图切换，还是批量重命名与内容对比，完全无需触碰鼠标即可瞬间完成。

为了兼顾拥有数十年经验的老牌 Commander 用户习惯与苹果 macOS 触控原生人机工学，ATBCmder 独创了**双矩阵快捷键架构**：几乎每一项功能都同时绑定了**经典 Commander 功能键**（`F1`–`F12`、`Insert`、小键盘等）与 **macOS 原生组合修饰键**（`⌘` Command、`⌥` Option、`⇧` Shift、`⌃` Control）。

---

## 1. 双矩阵设计哲学与按键符号速查

无论你习惯了 Norton Commander / Total Commander 传承数十年的肌肉记忆，还是早已习惯原生 macOS Finder 的按键风格，ATBCmder 都能即开即用、完美契合，无需痛苦地重设键位。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          双矩阵快捷键引擎架构                               │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  经典 COMMANDER 体系 (PC/经典习惯)     │  macOS 原生体系 (Mac 标准人机工学) │
│  • 以功能键为核心 (F1–F12)            │  • 以修饰组合键为核心 (⌘, ⌥, ⇧, ⌃)  │
│  • 专用小键盘标记快捷键 (+, -, *)    │  • 与 Finder 深度一致 (⌘C, ⌘V, ⌘⌫, ⏎)│
│  • 盲操盲打、极速响应                │  • 深度集成原生菜单栏加速键          │
│  典型示例：                          │  典型示例：                          │
│    F5        ➔ 复制文件到对侧        │    ⌘C ➔ ⌘V   ➔ 复制文件              │
│    F6        ➔ 移动文件到对侧        │    ⌘C ➔ ⌥⌘V  ➔ 剪切移动文件          │
│    Shift+F4  ➔ 快速新建文本文件      │    ⇧⌘4       ➔ 快速新建文本文件      │
│    Alt+F7    ➔ 高级文件搜索          │    ⌥⌘F       ➔ 高级文件搜索          │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Apple 修饰键符号对照表

在本文档及 ATBCmder 的首选项配置窗口中，按键组合均采用 macOS 标准印刷体图标表示：

| 符号 | 修饰键名称 | PC / Windows 对应 | 说明 |
| :---: | :--- | :--- | :--- |
| **`⌘`** | **Command** (`Cmd`) | `Win` / `Ctrl` | macOS 最主要的操作主键 |
| **`⌥`** | **Option** (`Alt`) | `Alt` | 次级修饰键，用于备用动作、特殊字符或增强指令 |
| **`⇧`** | **Shift** | `Shift` | 扩展多选、反转动作或触发大写功能 |
| **`⌃`** | **Control** (`Ctrl`) | `Ctrl` | 终端控制键及经典 Commander 组合修饰键 |
| **`⎋`** | **Escape** (`Esc`) | `Esc` | 取消当前操作、清空筛选输入或关闭模态弹窗 |
| **`⏎`** | **Return** (`Enter`) | `Enter` | 执行动作、打开项目或确认对话框 |
| **`⌫`** | **Delete / 退格键** | `Backspace` | 向后删除字符，或在面板中返回上一级父目录 |
| **`⌦`** | **Forward Delete (前向删除)** | `Del` | 向前删除字符，或直接删除选中的文件项目 |
| **`⇥`** | **Tab (制表键)** | `Tab` | 在左右双面板之间循环切换键盘焦点 |
| **`⇞`** | **Page Up (上翻页)** | `PgUp` | 向上翻动一整屏文件列表 |
| **`⇟`** | **Page Down (下翻页)** | `PgDn` | 向下翻动一整屏文件列表 |

---

## 2. Mac 键盘 Fn 功能键使用指引

> [!IMPORTANT]
> ### 如何在苹果 Mac 键盘上顺畅使用 F1–F12 功能键
>
> 苹果 Mac 键盘（包括 MacBook 笔记本内置键盘、Magic Keyboard 外接键盘以及带 Touch Bar 的机型）在出厂默认状态下，顶部的物理 `F1`–`F12` 键会被系统优先分配给**硬件多媒体控制**（如调节屏幕亮度、调度中心、聚焦搜索、听写、播放暂停、音量控制等）。
>
> 鉴于经典 Commander 工作流重度依赖 `F1`–`F12`，建议根据自身习惯从以下两种方案中任选其一：
>
> #### 方案 A：配合物理 `Fn` 键同按（默认即开即用）
> 按住 Mac 键盘左下角的 **`Fn`** 键（或带地球仪图标 🌐 的按键），同时按下相应的功能键：
>
> * **`Fn + F3`**：全能查看器 Lister 快速只读预览
> * **`Fn + F4`**：内置编辑器编辑文本
> * **`Fn + F5`**：复制选中文件到对侧目标面板
> * **`Fn + F6`**：移动选中文件到对侧目标面板
> * **`Fn + F7`**：新建文件夹目录
> * **`Fn + F8`**：删除文件到废纸篓
> * **`Fn + Shift + F4`**：新建并立即编辑文本文件
> * **`Fn + Alt + F7`**：呼出高级文件搜索对话框
>
> #### 方案 B：在 macOS 系统中开启“标准功能键”（强烈推荐）
> 如果你将 ATBCmder 作为主力文件管理工具，建议在系统设置中将顶排按键切换为“标准功能键”。切换后直接单按 `F1`–`F12` 即可触发对应命令，需要调节音量亮度时再组合 `Fn` 键：
>
> 1. **macOS 13 Ventura、macOS 14 Sonoma、macOS 15 Sequoia**：
>    - 打开 ** 苹果菜单 ➔ 系统设置...**
>    - 在左侧侧边栏选择 **键盘**。
>    - 点击右侧的 **键盘快捷键...** 按钮。
>    - 在弹出对话框的左栏选择 **功能键**。
>    - 将 **“将 F1、F2 等键用作标准功能键”** 开关打开（ON）。
>    - 点击 **完成** 保存生效。
>
> 2. **macOS 12 Monterey 及更早系统**：
>    - 打开 ** 苹果菜单 ➔ 系统偏好设置... ➔ 键盘**。
>    - 在“键盘”标签页中，勾选 **“将 F1、F2 等键用作标准功能键”**。
>
> #### 配备 Touch Bar 的 MacBook Pro 机型
>
> * 按住左下角的物理 **`Fn`** 键，Touch Bar 会瞬间展开虚拟的 `F1`–`F12` 功能键栏。
> * 也可以前往 **系统设置 ➔ 键盘 ➔ 触控栏设置...**，将当前在前台运行 ATBCmder 时的显示模式设定为**“显示 F1、F2 等键”**。
>
> #### 没有独立 F 键的 60%/65% 紧凑型机械键盘
>
> * 无需使用别扭的层级按键切换，直接使用 ATBCmder 原生支持的 macOS 修饰组合键（如 `⌘C`、`⌥⌘V`、`⇧⌘N`、`⌘⌫`、`⌥⏎` 等），功能 100% 齐备对等。

---

## 3. 按键作用域分层架构

为了彻底避免全局热键与局部工具环境发生冲突（例如：在文件列表中搜索文件名，与在文本查看器中搜索段落文字），ATBCmder 将快捷键划分至明确的层级作用域中：

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          全局主作用域 (Main Scope)                          │
│  通用命令、双面板跳转、标签页切换、工具栏、系统级自动化工具                 │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  文件面板作用域 (FilePanel)   │  专用模态工具作用域 (Modal Tools)           │
│  在目录列表与缩略图浏览时生效  │  • Viewer      (全能查看器 Lister 窗口)    │
│  (文件多选、通配符标记、行内  │  • Editor      (内置代码/文本编辑器)        │
│  快速重命名、目录容量统计)    │  • Differ      (双栏文件差异对比窗口)       │
│                               │  • FindFiles   (多线程高级文件搜索对话框)   │
│                               │  • MultiRename (多重批量重命名工具)         │
└───────────────────────────────┴─────────────────────────────────────────────┘
```

当你在软件中按下任意按键时，**`HotkeyManager`** 核心按键引擎会按如下顺序智能分发：

1. 检测当前处于焦点状态的局部上下文（如 `Viewer` 或 `FilePanel`）。
2. 若该上下文中已绑定该快捷键，则立即触发专属命令。
3. 若局部上下文中未配置该按键，则优雅向上回退至全局 `Main` 作用域匹配。
4. 若全局作用域也未拦截，则直接交付给基础文本输入控件或系统底层默认处理。

---

## 4. 全分类双矩阵快捷键一览表

以下收录了 ATBCmder 全部常用操作命令与对应的双矩阵键位绑定，按工作场景详细归类。

### 4.1 基础文件操作

文件操作是双面板管理的核心。除特殊标明外，所有操作均严格遵循经典的**“源面板 ➔ 目标面板”**原则：在当前激活面板中选中的文件，将被处理到对侧闲置面板所打开的目标路径中。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_View` | 使用全能查看器 Lister 打开（只读预览） | `⌘3` / `Space` *(快速查看)* | `F3` / `Shift+F3` | Main |
| `cm_Edit` | 在内置文本/代码编辑器中打开 | `⌘4` | `F4` | Main |
| `cm_EditNew` | 新建空文件并立即在编辑器中打开 | `⇧⌘4` / `⇧F4` | `Shift+F4` | Main |
| `cm_Copy` | 复制选中项目至对侧目标面板 | `⌘C` *(至剪贴板)* / `F5` | `F5` | Main |
| `cm_CopySamePanel` | 在同目录下快速克隆/副本当前选中的文件 | `⇧F5` | `Shift+F5` | Main |
| `cm_Move` | 移动选中项目至对侧目标面板 | `⌥⌘V` *(粘贴移动)* / `F6` | `F6` | Main |
| `cm_RenameOnly` | 行内快速重命名光标所在的项目 | `⏎` *(Return)* / `F2` | `F2` / `Shift+F6` | Main |
| `cm_Rename` | 弹出对话框重命名选中项目 | `⇧F6` | `Shift+F6` | Main |
| `cm_MkDir` | 在当前面板中新建文件夹目录 | `⇧⌘N` / `F7` | `F7` | Main |
| `cm_Delete` | 将选中项目移动至 macOS 废纸篓 | `⌘⌫` *(Cmd+Delete)* / `⌦` | `F8` / `Delete` | Main |
| `cm_Wipe` | 永久粉碎/强制抹除文件（绕过废纸篓） | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | FilePanel |
| `cm_Open` | 调用系统默认程序打开，或进入所选目录 | `⌘↓` / `⏎` *(Return)* | `Enter` | Main |
| `cm_SetFileProperties` | 查看并编辑文件属性、时间戳与 UNIX 权限 | `⌥⏎` *(Option+Return)* / `⌘I` | `Alt+Enter` | Main |
| `cm_CountDirContent` | 统计光标所在文件夹的真实字节占用大小 | `⌥⇧⏎` *(Option+Shift+Return)* | `Alt+Shift+Enter` | FilePanel |
| `cm_CalculateSpace` | 统计所有选中文件夹的累计容量大小 | `⌃L` / `⌘L` | `Ctrl+L` | Main |
| `cm_SymLink` | 在对侧目标面板创建符号链接 (Symlink) | `⌥⌘S` | *(菜单: 文件 ➔ 创建符号链接)* | Main |
| `cm_HardLink` | 在对侧目标面板创建文件系统硬链接 (Hardlink) | `⌥⌘H` | *(菜单: 文件 ➔ 创建硬链接)* | Main |
| `cm_PackFiles` | 打包压缩选中项目 (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Main |
| `cm_ExtractFiles` | 将压缩包解压提取到对侧目标面板 | `⌥F9` / `⌥⌘E` | `Alt+F9` | Main |
| `cm_ArchiveView` | 以虚拟文件系统进入压缩包原地浏览 (`vfs://`) | `⌃⇟` *(Ctrl+PgDn)* / `⌘↓` | `Ctrl+PgDn` | Main |
| `cm_CompareContents` | 快速比对两个选中文件的内容差异 | `⇧F3` | `Shift+F3` | Main |

---

### 4.2 选择与标记

Commander 类软件的一大精髓是闪电般的多文件批量标记。你可以无需鼠标，通过通配符、同扩展名、反转或者键盘连续按键完成各种复杂选择。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_MarkMarkAll` | 全选当前面板内的所有文件与文件夹 | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Main |
| `cm_MarkUnmarkAll` | 取消全选（清空面板内所有已勾选项） | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Main |
| `cm_MarkInvert` | 反选（反转当前面板内各项目的勾选状态） | `⌘I` / `⌃I` | `Num*` *(小键盘 `*`)* | FilePanel |
| `cm_MarkPlus` | 按通配符规则批量选定（如 `*.ts;*.tsx`） | `⌘+` / `⌃+` | `Num+` *(小键盘 `+`)* | FilePanel |
| `cm_MarkMinus` | 按通配符规则反向剔除（如 `*.log`） | `⌘-` / `⌃-` | `Num-` *(小键盘 `-`)* | FilePanel |
| `cm_MarkCurrentExtension` | 自动选中与当前光标文件相同后缀的所有文件 | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Main |
| `cm_UnmarkCurrentExt` | 剔除与当前光标文件相同后缀的所有选中项 | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Main |
| `cm_MarkCurrentName` | 自动选中与当前光标同名（不计扩展名）的文件 | `⌥⌘N` | *(菜单: 选择 ➔ 同名文件)* | Main |
| `cm_SelectOrDeselectFile` | 切换选中状态并将光标向下移动一行 | `Space` | `Insert` / `Space` | FilePanel |
| `Shift+Up / Shift+Down` | 向上/向下展开或收缩连续区域选择 | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | FilePanel |
| `Shift+PageUp / Shift+PageDown` | 向上/向下快速扩展整整一屏的选区 | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | FilePanel |
| `cm_ClearAll` | 清空所有选区标记与快速搜索高亮 | `⌃L` | `Ctrl+L` | Main |
| `cm_CopyToClipboard` | 将选中文件复制到系统剪贴板 | `⌘C` | `Ctrl+C` | Main |
| `cm_CutToClipboard` | 将选中文件剪切到系统剪贴板 | `⌘X` | `Ctrl+X` | Main |
| `cm_PasteFromClipboard` | 将剪贴板中的文件粘贴到当前面板目录中 | `⌘V` | `Ctrl+V` | Main |
| `cm_PasteAsMove` | 将剪贴板中的文件以“移动”形式粘贴过来 | `⌥⌘V` | `Ctrl+Alt+V` | Main |
| `cm_CopyNamesToClip` | 仅复制选中文件的文件名到剪贴板 | `⇧⌘X` | `Ctrl+Shift+X` | Main |
| `cm_CopyFullNamesToClip` | 复制选中文件的绝对完整路径到剪贴板 | `⇧⌘C` | `Ctrl+Shift+C` | Main |
| `cm_CompareDirectories` | 对比左右面板，自动标记出单侧独有的文件 | `⌥⇧C` | *(菜单: 选择 ➔ 比较目录)* | Main |

---

### 4.3 面板导航与书签

在多层目录、本地驱动器、外接磁盘、网络挂载点与历史记录之间瞬间穿梭。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FocusSwap` / `cm_SwitchPanel` | 在左面板与右面板之间轮换键盘焦点 | `⇥` *(Tab)* | `Tab` | Main |
| `cm_Refresh` | 强制重新读取并刷新当前面板目录 | `⌘R` / `⌃R` | `Ctrl+R` | Main |
| `cm_ChangeDirToParent` | 跳转到上一级父目录 (`..`) | `⌘↑` / `⌫` *(退格键)* | `Backspace` / `Ctrl+PgUp` | Main |
| `cm_ChangeDirToRoot` | 瞬间直达磁盘根目录 (`/`) | `⌘\` | `Ctrl+\` | Main |
| `cm_ChangeDirToHome` | 瞬间直达用户个人主目录 (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | FilePanel |
| `cm_ViewHistoryPrev` | 沿浏览历史后退至上一个访问过的路径 | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Main |
| `cm_ViewHistoryNext` | 沿浏览历史前进至下一个访问过的路径 | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Main |
| `cm_DirHistory` | 弹出近期访问过的历史目录交互下拉菜单 | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Main |
| `cm_Drives` | 呼出已挂载卷宗与驱动器列表快速切换弹窗 | `⌥D` | `Alt+D` | Main |
| `cm_LeftOpenDrives` | 为**左面板**呼出驱动器/磁盘切换菜单 | `⌥F1` | `Alt+F1` | Main |
| `cm_RightOpenDrives` | 为**右面板**呼出驱动器/磁盘切换菜单 | `⌥F2` | `Alt+F2` | Main |
| `cm_Exchange` | 互换左右面板的当前目录、标签页与浏览状态 | `⌘U` | `Ctrl+U` | Main |
| `cm_TargetEqualSource` | 将对侧面板同步跳转到与当前面板完全一致的目录 | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Main |
| `cm_SyncSlaveDir` | 开启双面板协同镜像导航（同进同退） | `⌥S` | *(菜单: 命令 ➔ 联动导航)* | Main |
| `cm_DirHotList` | 打开常用目录书签 (Hotlist) 快捷列表 | `⌘D` | `Ctrl+D` | Main |
| `cm_ConfigDirHotList` | 打开常用目录书签的管理与编辑窗口 | `⇧⌘D` | `Ctrl+Shift+D` | Main |
| `cm_GoToFirst` | 将光标定位至面板内第一个文件条目 | `⌘↑` / `Fn+←` *(Home)* | `Home` | Main |
| `cm_GoToLast` | 将光标定位至面板内最后一个文件条目 | `⌘↓` / `Fn+→` *(End)* | `End` | Main |
| `PageUp / PageDown` | 向上/向下滚动整整一屏视图 | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | FilePanel |

---

### 4.4 视图模式与排序

在紧凑列表、详细信息列、高保真缩略图、多层级递归展平模式与双栏目录树之间无缝切换。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_BriefView` | 切换为简要列表模式（多列紧凑排列文件名） | `⌃F1` | `Ctrl+F1` | Main |
| `cm_ColumnsView` | 切换为详细列表模式（名称、大小、日期、权限等完整列） | `⌃F2` | `Ctrl+F2` | Main |
| `cm_ThumbnailsView` | 切换为缩略图网格模式（图片、音视频与 PDF 大图预览） | `⌃⇧F1` | `Ctrl+Shift+F1` | Main |
| `cm_FlatView` | 切换为扁平视图（平铺穿透显示所有子目录文件） | `⌘B` | `Ctrl+B` | Main |
| `cm_FlatViewSel` | 仅将选中的子目录在扁平视图中展开平铺 | `⇧⌘B` | `Ctrl+Shift+B` | Main |
| `cm_TreeView` | 目录树视图（将当前面板替换为多级目录树） | `⌃⇧F8` | `Ctrl+Shift+F8` | Main |
| `cm_TreeViewSplit` | 目录树视图（单侧面板内部分割：上/左为树，下/右为文件） | `cm_TreeViewSplit` | *(菜单: 显示 ➔ 目录树分割)* | Main |
| `cm_TreeViewBoth` | 目录树视图（左右两个面板同时显示目录树） | `cm_TreeViewBoth` | *(菜单: 显示 ➔ 双面板目录树)* | Main |
| `cm_QuickView` | 开启/关闭对侧快速预览（在闲置面板即时预览当前文件） | `⌘Q` / `⌃Q` | `Ctrl+Q` | Main |
| `cm_SortByName` | 按文件名排序（再次按下可在升序/降序间切换） | `⌃F3` | `Ctrl+F3` | Main |
| `cm_SortByExt` | 按扩展名后缀排序 | `⌃F4` | `Ctrl+F4` | Main |
| `cm_SortByDate` | 按修改日期与时间排序 | `⌃F5` | `Ctrl+F5` | Main |
| `cm_SortBySize` | 按文件体积大小排序 | `⌃F6` | `Ctrl+F6` | Main |
| `cm_SortByAttr` | 按 UNIX 属性与权限排序 | `cm_SortByAttr` | *(菜单: 排序 ➔ 文件属性)* | Main |
| `cm_ShowHiddenFiles` | 切换是否显示以点 `.` 开头的隐藏文件 | `⌘H` / `⇧⌘.` | `Ctrl+H` | Main |
| `cm_ShowSysFiles` | 切换是否显示 macOS 系统关键受保护文件 | `⇧⌘.` | `Ctrl+.` | Main |
| `cm_QuickSearch` | 呼出面板内快速搜索栏（直接键入字符过滤列表） | `⌥S` / `⌃S` *(或直接键盘打字)* | `Ctrl+S` / *(直接打字)* | Main |
| `cm_SemanticFilter` | 呼出自然语言语义智能过滤栏 | `⌘F` | `Ctrl+F` | Main |
| `cm_HorizontalFilePanels` | 切换水平上下堆叠显示双面板（默认左右并排） | `⇧⌘H` | `Ctrl+Shift+H` | Main |

---

### 4.5 标签页与窗口管理

支持在任意一侧面板开启无限数量的文件夹标签页，支持工作区保存与跨面板克隆。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_NewTab` | 在当前面板新建一个文件夹标签页 | `⌘T` | `Ctrl+T` | Main |
| `cm_CloseTab` | 关闭当前正在浏览的标签页 | `⌘W` | `Ctrl+W` | Main |
| `cm_NextTab` / `cm_NextTabCtrl` | 切换至右侧下一个标签页 | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Main |
| `cm_PrevTab` / `cm_PrevTabCtrl` | 切换至左侧上一个标签页 | `⌃⇧⇥` *(Ctrl+Shift+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Main |
| `cm_ShowTabsList` | 弹出当前面板已打开的全部标签页汇总菜单 | `⇧⌘L` | `Ctrl+Shift+L` | Main |
| `cm_CloseAllTabs` | 关闭当前面板的所有标签页（保留最后一张） | `⌥⌘W` | *(标签右键菜单: 关闭全部)* | Main |
| `cm_CloseOtherTabs` | 关闭当前面板除活动标签之外的其他全部标签页 | `⇧⌘W` | *(标签右键菜单: 关闭其他)* | Main |
| `cm_Duplicatetab` | 快速克隆副本当前标签页 | `⌘D` / `cm_Duplicatetab` | *(标签右键菜单: 复制标签)* | Main |
| `cm_MoveTabLeft` | 将当前活动标签向左移动一个位置 | `⌃⇧←` | *(标签右键菜单: 向左移动)* | Main |
| `cm_MoveTabRight` | 将当前活动标签向右移动一个位置 | `⌃⇧→` | *(标签右键菜单: 向右移动)* | Main |
| `cm_CopyTabToOtherPanel` | 将当前标签页直接复制克隆到对侧面板中 | `⌥⌘T` | *(标签右键菜单: 复制到对侧)* | Main |
| `cm_SaveTab` / `cm_SaveTabs` | 将当前的双面板标签页布局保存到配置文件 | `cm_SaveTab` | *(菜单: 标签 ➔ 保存标签)* | Main |
| `cm_LoadTab` / `cm_LoadTabs` | 从配置文件重新恢复加载已保存的标签页布局 | `cm_LoadTab` | *(菜单: 标签 ➔ 加载标签)* | Main |
| `cm_OptionsFavorites` | 打开“常用标签组 (Favorite Tabs)”多会话管理面板 | `cm_OptionsFavorites` | *(菜单: 标签 ➔ 常用标签组)* | Main |
| `cm_FullScreen` | 切换软件全屏模式 | `⌃⌘F` / `F11` | `F11` | Main |

---

### 4.6 效率工具与系统辅助

通过快捷键直接唤起多重批量重命名、差异对比、双向同步、文件粉碎与内置终端等工具。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FileSearch` / `cm_Search` | 呼出高级多维度文件搜索对话框 | `⌥F7` / `⌥⌘F` | `Alt+F7` | Main |
| `cm_FileDiff` / `cm_CompareFiles` | 启动双栏文件差异对比工具 (Diff) | `⌘⇧F12` | `Meta+Shift+F12` | Main |
| `cm_SyncDirs` | 启动文件夹双向同步工具 (Sync Dirs) | `⇧F12` | `Shift+F12` | Main |
| `cm_MultiRename` | 启动多重批量重命名工具（支持正则与动态占位符） | `⌘M` | `Ctrl+M` | Main |
| `cm_Split` | 将超大文件分割为指定大小的均匀数据切片 | `⌥F6` | `Alt+F6` | Main |
| `cm_Combine` | 将有序的切片文件合并复原为原始文件 | `⌥F7` | `Alt+F7` | Main |
| `cm_CalculateChecksum` | 计算文件的安全校验哈希值 (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Main |
| `cm_VerifyChecksum` | 读取校验文件 (`.md5`, `.sha256`) 批量核验文件完整性 | `cm_VerifyChecksum` | *(菜单: 文件 ➔ 验证校验值)* | Main |
| `cm_RunTerm` | 在当前面板目录路径下唤起 macOS 系统终端 | `⌃J` / `F9` | `Ctrl+J` / `F9` | Main |
| `cm_FocusCmdLine` | 将键盘焦点直接转移至底部嵌入式命令行输入框 | `⇧F2` | `Shift+F2` | Main |
| `cm_ShowCmdLineHistory` | 弹出近期在底部命令行中执行过的历史指令下拉菜单 | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Main |
| `cm_AddPathToCmdLine` | 将当前目录绝对路径追加填入到底部命令行中 | `⌘P` | `Ctrl+P` | Main |
| `cm_ShowCommandLine` | 显示/隐藏底部命令行与控制台输入栏 | `⌘O` | `Ctrl+O` | Main |
| `cm_DiskBenchmark` | 启动磁盘读写性能基准测速工具 | `cm_DiskBenchmark` | *(菜单: 命令 ➔ 磁盘测速)* | Main |
| `cm_VisSemanticCommand` | 激活自然语言语义命令与智能检索条 | `/` / `⇧⌘P` | `/` | Main |

---

### 4.7 系统偏好、配置与帮助

快速访问软件偏好设置、配置导入导出以及在线文档。

| 命令标识 (Command ID) | 功能描述 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| `cm_Options` | 打开偏好设置 / 选项配置中心 | `⌘,` | `Ctrl+,` | Main |
| `cm_HelpContents` / `cm_HelpIndex` | 打开交互式帮助文档与用户指南手册 | `⌘?` / `F1` | `F1` | Main |
| `cm_HelpKeyboard` | 弹出快捷键快速速查卡片 | `cm_HelpKeyboard` | *(菜单: 帮助 ➔ 快捷键)* | Main |
| `cm_Exit` | 完全退出关闭 ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Main |
| `cm_About` | 显示关于 ATBCmder 版本与版权信息 | `cm_About` | *(菜单: ATBCmder ➔ 关于)* | Main |
| `cm_OpenConfigDirectory` | 在面板中直接打开软件配置存储文件夹 | `cm_OpenConfigDirectory` | *(菜单: 配置 ➔ 打开配置目录)* | Main |
| `cm_ExportConfiguration` | 将软件所有个性化配置导出打包为可迁移 ZIP 文件 | `cm_ExportConfiguration` | *(菜单: 配置 ➔ 导出配置)* | Main |
| `cm_ImportConfiguration` | 从导出的 ZIP 配置包中导入恢复软件设置 | `cm_ImportConfiguration` | *(菜单: 配置 ➔ 导入配置)* | Main |
| `cm_CheckForUpdate` | 在线检查软件最新发布版本 | `cm_CheckForUpdate` | *(菜单: 帮助 ➔ 检查更新)* | Main |

---

## 5. 专属模态工具环境快捷键

当你打开全能查看器、内置代码编辑器、双栏差异比对或多重批量重命名等独立窗口时，ATBCmder 会自动切换为各工具特有的键位表。这些按键在该工具窗口内部直接生效，不占用全局 `cm_*` 命名空间。

### 5.1 全能查看器 (`Viewer` 作用域)

在浏览各种纯文本、源代码、二进制 Hex 数据、图片、音视频与 PDF 文档时生效：

| 操作 / 功能 | 详细说明 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 全选 | 选定查看器内的全部文本或数据内容 | `⌘A` | `Ctrl+A` | Viewer |
| 纯文本模式 | 强制以纯文本形式显示内容 | `1` | `1` | Viewer |
| 二进制模式 | 强制以原始二进制字符流显示 | `2` | `2` | Viewer |
| 十六进制模式 | 切换为 Hex 双列十六进制字节检查模式 | `3` | `3` | Viewer |
| 十进制模式 | 切换为十进制字节数据解析模式 | `4` | `4` | Viewer |
| 翻页图书模式 | 切换为分页自适应排版阅读模式 | `5` | `5` | Viewer |
| 图像模式 | 切换为高保真图片查看器引擎 | `6` | `6` | Viewer |
| 插件模式 | 切换为第三方扩展插件解析视图 | `7` | `7` | Viewer |
| PDF/文档模式 | 切换为 PDF 与办公文档专用阅读引擎 | `8` | `8` | Viewer |
| 代码高亮模式 | 切换为带语法高亮的代码着色模式 | `9` | `9` | Viewer |
| 图像居中 | 将图片精准居中在窗口正中间 | `C` | `C` | Viewer |
| 自适应窗口 | 缩放图片使其完整适应当前窗口长宽 | `F` | `F` | Viewer |
| 仅缩小超大图 | 图片小于窗口时保持 100%，超出时自适应缩小 | `L` | `L` | Viewer |
| 自动换行切换 | 开启或关闭长文本按窗口宽度自动折行 | `W` | `W` | Viewer |
| 显示光标插入符 | 在只读查看器中开启可见的文本光标 | `F6` | `F6` | Viewer |
| 查找文本 | 在当前打开的文件中搜索关键字 | `⌘F` / `F7` | `F7` | Viewer |
| 查找下一个 | 跳转到下一个搜索匹配命中项 | `⌘G` / `F3` | `F3` | Viewer |
| 查找上一个 | 跳转到上一个搜索匹配命中项 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Viewer |
| 放大视图 | 放大图片或 PDF 显示比例 | `⌘+` / `Num+` | `Num+` | Viewer |
| 缩小视图 | 缩小图片或 PDF 显示比例 | `⌘-` / `Num-` | `Num-` | Viewer |
| 全屏沉浸查看 | 切换查看器全屏沉浸显示 | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Viewer |
| 关闭查看器 | 退出关闭 Lister 查看器窗口 | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Viewer |

---

### 5.2 内置代码编辑器 (`Editor` 作用域)

在新建或编辑源文件、配置文件与文本文件时生效：

| 操作 / 功能 | 详细说明 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 保存文件 | 将已修改的内容安全写入磁盘 | `⌘S` / `F2` | `F2` | Editor |
| 查找内容 | 在编辑器中呼出文本搜索栏 | `⌘F` / `F7` | `F7` | Editor |
| 查找下一个 | 跳转到下一个搜索匹配项 | `⌘G` / `F3` | `F3` | Editor |
| 查找上一个 | 跳转到上一个搜索匹配项 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Editor |
| 剪切 | 剪切选中文本到系统剪贴板 | `⌘X` | `Ctrl+X` | Editor |
| 复制 | 复制选中文本到系统剪贴板 | `⌘C` | `Ctrl+C` | Editor |
| 粘贴 | 从系统剪贴板粘贴文本内容 | `⌘V` | `Ctrl+V` | Editor |
| 撤销 (Undo) | 撤销上一步编辑或输入操作 | `⌘Z` | `Ctrl+Z` | Editor |
| 重做 (Redo) | 重新执行刚刚被撤销的操作 | `⇧⌘Z` | `Ctrl+Shift+Z` | Editor |
| 全选 | 选中文档中的全部文本内容 | `⌘A` | `Ctrl+A` | Editor |
| 关闭编辑器 | 关闭当前编辑窗口（若有未保存修改会自动提示） | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Editor |

---

### 5.3 双栏文件差异比对 (`Differ` 作用域)

在可视化比对两个文件或代码版本的窗口中生效：

| 操作 / 功能 | 详细说明 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 查找文本 | 在差异分栏中搜索文本内容 | `⌘F` / `F7` | `F7` | Differ |
| 查找下一个 | 跳转到下一个文本匹配项 | `⌘G` / `F3` | `F3` | Differ |
| 查找上一个 | 跳转到上一个文本匹配项 | `⇧⌘G` / `⇧F3` | `Shift+F3` | Differ |
| 下一处差异 | 将光标定位并滚动至下一处不同代码块 | `⌥↓` *(Option+Down)* | `Alt+Down` | Differ |
| 上一处差异 | 将光标定位并滚动至上一处不同代码块 | `⌥↑` *(Option+Up)* | `Alt+Up` | Differ |
| 第一处差异 | 直达两个文件之间最初的第一处差异点 | `⌥Fn+←` *(Opt+Home)* | `Alt+Home` | Differ |
| 最后一处差异 | 直达两个文件之间最后的一处差异点 | `⌥Fn+→` *(Opt+End)* | `Alt+End` | Differ |
| 向左合并代码块 | 将右侧窗口中的差异块复制覆盖到左侧对应行 | `⌥←` *(Option+Left)* | `Alt+Left` | Differ |
| 向右合并代码块 | 将左侧窗口中的差异块复制覆盖到右侧对应行 | `⌥→` *(Option+Right)* | `Alt+Right` | Differ |
| 重新扫描刷新 | 重新自磁盘载入两个文件并重新计算差异 | `⌘R` | `Ctrl+R` | Differ |
| 关闭比对工具 | 退出关闭差异比对窗口 | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Differ |

---

### 5.4 高级文件搜索窗口 (`FindFiles` 作用域)

在后台多线程文件搜索对话框中生效：

| 操作 / 功能 | 详细说明 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 开始搜索 | 立即启动多线程磁盘扫描 | `⏎` *(Return)* / `F9` | `F9` | FindFiles |
| 取消 / 关闭 | 停止正在运行的搜索任务，或直接关闭对话框 | `⎋` *(Esc)* | `Esc` | FindFiles |
| 查看选中文件 | 在全能查看器中预览当前高亮的搜索结果条目 | `⌘3` / `F3` | `F3` | FindFiles |
| 编辑选中文件 | 在内置编辑器中打开当前高亮的搜索结果条目 | `⌘4` / `F4` | `F4` | FindFiles |
| 新建搜索 | 清空当前关键词并重置搜索表单 | `⌘N` | `Ctrl+N` | FindFiles |
| 重置全部过滤器 | 快速清除日期、体积与属性等全部附加限制条件 | `⇧⌘N` | `Ctrl+Shift+N` | FindFiles |
| 读取上次搜索条件 | 恢复上一次成功执行过的搜索参数配置 | `⌘L` | `Ctrl+L` | FindFiles |

---

### 5.5 多重批量重命名工具 (`MultiRename` 作用域)

在多文件批量重命名规则配置工作区中生效：

| 操作 / 功能 | 详细说明 | macOS 原生快捷键 | 经典 Commander 键位 | 生效上下文 |
| :--- | :--- | :---: | :---: | :---: |
| 重置规则 | 将命名模板与正则替换规则恢复至默认初值 | `⌘R` | `Ctrl+R` | MultiRename |
| 在编辑器中手动改名 | 将目标更名列表导出至外置文本编辑器进行批量手动微调 | `⌘I` | `Ctrl+I` | MultiRename |
| 导入外部名称文件 | 从外部纯文本文件中逐行读取新名称以替换当前文件 | `F3` | `F3` | MultiRename |

---

## 6. 进阶技巧与系统热键避让优化

### 6.1 解决 macOS 全局系统热键拦截冲突

部分 macOS 默认全局热键会在系统层拦截按键，导致应用程序无法正常捕获。若想释放 ATBCmder 的极致键盘潜能，建议按需微调以下 macOS 系统设置：

1. **聚焦搜索 (`⌘Space` 与快速搜索冲突)**：
   - 默认情况下 `⌘Space` 会唤起系统 Spotlight 搜索。如果你习惯用 `⌘Space` 选定文件或搜索面板条目，可前往 **系统设置 ➔ 键盘 ➔ 键盘快捷键... ➔ 聚焦 (Spotlight)**，将系统 Spotlight 快捷键微调为 `⌥Space`。
2. **调度中心 (`⌃↑`) 与应用程序窗口 (`⌃↓`)**：
   - macOS 默认占用 `⌃↑` 和 `⌃↓`。而在 ATBCmder 中，`⌃↓` 是打开目录访问历史菜单的经典键位。你可以在 **系统设置 ➔ 键盘 ➔ 键盘快捷键... ➔ 调度中心** 中更改系统热键。
3. **隐藏应用程序 (`⌘H`)**：
   - macOS 默认将 `⌘H` 绑定为隐藏当前前台应用窗口。ATBCmder 中使用 `⌘H` 或 `⇧⌘.` 快速切换显示隐藏的点文件 (`.`)。若希望更顺畅，可以直接使用完全符合 Finder 习惯的 `⇧⌘.`（`Cmd+Shift+点`）。
4. **窗口最小化 (`⌘M`)**：
   - macOS 默认使用 `⌘M` 最小化窗口到 Dock。ATBCmder 将其赋予了生产力极高的批量重命名工具 (`cm_MultiRename`)。在 ATBCmder 窗口激活时它会被优先捕获；你也可以随时使用备用的经典按键 `Ctrl+M` 或工具栏按钮唤起。

---

### 6.2 触控板手势与鼠标配合

对于使用 MacBook 笔记本触控板的用户，ATBCmder 深度融合了直觉式的多指触控手势：

* **双指捏合缩放缩略图**：在缩略图网格视图 (`cm_ThumbnailsView`) 中，在触控板上双指轻捏放大或缩小，缩略图即可在 `48 px` 到 `512 px` 之间无级平滑缩放。
* **双指左右轻扫前后导航**：在文件列表区域双指左右轻扫，可快速后退（`cm_ViewHistoryPrev`）与前进（`cm_ViewHistoryNext）访问过的目录路径。
* **双击中缝重置 50/50 分屏**：双击左右双面板中间的垂直分割线，即可瞬间将两栏面板恢复为精确对半平分。
* **标签页中键直接关闭**：对准任意文件夹标签页按鼠标中键（或在触控板上三指轻击），即可瞬间关闭该标签，省去按 `⌘W` 的步骤。

---

### 6.3 在首选项中自定义修改热键

以上列出的所有快捷键均可在软件设置中自由更改或补充：

1. 按下 **`⌘,`**（或点击菜单栏 **配置 ➔ 选项...**）打开偏好设置窗口。
2. 在左侧分类中选择 **快捷键 (Hotkeys)**。
3. 在顶部的 **作用域 (Context)** 下拉菜单中选择要修改的环境（如 `Main` 全局、`FilePanel` 面板、`Viewer` 查看器等）。
4. 在搜索框中输入功能名称或 `cm_*` 标识符快速定位。
5. 点击快捷键输入框，直接在物理键盘上按下你心仪的键位组合。内置的**按键冲突检测引擎**会实时判断是否有重叠，若有冲突将明确预警。
6. 点击 **应用** 按钮，修改立即生效，无需重启软件。

你自定义的按键数据将安全保存在 `~/.config/atbcmder/atbcmder_hotkeys.xml`（macOS 位于 `~/Library/Preferences/atbcmder/`）。日后使用 **`cm_ExportConfiguration`** 即可一键打包导出并迁移至新设备。

---

<div align="center">
  <p>想了解如何使用双向同步做日常备份？或是快速连接局域网 NAS？</p>
  <p><strong><a href="faq_howtos.md">前往第 9 章：实战指南与疑难解答 &rarr;</a></strong></p>
</div>
