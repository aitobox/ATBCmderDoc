# Default Keyboard Shortcuts Reference

ATBCmder is heavily keyboard-driven. Here is a comprehensive reference list of **ATBCmder Default Keyboard Shortcuts** based on the default configuration. You can assign up to two shortcuts (Primary and Secondary) for any command. To customize shortcuts and view the full list for each context, visit **Preferences → Hotkeys**. The editor will automatically warn you if you try to use a shortcut that is already assigned. The table is categorized by functionality:

## 1. File Operations

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_View` | View File (Lister) | `F3` | `Shift+F3` |
| `cm_Edit` | Edit File | `F4` | — |
| `cm_EditNew` | Create & Edit New Text File | `Shift+F4` | — |
| `cm_Copy` | Copy file to target panel | `F5` | — |
| `cm_CopySamePanel` | Copy file to same panel | `Shift+F5` | — |
| `cm_Move` / `cm_Rename` | Move / Rename file | `F6` | — |
| `cm_RenameOnly` | Inline Quick Rename | `F2` | `Shift+F6` |
| `cm_MkDir` | Create New Directory | `F7` | — |
| `cm_Delete` | Delete Selected File/Folder | `F8` | `Delete`, `Shift+Delete` |
| `cm_Wipe` | Securely Wipe/Delete | `Alt+Delete` | — |
| `cm_Open` | Open Selected File / Directory | `Cmd+Down` | `Enter` |
| `cm_PackFiles` | Pack/Compress Files | `Alt+F5` | — |
| `cm_ExtractFiles` | Extract Files | `Alt+F9` | — |
| `cm_SetFileProperties` | View / Edit File Properties | `Alt+Enter` | — |
| `cm_CountDirContent` | Calculate Directory Size | `Alt+Shift+Enter` | — |

## 2. Mark & Selection

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_MarkMarkAll` | Select All Items in Panel | `Ctrl+A` | `Ctrl+Num+`, `Cmd+A` |
| `cm_MarkUnmarkAll` | Deselect All Items in Panel | `Ctrl+Num-` | `Ctrl+Shift+A` |
| `cm_MarkInvert` | Invert Selection | `Num*` | — |
| `cm_MarkPlus` | Select by Wildcard (e.g. `*.py`) | `Num+` | — |
| `cm_MarkMinus` | Deselect by Wildcard (e.g. `*.bak`) | `Num-` | — |
| `cm_MarkCurrentExtension` | Select All Files with Same Extension | `Shift+Num+` | — |
| `cm_SelectOrDeselectFile` | Toggle Item Selection / Move Down | `Space` | `Insert` |
| `cm_ClearAll` | Clear All Marking States | `Ctrl+L` | — |
| `cm_CopyToClipboard` | Copy Selected to Clipboard | `Ctrl+C` | — |
| `cm_CutToClipboard` | Cut Selected to Clipboard | `Ctrl+X` | — |
| `cm_PasteFromClipboard` | Paste from Clipboard | `Ctrl+V` | — |

## 3. Panel Navigation

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_Refresh` | Refresh Current Panel | `Ctrl+R` | — |
| `cm_LeftOpenDrives` | Open Left Panel Drive Menu | `Alt+F1` | — |
| `cm_RightOpenDrives` | Open Right Panel Drive Menu | `Alt+F2` | — |
| `cm_Drives` | Show Drive Selection List | `Alt+D` | — |
| `cm_ChangeDirToParent` | Go to Parent Directory | `Ctrl+PgUp` | `Cmd+Up`, `Backspace` |
| `cm_ChangeDirToRoot` | Go to Root Directory | `Ctrl+\` | — |
| `cm_ChangeDirToHome` | Go to User Home Directory | `Ctrl+Shift+Home` | — |
| `cm_ViewHistoryPrev` | Directory History Back | `Alt+Left` | `Cmd+[` |
| `cm_ViewHistoryNext` | Directory History Forward | `Alt+Right` | `Cmd+]` |
| `cm_DirHistory` | Popup Directory History List | `Alt+F8` | `Ctrl+Down` |
| `cm_DirHotList` | Directory Hotlist Menu | `Ctrl+D` | — |
| `cm_ConfigDirHotList` | Configure Directory Hotlist | `Ctrl+Shift+D` | — |
| `cm_Exchange` | Swap Left & Right Panels | `Ctrl+U` | — |
| `cm_TargetEqualSource` | Set Target Panel to Source Path | `Ctrl+Left` | `Ctrl+Right`, `Alt+Z` |
| `cm_FocusSwap` / `cm_SwitchPanel` | Toggle Focus Between Panels | `Tab` | — |
| `cm_GoToHome` | Go to Home | `Alt+Home` | — |
| `cm_GoToFirst` | Go to First File | `Home` | — |
| `cm_GoToLast` | Go to Last File | `End` | — |

## 4. View & Sort

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_BriefView` | Brief View Mode | `Ctrl+F1` | — |
| `cm_ColumnsView` | Full/Columns View Mode | `Ctrl+F2` | — |
| `cm_ThumbnailsView` | Thumbnails View Mode | `Ctrl+Shift+F1` | — |
| `cm_FlatView` | Flat View | `Ctrl+B` | — |
| `cm_FlatViewSel` | Flat View of Selected Directories | `Ctrl+Shift+B` | — |
| `cm_TreeView` | Tree View | `Ctrl+Shift+F8` | — |
| `cm_QuickView` | Quick View Panel | `Ctrl+Q` | — |
| `cm_SortByName` | Sort by Name | `Ctrl+F3` | — |
| `cm_SortByExt` | Sort by Extension | `Ctrl+F4` | — |
| `cm_SortByDate` | Sort by Date | `Ctrl+F5` | — |
| `cm_SortBySize` | Sort by Size | `Ctrl+F6` | — |
| `cm_ShowHiddenFiles` | Toggle Hidden Files | `Ctrl+H` | — |
| `cm_ShowSysFiles` | Toggle System Files | `Ctrl+.` | `Shift+Cmd+.` |
| `cm_QuickSearch` | In-Panel Quick Search | `Ctrl+S` | — |
| `cm_SemanticFilter` | Semantic Smart Filter | `Ctrl+F` | — |

## 5. Tabs & Window

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_NewTab` | New Tab | `Cmd+T` | `Ctrl+T` |
| `cm_CloseTab` | Close Current Tab | `Cmd+W` | `Ctrl+W` |
| `cm_NextTab` | Switch to Next Tab | `Meta+Tab` (`Cmd+Tab`) | `Ctrl+Tab` |
| `cm_PrevTab` | Switch to Previous Tab | `Meta+Shift+Tab` (`Cmd+Shift+Tab`) | `Ctrl+Shift+Tab` |
| `cm_ShowTabsList` | Show Opened Tabs List | `Ctrl+Shift+L` | — |
| `cm_FullScreen` | Toggle Full Screen | `F11` | — |

## 6. Tools & Operations

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_Search` / `cm_FileSearch` | File Search Tool | `Alt+F7` | — |
| `cm_MultiRename` | Multi-Rename Tool | `Ctrl+M` | — |
| `cm_SyncDirs` | Compare & Sync Directories | `Shift+F12` | — |
| `cm_CompareFiles` / `cm_FileDiff` | Compare Files (Diff) | `Meta+Shift+F12` | — |
| `cm_Split` | Split File | `Alt+F6` | — |
| `cm_Combine` | Combine Files | `Alt+F7` | — |
| `cm_CalculateChecksum` | Calculate Checksum (MD5/SHA) | `Ctrl+X` | — |
| `cm_CopyFullNamesToClip` | Copy Full Paths to Clipboard | `Ctrl+Shift+C` | — |
| `cm_CopyNamesToClip` | Copy File Names to Clipboard | `Ctrl+Shift+X` | — |
| `cm_CalculateSpace` | Calculate Selected Dir Size | `Ctrl+L` | — |
| `cm_RunTerm` | Open Terminal in Current Dir | `Ctrl+J` | — |
| `cm_FocusCmdLine` | Focus Built-in Command Line | `Shift+F2` | — |
| `cm_ShowCmdLineHistory` | Show Command Line History | `Alt+F8` | `Ctrl+Down` |
| `cm_AddPathToCmdLine` | Append Path to Command Line | `Ctrl+P` | — |

## 7. System & Options

| Command ID | Description | Primary Shortcut | Secondary Shortcut |
| :--- | :--- | :---: | :---: |
| `cm_Options` | Open Preferences/Settings | `Cmd+,` | — |
| `cm_HelpContents` / `cm_HelpIndex` | Open Help Documentation | `F1` | — |
| `cm_Exit` | Exit Application | `F10` | `Alt+F4`, `Alt+X` |
