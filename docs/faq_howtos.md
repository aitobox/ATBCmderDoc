# 05. FAQ and How-Tos

This guide provides task-based quick references and answers to frequently asked questions about using ATBCmder.

## General Usage

### How do I switch between the left and right panels?
Press the **`Tab`** key to toggle focus between the active and inactive panels.

### How do I view all files in a directory and its subdirectories at once?
Use **Branch View (Flat View)**. Press **`Cmd+B`** to activate or deactivate it. This will show a flat list of all files recursively. Press `Esc` or `Backspace` to return to standard directory browsing.

### How do I find out what a button or option does?
Hover your mouse over the button, menu item, or input field. ATBCmder features highly informative tooltips that explain the feature's function, provide the associated keyboard shortcut, and offer advanced help where applicable.

## File Operations

### How do I copy, move, or delete files?
ATBCmder uses classic Double Commander shortcuts for primary file operations:
- **Copy:** Select files and press **`F5`**.
- **Move/Rename:** Select files and press **`F6`**.
- **Make Directory:** Press **`F7`**.
- **Delete:** Select files and press **`F8`**.

### How do I preview files without opening an external application?
Select the file and press **`F3`**. ATBCmder includes specialized built-in viewers for audio, PDFs, and text, allowing you to preview content directly within the application.

### How do I listen to multiple audio files?
Select multiple audio files (like `.mp3`, `.flac`) and press `F3`. The built-in Audio Player will automatically build a playlist. You can click the "Background" button to minimize the player to the right panel and continue working while the music plays. To add more songs, select them and press `F3` while the player is backgrounded.

## Advanced Search & Commands

### How do I use natural language to find files?
ATBCmder features a **Semantic Command** input. 
1. Press **`/`** or **`Cmd+F`** to open the input at the bottom of the active panel.
2. Type a command in natural language, such as *"Select all files larger than 1MB"* or *"Find PDF files modified today"*.
3. By default, it searches the current directory. To perform a global Spotlight search, prefix your command with `//` (e.g., `//today modified pdf`).
4. Type `/help` for examples or `/history` to replay recent commands.

## Archives and Network File Systems

### How do I extract an archive?
You don't necessarily have to extract it! ATBCmder treats archives (`.zip`, `.tar`, `.7z`) as Virtual File Systems (`vfs://`). Simply select the archive and press `Enter` to navigate inside it as if it were a regular folder. If you still want to extract files, you can copy (`F5`) them from inside the archive to a standard directory in the other panel.

### How do I modify a file inside a ZIP archive?
Navigate into the archive, open the file you want to edit, and save your changes. ATBCmder's RepackWorker will detect the modifications and automatically prompt you to repack the file back into the archive.

### How do I connect to FTP, SFTP, WebDAV, or Samba?
Use the **Network Virtual File System (VFS)** feature. Once connected, the remote file system will appear in your panels, and you can interact with it—copying, moving, renaming, and deleting files—just as you would with local directories. Connections are managed securely without saving passwords to configuration files.

## Troubleshooting & Configuration

### Why aren't the file panels updating when a file changes on disk?
ATBCmder has an **Auto-refresh** feature that might be configured differently. Check your settings under the Options dialog:
- Ensure Auto-refresh is enabled.
- Check if it's set to disable when ATBCmder is in the background.
- Verify that the directory you are in hasn't been added to the excluded paths list.

### How can I test new configurations without breaking my setup?
You can run ATBCmder in an isolated test environment. Use the `ATBCmder_test.sh` script, which loads a separate `.test_config` profile. This allows you to experiment with internal `cm_*` commands and hotkeys safely.
