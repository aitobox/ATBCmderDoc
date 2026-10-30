# Chapter 11: Download & Installation

Thank you for your interest in ATBCmder! We provide two different download and installation methods to suit your needs.

> [!IMPORTANT]
> **System & Architecture Requirements**  
>
> - **Operating System**: macOS 12.0 (Monterey) or later (including macOS 13 Ventura, macOS 14 Sonoma, and macOS 15 Sequoia).  
> - **Supported Hardware Architecture**: **Universal (Apple Silicon ARM64 & Intel x86_64)**.  
> - **Intel (x86_64) Compatibility**: Fully supported via universal binaries and dual-architecture packaging.

## 1. Mac App Store (Recommended)

This is the recommended way to install ATBCmder. **ATBCmder is now officially available on the Mac App Store!** Downloading through the official Mac App Store ensures you get seamless automatic updates, native macOS sandbox protection, and the best system integration.

- **Mac App Store**: [Download ATBCmder on the Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)

## 2. DMG Installer Download

If you cannot access the Mac App Store or prefer direct downloads, we provide standalone DMG installer packages built natively for macOS with dual-architecture support (Universal / ARM64 & Intel x86_64).

- **DMG Download Link**: [Click here to download ATBCmder DMG](https://storage.aitobox.com/@s/atbcenter/ATBCmder) *(Universal: Apple Silicon & Intel x86_64)*

*Note: When installing via DMG, macOS security features might require you to explicitly allow the application in "System Settings > Privacy & Security" the first time you open it.*

### ⚠️ Grant Full Disk Access

ATBCmder is a file management tool and requires explicit disk management permissions from the user. Please follow these steps:

1. Click the Apple icon in the top-left corner of your screen and select **System Settings** (or "System Preferences" on older macOS versions).
2. Navigate to **Privacy & Security** in the left or right menu.
3. Scroll down and select **Full Disk Access**.
4. Find the application (**ATBCmder**) in the list and toggle the switch to turn it on. If the application is not in the list, click the **+** button at the bottom to add it manually.
5. The system will ask you to enter your Mac login password or use Touch ID to confirm the changes.

## Release Notes

### 2.4.3 (2026-10-30)

- Advanced Recent File & Folder Changes Tool: Built a dedicated "Recent Changes" system tool powered by native bridge commands, supporting flexible time ranges (1 hour, 24 hours, 7 days, 30 days) and minimum size filters (>1MB, >10MB, >100MB, >1GB); integrates macOS Spotlight metadata to seed candidates for ultra-fast deep scans; search results support instant text filtering, double-click/contextual navigation to Finder or panel paths, and batch moving to Trash
- Collision-Safe Paste Auto-Rename & Cloud Storage Reliability: Automatically appends incremental numeric suffixes (e.g. `name (1).ext`) when pasted files or directories collide with existing items, preventing accidental overwrites (Fixes #92); restored missing Google Drive discovery data across virtual filesystems (Fixes #87, #91); bundled essential Dropbox cloud dependencies in macOS application builds (Fixes #90)
- Comprehensive 31-Language Audit & Terminology Standardization: Rigorously audited and polished translations across all 31 supported languages, resolving PO line-wrap escaping issues and syntax errors while eliminating machine-translation anomalies (Fixes #88, #93); standardized professional file manager terminology and refreshed compiled binary `.mo` catalogs
- macOS Native UX Polish & Visual Refinement: Standardized confirmation dialog buttons to macOS conventions ("Yes/Confirm" preceding "No/Cancel"); cleaned up redundant hairline borders around path tabs for a refined capsule appearance; fixed macOS Dock icon fuzziness caused by Qt downsampling, improved table header column divider contrast, and resolved a path checker thread retirement race condition

### 2.4.2 (2026-10-26)

- System Cleaner Overhaul & Per-Application Cleanup: Added dual grouping modes (by Application or by Category) to inspect and clean caches and logs per app (Fixes #85); accurate group size calculation excluding unknown entries, pre-scan permission checks, and live status indicators (Cleaned 0 B, failure tooltips); added "Reveal in Finder" and "Open in ATBCmder" toolbar buttons with double-click support; aligned window geometry with Disk Space Analyzer
- atbsys Privileged Bridge & Storage Accounting Hardening: Synchronized Mole safety verification for cleanup and uninstall plans (Fixes #80), ensuring execution strictly matches confirmed plans, protects personal/shared data, and honors App Store sandbox writable locations; hardened filesystem accounting for hard links, APFS clone tracking, CPU sampling, and command timeouts
- macOS Packaging Pipeline & Multi-Architecture Hardening: Aligned version and build metadata across modules; pinned Go and Qt toolchains compatible with macOS 12+; fixed Mach-O slice verification on x86_64 hosts by passing `-arch all` to otool; safeguarded codesign plist parsing against padding bytes and enforced build abortion on packaging or signing failures
- Panel Interaction, Context Icons & Localization Polish: Resolved the issue where deleting files or refreshing caused the file panel to jump back to the top (Fixes #81, #82), smoothly shifting focus to adjacent rows while preserving scroll positions; configured semantic vector icons for all context menu actions (Fixes #83, #84); polished CSV viewer cell status and terminology translations across all 31 supported languages

### 2.4.1 (2026-10-24)

- Header Interaction Overhaul & Finder-Style Column Dividers: Introduced a dedicated `DividerHeaderView` for file table headers, drawing subtle, inset vertical hairline dividers centered between columns for crisp visual separation without bulky borders; overhauled `HeaderResizeCursorController` with an 8px forgiving hit-test zone and clean gesture separation between column sorting and resizing, eliminating cursor flicker and drag-handle conflicts
- Options Dialog Theme Anti-Jitter & Performance Optimization: Refined cancel/rejection behavior in the Options dialog so global theme rollback is only invoked if the active theme was actually modified during preview; eliminates redundant stylesheet recompilation and polish passes across all UI widgets when dismissing preferences without theme changes, removing modal close stutters
- High-Resolution App Icons & macOS Packaging Pipeline Fix: Updated higher-resolution official logo assets; fixed an issue in macOS DMG/PKG and Nuitka build scripts where `AppIcon.icns` was inadvertently pruned during asset cleanup; expanded icon discovery to resolve directly from standard `.app/Contents/Resources/AppIcon.icns`, guaranteeing crisp icon rendering in the Dock and Finder

### 2.4.0 (2026-10-23)

- File Panel Tabs Overhaul with macOS Native Card/Capsule Design: Completely redesigned path tab bars into rounded card capsules with slot backgrounds and hairline dividers, fixing uneven borders and clipping; established active/inactive focus hierarchy (vibrant blue indicator for active panel, neutral gray for inactive); introduced semantic vector icons (locked padlocks, Home, Root, Search results); standardized 28px height aligned pixel-perfectly with drive selectors (Fixes #78, #79)
- Smart Encoding Auto-Detection in Viewer & Editor: Built a dedicated encoding detection engine (`encoding_utils`) combining BOM inspection, chardet analysis, and common codepage heuristics; completely resolved garbled text when opening GBK, GB18030, Big5, Shift-JIS, and EUC-KR files in Universal Viewer (F3) and Editor (F4)
- Lightweight Architecture & Dramatic Package Size Reduction: Completely removed the heavy `opencv-python-headless` dependency (shaving 70MB+), reimplementing image processing and watermark removal with Pillow and Apple CoreImage; pruned unused transcoding libraries (libtesseract, libx265), significantly reducing DMG/PKG installer sizes and runtime memory footprint
- Core Safety Audit & Broad Stability Hardening: Eliminated the risk of source file truncation when copying to identical physical files across paths or VFS layers; secured text editor symlink preservation, read-only permissions, and multibyte/Emoji replacement synchronization; hardened command-line `cd` path escaping, multi-rename conflict resolution, checksum cancellation responsiveness, 7z extraction, and image scanline alignment crashes

### 2.3.9 (2026-10-22)

- Default Theme Refinement & Modern UI Architecture: Introduced semantic appearance tokens and contrast rules with seamless light and dark mode adaptation; restored colorful icons, classic blue panel accents, and unified high-contrast active, marked, and translucent hover states; expanded default toolbar with native overflow while preserving custom toolbar configurations; slightly widened drive selector with green disk capacity bars and clear unknown capacity handling; hidden semantic command bar by default for a cleaner look, kept bookmark popups within panels, and unified footer shortcut badges
- Archive Encoding Auto-Detection & ZIP Panel Copying: Completely resolved garbled non-UTF-8 archive filenames (GBK, GB18030, CP936, Shift-JIS) during compression and extraction (Fixes #74); integrated smart charset detection across ZIP browsing and extraction; added full support for copying selected entries directly from ZIP virtual panels
- Directory Sync Dialog Constraint & Robustness: Added sensible maximum width limits to the Synchronize Directories dialog, preventing tables from infinitely expanding horizontally during large comparison tasks (Fixes #76); strengthened comparison logic and test stability across ARM64 and x86_64 runners
- Accessibility (a11y) Upgrades & Contextual Terminal Action: Assigned accessible names to all toolbar actions and exposed full keyboard navigation; added a "System Terminal" action to file panel context menus to open terminal sessions directly in the active folder; updated all 31 language catalogs for refined theme controls and disk capacity summaries

### 2.3.8 (2026-10-20)

- File Panel Interaction Overhaul & Visual Hierarchy: Refactored row item delegates to render subtle translucent hover highlights with rounded pill borders, clearly separating mouse hover states from active file selections (Fixes #72); eliminated right-click delays and ensured right-clicking preserves current selections (Fixes #60); added "New File" (Shift+F4) and "New Folder" (F7) actions directly to the file panel context menu with full 31-language i18n support (Fixes #61, #70); automatically resets file selections upon changing directories to prevent accidental cross-folder file operations (Fixes #67)
- Command Line Terminal Execution & Seamless Path Navigation: Pressing Enter on any external shell command in the bottom command line automatically launches the default system terminal (Terminal.app / iTerm2) and executes it in the current panel directory (Fixes #63); entering directory paths or `cd` commands navigates directly with robust escaping for spaces and special characters
- Deep Memory Governance & System Status Ring Buffers: Enforced `WA_DeleteOnClose` and deterministic destruction across Universal Viewer (F3), Editor (F4), and all modal dialogs to eliminate memory accumulation across repeated lifecycles; migrated i18n dispatchers to `weakref.WeakMethod`, broke `DiskTreeNode` reference cycles, and introduced a QIcon LRU cache; upgraded System Status Panel and AtbSysBridge with 120-sample fixed ring buffers and in-place widget reuse to eliminate memory and stylesheet churn during high-frequency telemetry polling
- Toolbar Configuration Fix & Sandbox Guidance Alignment: Resolved an issue where newly added buttons in the middle toolbar could be overwritten and lost upon saving settings (Fixes #62); synchronized sandbox Full Disk Access (FDA) status bar indicators with Configuration menu actions

### 2.3.7 (2026-10-16)

- macOS Runtime Integrity & Application Exit Hardening: Fixed missing `os`, `sys`, and `traceback` imports across platform and logging modules, completely eliminating `NameError` risks during headless/standalone startup; streamlined `MainWindow.closeEvent` by removing redundant signal disconnections to ensure smooth application teardown without `SIGSEGV` segmentation faults
- Full Disk Access (FDA) Permission Onboarding Streamlining & Safe Fallback: Refined the onboarding dialog to automatically hide the redundant "Open Full Disk Access Settings" button when native drag-to-grant is supported, establishing a single clear entry point that updates to "Full Disk Access Granted ✓" once active; added a defensive fallback that dynamically reveals the settings button if the native Cocoa panel fails to present, ensuring uninterrupted permission granting in all environments

### 2.3.6 (2026-10-16)

- Nuitka Compiler Pinning & Apple Silicon (ARM64) Crash Elimination: Pinned Nuitka compiler to stable 4.2.2 across all CI workflows, preventing a critical PySide6/Shiboken compiler freelist corruption (`SIGSEGV / EXC_BAD_ACCESS`) introduced by Nuitka 4.3; integrated Qt signal/slot and compiler freelist integrity assertions into `smoke_test.py`; cleaned up build scripts to align local packaging options strictly with CI release pipelines
- macOS 15 Sequoia Window & System Tray Lifecycle Hardening: Overhauled window restoration, activation (`activate_app`), and Dock icon toggling to prevent invalid WindowServer `FocusWindowEvent` dispatches and crashes in headless/test environments; safely shut down and isolated pynput global hotkey listener threads to prevent background thread leaks and dangling `CGEventTap` hooks; added clipboard sanitization on teardown to eliminate static `QMimeData` destructor crashes
- Test Suite Stability & CI Pipeline Optimization: Resolved sporadic segmentation faults during pytest tray and window teardown, improving headless and offscreen test reliability; streamlined CI workflows to skip redundant package builds on documentation-only updates

### 2.3.5 (2026-10-15)

- Native Google Drive & Dropbox Cloud VFS Integration with OAuth 2.0: Introduced native virtual filesystem support for Google Drive (`gdrive://`) and Dropbox (`dropbox://`); added dedicated cloud storage profiles in Connection Manager with support for custom Client ID / Client Secret credentials and one-click browser-based OAuth 2.0 authorization; optimized direct stream copy fast-paths, quota TTL caching, and lazy directory listings with automatic connection profile saving
- Consolidated Keychain Security & Encrypted Credential Import/Export: Cleaned up Keychain service namespaces to eliminate repetitive startup authorization dialogs and ensure robust credential and license persistence; introduced encrypted export and import for saved connection credentials protected by user-defined passwords for secure cross-device migration, backed by full 31-language i18n
- Nuitka Runtime Hardening & Zip Streaming Improvements: Resolved edge-case launch crashes in standalone Nuitka builds and extended CI smoke test coverage across all packaged artifacts; refined the archive system's Zip streaming engine and fixed potential file panel wiping during cloud cache invalidation
- Sorting Concurrency Fix & Comprehensive Cloud Setup Guide: Resolved thread race conditions in folder-first and natural-case sorting tests (Fixes #58); expanded Chapter 6 of the User Guide with step-by-step instructions for Google Drive and Dropbox API setup, OAuth consent screen branding, and security guidance

### 2.3.4 (2026-10-13)

- Sandbox Permission Flow Overhaul & Unified Authorization Workflow: Restored and unified user Home (`~`) and `/Volumes` authorization into a streamlined single-button "Grant Permissions" onboarding workflow; introduced intelligent path promotion that automatically promotes subfolder access requests to the user home or volume root and persists security-scoped bookmarks, completely eliminating repetitive permission prompts under macOS App Store sandbox
- Dialog Standard Buttons i18n & 31-Language Catalog Deepening: Implemented `_GettextQtTranslator` to dynamically intercept and translate Qt standard buttons (Yes, No, OK, Cancel, Save, Discard, Apply, Close, Open, Reset) via gettext with automatic shortcut accelerator stripping (`&Yes` -> `Yes`); enhanced options pages (Toolbar, Hotkeys, Favorite Tabs, Auto Refresh), Connection Manager, and Queue Viewer with full dynamic UI retranslation (`retranslate_ui`); updated and compiled `.po`/`.mo` catalogs across all 31 supported languages, backed by new automated tests

### 2.3.3 (2026-10-10)

- Packer Overhaul, Separate Archiving & Streaming Progress: Added "Create separate archive for each selected file/folder" in ArchiveDialog to batch-compress multiple items individually; implemented streaming progress tracking for large files (≥1MB) across Zip, Tar, and 7z drivers; introduced thread-safe collision handling (Overwrite, Skip, Auto-Rename, Cancel), enhanced batch error tolerance for damaged items, robustly preserved symlinks, and synchronized 31-language translations
- System Tray Geometry & macOS Global Hotkey Hardening: Perfectly restored window position, dimensions, and maximized state when unhiding from the system tray; prevented tray context menus from inadvertently bringing the main window to foreground; revamped the macOS global wake/hide hotkey by normalizing Option dead-key characters via virtual keycodes and caching Darwin key contexts on the main thread to eliminate macOS Sequoia background assertions; added dynamic minimize-to-tray toggle in Preferences
- Drive Selector & Disk Capacity Tooltip Enhancements: Upgraded the drive selector bar with native volume labels and hardware disk icons; enriched tooltip previews with mount points, filesystem types, free disk space, and total capacity statistics
- Nuitka Build Integrity & Automated Bundle Smoke Tests: Added `--include-package=atbcmder` across all Nuitka build scripts to eliminate runtime `ModuleNotFoundError` caused by lazy-loaded UI dialogs; introduced headless `--smoke-test` verification integrated into DMG, Mac App Store PKG, and CI release workflows to guarantee rock-solid application bundles out of the box
- Multilingual Official Landing Page Launch: Launched the official modern product showcase website with a smart client-side language router (supporting English, Chinese, Japanese, Korean, and more) highlighting dual-pane productivity and native macOS craftsmanship

### 2.3.2 (2026-10-07)

- PySide6 Runtime Memory Optimization & Darwin Heap Compaction: Implemented lazy proxying for heavyweight secondary dialogs (`_make_lazy_dialog`) and PEP 562 module exports to dramatically reduce resident memory; wrapped Cocoa/PyObjC calls in `objc.autorelease_pool()` to eliminate memory accumulation during Finder color tag polling; added Darwin native heap compaction via `malloc_zone_pressure_relief` on idle timers and dialog closure; bounded ThumbnailManager to 4 worker threads with thread-safe decoding and multi-tier icon caching
- Restored Blinking Caret & Automatic Focus in F3 Viewer & F4 Editor: Fixed focus loss upon opening the file viewer or editor by automatically focusing the text buffer upon activation for immediate keyboard interaction; restored the visible 1px blinking caret, decoupled viewer and editor caret settings, enabled caret display by default, and added F6 shortcut (`cm_ShowCaret`) to toggle caret visibility in Universal Viewer
- Resource Lifecycle Hardening & Documentation Updates: Added `WA_DeleteOnClose` to Universal Viewer to guarantee complete widget destruction and memory reclamation on close; updated user guides and illustrative documentation assets

### 2.3.1 (2026-10-06)

- Sandbox Permissions Onboarding & Smart Window Repositioning: When requesting Full Disk Access (FDA) and opening System Settings, the onboarding dialog now automatically resizes and moves to the left portion of the screen, perfectly arranging side-by-side with macOS System Settings without overlap
- Clear Step-by-Step Guidance & Relaunch Reminders: Redesigned the permission prompt with an intuitive 1-2-3-4 walkthrough (locating or adding ATBCmder, toggling the switch, quitting and restarting the application) and clear reminders that FDA takes effect upon relaunch
- 31-Language Translation & Glossary Synchronization: Updated the localization glossary and recompiled message catalogs across all 31 supported languages, ensuring natural and helpful onboarding prompts worldwide

### 2.3.0 (2026-10-05)

- macOS Finder Native Color Tags & Live-Sync: Deeply integrated macOS Foundation APIs (`NSURLTagNamesKey`) and `NSWorkspace` to display native color dot tags in file panels; supports sorting by Finder native color order with 2-second viewport polling for real-time tag synchronization; includes customizable column visibility in Preferences and fully localized color labels
- Directory Synchronization Overhaul (`cm_SyncDirs`): Comprehensively re-engineered directory synchronization to eliminate UI state deadlocks and added a dedicated `SyncErrorsDialog`; introduced Swap Dirs, bidirectional deletion (`OP_DELETE_BOTH`), pipe `|` wildcard exclusion syntax, real-time selection statistics, CSV export, selection submenus, and Reveal in Finder with persistent window geometry and column widths
- Apple HIG Frosted Glass Interactive Tooltips: Built a centralized tooltip architecture featuring 80% translucent frosted glass cards matching native macOS Light and Dark appearances; unified tooltips across toolbars, splitters, breadcrumbs, Fx function keys, and dialogs with native macOS shortcut badges while suppressing duplicate Qt tooltips
- Native macOS Shortcut Conventions & Conflict Auto-Deduplication: Standardized shortcut descriptions and glyphs to match native macOS conventions, strictly synchronizing menu items and toolbar actions; eliminated historical 1-to-1 shortcut collisions with automatic deduplication across settings dialogs, command registry, and XML storage
- 100% 31-Language Translation Coverage & Demo Showcase Expansion: Reached 100% localization coverage and accurate plural forms across all 31 supported languages; enhanced Universal File Viewer (F3) with an "Open in Text Mode" fallback and added hover tooltips for truncated filenames; expanded demo scripts to showcase Quick Filter, Multi-Rename, transparent archive VFS, directory sync, and Tree View

### 2.2.0 (2026-10-03)

- Main Toolbar Ergonomics & Apple HIG Gradients: Enlarged main toolbar icons to 38px and increased toolbar height to 42px, eliminating squashed graphics and providing comfortable click targets on Retina displays; refreshed toolbar icons with vibrant Apple HIG colorful gradients and enhanced glyph contrast, harmonizing sizing between the main and middle toolbars
- Complete Preferences Wiring & Code Editor Settings: Fully wired up previously disconnected settings across the app (font zoom, archive compression defaults, editor auto-indent, viewer maximum text width); fixed tab size (`tab_size`) and indentation persistence in `CodeEditorWidget` via reliable runtime configuration loading
- Global Memory Management & Deep Performance Optimization: Overhauled icon and file metadata caching with lazy initialization for heavy UI components; hardened component lifecycles and weak-reference cleanups to eliminate memory leaks, keeping large directory browsing snappy and light
- Modal Dialog Hang Prevention & Tree View Focus Stability: Fixed potential modal hanging on closing `ArchiveDialog` and `SplitLinkDialog`; guaranteed active tab keyboard focus preservation during tree view mode toggling and folder hierarchy navigation
- Nuitka Packaging Optimizations & Crash Prevention: Streamlined standalone and DMG build pipelines to lower peak build memory and bundle size; refined compiler flags to eradicate runtime mock/unittest import crashes on packaged application releases

### 2.1.0 (2026-10-02)

- Apple HIG Redesign for Drive Bar & Tabs: Redesigned the drive bar and navigation buttons with Apple-style borderless controls; modernized the breadcrumb path bar and file tabs using Apple HIG borderless tonal surfaces for a polished, native macOS aesthetic
- Modern HIG Steppers, Capsule Tooltips & Pagination: Upgraded numeric controls (QSpinBox / QDoubleSpinBox) with macOS HIG integrated steppers; introduced Apple-style translucent capsule tooltips positioned intelligently beneath icons; adapted settings pagination and icons to HIG standards
- Dual-Panel Vertical Toolbar & Thumbnail Hierarchy Polish: Added a dedicated icon for "Target Equal Source (`cm_TargetEqualSource`)" to the vertical middle toolbar; fixed the z-order of thumbnail selection checkmark badges to ensure they render reliably atop images; fixed image editor status bar zoom button overflow
- Comprehensive 31-Language Localization & Terminology Review: Audited and refined UI terminology, tooltips, and dialog text across all 31 supported languages, eliminating missing keys and awkward phrasing for a natural native-speaker experience
- Tooling & Automation Infrastructure Improvements: Standardized localized catalog workflows (`atb-python-i18n`), streamlined token resolution for release helpers, and hardened test isolation for robust CI/CD delivery

### 2.0.0 (2026-09-28)

- 🎉 ATBCmder 2.0 Major Architecture Milestone: Celebrates the complete maturity of ATBCmder's modern dual-panel file manager architecture, bringing together the legendary keyboard-centric workflow of Double Commander with modern, native macOS performance and design
- Complete 31-Language Global Localization: Finished full, natural localization for the entire permission onboarding flow and native Drag-to-Grant panel across all 31 supported languages; recompiled all .mo catalogs and added automated multilingual regression tests for a seamless worldwide experience
- Revolutionary Drag-to-Grant Full Disk Access: Built on native Cocoa NonactivatingPanel to let users drag the application icon directly into System Settings without stealing window focus; the guidance dialog docks intelligently alongside System Settings with a smooth Quit & Reopen option, banishing disruptive auto-restart timers
- Dual-Panel Workflow & Human Interface Polish: Double-click the middle splitter or toolbar to instantly snap panels to a balanced 50:50 ratio with localized tooltips; the main toolbar features a sleek system status capsule by default with quick-close and context menu toggles; refined mixed folder sorting across all columns
- Modern Text Editor & High-Performance ATBSys Suite: The built-in editor now provides full macOS Home/End navigation with Smart Home line positioning; seamlessly integrated with our native Go `atbsys` system daemon for 64-bit precision junk cleaning and deep application remnant uninstallation

### 1.9.9 (2026-09-27)

- Drag-to-Grant Full Disk Access & Redesigned Onboarding: Introduced an innovative floating panel powered by native Cocoa NonactivatingPanel that allows dragging the app icon straight into System Settings without stealing window focus; the guidance dialog docks cleanly alongside System Settings and provides a smooth Quit & Reopen option upon FDA grant, completely eliminating jarring auto-restart timers
- Dual-Panel 5:5 Equalization & Middle Splitter Polish: Double-clicking the middle toolbar or splitter instantly equalizes panel widths (or heights in horizontal mode) to a 50:50 ratio with localized tooltips; resolved i18n subscriber leaks, fixed mouse cursor leaks, and refined viewer and dialog styling
- Editor Keyboard Ergonomics (Home/End & Smart Home): Built-in text editor now fully supports standard Home and End key navigation on macOS, featuring Smart Home behavior (toggling between the first non-whitespace character and column 0)
- Toolbar System Status Controls & Context Menu: Enabled the system status capsule on the main toolbar by default with a quick-dismiss (×) button, and introduced a right-click toolbar context menu to effortlessly toggle toolbar components and system monitors
- Mixed Folder Sorting Parity & Font Rendering Acceleration: Ensured `sort_folder_mode = mixed` truly interleaves files and folders across all column sorts with immediate runtime application; removed pseudo font declarations to eliminate macOS CoreText alias lookup overhead, unified tutorial card heights, and prevented native menu click-through

### 1.9.8 (2026-09-24)

- System Tools >2GB Metric Precision & Uninstaller Enhancements: Fixed 32-bit integer signal overflow and 64-bit precision loss when reporting cleanup byte counts exceeding 2 GB; added application installation date display and sorting in the Application Uninstaller
- Mac App Store Sandbox Compliance & Real Home Propagation: Propagated the real user home directory (`real_home`) across the `atbsys` bridge for accurate disk cleaning and remnant detection inside the App Sandbox; hardened elevation, terminal execution, and scripting interfaces for strict App Store review compliance
- Preferences Layout Controls & Directory Hotlist Fixes: Added main window layout toggle controls in General Preferences with live `MainWindow` and `ThemeManager` synchronization, and disabled the main toolbar system status capsule by default for a cleaner initial workspace; fixed empty dropdown menus and live language retranslation in Directory Hotlist settings
- Localization Terminology & Language Selector Polish: Standardized the Chinese translation of "Directory Hotlist" to "路径收藏夹" across all UI surfaces and enhanced the Preferences language selector with dual native-script and localized display names
- Keychain ACL Preservation & Stream Copy Reliability: Preserved existing macOS Keychain access control lists (ACLs) and eliminated redundant startup writes to prevent repeated Keychain authorization prompts; ensured deterministic `operation_completed` signal emission before thread completion in `StreamCopyWorker`

### 1.9.7 (2026-09-23)

- Runtime Settings Immediate Application (Hot Reload): All configuration settings across 7 major options pages (File Operations, Editor, Viewer, Quick Search & Filter, Tabs, File Panel Icons, and Sorting) now take effect immediately upon saving without restarting the application; added a configurable `sort_folder_mode` supporting Folders First, Files First, and Mixed sorting
- Directory Synchronization Safety & Parity: Comprehensive audit of Directory Synchronization (`cm_SyncDirs`) aligning behavior directly with classic Double Commander; strengthened bidirectional state validation and safety checks to eliminate asymmetric synchronization risks
- Smart Tooltips for Truncated Filenames with CJK Precision: Added intelligent hover/selection tooltips that appear exclusively when long filenames are truncated with ellipses, keeping UI clean for fully visible items; integrated high-precision CJK character width calculations to eliminate font metric discrepancies
- Dual-Panel Workflow & Interaction Polish: Right-click archive packing and unpacking defaults destination to the peer panel directory with default focus on the Start button; refined delete confirmation dialog button ordering and keyboard default; restored pointer cursors for middle toolbar action buttons
- Mac App Store Sandbox Real Home & FDA Hardening: Implemented the `real_home` resolution engine to resolve user home directories and Favorite Hotlists accurately under App Sandbox containers; fixed Full Disk Access (FDA) false alarms and auto-closed prompt dialogs upon authorization; migrated system CPU metrics to Mach host statistics for sandbox compliance

### 1.9.6 (2026-09-21)

- Image Editor Custom Size Resize Mode: Introduced a "Custom Size" mode to the image resize dialog, allowing direct pixel input for target width and height with an optional aspect ratio lock toggle, giving users precise control over image scaling
- Mac App Store Sandbox & Review Compliance Hardening: Strictly complied with Apple App Store Review Guidelines 2.4.5(v) and 2.5.2 by removing root directory authorization prompts in sandboxed builds and disabling process termination (SIGKILL/SIGTERM) UI and logic in MAS sandbox mode, eliminating sandbox violation and rejection risks
- Adaptive Toolbar Overflow & Diff Viewer Stability: Added automatic overflow handling to the main toolbar to gracefully collapse action buttons into a dropdown menu on smaller or compact screens; resolved an intermittent hang in the Diff Viewer test suite on macOS x86
- 30-Language Menu Localization: Completed comprehensive translations for the top-level "Tools" menu and related actions across all 30 supported languages
- UI Performance & CI/CD Pipeline Resilience: Cleaned up residual text panel widget references to significantly accelerate theme restyling and redraw speeds; updated CI/CD workflows to support parameterized ARM64 runner selection (self-hosted vs. cloud) with exponential backoff and retry for artifact transfers

### 1.9.5 (2026-09-19)

- Mac App Store Helper Executable Sandbox Inheritance: Added dedicated helper entitlements (`com.apple.security.app-sandbox` and `com.apple.security.inherit`) for all child executables (such as the `atbsys` system tools binary) in `Contents/MacOS/`, ensuring helper processes properly inherit the main application's App Sandbox container and security policies for full Mac App Store compliance
- Hardened Runtime Code Signing for DMG Helpers: Enabled Hardened Runtime (`--options runtime`) with appropriate entitlements for all auxiliary Mach-O executables in DMG distribution bundles, guaranteeing complete compliance with Apple Developer ID code-signing and notarization requirements
- Bundle Structure Cleanup & Packaging Integration Tests: Automated removal of redundant resource binary directories (`Contents/Resources/bin`) for cleaner bundle structure and App Store policy compliance; added automated packaging integration tests covering helper entitlements, Hardened Runtime, and multi-architecture build scripts

### 1.9.4 (2026-09-19)

- ATBSys System Tools & Maintenance Suite: Fully integrated native system utility suite, featuring a main toolbar System Status Capsule (real-time CPU, Memory, Disk, and Network bandwidth monitoring with right-click pause/interval/hide menu and settings toggle), full System Status Panel (hardware metrics and right-click process termination/kill management), Disk Space Analyzer (squarified Treemap hierarchy visualization, interactive column sorting, reveal/trash actions, and CSV/TXT report export), two-stage safe System Cleaner (scans and cleans user caches, application logs, leftover files, plus Homebrew, CocoaPods, and Docker categories with `~/.config/mole/whitelist` protection), and deep Application Uninstaller with remnant detection
- High-Performance Go Bridge Engine & Audit Logging: Powered by the lightweight, standalone Go native binary `atbsys`, communicating via asynchronous non-blocking QProcess; packaged as a Universal Binary with automated bundling and CI/CD pipeline integration; all cleaning and uninstallation operations are structured and recorded in audit logs in the ATBCmder log directory
- Interactive Onboarding Tutorial Expanded to 27 Steps: Upgraded beginner tutorial curriculum to include hands-on walkthroughs for system monitoring and maintenance tools; redesigned menu bar highlight positioning for language-agnostic precision on macOS native menu bars
- Comprehensive 30-Language Localization & Official Documentation: Complete translations for all ATBSys components, status capsule options, settings, and tutorial steps across all 30 supported languages; official English user guide enriched with Chapter 7: System Tools & Maintenance
- UI Polishing & Packaging Hardening: Widened the status bar capsule and network rate labels to eliminate text truncation during high-throughput network transfers; refined right-aligned capsule layout and menu shortcut unbinding synchronization; hardened dylib and binary injection logic for single-architecture and universal binaries on macOS 12 x86_64 runners

### 1.9.3 (2026-09-17)

- Universal Viewer .ini File Preview Support: Added native plain text preview support for `.ini` configuration files in the Universal Viewer (F3) and Quick View (`Ctrl+Q` / `⌘Q`), enabling instant inspection of configuration settings without opening external editors
- App Store Packaging & Frameworks Signing: Automated compilation and injection of `libATBLicenseKit.dylib` into `Contents/Frameworks/` for macOS Store and DMG release builds; added strict code-signing and notarization for dynamic libraries, enhanced runtime bundle discovery, and hardened universal binary merging
- Interactive Tutorial Engine Stability: Resolved step navigation timeouts in the favorite hotlist curriculum, properly cleared pending transition flags upon step switching, and disconnected dangling event signals to eliminate signal leaks during onboarding

### 1.9.2 (2026-09-17)

- StoreKit 2 Licensing & Trial System: Built-in Swift StoreKit 2 licensing and lifetime purchase system for the Mac App Store, featuring local calendar-day trial tracking, offline receipt validation, and purchase restoration; includes a toolbar license badge, paywall dialog, and universal binary support (macOS 12+, Apple Silicon & Intel)
- Embedded Shell Command Execution: Bottom command line bar now directly executes arbitrary shell commands in system terminal (Terminal / iTerm2); supports Tab path completion, and pure `cd` commands navigate active panels directly
- Directory Sync Overhaul & Inline Word Diff: Redesigned Directory Synchronization (`cm_SyncDirs`) with a classic 7-column grid and double-click Diff integration, eliminating asymmetric sync risks; Diff Viewer adds fine-grained inline word/character highlighting and First/Last diff navigation
- macOS Native Storage Alignment & VFS Hardening: Drive capacity and free space display aligned with macOS System Settings "Storage" specs; Network VFS (SFTP/FTP/Samba/WebDAV) strengthened with liveness checks, auto-reconnect, and FTPS; updated system tray to a minimalist monochrome template icon

### 1.9.1 (2026-09-14)

- Interactive Tutorial Quick Search Step: Expanded curriculum to 25 steps with interactive hands-on training for Quick Search & Filter (`⌘S` / `Ctrl+S`); added a Quick Search entry in the Commands menu and refined overlay cleanup during step transitions
- CI Packaging Pipeline & Dependency Hardening: Restored `ebooklib` in release build dependencies to ensure full EPUB preview capabilities; improved workspace cleanup steps to prevent permission conflicts

### 1.9.0 (2026-09-13)

- Newbie Interactive Tutorial System: Added a 24-step interactive onboarding curriculum for newcomers with a first-run welcome prompt (accessible anytime via "Help → Interactive Tutorial"); features a spotlight cutout overlay, adaptive floating cards, and dual menu-path + native shortcut prompts
- SFTP Network Security Upgrade: Replaced insecure host key auto-acceptance with a strict TOFU (Trust-On-First-Use) verification policy; connecting to unknown SFTP hosts now prompts with an interactive SHA-256 fingerprint confirmation dialog and safely persists keys to `~/.ssh/known_hosts` against MITM attacks
- macOS Native Shortcuts & Navigation Polish: Fixed `Command+Up` (parent folder navigation) and `Command+Shift+F1` (thumbnail view toggle) modifier handling, standardizing all key prompts with native macOS symbols (⌘, ⌥, ⌃, ⇧)
- Core Performance & Packaging Pipeline: Optimized semantic template matching and autocompletion responsiveness; restructured GitHub Actions automated release workflows with AppKit sandbox anti-crash protections

### 1.8.0 (2026-09-11)

- Universal Package: Support x86_64 and ARM universal packages
- Automated Build: Auto build package via GitHub Actions
- Smart File Associations & External Apps: Introduced standalone file associations management (`extassoc.xml`) allowing custom actions, external viewers, and editors per extension; integrated smart fallback to macOS LaunchServices and a dedicated "Open With" dialog
- Large File Transfer & 64-bit Overflow Protection: Completely eliminated 32-bit integer overflow issues in progress signals and text panel sliders, ensuring seamless transfers and accurate progress reporting for files larger than 2GB across mounted volumes and network shares
- Unified Viewer ESC Navigation Hierarchy: Standardized ESC key handling across all preview panels with tiered dismissals (search bar → active filter → fullscreen → close window), eliminating shortcut collisions and optimizing rapid file switching
- Real-Time Dynamic Localization: Bottom function key bar (F3–F8) now instantly retranslates upon language changes in Preferences without requiring an application restart

### 1.7.0 (2026-09-06)

- Universal File Viewer & Office Preview Suite: Added native preview engines for Excel spreadsheets (with lazy virtual loading), Word documents (with pagination and embedded image rendering), and PowerPoint presentations (slide card view); added previews for SQLite databases, Markdown (with TOC), Jupyter Notebooks, fonts, archives, audio, and EML; implemented instant streaming infinite scroll for large text files
- Side-by-Side File Diff Viewer: Built-in vimdiff-style two-way comparison tool with character-level diff highlighting, hunk copying, live editing, undo/redo, and encoding preservation
- Advanced File Search Engine: Rewritten search subsystem with default fuzzy substring matching, regex support, and a "Feed to Listbox" tab mode; batched UI throttling eliminates UI freezes on massive search results
- File Operations & UI Hardening: Fixed duplicate overwrite prompts during cross-device moves and transfer queue deadlocks; added file creation timestamps in properties dialog; enabled vertical middle toolbar by default and refined active pane visual indicators

### 1.6.2 (2026-09-03)

- Rubberband Drag Selection & Interaction: Added mouse rubberband drag selection in both File Table View and Thumbnail View, along with clicking empty space to deselect all
- Global Window Hotkey & Shortcut Input: Added a configurable global hotkey to show/hide the application window; fixed 4-key modifier combinations input in hotkey settings
- macOS Dock & Tray Restore Fix: Resolved an issue where clicking the Dock icon while minimized to the tray could fail to restore the main window or show a blank frame
- Core Hardening & Stability Improvements: Fixed potential lifecycle segfaults, strengthened VFS backends, and stabilized thread teardown and test suites

### 1.6.1 (2026-08-27)

- Comprehensive macOS UI/UX Overhaul: Grounded in Apple HIG with refined Light/Dark palettes, Finder-style pane highlight contrast, native card tooltips, and smooth segmented control animations
- Vector Icon Engine & Modern Widgets: Added an SF Symbols-inspired resolution-independent vector icon generator and modernized drive bars, breadcrumbs, and combo boxes
- Interaction & Layout Polish: Multi-rename redesigned with a 2-column layout and real-time name collision detection; Thumbnail View supports `Cmd + Wheel` dynamic zooming; unified empty state views added

### 1.6.0 (2026-08-27)

- Dual-Distribution Pipeline: Established separate automated build workflows tailored for Standalone DMG distribution and Mac App Store (MAS) release
- App Store Policy Compliance: Dynamically adjusts UI menus in MAS builds by removing external update check items to strictly meet Apple Review Guidelines, while preserving manual update checks in DMG builds
- `itms-services` Binary Patcher: Added an automated binary scanner and safe patcher to eliminate private protocol strings in compiled PySide6/Qt artifacts, ensuring flawless App Store Connect automated validation

### 1.5.6 (2026-08-22)

- Per-Tab Independent View Modes: Each tab now retains its own independent view layout (Flat View / Tree Mode), automatically synchronizing menu state and seamlessly persisting across session restores
- Smart File Open & System Fallback: Added a multi-layer file type detector (magic bytes / MIME / extension) to open supported media and documents in the built-in Viewer/Editor while cleanly falling back to OS default apps for unsupported files

### 1.5.5 (2026-08-21)

- Update Check Policy Optimization: Disabled automatic update checks on application startup by default; updates can now be checked manually via `Help` -> `Check for Updates...`, improving launch speed and offline privacy

### 1.5.4 (2026-08-21)

- Panel Focus & Selection Polish: Fixed lingering focus outlines on inactive split panels when switching panes; improved selection reset logic after moving files across panels to prevent accidental operations

### 1.5.3 (2026-08-19)

- Breadcrumb Cascading Submenu Polish: Precisely aligned the vertical position of cascading subfolder menus with the highlighted row, eliminating layout jumping and smoothing out deep folder traversal

### 1.5.2 (2026-08-19)

- Startup & Release Notes Fix: Fixed an issue where the Release Notes dialog repeatedly appeared on every app startup; enhanced `Config.get` default fallback handling to ensure release notes only prompt on initial launch or version upgrades

### 1.5.1 (2026-08-19)

- Multilingual Release Notes: Added 7 new mainstream language release notes (zh_TW, ja, ko, de, fr, ru, es) with dynamic discovery and 5-tier hierarchical fallback
- macOS Code Signing & Build Polish: Refactored packaging scripts with Mach-O binary targeting and timestamp retry wrappers, eliminating signing failures and throttling

### 1.5.0 (2026-08-17)

- Global Session Manager: Implemented application-level session persistence that seamlessly restores all left/right panel tabs, paths, view modes (Flat/Tree), panel ratios, and multi-monitor window bounds upon restart
- Settings Import/Export: Added 1-click ZIP export and import for all application configurations and data, streamlining cross-device migration
- Image Editor Enhancements: Added custom image resizing with aspect ratio locking and quick preset resolutions

### 1.4.9 (2026-08-17)

- Advanced Image Editor: Added image cropping, fine rotation, filter adjustments, and an OpenCV-powered AI watermark removal & inpainting module
- Enhanced Image Viewer: Full support for animated GIFs, zooming, panning, rotation, EXIF metadata extraction, and slideshow mode
- Spotlight Search Integration: Deeply integrated macOS native Spotlight for instant file searching and improved search result focus navigation

### 1.4.8 (2026-08-16)

- Comprehensive Localization (i18n): Full audit and translation completion across the UI, F3 Viewer, and F4 Editor, significantly improving the localization of media players and preview components
- F3 Viewer Optimizations: Improved external link handling and search wrap-around logic in the fallback EPUB reader (SimpleEpubPanel); streamlined the PDF viewer toolbar by removing redundant rotation buttons

### 1.4.7 (2026-08-16)

- Media Player Enhancements: significantly improved UI, UX, and stability of the built-in audio and video players
- Build System Refactoring: renamed `BUILD_EPUB` env flag to `BUILD_WEBENGINE` to accurately reflect packaging behavior
- Packaging Dependencies Fix: ensured `ebooklib` is always bundled in lightweight DMG builds for the fallback EPUB reader

### 1.4.6 (2026-08-16)

- Lightweight EPUB Reader (SimpleEpubPanel): Added a WebEngine-free fallback EPUB reader with chapter navigation and search, plus a `--epub-reader` CLI argument to override the default engine
- Cascading Breadcrumb Menus: Refactored the breadcrumb dropdown into a single-column scrollable layout with infinite cascading submenus, fixing overlap and mouse-grab lockup issues

### 1.4.5 (2026-08-15)

- Advanced Code Viewer (F3): Added syntax highlighting (Pygments), live file tailing, regex search, and line numbers
- Advanced Code Editor (F4): Added dynamic encoding/EOL conversion, atomic safe saving, smart indentation, and find/replace
- Global External Drag & Drop: Seamlessly drag files, including deeply nested archive contents, directly to macOS desktop or third-party editors (e.g. VSCode)

### 1.4.4 (2026-08-15)

- Typography Enhancements: increased font sizes across menus, buttons, tooltips, and settings dialog for better readability
- Resize Cursor Fixes: restored missing mouse resize cursors on window edges, splitters, and table column headers
- macOS UI Fixes: resolved black selection backgrounds on dropdown menus and fixed title overflows in group boxes

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
