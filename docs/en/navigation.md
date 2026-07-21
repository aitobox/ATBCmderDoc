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
ATBCmder is heavily keyboard-driven. Shortcuts are organized into contexts (like Main, FilePanel, Editor, and FindFiles).
Some essential shortcuts include:

- `Tab` / `Shift+Tab`: Switch focus between left and right panels, or tree view.

- `Ctrl+PgDn`: Open archive.

- `Ctrl+PgUp`: Go to parent directory.

- `Ctrl+Left` / `Ctrl+Right`: Transfer focus/contents to the opposite panel.

You can assign up to two shortcuts (Primary and Secondary) for any command. To customize shortcuts and view the full list for each context, visit **Preferences → Hotkeys**. The editor will automatically warn you if you try to use a shortcut that is already assigned.

## Auto-Fitting Columns
By default, the file panel automatically adjusts column widths so you can see the full file names.

- **Max text width (Default)**: Columns automatically fit the widest file name currently visible.

- **Average text width**: Sizes columns based on average text width plus a padding factor.

- **Fixed widths**: Retains a fixed width, which is automatically activated if you manually resize a column.

You can change the auto-fit mode in **Preferences → File Views**.
