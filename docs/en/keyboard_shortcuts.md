# Chapter 8: Master Keyboard Shortcut Reference

ATBCmder is designed from the ground up as a keyboard-first file manager. Every file operation, directory jump, view transformation, and batch utility can be executed with zero mouse interaction.

To bridge orthodox Commander traditions with native Apple ergonomics, ATBCmder employs a **Dual-Matrix Keyboard Architecture**: every command can be invoked using either classic Commander function keys (`F1`–`F12`, `Insert`, numeric keypad) or native macOS modifier chords (`⌘` Command, `⌥` Option, `⇧` Shift, `⌃` Control).

---

## 1. The Dual-Matrix Philosophy & Key Notation

Whether you have twenty years of muscle memory from Total Commander and Norton Commander or you live entirely within native macOS Finder shortcuts, ATBCmder accommodates your reflexes out of the box without requiring manual remapping.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      DUAL-MATRIX KEYBOARD ENGINE                            │
├──────────────────────────────────────┬──────────────────────────────────────┤
│  CLASSIC COMMANDER PARADIGM          │  NATIVE macOS PARADIGM               │
│  • Function Key Centric (F1–F12)     │  • Modifier Chords (⌘, ⌥, ⇧, ⌃)      │
│  • Dedicated Keypad Marking (+, -, *)│  • Finder Parity (⌘C, ⌘V, ⌘⌫, ⏎)     │
│  • Zero-Modal Terminal Velocity      │  • Native Menu Bar Integration       │
│  Examples:                           │  Examples:                           │
│    F5        ➔ Copy Files            │    ⌘C ➔ ⌘V   ➔ Copy Files            │
│    F6        ➔ Move Files            │    ⌘C ➔ ⌥⌘V  ➔ Move Files            │
│    Shift+F4  ➔ Create Text File      │    ⇧⌘4       ➔ Create Text File      │
│    Alt+F7    ➔ Find Files            │    ⌥⌘F       ➔ Find Files            │
└──────────────────────────────────────┴──────────────────────────────────────┘
```

### Apple Keyboard Modifier Symbols

Throughout this guide and within ATBCmder's preferences dialogs, key combinations are represented using standard macOS typographical glyphs:

| Glyph | Modifier Name | Windows / PC Equivalent | Description |
| :---: | :--- | :--- | :--- |
| **`⌘`** | **Command** (`Cmd`) | `Win` / `Ctrl` | Primary macOS action modifier key. |
| **`⌥`** | **Option** (`Alt`) | `Alt` | Secondary modifier for alternate actions and special characters. |
| **`⇧`** | **Shift** | `Shift` | Extends selections, inverts actions, or activates capital modes. |
| **`⌃`** | **Control** (`Ctrl`) | `Ctrl` | Terminal control and classic commander chord modifier. |
| **`⎋`** | **Escape** (`Esc`) | `Esc` | Cancels operations, clears filters, or closes dialogs. |
| **`⏎`** | **Return** (`Enter`) | `Enter` | Executes actions, opens items, or commits dialog prompts. |
| **`⌫`** | **Delete / Backspace** | `Backspace` | Backward character delete or parent directory navigation. |
| **`⌦`** | **Forward Delete** | `Del` | Forward delete character or delete selected file. |
| **`⇥`** | **Tab** | `Tab` | Alternates focus between source and target panels. |
| **`⇞`** | **Page Up** | `PgUp` | Scrolls panel listing up by one window viewport. |
| **`⇟`** | **Page Down** | `PgDn` | Scrolls panel listing down by one window viewport. |

---

## 2. macOS Function (`Fn`) Key Guidance

> [!IMPORTANT]
> ### How to Use Function Keys on Mac Keyboards
>
> By default, Apple keyboards (including built-in MacBook keyboards, Magic Keyboards, and Touch Bar Macs) assign the top physical row (`F1` through `F12`) to hardware controls such as display brightness, Mission Control, Spotlight, Dictation, media playback, and speaker volume.
>
> Because classic Commander workflows rely heavily on `F1`–`F12`, you have two options:
>
> #### Method A: Hold the `Fn` Key Chord (Default Out-of-the-Box)
> Hold the physical **`Fn`** key (or Globe 🌐 key) located in the lower-left corner of your Mac keyboard while pressing any function key:
> * **`Fn + F3`**: View file in Lister
> * **`Fn + F4`**: Edit file
> * **`Fn + F5`**: Copy files to target panel
> * **`Fn + F6`**: Move files to target panel
> * **`Fn + F7`**: Create new directory
> * **`Fn + F8`**: Delete files
> * **`Fn + Shift + F4`**: Create and edit new text file
> * **`Fn + Alt + F7`**: Open File Search
>
> #### Method B: Enable "Standard Function Keys" in macOS Settings (Recommended)
> If you use ATBCmder regularly, switch your function row so that pressing `F1`–`F12` triggers function commands directly, while holding `Fn` triggers brightness and volume adjustments:
>
> 1. **macOS 13 Ventura, macOS 14 Sonoma, macOS 15 Sequoia**:
>    - Open ** Apple Menu ➔ System Settings...**
>    - In the left sidebar, select **Keyboard**.
>    - Click the **Keyboard Shortcuts...** button.
>    - In the dialog sidebar, select **Function Keys**.
>    - Toggle **"Use F1, F2, etc. keys as standard function keys"** to **ON**.
>    - Click **Done**.
>
> 2. **macOS 12 Monterey & macOS 11 Big Sur**:
>    - Open ** Apple Menu ➔ System Preferences... ➔ Keyboard**.
>    - In the **Keyboard** tab, check the box labeled **"Use F1, F2, etc. keys as standard function keys"**.
>
> #### MacBook Pro Models with Touch Bar
> * Hold the physical **`Fn`** key at the bottom left to instantly display the virtual `F1`–`F12` row on the Touch Bar.
> * Alternatively, configure **System Settings ➔ Keyboard ➔ Touch Bar Settings...** and set **"Touch Bar shows"** to **"F1, F2, etc. Keys"** when ATBCmder is the active frontmost application.
>
> #### Compact Keyboards Without a Dedicated Function Row
> * If you are using a 60% or 65% mechanical keyboard without dedicated `F` keys, you do not need to contort your fingers. Use ATBCmder's native macOS modifier chords (`⌘C`, `⌥⌘V`, `⇧⌘N`, `⌘⌫`, `⌥⏎`) which provide 100% operational parity.

---

## 3. Context-Scoped Shortcut Architecture

To prevent hotkey collisions between different application areas (for example, searching inside the main file list versus searching inside a text file viewer), ATBCmder segments all shortcuts into distinct hierarchical contexts:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          APPLICATION SCOPE: Main                            │
│  Global commands, panel navigation, window management, toolbar, power tools │
├───────────────────────────────┬─────────────────────────────────────────────┤
│  PANEL SCOPE: FilePanel       │  MODAL TOOLS SCOPES                         │
│  Active during directory      │  • Viewer      (Lister preview window)      │
│  table and thumbnail browsing │  • Editor      (Built-in code editor)       │
│  (marking, range selection,   │  • Differ      (Side-by-side diff viewer)   │
│  inline editing, space count) │  • FindFiles   (Multi-threaded file search) │
│                               │  • MultiRename (Batch rename engine)        │
└───────────────────────────────┴─────────────────────────────────────────────┘
```

When you press a key chord, the **`HotkeyManager`** engine:
1. Evaluates the active focused context (e.g., `Viewer` or `FilePanel`).
2. If an exact binding matches, the associated `cm_*` command executes immediately.
3. If no binding exists in the local context, the keystroke falls back gracefully to the `Main` context.
4. If still unbound, standard text editing or system keystroke handling takes over.

---

## 4. Master Categorized Dual-Matrix Tables

The following reference tables document all commands supported by ATBCmder v1.7.0, categorized by functional workflow.

### 4.1 File Operations

File operations form the backbone of daily work. Every operation defaults to the **Source ➔ Target** paradigm: items selected in the active panel are processed into the directory open in the inactive opposite panel.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_View` | View file using Universal Lister (read-only preview) | `⌘3` / `Space` *(Quick View)* | `F3` / `Shift+F3` | Main |
| `cm_Edit` | Open file in built-in text editor | `⌘4` | `F4` | Main |
| `cm_EditNew` | Create and immediately edit a new text file | `⇧⌘4` / `⇧F4` | `Shift+F4` | Main |
| `cm_Copy` | Copy selected files from active to target panel | `⌘C` *(to clipboard)* / `F5` | `F5` | Main |
| `cm_CopySamePanel` | Duplicate/clone selected file within same directory | `⇧F5` | `Shift+F5` | Main |
| `cm_Move` | Move selected files from active to target panel | `⌥⌘V` *(paste move)* / `F6` | `F6` | Main |
| `cm_RenameOnly` | Quick inline rename of file under cursor | `⏎` *(Return)* / `F2` | `F2` / `Shift+F6` | Main |
| `cm_Rename` | Rename selected file via dialog | `⇧F6` | `Shift+F6` | Main |
| `cm_MkDir` | Create a new directory / folder | `⇧⌘N` / `F7` | `F7` | Main |
| `cm_Delete` | Delete selected items to macOS Trash | `⌘⌫` *(Cmd+Delete)* / `⌦` | `F8` / `Delete` | Main |
| `cm_Wipe` | Securely delete files (bypass Trash permanently) | `⌥⇧⌫` / `⌥⌦` | `Alt+Delete` / `Shift+Delete` | FilePanel |
| `cm_Open` | Open file with default app or enter directory | `⌘↓` / `⏎` *(Return)* | `Enter` | Main |
| `cm_SetFileProperties` | Inspect & edit file metadata, dates, and UNIX permissions | `⌥⏎` *(Option+Return)* / `⌘I` | `Alt+Enter` | Main |
| `cm_CountDirContent` | Calculate byte size of directory under cursor | `⌥⇧⏎` *(Option+Shift+Return)* | `Alt+Shift+Enter` | FilePanel |
| `cm_CalculateSpace` | Calculate total size of all selected directories | `⌃L` / `⌘L` | `Ctrl+L` | Main |
| `cm_SymLink` | Create symbolic link in target panel | `⌥⌘S` | *(Menu: Files ➔ Symlink)* | Main |
| `cm_HardLink` | Create filesystem hard link in target panel | `⌥⌘H` | *(Menu: Files ➔ Hardlink)* | Main |
| `cm_PackFiles` | Pack / compress selected files into archive (`.zip`, `.tar`, `.7z`) | `⌥F5` / `⌥⌘P` | `Alt+F5` | Main |
| `cm_ExtractFiles` | Extract archive contents directly into target panel | `⌥F9` / `⌥⌘E` | `Alt+F9` | Main |
| `cm_ArchiveView` | Enter archive as a virtual filesystem directory (`vfs://`) | `⌃⇟` *(Ctrl+PgDn)* / `⌘↓` | `Ctrl+PgDn` | Main |
| `cm_CompareContents` | Compare contents of two selected files | `⇧F3` | `Shift+F3` | Main |

---

### 4.2 Selection & Marking

Orthodox file managers excel at rapid multi-file selection. ATBCmder allows selecting individual items, wildcard patterns, extension groups, or continuous blocks without using a mouse.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_MarkMarkAll` | Select all files and folders in active panel | `⌘A` | `Ctrl+A` / `Ctrl+Num+` | Main |
| `cm_MarkUnmarkAll` | Deselect all files and folders in active panel | `⇧⌘A` | `Ctrl+Shift+A` / `Ctrl+Num-` | Main |
| `cm_MarkInvert` | Invert current selection state in active panel | `⌘I` / `⌃I` | `Num*` *(Keypad `*`)* | FilePanel |
| `cm_MarkPlus` | Select group matching wildcard pattern (e.g. `*.ts`) | `⌘+` / `⌃+` | `Num+` *(Keypad `+`)* | FilePanel |
| `cm_MarkMinus` | Deselect group matching wildcard pattern (e.g. `*.log`) | `⌘-` / `⌃-` | `Num-` *(Keypad `-`)* | FilePanel |
| `cm_MarkCurrentExtension` | Select all files sharing cursor's file extension | `⇧⌘E` / `⌥F8` | `Shift+Num+` / `Alt+Num+` | Main |
| `cm_UnmarkCurrentExt` | Deselect all files sharing cursor's file extension | `⌥⇧Num-` | `Shift+Num-` / `Alt+Num-` | Main |
| `cm_MarkCurrentName` | Select all files sharing cursor's base filename | `⌥⌘N` | *(Menu: Mark ➔ Same Name)* | Main |
| `cm_SelectOrDeselectFile` | Toggle item selection and advance cursor down | `Space` | `Insert` / `Space` | FilePanel |
| `Shift+Up / Shift+Down` | Expand or contract continuous selection range | `⇧↑` / `⇧↓` | `Shift+↑` / `Shift+↓` | FilePanel |
| `Shift+PageUp / Shift+PageDown` | Expand continuous selection by full viewport page | `⇧⇞` / `⇧⇟` | `Shift+PgUp` / `Shift+PgDn` | FilePanel |
| `cm_ClearAll` | Clear all selection marks and search highlights | `⌃L` | `Ctrl+L` | Main |
| `cm_CopyToClipboard` | Copy selected files to macOS system clipboard | `⌘C` | `Ctrl+C` | Main |
| `cm_CutToClipboard` | Cut selected files to macOS system clipboard | `⌘X` | `Ctrl+X` | Main |
| `cm_PasteFromClipboard` | Paste files from clipboard into active directory | `⌘V` | `Ctrl+V` | Main |
| `cm_PasteAsMove` | Paste files from clipboard as a Move operation | `⌥⌘V` | `Ctrl+Alt+V` | Main |
| `cm_CopyNamesToClip` | Copy filename(s) only to clipboard | `⇧⌘X` | `Ctrl+Shift+X` | Main |
| `cm_CopyFullNamesToClip` | Copy full absolute path(s) to clipboard | `⇧⌘C` | `Ctrl+Shift+C` | Main |
| `cm_CompareDirectories` | Mark files that exist in one panel but not the other | `⌥⇧C` | *(Menu: Mark ➔ Compare Dirs)* | Main |

---

### 4.3 Panel Navigation & Bookmarks

Effortlessly move across folders, local volumes, network mounts, and browsing history.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FocusSwap` / `cm_SwitchPanel` | Alternate keyboard focus between left & right panels | `⇥` *(Tab)* | `Tab` | Main |
| `cm_Refresh` | Refresh / reread active directory contents | `⌘R` / `⌃R` | `Ctrl+R` | Main |
| `cm_ChangeDirToParent` | Navigate up to parent directory (`..`) | `⌘↑` / `⌫` *(Backspace)* | `Backspace` / `Ctrl+PgUp` | Main |
| `cm_ChangeDirToRoot` | Jump directly to filesystem root (`/`) | `⌘\` | `Ctrl+\` | Main |
| `cm_ChangeDirToHome` | Jump directly to user's home folder (`~`) | `⇧⌘H` | `Ctrl+Shift+Home` / `Alt+Home` | FilePanel |
| `cm_ViewHistoryPrev` | Navigate back in directory browsing history | `⌘[` / `⌥←` | `Alt+Left` / `Ctrl+[` | Main |
| `cm_ViewHistoryNext` | Navigate forward in directory browsing history | `⌘]` / `⌥→` | `Alt+Right` / `Ctrl+]` | Main |
| `cm_DirHistory` | Open interactive directory history dropdown menu | `⌥↓` / `⌃↓` | `Alt+Down` / `Alt+F8` | Main |
| `cm_Drives` | Open drive and mounted volume selector popup | `⌥D` | `Alt+D` | Main |
| `cm_LeftOpenDrives` | Open drive selection menu for Left panel | `⌥F1` | `Alt+F1` | Main |
| `cm_RightOpenDrives` | Open drive selection menu for Right panel | `⌥F2` | `Alt+F2` | Main |
| `cm_Exchange` | Swap left and right panels (directories, tabs, states) | `⌘U` | `Ctrl+U` | Main |
| `cm_TargetEqualSource` | Set inactive panel directory to match active directory | `⌥Z` / `⌃←` / `⌃→` | `Alt+Z` / `Ctrl+Left` / `Ctrl+Right` | Main |
| `cm_SyncSlaveDir` | Lock target panel navigation to mirror source panel | `⌥S` | *(Menu: Commands ➔ Sync Navigation)* | Main |
| `cm_DirHotList` | Open Directory Hotlist / Bookmarks menu | `⌘D` | `Ctrl+D` | Main |
| `cm_ConfigDirHotList` | Open Directory Hotlist configuration dialog | `⇧⌘D` | `Ctrl+Shift+D` | Main |
| `cm_GoToFirst` | Jump cursor to first item in active panel | `⌘↑` / `Fn+←` *(Home)* | `Home` | Main |
| `cm_GoToLast` | Jump cursor to last item in active panel | `⌘↓` / `Fn+→` *(End)* | `End` | Main |
| `PageUp / PageDown` | Scroll active panel up or down by one full viewport | `⇞` *(Fn+↑)* / `⇟` *(Fn+↓)* | `PageUp` / `PageDown` | FilePanel |

---

### 4.4 View Modes & Sorting

Switch seamlessly between compact lists, detailed metadata columns, visual thumbnail grids, recursive directory flattening, and synchronized tree views.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_BriefView` | Switch to Brief View (multi-column compact names) | `⌃F1` | `Ctrl+F1` | Main |
| `cm_ColumnsView` | Switch to Columns / Details View (name, size, date, perms) | `⌃F2` | `Ctrl+F2` | Main |
| `cm_ThumbnailsView` | Switch to Thumbnails Grid View (images, media, PDFs) | `⌃⇧F1` | `Ctrl+Shift+F1` | Main |
| `cm_FlatView` | Toggle Flat / Branch View (recursive directory listing) | `⌘B` | `Ctrl+B` | Main |
| `cm_FlatViewSel` | Flat / Branch View of selected directories only | `⇧⌘B` | `Ctrl+Shift+B` | Main |
| `cm_TreeView` | Tree View (Replace active panel with directory tree) | `⌃⇧F8` | `Ctrl+Shift+F8` | Main |
| `cm_TreeViewSplit` | Tree View (Split panel: tree top/left, files bottom/right) | `cm_TreeViewSplit` | *(Menu: Show ➔ Tree View Split)* | Main |
| `cm_TreeViewBoth` | Tree View (Both panels show directory trees) | `cm_TreeViewBoth` | *(Menu: Show ➔ Tree View Both)* | Main |
| `cm_QuickView` | Toggle Quick View panel (live preview in opposite panel) | `⌘Q` / `⌃Q` | `Ctrl+Q` | Main |
| `cm_SortByName` | Sort items by Name (toggle ascending / descending) | `⌃F3` | `Ctrl+F3` | Main |
| `cm_SortByExt` | Sort items by Extension | `⌃F4` | `Ctrl+F4` | Main |
| `cm_SortByDate` | Sort items by Modification Date/Time | `⌃F5` | `Ctrl+F5` | Main |
| `cm_SortBySize` | Sort items by File Size | `⌃F6` | `Ctrl+F6` | Main |
| `cm_SortByAttr` | Sort items by UNIX Attributes / Permissions | `cm_SortByAttr` | *(Menu: Sort ➔ Attributes)* | Main |
| `cm_ShowHiddenFiles` | Toggle visibility of hidden files (`.` dotfiles) | `⌘H` / `⇧⌘.` | `Ctrl+H` | Main |
| `cm_ShowSysFiles` | Toggle visibility of macOS system & protected files | `⇧⌘.` | `Ctrl+.` | Main |
| `cm_QuickSearch` | Open in-panel Quick Search bar (type letters to filter) | `⌥S` / `⌃S` *(or typing)* | `Ctrl+S` / *(Letter typing)* | Main |
| `cm_SemanticFilter` | Open Natural Language Semantic Smart Filter bar | `⌘F` | `Ctrl+F` | Main |
| `cm_HorizontalFilePanels` | Toggle horizontal dual-panel layout (stacked vertically) | `⇧⌘H` | `Ctrl+Shift+H` | Main |

---

### 4.5 Tabs & Window Management

ATBCmder allows opening unlimited tabs in either panel, locking favorite working locations, and managing dual-panel multi-tab sessions.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_NewTab` | Open new folder tab in active panel | `⌘T` | `Ctrl+T` | Main |
| `cm_CloseTab` | Close currently active folder tab | `⌘W` | `Ctrl+W` | Main |
| `cm_NextTab` / `cm_NextTabCtrl` | Switch to next tab on the right | `⌃⇥` *(Ctrl+Tab)* / `⌘⇧]` | `Ctrl+Tab` | Main |
| `cm_PrevTab` / `cm_PrevTabCtrl` | Switch to previous tab on the left | `⌃⇧⇥` *(Ctrl+Shift+Tab)* / `⌘⇧[` | `Ctrl+Shift+Tab` | Main |
| `cm_ShowTabsList` | Show popup menu of all open tabs in active panel | `⇧⌘L` | `Ctrl+Shift+L` | Main |
| `cm_CloseAllTabs` | Close all tabs in active panel except the last one | `⌥⌘W` | *(Tab Context Menu: Close All)* | Main |
| `cm_CloseOtherTabs` | Close all tabs other than the currently active tab | `⇧⌘W` | *(Tab Context Menu: Close Others)* | Main |
| `cm_Duplicatetab` | Duplicate active folder tab | `⌘D` / `cm_Duplicatetab` | *(Tab Context Menu: Duplicate)* | Main |
| `cm_MoveTabLeft` | Move active tab one position to the left | `⌃⇧←` | *(Tab Context Menu: Move Left)* | Main |
| `cm_MoveTabRight` | Move active tab one position to the right | `⌃⇧→` | *(Tab Context Menu: Move Right)* | Main |
| `cm_CopyTabToOtherPanel` | Clone active tab directly into opposite panel | `⌥⌘T` | *(Tab Context Menu: Copy to Other)* | Main |
| `cm_SaveTab` / `cm_SaveTabs` | Save current tab layout to configuration | `cm_SaveTab` | *(Menu: Tabs ➔ Save Tabs)* | Main |
| `cm_LoadTab` / `cm_LoadTabs` | Restore saved tab layout from configuration | `cm_LoadTab` | *(Menu: Tabs ➔ Load Tabs)* | Main |
| `cm_OptionsFavorites` | Configure Favorite Tab sets and persistent workspaces | `cm_OptionsFavorites` | *(Menu: Tabs ➔ Favorite Tabs)* | Main |
| `cm_FullScreen` | Toggle full screen application window | `⌃⌘F` / `F11` | `F11` | Main |

---

### 4.6 Power Tools & Utilities

Launch advanced automation tools, batch utilities, and embedded system tools directly from keyboard chords.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_FileSearch` / `cm_Search` | Open Advanced Multi-Filter Search Dialog | `⌥F7` / `⌥⌘F` | `Alt+F7` | Main |
| `cm_FileDiff` / `cm_CompareFiles` | Open Side-by-Side Visual File Difference Viewer | `⌘⇧F12` | `Meta+Shift+F12` | Main |
| `cm_SyncDirs` | Open Two-Way Directory Synchronization Tool | `⇧F12` | `Shift+F12` | Main |
| `cm_MultiRename` | Open Batch Multi-Rename Tool (RegEx & tokens) | `⌘M` | `Ctrl+M` | Main |
| `cm_Split` | Split large file into uniform chunk segments | `⌥F6` | `Alt+F6` | Main |
| `cm_Combine` | Combine split numbered segments back into original file | `⌥F7` | `Alt+F7` | Main |
| `cm_CalculateChecksum` | Calculate cryptographic hash (MD5, SHA-1, SHA-256) | `⌃X` / `⌘K` | `Ctrl+X` | Main |
| `cm_VerifyChecksum` | Verify files against checksum file (`.md5`, `.sha256`) | `cm_VerifyChecksum` | *(Menu: Files ➔ Verify Checksum)* | Main |
| `cm_RunTerm` | Launch system Terminal at active panel directory | `⌃J` / `F9` | `Ctrl+J` / `F9` | Main |
| `cm_FocusCmdLine` | Shift keyboard focus directly to bottom command line | `⇧F2` | `Shift+F2` | Main |
| `cm_ShowCmdLineHistory` | Open history dropdown of past shell commands | `⌥↓` / `⌃↓` | `Alt+F8` / `Ctrl+Down` | Main |
| `cm_AddPathToCmdLine` | Append active directory path to command line | `⌘P` | `Ctrl+P` | Main |
| `cm_ShowCommandLine` | Toggle bottom command line / console input bar | `⌘O` | `Ctrl+O` | Main |
| `cm_DiskBenchmark` | Run storage drive read/write performance benchmark | `cm_DiskBenchmark` | *(Menu: Commands ➔ Benchmark)* | Main |
| `cm_VisSemanticCommand` | Open Semantic Search & Natural Language Command Bar | `/` / `⇧⌘P` | `/` | Main |

---

### 4.7 System, Configuration & Help

Access application preferences, configuration management, software updates, and user documentation.

| Command ID | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| `cm_Options` | Open Application Preferences / Settings Dialog | `⌘,` | `Ctrl+,` | Main |
| `cm_HelpContents` / `cm_HelpIndex` | Open Interactive User Documentation & Guide | `⌘?` / `F1` | `F1` | Main |
| `cm_HelpKeyboard` | Open Quick Keyboard Shortcuts Reference Card | `cm_HelpKeyboard` | *(Menu: Help ➔ Keyboard)* | Main |
| `cm_Exit` | Quit / Exit ATBCmder | `⌘Q` | `F10` / `Alt+F4` / `Alt+X` | Main |
| `cm_About` | Display ATBCmder version, license, and credits | `cm_About` | *(Menu: ATBCmder ➔ About)* | Main |
| `cm_OpenConfigDirectory` | Reveal configuration folder (`atbcmder.xml`) in panel | `cm_OpenConfigDirectory` | *(Menu: Configuration ➔ Open Config)* | Main |
| `cm_ExportConfiguration` | Export all preferences to portable ZIP bundle | `cm_ExportConfiguration` | *(Menu: Configuration ➔ Export)* | Main |
| `cm_ImportConfiguration` | Import preferences from portable ZIP bundle | `cm_ImportConfiguration` | *(Menu: Configuration ➔ Import)* | Main |
| `cm_CheckForUpdate` | Check for application software updates | `cm_CheckForUpdate` | *(Menu: Help ➔ Check for Updates)* | Main |

---

## 5. Modal Tool Context Shortcuts

When opening specialized tools such as Universal Lister, the built-in text editor, the side-by-side differ, or batch dialogs, ATBCmder activates context-specific keymaps. These shortcuts operate directly within each tool window rather than through global application-wide `cm_*` registry commands.

### 5.1 Universal Lister (`Viewer` Context)

Active when previewing documents, text, code, images, audio, video, or raw hex bytes.

| Action / Feature | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| Select All | Select all text / content in viewer | `⌘A` | `Ctrl+A` | Viewer |
| Plain Text Mode | Switch to Plain Text mode | `1` | `1` | Viewer |
| Binary Mode | Switch to Binary mode | `2` | `2` | Viewer |
| Raw Hex Mode | Switch to Raw Hex byte inspection mode | `3` | `3` | Viewer |
| Decimal Mode | Switch to Decimal mode | `4` | `4` | Viewer |
| Book View | Switch to Paginated Book mode | `5` | `5` | Viewer |
| Image View | Switch to Image viewer mode | `6` | `6` | Viewer |
| Custom Plugins | Switch to Custom plugin viewer | `7` | `7` | Viewer |
| PDF / Office View | Switch to PDF / Office document reader mode | `8` | `8` | Viewer |
| Code Mode | Switch to Syntax-highlighted code mode | `9` | `9` | Viewer |
| Center Image | Center image within viewer window | `C` | `C` | Viewer |
| Fit to Window | Fit image to window dimensions | `F` | `F` | Viewer |
| Fit Large Only | Downscale only if image exceeds window dimensions | `L` | `L` | Viewer |
| Toggle Wrap | Toggle line wrapping on / off | `W` | `W` | Viewer |
| Toggle Caret | Toggle visible text cursor caret | `F6` | `F6` | Viewer |
| Find Text | Find text within document | `⌘F` / `F7` | `F7` | Viewer |
| Find Next | Jump to next search match | `⌘G` / `F3` | `F3` | Viewer |
| Find Previous | Jump to previous search match | `⇧⌘G` / `⇧F3` | `Shift+F3` | Viewer |
| Zoom In | Zoom in image or PDF | `⌘+` / `Num+` | `Num+` | Viewer |
| Zoom Out | Zoom out image or PDF | `⌘-` / `Num-` | `Num-` | Viewer |
| Full Screen | Toggle full screen viewing mode | `⌃⌘F` / `⌥⏎` | `Alt+Enter` | Viewer |
| Close Viewer | Close Lister viewer window | `⎋` *(Esc)* / `Q` | `Escape` / `Q` | Viewer |

---

### 5.2 Built-in Text Editor (`Editor` Context)

Active when creating or modifying text and source code files.

| Action / Feature | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| Save File | Save modified file to disk | `⌘S` / `F2` | `F2` | Editor |
| Find Text | Find text in editor document | `⌘F` / `F7` | `F7` | Editor |
| Find Next | Jump to next search match | `⌘G` / `F3` | `F3` | Editor |
| Find Previous | Jump to previous search match | `⇧⌘G` / `⇧F3` | `Shift+F3` | Editor |
| Cut | Cut selected text to clipboard | `⌘X` | `Ctrl+X` | Editor |
| Copy | Copy selected text to clipboard | `⌘C` | `Ctrl+C` | Editor |
| Paste | Paste text from clipboard | `⌘V` | `Ctrl+V` | Editor |
| Undo | Undo last typing action | `⌘Z` | `Ctrl+Z` | Editor |
| Redo | Redo last undone action | `⇧⌘Z` | `Ctrl+Shift+Z` | Editor |
| Select All | Select entire document text | `⌘A` | `Ctrl+A` | Editor |
| Close Editor | Close text editor window | `⎋` *(Esc)* / `⌘W` | `Esc` / `Alt+X` | Editor |

---

### 5.3 Side-by-Side Visual Differ (`Differ` Context)

Active inside the visual difference comparison tool.

| Action / Feature | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| Find Text | Search text within difference panes | `⌘F` / `F7` | `F7` | Differ |
| Find Next | Jump to next search occurrence | `⌘G` / `F3` | `F3` | Differ |
| Find Previous | Jump to previous search occurrence | `⇧⌘G` / `⇧F3` | `Shift+F3` | Differ |
| Next Difference | Jump cursor to next difference block | `⌥↓` *(Option+Down)* | `Alt+Down` | Differ |
| Previous Difference | Jump cursor to previous difference block | `⌥↑` *(Option+Up)* | `Alt+Up` | Differ |
| First Difference | Jump directly to first difference in files | `⌥Fn+←` *(Opt+Home)* | `Alt+Home` | Differ |
| Last Difference | Jump directly to last difference in files | `⌥Fn+→` *(Opt+End)* | `Alt+End` | Differ |
| Copy Right to Left | Copy difference block from Right pane to Left pane | `⌥←` *(Option+Left)* | `Alt+Left` | Differ |
| Copy Left to Right | Copy difference block from Left pane to Right pane | `⌥→` *(Option+Right)* | `Alt+Right` | Differ |
| Refresh / Rescan | Reread files from disk and re-run difference comparison | `⌘R` | `Ctrl+R` | Differ |
| Close Differ | Close difference comparison window | `⎋` *(Esc)* / `⌘W` | `Alt+X` / `Esc` | Differ |

---

### 5.4 Advanced File Search Dialog (`FindFiles` Context)

Active inside the background multi-threaded search dialog.

| Action / Feature | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| Start Search | Start search execution | `⏎` *(Return)* / `F9` | `F9` | FindFiles |
| Cancel / Close | Cancel running search or close dialog | `⎋` *(Esc)* | `Esc` | FindFiles |
| View Selected | View selected search result in Lister | `⌘3` / `F3` | `F3` | FindFiles |
| Edit Selected | Open selected search result in Editor | `⌘4` / `F4` | `F4` | FindFiles |
| New Search | Reset search query and prepare new search | `⌘N` | `Ctrl+N` | FindFiles |
| Clear Filters | New search with all date/size/attribute filters cleared | `⇧⌘N` | `Ctrl+Shift+N` | FindFiles |
| Recall Previous | Recall parameters from previous search | `⌘L` | `Ctrl+L` | FindFiles |

---

### 5.5 Batch Multi-Rename Tool (`MultiRename` Context)

Active inside the batch renaming workspace.

| Action / Feature | Description | Primary macOS Shortcut (with ⌘/⌥/⇧/⌃ glyphs) | Classic Commander Shortcut (with Fn keys) | Context |
| :--- | :--- | :---: | :---: | :---: |
| Reset Rules | Reset renaming mask and pattern rules to default | `⌘R` | `Ctrl+R` | MultiRename |
| Edit Names in Editor | Open target filename list in external editor for manual editing | `⌘I` | `Ctrl+I` | MultiRename |
| Load Names File | Load replacement names from an external text file | `F3` | `F3` | MultiRename |

---

## 6. Pro Tips & System Hotkey Optimization

### 6.1 Resolving macOS Global Shortcut Collisions

Certain default macOS system hotkeys intercept keypresses before they reach desktop applications. To unlock full Commander agility, you can customize or disable conflicting macOS shortcuts:

1. **Spotlight Search (`⌘Space` vs Quick Search)**:
   - By default, `⌘Space` activates Spotlight. If you prefer to use `⌘Space` for file marking or in-panel search, remap Spotlight to `⌥Space` in **System Settings ➔ Keyboard ➔ Keyboard Shortcuts... ➔ Spotlight**.
2. **Mission Control (`⌃↑`) & App Exposé (`⌃↓`)**:
   - macOS uses `⌃↑` and `⌃↓` for Mission Control. In ATBCmder, `⌃↓` opens the Directory History dropdown. You can reassign Mission Control in **System Settings ➔ Keyboard ➔ Keyboard Shortcuts... ➔ Mission Control**.
3. **Application Hiding (`⌘H`)**:
   - In macOS, `⌘H` hides the frontmost application. ATBCmder uses `⌘H` or `⇧⌘.` to toggle hidden dotfiles. If you want `⌘H` to strictly toggle hidden files, disable "Hide Application" in macOS or use the Finder-standard `⇧⌘.` (`Cmd+Shift+Period`).
4. **Window Minimizing (`⌘M`)**:
   - macOS assigns `⌘M` to minimize the window to the Dock. ATBCmder assigns `⌘M` to the Batch Multi-Rename Tool (`cm_MultiRename`). ATBCmder captures `⌘M` within its main window, but you can also trigger Multi-Rename via `Ctrl+M` or the toolbar.

---

### 6.2 Trackpad & Mouse Ergonomics

For laptop users without an external keyboard, ATBCmder pairs keyboard shortcuts with intuitive trackpad gestures:

* **Pinch to Zoom Thumbnails**: In Thumbnails View (`cm_ThumbnailsView`), pinch in or out on your MacBook trackpad (or hold `⌃` and scroll) to resize thumbnail previews continuously from `48 px` up to `512 px`.
* **Two-Finger Swipe Back / Forward**: Swipe left or right with two fingers on the file table to navigate backward (`cm_ViewHistoryPrev`) and forward (`cm_ViewHistoryNext`) through folder history.
* **Double-Click Splitter**: Double-click anywhere on the vertical center divider bar to reset panels to an exact 50/50 horizontal split.
* **Middle-Click on Tabs**: Middle-click (or three-finger tap) any folder tab to close it immediately without pressing `⌘W`.

---

### 6.3 Customizing Keybindings in Preferences

Every shortcut documented above can be customized or rebound:

1. Press **`⌘,`** (or select **Configuration ➔ Options...**) to open the Preferences dialog.
2. Select **Hotkeys** from the sidebar.
3. Use the **Context** dropdown to choose which area you want to configure (`Main`, `FilePanel`, `Viewer`, etc.).
4. Use the search filter box to locate any command by name or `cm_*` ID.
5. Click the shortcut box and press your desired key combination. The built-in collision detector will warn you immediately if that chord is already assigned elsewhere.
6. Click **Apply** to activate changes instantly without restarting the application.

User keybindings are saved to `~/.config/atbcmder/atbcmder_hotkeys.xml` (or `~/Library/Preferences/atbcmder/` on macOS). You can export and transfer this file across machines using **`cm_ExportConfiguration`**.

---

<div align="center">
  <p>Looking for practical everyday recipes, NAS mounting workflows, or troubleshooting tips?</p>
  <p><strong><a href="faq_howtos.md">Proceed to Chapter 9: Real-World Recipes & Troubleshooting &rarr;</a></strong></p>
</div>
