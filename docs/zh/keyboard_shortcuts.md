# 默认快捷键参考

ATBCmder 高度依赖键盘操作。这里是一份整理自项目默认配置文件的 **ATBCmder 默认快捷键完整参考列表**。您可以为任何命令绑定最多两个快捷键（主快捷键与副快捷键）。如需自定义快捷键或查看各场景的完整快捷键列表，请访问**偏好设置 → 快捷键**。如果您尝试使用已被占用的快捷键，编辑器会自动发出警告。表格已按功能进行分类整理：

## 1. 基础文件操作 (File Operations)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_View` | 查看文件 (Lister) | `F3` | `Shift+F3` |
| `cm_Edit` | 编辑文件 | `F4` | — |
| `cm_EditNew` | 新建并编辑文本文件 | `Shift+F4` | — |
| `cm_Copy` | 复制文件到目标面板 | `F5` | — |
| `cm_CopySamePanel` | 复制文件到同侧面板 | `Shift+F5` | — |
| `cm_Move` / `cm_Rename` | 移动 / 重命名文件 | `F6` | — |
| `cm_RenameOnly` | 行内快速重命名 | `F2` | `Shift+F6` |
| `cm_MkDir` | 创建新目录 | `F7` | — |
| `cm_Delete` | 删除所选文件/文件夹 | `F8` | `Delete`, `Shift+Delete` |
| `cm_Wipe` | 安全彻底粉碎删除 | `Alt+Delete` | — |
| `cm_Open` | 打开所选文件 / 目录 | `Cmd+Down` | `Enter` |
| `cm_PackFiles` | 打包压缩文件 | `Alt+F5` | — |
| `cm_ExtractFiles` | 解压文件 | `Alt+F9` | — |
| `cm_SetFileProperties` | 查看 / 修改文件属性 | `Alt+Enter` | — |
| `cm_CountDirContent` | 计算所选文件夹占用空间 | `Alt+Shift+Enter` | — |

## 2. 选择与标记 (Mark & Selection)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_MarkMarkAll` | 全选当前面板所有项 | `Ctrl+A` | `Ctrl+Num+`, `Cmd+A` |
| `cm_MarkUnmarkAll` | 取消全选当前面板所有项 | `Ctrl+Num-` | `Ctrl+Shift+A` |
| `cm_MarkInvert` | 反向选择 | `Num*` | — |
| `cm_MarkPlus` | 按通配符模式加选 (如 `*.py`) | `Num+` | — |
| `cm_MarkMinus` | 按通配符模式减选 (如 `*.bak`) | `Num-` | — |
| `cm_MarkCurrentExtension` | 选中同扩展名的所有文件 | `Shift+Num+` | — |
| `cm_SelectOrDeselectFile` | 切换单项选中状态 / 下移 | `Space` | `Insert` |
| `cm_ClearAll` | 清除所有标记状态 | `Ctrl+L` | — |
| `cm_CopyToClipboard` | 复制所选到剪贴板 | `Ctrl+C` | — |
| `cm_CutToClipboard` | 剪切所选到剪贴板 | `Ctrl+X` | — |
| `cm_PasteFromClipboard` | 从剪贴板粘贴 | `Ctrl+V` | — |

## 3. 面板与导航 (Panel Navigation)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_Refresh` | 刷新当前面板 | `Ctrl+R` | — |
| `cm_LeftOpenDrives` | 打开左侧面板磁盘选择菜单 | `Alt+F1` | — |
| `cm_RightOpenDrives` | 打开右侧面板磁盘选择菜单 | `Alt+F2` | — |
| `cm_Drives` | 显示磁盘选择列表 | `Alt+D` | — |
| `cm_ChangeDirToParent` | 返回上一级目录 | `Ctrl+PgUp` | `Cmd+Up`, `Backspace` |
| `cm_ChangeDirToRoot` | 返回根目录 | `Ctrl+\` | — |
| `cm_ChangeDirToHome` | 切换到用户 Home 目录 | `Ctrl+Shift+Home` | — |
| `cm_ViewHistoryPrev` | 目录历史后退 | `Alt+Left` | `Cmd+[` |
| `cm_ViewHistoryNext` | 目录历史前进 | `Alt+Right` | `Cmd+]` |
| `cm_DirHistory` | 弹出目录访问历史列表 | `Alt+F8` | `Ctrl+Down` |
| `cm_DirHotList` | 常用文件夹 (Hotlist) 菜单 | `Ctrl+D` | — |
| `cm_ConfigDirHotList` | 配置常用文件夹列表 | `Ctrl+Shift+D` | — |
| `cm_Exchange` | 左右面板互换位置 | `Ctrl+U` | — |
| `cm_TargetEqualSource` | 将目标面板设为源面板当前路径 | `Ctrl+Left` | `Ctrl+Right`, `Alt+Z` |
| `cm_FocusSwap` / `cm_SwitchPanel` | 在左右面板间切换焦点 | `Tab` | — |
| `cm_GoToHome` | 定位到 Home | `Alt+Home` | — |
| `cm_GoToFirst` | 定位到第一个文件 | `Home` | — |
| `cm_GoToLast` | 定位到最后一个文件 | `End` | — |

## 4. 视图与排序 (View & Sort)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_BriefView` | 简略视图模式 | `Ctrl+F1` | — |
| `cm_ColumnsView` | 详细列表视图模式 | `Ctrl+F2` | — |
| `cm_ThumbnailsView` | 缩略图视图模式 | `Ctrl+Shift+F1` | — |
| `cm_FlatView` | 展平视图 (Flat View) | `Ctrl+B` | — |
| `cm_FlatViewSel` | 对已选目录展平视图 | `Ctrl+Shift+B` | — |
| `cm_TreeView` | 目录树视图 | `Ctrl+Shift+F8` | — |
| `cm_QuickView` | 快速预览面板 (Quick View) | `Ctrl+Q` | — |
| `cm_SortByName` | 按文件名排序 | `Ctrl+F3` | — |
| `cm_SortByExt` | 按扩展名排序 | `Ctrl+F4` | — |
| `cm_SortByDate` | 按修改时间排序 | `Ctrl+F5` | — |
| `cm_SortBySize` | 按文件大小排序 | `Ctrl+F6` | — |
| `cm_ShowHiddenFiles` | 切换显示隐藏文件 | `Ctrl+H` | — |
| `cm_ShowSysFiles` | 切换显示系统文件 | `Ctrl+.` | `Shift+Cmd+.` |
| `cm_QuickSearch` | 面板内快速搜索 | `Ctrl+S` | — |
| `cm_SemanticFilter` | 智能语义过滤器 | `Ctrl+F` | — |

## 5. 标签页与窗口管理 (Tabs & Window)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_NewTab` | 新建标签页 | `Cmd+T` | `Ctrl+T` |
| `cm_CloseTab` | 关闭当前标签页 | `Cmd+W` | `Ctrl+W` |
| `cm_NextTab` | 切换到下一标签页 | `Meta+Tab` (`Cmd+Tab`) | `Ctrl+Tab` |
| `cm_PrevTab` | 切换到上一标签页 | `Meta+Shift+Tab` (`Cmd+Shift+Tab`) | `Ctrl+Shift+Tab` |
| `cm_ShowTabsList` | 显示所有已打开标签页列表 | `Ctrl+Shift+L` | — |
| `cm_FullScreen` | 切换全屏显示 | `F11` | — |

## 6. 工具与高级操作 (Tools & Operations)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_Search` / `cm_FileSearch` | 文件查找工具 | `Alt+F7` | — |
| `cm_MultiRename` | 批量重命名工具 | `Ctrl+M` | — |
| `cm_SyncDirs` | 目录比较与同步工具 | `Shift+F12` | — |
| `cm_CompareFiles` / `cm_FileDiff` | 文件内容对比 (Diff) | `Meta+Shift+F12` | — |
| `cm_Split` | 拆分文件 | `Alt+F6` | — |
| `cm_Combine` | 合并已拆分文件 | `Alt+F7` | — |
| `cm_CalculateChecksum` | 计算校验和 (MD5/SHA) | `Ctrl+X` | — |
| `cm_CopyFullNamesToClip` | 复制所选文件的完整路径到剪贴板 | `Ctrl+Shift+C` | — |
| `cm_CopyNamesToClip` | 复制所选文件名到剪贴板 | `Ctrl+Shift+X` | — |
| `cm_CalculateSpace` | 计算所选目录大小 | `Ctrl+L` | — |
| `cm_RunTerm` | 在当前目录启动终端 | `Ctrl+J` | — |
| `cm_FocusCmdLine` | 焦点跳转至内置命令行 | `Shift+F2` | — |
| `cm_ShowCmdLineHistory` | 显示命令行历史记录 | `Alt+F8` | `Ctrl+Down` |
| `cm_AddPathToCmdLine` | 追加当前文件路径至命令行 | `Ctrl+P` | — |

## 7. 系统与软件配置 (System & Options)

| 命令 ID | 功能描述 | 主快捷键 | 副快捷键 |
| :--- | :--- | :---: | :---: |
| `cm_Options` | 打开首选项 / 设置对话框 | `Cmd+,` | — |
| `cm_HelpContents` / `cm_HelpIndex` | 打开帮助文档 | `F1` | — |
| `cm_Exit` | 退出应用程序 | `F10` | `Alt+F4`, `Alt+X` |

## 8. 文件列表导航 (File Panel Navigation)

详细列表视图与缩略图视图支持以下快捷导航操作：

1. **Home 键（跳转到顶部第一行）**：
   - 原生 **Home** / **Fn + Left Arrow (`Fn + ←`)**
   - macOS **Cmd + Up Arrow (`⌘ + ↑`)** / **Cmd + Home (`⌘ + Home`)** / **Ctrl + Home**
   - 支持结合 **Shift** 键触发从当前行到首行的范围选择。
2. **End 键（跳转到底部最后一行）**：
   - 原生 **End** / **Fn + Right Arrow (`Fn + →`)**
   - macOS **Cmd + Down Arrow (`⌘ + ↓`)** / **Cmd + End (`⌘ + End`)** / **Ctrl + End**
   - 支持结合 **Shift** 键触发从当前行到末行的范围选择。
3. **PageUp / PageDown（向上 / 向下翻页）**：
   - 原生 **PageUp** / **Fn + Up Arrow (`Fn + ↑`)**
   - 原生 **PageDown** / **Fn + Down Arrow (`Fn + ↓`)**
   - 支持结合 **Shift** 键按页批量选择文件。
