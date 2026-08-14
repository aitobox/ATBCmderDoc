# Download ATBCmder

Thank you for your interest in ATBCmder! We provide two different download and installation methods to suit your needs.

## 1. Mac App Store (Recommended)

This is the recommended way to install ATBCmder. Downloading through the official Mac App Store ensures you get automatic updates and the best system integration.

> **🚧 Under Review**  
> Our application is currently undergoing the review process for the Mac App Store. Stay tuned! In the meantime, please use the DMG installation method below.

[Mac App Store Download Page](https://apps.apple.com/app/atbcmder/6792398333)

## 2. DMG Installer Download

If you cannot access the Mac App Store or prefer direct downloads, we provide a DMG installer package.

- **DMG Download Link**: [Click here to download ATBCmder DMG](https://storage.aitobox.com/@s/bNAshV6G/ATBCmder)

*Note: When installing via DMG, macOS security features might require you to explicitly allow the application in "System Settings > Privacy & Security" the first time you open it.*

### ⚠️ Grant Full Disk Access

ATBCmder is a file management tool and requires explicit disk management permissions from the user. Please follow these steps:

1. Click the Apple icon in the top-left corner of your screen and select **System Settings** (or "System Preferences" on older macOS versions).
2. Navigate to **Privacy & Security** in the left or right menu.
3. Scroll down and select **Full Disk Access**.
4. Find the application (**ATBCmder**) in the list and toggle the switch to turn it on. If the application is not in the list, click the **+** button at the bottom to add it manually.
5. The system will ask you to enter your Mac login password or use Touch ID to confirm the changes.

## Release Notes

### 1.4.3 (2026-08-14)

- New macOS Native UI (Aqua Blue Theme): introduced as the new default theme, featuring interactive breadcrumb navigation (with cascading subfolder drilldown), Mac-style storage meter (fixed TB overflow), and rounded capsule selection
- Deep UI Polish: refined tab close button layout, fixed command prompt overlapping, and unified toolbar backgrounds, dividers, and panel borders across all themes
- i18n & App Upgrade: completed full project i18n coverage audit; added AList/OpenList share API support in the automatic update module

### 1.4.2 (2026-08-13)

- Enhanced AI Semantic Filter: supported parsing more common extensions, plural forms, and fully integrated with i18n
- Semantic Search UX: replaced wait cursor with QProgressBar, and improved Enter key behavior for completions
- Core Semantic Parsing: improved target type detection and keyword stripping for more accurate natural language search

### 1.4.1 (2026-08-13)

- Comprehensive codebase review and refactoring (Batches A-D)
- Security enhancements: Fixed potential path traversal and access vulnerabilities
- Concurrency & Performance: Improved background thread safety and execution efficiency
- Architecture: Enhanced stability and resource management in core components

### 1.4.0 (2026-08-12)

- Deep VFS network fixes: multi-encoding support, protocol drivers, chained archive mounting, and conflict resolution
- Enhanced app upgrade module: SSL verification fixes, DMG download validation, and UI integration
- Release note UI: display full version history during automatic updates

### 1.3.9 (2026-08-12)

- Added built-in EPUB reader (F3 quick view)
- Implemented app upgrade detection mechanism
- Fixed VFS worker freeze during file conflict resolution

### 1.3.8 (2026-08-08)

- Tree View UI refinement
- Refactored fsspec network integration
- Improved handling of invalid file characters

### 1.3.7 (2026-08-06)

- Network VFS Architecture: overhaul network file systems (FTP/WebDAV/SMB) using `fsspec`, implementing async `VfsTableModel`, streaming `StreamCopyWorker`, remote file operations (mkdir/rename/delete/overwrites), and F3/F4 remote viewing/editing
- System Tray & Hotkeys: support minimize to system tray, global shortcut (`Option+Cmd+H`), macOS Dock icon toggle, and native template icon integration
- LLM Configuration: introduce `default_llm.xml` resource and singleton for AI semantic filtering and options UI
- Navigation Enhancements: support PageUp / PageDown / Home / End / Fn navigation shortcuts across file panels and hotlist popups
- Internationalization: wrap all VFS error messages, Quick View panel labels, and tray menu strings with i18n translation catalogs

### 1.3.6 (2026-08-04)

- Network VFS Enhancements: add UTF-8/GBK auto-detection, dynamic makefile encoding update, fallback handling, and socket reset for FTP; resolve timeout & reply desync
- WebDAV & SMB Fixes: fix WebDAV/SMB root path stripping, last_error propagation, connection reliability, VFS icons & tab title displays
- Thumbnail Navigation: implement smooth 2D grid arrow navigation for Thumbnail View
- i18n & Code Quality: fix corrupted Close Tab translations in zh_CN/zh_TW catalogs and complete codebase optimization audit

### 1.3.5 (2026-08-03)

- Quick View Panel: implement Quick View feature (`cm_QuickView`, `Cmd+Q`/`Ctrl+Q`) supporting multi-format previews, fallback file properties, symmetric flip, Show menu integration, and full i18n
- Quick View Widgets: add `QuickViewContainer` and `QuickViewPropertiesWidget` integrated into FilePanel
- UI Polish: fix tab header alignment and options dialog page squishing issues in light theme

### 1.3.4 (2026-08-02)

- File Panel UI: add Shift+PageUp / Shift+PageDown batch selection in file panel views
- File Operations: fix F5 copy and F6 move file/directory defects
- Build Scripts: set exact certificate identity names, add timestamping to codesign, and handle notarization invalid status gracefully

### 1.3.3 (2026-08-01)

- Transfer Engine: calculate accurate real-time transfer speed and ETA in ProcessTransferWorker
- Permissions & Sandbox: separate macOS sandbox checks from Full Disk Access detection flow
- Build Scripts: update build script configuration for 1.3.3 DMG signed builds

### 1.3.2 (2026-08-01)

- Subprocess Transfer Worker: fix freeze/startup failure under Nuitka standalone App Store bundle mode
- Agent Skills: add i18n completeness audit check to code-review-optimization-audit skill

### 1.3.1 (2026-08-01)

- macOS Sandbox: fix false 'Full Disk Access Granted' state caused by `os.access` check
- Concurrent Tasks: resolve state cross-talk for concurrent background operations
- i18n: add Chinese translation for batch checkbox in permanent delete dialog
- Agent Skills: add and update code review optimization audit skill

### 1.3.0 (2026-08-01)

- Process-isolated transfer engine: implement ProcessTransferWorker & ProcessIOEngine to offload file copy/move I/O from UI thread
- Transfer performance & responsiveness: 10Hz IPC rate limiting, adaptive buffering, and macOS `F_NOCACHE` optimization to prevent GUI stutter
- Code audit & hardening: 4-phase refactoring including concurrency mutex locks, security hardening, and architecture cleanups
- UI fixes: fix Shiboken C++ deletion error, horizontal panel mode layout, and background task progress indicator signals

### 1.2.0 (2026-07-30)

- Implement global I/O process pool (IoWorkerPool) to isolate blocking file I/O operations and prevent GUI freezes
- Config versioning: read/write app_version on XML root node and add automated migration runner registry
- Drag & Drop / Clipboard: integrate native macOS Finder bridge, spring-loaded folders, and clipboard state machine
- Path expansion: add shared `expand_path` utility supporting `~`, `$VAR`, `%VAR%`, and `%COMMANDER_PATH%`
- Hotlist: implement standalone HotlistConfig singleton and default hotlist configuration

### 1.1.0 (2026-07-29)

- Fix release note entry order to ensure reverse chronological sorting below Release Note header
- Fix version manager script to support System/LastVersion XML node in default_config.xml
- Hotkeys: add Meta+Tab and Meta+Shift+Tab default shortcuts for tab navigation
- Favorite Tabs: add auto-migration and cleanup for legacy favorite tabs from main config
- File Viewer: optimize large file loading performance and memory usage

### 1.0.1 (2026-07-22)

> Fix F3 text preview failure in App Store sandbox environments

### 1.0.0 (2026-07-18)

> Initial implementation of the Python port of TotalCommander.
