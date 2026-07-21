# Navigation Guide

Welcome to the ATBCmder Navigation Guide. This guide covers the primary ways to navigate the file system and manage your view.

## Tree View
The Tree View provides a hierarchical look at your file system, including virtual file systems (VFS) like archives. 
It supports three layout modes, accessible from the **Show** menu:

- **Tree View (Replace)**: Replaces the file list with the tree view.

- **Tree View (Split)**: Shows both the tree view and the file list side-by-side in the current panel.

- **Tree View (Both Panels)**: Enables the split view in both the left and right panels.

Right-click the tree view to toggle the **Show Files** option if you want to see files alongside directories in the tree.

## Folder Tabs & Favorites (Directory Hotlist)
### Folder Tabs
You can open multiple folders in tabs within both the left and right panels.
Right-click the tab bar to access options like New Tab, Close Tab, and tab navigation. 

### Favorite Tabs
You can save your entire dual-panel tab layout (left and right tabs) as a named "Favorite Tab" set. 

- **Save/Load**: Right-click the tab bar and select **Save current tabs to a New Favorite Tabs** or load an existing set.

- **Management**: Go to **Preferences → Favorite Tabs** to rename, delete, or reorder your saved sets.

### Directory Hotlist (Bookmarks)
The Directory Hotlist acts as your bookmarks for frequently used folders.

- **Access**: Use the hotlist popup menu to quickly jump to a bookmarked folder. The popup includes a search box for real-time filtering by name or path.

- **Management**: Manage your bookmarks in **Preferences → Directory Hotlist**, where you can add, delete, edit, and reorder your hotlist entries.

## Quick Search
Quick Search allows you to jump directly to a file by typing its name.

- **Trigger**: Depending on your settings (**Preferences → Quick Search**), typing a letter or using a shortcut (like `Option+Letter` or `Cmd+Option+Letter`) will open the Quick Search overlay.

- **Navigation**: Use the `Up` and `Down` arrows to jump between matching files. Press `Enter` to open the file or folder.

- **Matching Rules**: You can configure it to match the beginning of the filename, or anywhere in the name. Type a trailing dot (`.`) to specifically match the end of a filename (excluding the extension).

## Essential Keyboard Shortcuts (Hotkeys)

ATBCmder is heavily keyboard-driven. Below is a categorized reference of the most frequently used default keyboard shortcuts and their corresponding command IDs from the application configuration:

### 📁 File & Directory Operations

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`F5`** | `cm_Copy` | Copy selected files/folders to the target panel |
| **`F6`** | `cm_Move` | Move selected files/folders to the target panel |
| **`F7`** | `cm_MkDir` | Create a new directory |
| **`F8`** / **`Delete`** | `cm_Delete` | Delete selected files/folders |
| **`Shift+Delete`** | `cm_Wipe` | Permanently wipe/erase files/folders |
| **`F2`** / **`Shift+F6`** | `cm_Rename` | Rename the file/folder under the cursor |
| **`Ctrl+C`** | `cm_CopyToClipboard` | Copy to clipboard |
| **`Ctrl+X`** | `cm_CutToClipboard` | Cut to clipboard |
| **`Ctrl+V`** | `cm_PasteFromClipboard` | Paste from clipboard |

---

### ✅ Selection & Marking

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`Space`** / **`Insert`** | `cm_SelectOrDeselectFile` | Select/deselect current file and move cursor down |
| **`Ctrl+A`** | `cm_MarkAll` | Select all items |
| **`Ctrl+I`** / **`Num*`** | `cm_MarkInvert` | Invert selection of files/folders in current list |
| **`Num+`** | `cm_MarkPlus` | Select files by extension/wildcard pattern |
| **`Num-`** | `cm_MarkMinus` | Deselect files by extension/wildcard pattern |

---

### 🧭 Navigation & Panels

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`Enter`** | `cm_Open` | Open selected file or enter directory |
| **`Backspace`** / **`Ctrl+Up`** | `cm_ChangeDirToParent` | Go to parent directory |
| **`Ctrl+\`** | `cm_ChangeDirToRoot` | Go to root directory of current drive |
| **`Tab`** | `cm_SwitchPanel` | Switch focus between left and right panels |
| **`Alt+Left`** | `cm_ViewHistoryPrev` | Navigate back in history |
| **`Alt+Right`** | `cm_ViewHistoryNext` | Navigate forward in history |
| **`Ctrl+Left/Right`** | `cm_TargetEqualSource` | Set target (opposite) panel directory to match active panel |
| **`Ctrl+D`** | `cm_DirHotList` | Open Directory Hotlist (bookmarks) menu |

---

### 📑 Tab Management

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`Ctrl+T`** | `cm_NewTab` | Open a new tab in active panel |
| **`Ctrl+W`** | `cm_CloseTab` | Close current tab |
| **`Ctrl+Tab`** | `cm_NextTabCtrl` | Switch to next tab |
| **`Ctrl+Shift+Tab`** | `cm_PrevTabCtrl` | Switch to previous tab |

---

### 👁️ Views & Display

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`Ctrl+F1`** | `cm_BriefView` | Brief View (list mode) |
| **`Ctrl+F2`** | `cm_ColumnsView` | Detailed View (columns mode) |
| **`Ctrl+Shift+F1`** | `cm_ThumbnailsView` | Thumbnails View |
| **`Ctrl+B`** | `cm_FlatView` | Flat View / Branch View (display all sub-directory files) |
| **`Ctrl+H`** | `cm_ShowHiddenFiles` | Toggle show/hide hidden files |
| **`Ctrl+R`** | `cm_Refresh` | Refresh active panel |

---

### 🛠️ Advanced Tools & Utilities

| Shortcut | Command ID | Description |
| :--- | :--- | :--- |
| **`Alt+F7`** | `cm_FileSearch` | Search files |
| **`Ctrl+M`** | `cm_MultiRename` | Multi-rename tool |
| **`Alt+F5`** | `cm_PackFiles` | Pack/Compress files into archive |
| **`Alt+F9`** | `cm_ExtractFiles` | Extract files from archive |
| **`F3`** | `cm_View` | Open built-in viewer |
| **`F4`** | `cm_Edit` | Open built-in editor |
| **`Ctrl+Q`** | `cm_QuickView` | Quick View (preview file in opposite panel) |
| **`Alt+Enter`** | `cm_Properties` | View file/folder properties |
| **`F9`** / **`Ctrl+J`** | `cm_RunTerm` | Open terminal at current directory |

---

You can assign up to two shortcuts (Primary and Secondary) for any command. To customize shortcuts and view the full list for each context, visit **Preferences → Hotkeys**. The editor will automatically warn you if you try to use a shortcut that is already assigned.

## Auto-Fitting Columns
By default, the file panel automatically adjusts column widths so you can see the full file names.

- **Max text width (Default)**: Columns automatically fit the widest file name currently visible.

- **Average text width**: Sizes columns based on average text width plus a padding factor.

- **Fixed widths**: Retains a fixed width, which is automatically activated if you manually resize a column.

You can change the auto-fit mode in **Preferences → File Views**.
