# Chapter 7: System Tools & Maintenance

A professional file manager does not operate in a vacuum—it is the central nerve center for your storage, memory, and operating system resources. While orthodox dual-panel file management excels at organizing, moving, and synchronizing directory hierarchies, power users, developers, and system administrators frequently face system-level challenges: pinpointing which hidden directory silently consumed 50 GB of disk space, identifying a runaway background process thrashing CPU cores, clearing gigabytes of abandoned developer caches and build artifacts, and completely uninstalling legacy macOS applications without leaving orphaned preference files, launch daemons, or application support folders scattered throughout `~/Library/`.

ATBCmder integrates four specialized system maintenance and diagnostic tools directly into the **Tools** menu. Powered by an asynchronous native monitoring daemon, these tools operate seamlessly alongside your file panels without locking the user interface or requiring heavy, ad-laden third-party utility applications.

---

## 1. Visual Quickstart: System Tools & Status HUD

ATBCmder divides system maintenance into four core operational instruments accompanied by an always-visible toolbar monitoring capsule:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       ATBCMDER SYSTEM TOOLS SUITE                                      │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                                        │
│  [1] Status Capsule HUD & Popover       [2] System Status & Diagnostics (⌘⇧M)                         │
│      • Real-time CPU, RAM, and Network      • Per-core utilization bars, full process table            │
│      • Color-coded threshold styling        • Search/filter processes, send SIGTERM/SIGKILL            │
│      • Click for multi-metric popover       • Disk filesystem capacity and network interface graphs   │
│                                                                                                        │
│  [3] Disk Usage Analyzer (⌘⇧D)          [4] System Cleaner (⌘⇧C)                                      │
│      • Multi-threaded directory scanner     • Two-stage safe cleaner: scan first, review, then clean   │
│      • Interactive squarified treemap       • 6 categories: caches, logs, Xcode, dev tools, trash      │
│      • Breadcrumb drill-down navigation     • 3 risk levels (Safe, Warning, Danger) + Whitelist        │
│                                                                                                        │
│  [5] Application Uninstaller (⌘⇧U)                                                                     │
│      • Complete removal of .app bundles and deep remnant files                                         │
│      • Cleans Application Support, Preferences, Caches, LaunchAgents, and Containers                   │
│      • Dual mode: Complete Uninstall vs. Remnants Only (clean up previously deleted apps)              │
│                                                                                                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### Dual-Matrix System Tools Shortcut Matrix

| Tool / Action | macOS Shortcut | Classic Commander Key | Command ID | Menu Location |
| :--- | :--- | :--- | :--- | :--- |
| **System Status Panel** | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` | **Tools ➔ System Status...** |
| **Disk Usage Analyzer** | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` | **Tools ➔ Disk Usage Analyzer...** |
| **System Cleaner** | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` | **Tools ➔ System Cleaner...** |
| **Application Uninstaller** | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` | **Tools ➔ Uninstall Application...** |
| **Toggle Status Capsule** | Preferences ➔ General | — | *(Settings)* | **Configuration ➔ Options ➔ General** |

---

## 2. Toolbar Status Capsule HUD & Live Popover

ATBCmder features an integrated **System Status Capsule** embedded directly on the right side of the Main Toolbar. This provides immediate, peripheral awareness of system health without requiring you to switch to Activity Monitor or open a separate terminal.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ [Left Panel Tabs]                   [Right Panel Tabs]          [ CPU 18% | RAM 44% | ↓1.2M ↑340K ]│
└───────────────────────────────────────────────────────────────────────────┬────────────┘
                                                                            │ Click Capsule
                                                                            ▼
                                                ┌───────────────────────────────────────┐
                                                │ SYSTEM METRICS SUMMARY                │
                                                ├───────────────────────────────────────┤
                                                │ CPU Usage:     [████░░░░░░░░░░]   18% │
                                                │ Memory:        [████████░░░░░░]   44% │
                                                │ GPU Load:      [██░░░░░░░░░░░░]   12% │
                                                │ Battery:       [████████████░░]   88% │
                                                ├───────────────────────────────────────┤
                                                │ Storage:                              │
                                                │  Macintosh HD:  312.4 GB / 994.6 GB   │
                                                │  External SSD:  842.1 GB / 2.0 TB     │
                                                ├───────────────────────────────────────┤
                                                │ Top Processes:                        │
                                                │  • ATBCmder         PID: 54102  CPU: 2%│
                                                │  • WindowServer     PID: 284    CPU: 8%│
                                                │  • Xcode            PID: 88120  CPU: 4%│
                                                ├───────────────────────────────────────┤
                                                │ [ Open Full System Monitor (⌘⇧M) ➔ ] │
                                                └───────────────────────────────────────┘
```

### 2.1 Capsule Components & Visual Styling

The status capsule (`320px` wide) displays three real-time telemetry metrics updated once per second:

1. **CPU Utilization**: Live aggregate processor usage percentage with dynamic color coding:
   - **Normal (< 75%)**: Accent blue / theme foreground.
   - **Elevated (75% – 90%)**: Warning orange.
   - **Critical (> 90%)**: Alert red.
2. **Memory Utilization (RAM)**: Current active and wired memory pressure expressed as a percentage of physical RAM.
3. **Network Throughput**: Real-time aggregate upload and download speeds across all active network adapters formatted compactly (e.g. `↓2.4 MB/s ↑512 KB/s`).

### 2.2 Interactive Popover (`StatusPopup`)

Clicking anywhere on the status capsule opens a non-modal floating **Status Popover**:

- **Hardware Telemetry**: View combined percentages for CPU, Memory, GPU, and Battery status (including charge percentage and charging state).
- **Filesystem Mounts**: Lists all mounted local APFS containers and external drives with free space and total capacity bars.
- **Top 5 Processes**: Highlights the five highest resource-consuming processes by CPU percentage and memory footprint.
- **Deep Dive Button**: Click **"Open Full System Monitor"** (or press `⌘⇧M`) to launch the comprehensive diagnostics window.

### 2.3 Configuring Capsule Visibility

If you prefer a distraction-free toolbar with only file navigation controls:

1. Open **Preferences** (`⌘,` / **Configuration ➔ Options...**).
2. Select **General** in the left sidebar.
3. Under **Display & Layout**, toggle the checkbox:
   `[X] Show system status capsule on toolbar`
4. Click **Apply** or **OK**. The capsule will immediately appear or disappear from the main toolbar.

---

## 3. System Status & Diagnostics (`cm_SystemStatus` / `⌘⇧M`)

Pressing **`⌘⇧M`** (or **`Ctrl+Shift+M`**) opens the full **System Status Panel**. This utility serves as an integrated diagnostic console tailored for system administrators, developers, and performance troubleshooting.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             SYSTEM STATUS & DIAGNOSTICS                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CPU USAGE: Apple M3 Max (14 Cores)                                                     │
│ Core 01: [██████░░░░] 60%    Core 05: [██░░░░░░░░] 20%    Core 09: [███░░░░░░░] 30%    │
│ Core 02: [████░░░░░░] 40%    Core 06: [████░░░░░░] 42%    Core 10: [█░░░░░░░░░] 10%    │
│ Core 03: [████████░░] 80%    Core 07: [█░░░░░░░░░] 12%    Core 11: [░░░░░░░░░░]  5%    │
│ Core 04: [███░░░░░░░] 30%    Core 08: [██░░░░░░░░] 18%    Core 12: [░░░░░░░░░░]  4%    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ MEMORY: Total 36.0 GB  |  Used: 16.2 GB (45%)  |  App: 9.4 GB  |  Wired: 4.1 GB       │
│ SWAP:   Total 2.0 GB   |  Used: 0 MB (0%)                                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ PROCESS LIST                                 Filter: [ node                     ] [x]  │
│ PID      Name             User           CPU %       Memory      Threads    Action     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ 72841    node (dev-srv)   brain          48.2%       612.4 MB    28         [ Kill ✕ ] │
│ 72910    node (esbuild)   brain          12.1%       184.2 MB    14         [ Kill ✕ ] │
│ 73104    node (lsp)       brain           1.4%        98.5 MB     8         [ Kill ✕ ] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Update Interval: [ 1.0s ▼ ]       [ Pause Monitoring ]              [ Close (Esc) ]    │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Diagnostic Features & Metric Sections

1. **Multi-Core Processor Monitor**:
   - Visualizes overall system load and breakdown across individual Performance and Efficiency cores.
   - Per-core progress meters highlight core saturation during multi-threaded compiles or renders.
2. **Memory Breakdown & Swap Pressure**:
   - Categorizes physical memory allocation into App Memory, Wired Memory, Compressed Memory, and Cached Files.
   - Monitors virtual swap usage to help identify when memory leaks are causing disk paging.
3. **Storage & Mounts Overview**:
   - Real-time disk read/write throughput metrics alongside mount point capacity data.
4. **Interactive Process Manager**:
   - Real-time sortable table containing all running system and user tasks.
   - **Search & Filter**: Type any process name or PID into the search box to filter results instantaneously.
   - **Process Termination**:
     - Click **Kill** or select a process and press `Delete`.
     - Prompts with a confirmation dialog offering **Terminate (`SIGTERM`)** for graceful shutdown or **Force Kill (`SIGKILL`)** for unresponsive tasks.

---

## 4. Disk Usage Analyzer (`cm_DiskUsageAnalyzer` / `⌘⇧D`)

When a solid-state drive begins running out of free space, finding where gigabytes of data are hidden can be painfully slow. Standard Finder file lists do not calculate folder sizes automatically, and manual inspection requires tedious drilling through nested hierarchies.

The **Disk Usage Analyzer** (`cm_DiskUsageAnalyzer`, hotkey **`⌘⇧D`** / **`Ctrl+Shift+D`**) scans entire directory trees asynchronously using a multi-threaded scanner and visualizes your storage using both a traditional hierarchical tree list and an interactive **Squarified Treemap**.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DISK USAGE ANALYZER: /Users/brainzhang                                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Path: /Users/brainzhang ➔ Developer ➔ Projects                                        │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ DIRECTORY HIERARCHY                  │ INTERACTIVE SQUARIFIED TREEMAP                  │
│ Folder Name      Size       Percent  │ ┌───────────────────────────┬─────────────────┐ │
│ ──────────────────────────────────── │ │                           │ node_modules    │ │
│ ▼ Developer      142.6 GB   58.2%    │ │ target/debug              │ 28.4 GB         │ │
│   ► Projects     118.2 GB   48.2%    │ │ 64.2 GB                   │ (Rust build)    │ │
│   ► Caches        24.4 GB   10.0%    │ │                           ├─────────────────┤ │
│ ▼ Library         64.2 GB   26.2%    │ │                           │ DerivedData     │ │
│   ► Caches        38.1 GB   15.5%    │ │                           │ 18.2 GB         │ │
│   ► App Support   22.4 GB    9.1%    │ ├───────────────────────────┴─────────────────┤ │
│ ► Downloads       24.1 GB    9.8%    │ │ Video Footage (4K Prores)                   │ │
│ ► Pictures        14.2 GB    5.8%    │ │ 31.8 GB                                     │ │
├──────────────────────────────────────┴─┴───────────────────────────────────────────────┤
│ [ Zoom Out (..) ]  [ Reveal in Dual Panel ]  [ Move to Trash (⌘⌫) ]  [ Export CSV... ]  │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Key Architecture & Capabilities

- **Asynchronous Multi-Threaded Scanning**: Scans hundreds of thousands of files across APFS containers without freezing ATBCmder's main interface. A progress bar displays directories scanned per second.
- **Squarified Treemap Visualization**:
  - Folders and files are represented as nested rectangular blocks whose 2D surface area is strictly proportional to their size on disk.
  - Colors automatically reflect directory depth, making massive storage consumers instantly identifiable at a glance.
- **Bi-directional Synchronization**:
  - Selecting an item in the directory tree highlights its corresponding block in the treemap.
  - Clicking any rectangle in the treemap highlights the row in the tree view and displays the full file path and exact byte size.

### 4.2 Interactive Navigation & Workflows

1. **Drill Down**: Double-click any folder row or treemap block to zoom into that subdirectory and re-calculate the view relative to the new root.
2. **Zoom Out**: Click the **Zoom Out** button in the toolbar or click any segment in the breadcrumb bar at the top to return to parent directories.
3. **Inspect in Dual Panels**: Click **Reveal in Dual Panel** to instantly navigate your active ATBCmder file panel to the selected directory.
4. **Instant Cleanup**: Select any large obsolete folder or file and press **`⌘⌫`** (or click **Move to Trash**). The item is safely sent to macOS Trash, and the scan tree updates automatically.
5. **Export Storage Reports**: Click **Export** to generate comprehensive disk usage audits formatted as either structured CSV or plain text summaries for storage planning.

---

## 5. System Cleaner (`cm_CleanSystem` / `⌘⇧C`)

Over months of daily use, macOS accumulates gigabytes of temporary data: stale application caches, Xcode build artifacts, package manager downloads, orphaned diagnostic logs, and browser caches. While some caches accelerate workflows, obsolete items waste valuable high-speed SSD storage.

The **System Cleaner** (`cm_CleanSystem`, hotkey **`⌘⇧C`** / **`Ctrl+Shift+C`**) provides a deterministic, two-stage system cleaner designed with enterprise safety guarantees.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              SYSTEM CLEANER: DRY RUN AUDIT                             │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Scan System ]  Scanned: 48,192 items in 2.1s        Total Reclaimable: 34.8 GB        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ CATEGORY                          ITEMS       SIZE        RISK LEVEL     SELECTION     │
│ ────────────────────────────────────────────────────────────────────────────────────── │
│ [X] Application Caches            12,410      14.2 GB     Safe (Green)   [ Select All] │
│ [X] System & User Logs             4,218       1.8 GB     Safe (Green)   [ Select All] │
│ [X] Xcode Derived Data             8,940      12.4 GB     Warning (Org)  [ Select All] │
│ [ ] Homebrew & CocoaPods Caches    1,420       3.6 GB     Warning (Org)  [ Select All] │
│ [ ] Web Browser Caches            21,200       2.8 GB     Safe (Green)   [ Select All] │
│ [ ] Trash Bin Container                4       8.2 GB     Danger (Red)   [ Unselected] │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Selected for Cleanup: 28.4 GB across 25,568 files                                     │
│ Whitelist: ~/.config/atbsys/whitelist (4 rules active)                                │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Whitelist Editor... ]      [ Export Log ]       [ Clean Selected Items (28.4 GB) ]   │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 The Two-Stage Safety Architecture

Unlike reckless "one-click cleaners" that delete files silently in the background, ATBCmder enforces a strict **Two-Stage Safety Protocol**:

1. **Stage 1: Dry-Run Scan & Assessment**:
   - The cleaner performs a read-only survey across standardized system locations.
   - Calculates exact file counts and byte sizes without modifying or deleting a single byte.
   - Groups results into transparent categories with explicit risk ratings.
2. **Stage 2: User-Reviewed Selective Deletion**:
   - You review the categorized list and check or uncheck individual items or entire categories.
   - Clicking **"Clean Selected Items"** executes deletion only on explicitly checked targets.
   - Every deletion event is written to an atomic audit log at `~/Library/Preferences/atbcmder/operations.log`.

### 5.2 Six Core Cleanup Domains

| Category | Typical Location | Risk Level | Description |
| :--- | :--- | :---: | :--- |
| **Application Caches** | `~/Library/Caches/` | **Safe** | Stale caches generated by desktop applications that are recreated automatically when needed. |
| **System & User Logs** | `~/Library/Logs/`, `/var/log/` | **Safe** | Old crash logs, diagnostic dumps, and software update logs no longer needed for troubleshooting. |
| **Browser Caches** | Safari, Chrome, Edge, Firefox | **Safe** | Cached web pages, media buffers, and script artifacts across installed desktop browsers. |
| **Xcode Derived Data** | `~/Library/Developer/Xcode/DerivedData` | **Warning** | Intermediary object files, module caches, and index data from past Apple developer builds. |
| **Package Manager Caches** | Homebrew, CocoaPods, NPM, Yarn | **Warning** | Downloaded tarballs, formula archives, and package cache directories. |
| **Trash Bin** | `~/.Trash`, `.Trashes` | **Danger** | Items previously moved to the macOS Trash that have not yet been permanently emptied. |

### 5.3 Risk Tiers & Safety Whitelist

- 🟢 **Safe (Green)**: Temporary caches and discarded metadata that can be removed with zero configuration loss or workflow disruption.
- 🟡 **Warning (Orange)**: Developer artifacts or package caches. Deleting them is safe, but subsequent project compilation or package downloads will take longer as items are refetched.
- 🔴 **Danger (Red)**: Contains files requiring explicit confirmation (e.g. permanently purging the Trash Bin).
- **Custom Whitelist Rules**:
  - Add specific paths, extensions, or folder names that ATBCmder must **never** touch to `~/.config/atbsys/whitelist`.
  - Built-in protective rules automatically prevent scanning critical macOS operating system files, user keychain directories, and cloud storage offline sync folders.

---

## 6. Application Uninstaller (`cm_UninstallApp` / `⌘⇧U`)

On macOS, dragging an application from `/Applications` to the Trash only removes the `.app` bundle itself. Modern applications frequently scatter hundreds of auxiliary files across your drive: preferences plists, application support databases, background launch agents, container sandboxes, and cached media. Over time, these orphaned leftovers consume gigabytes of storage and can leave unneeded background processes running at login.

The **Application Uninstaller** (`cm_UninstallApp`, hotkey **`⌘⇧U`** / **`Ctrl+Shift+U`**) provides deep dependency scanning to completely eradicate applications and their associated remnants.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             APPLICATION DEEP UNINSTALLER                               │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Filter: Docker                     ]  Found: 142 Applications (Total: 48.2 GB)       │
├──────────────────────────────────────┬─────────────────────────────────────────────────┤
│ INSTALLED APPLICATIONS               │ ASSOCIATED REMNANTS & SUPPORT FILES             │
│ App Name          Version    Size    │ File Path / Component               Size        │
│ ──────────────────────────────────── │ ─────────────────────────────────────────────── │
│ [X] Docker.app    4.28.0     1.8 GB  │ [X] /Applications/Docker.app        1.8 GB (.app│
│ [ ] Figma.app     116.15     240 MB  │ [X] ~/Library/Application Support/Docker 14.2 GB│
│ [ ] Slack.app     4.36.0     310 MB  │ [X] ~/Library/Caches/com.docker.docker   2.1 GB │
│ [ ] Visual Studio 1.87.0     450 MB  │ [X] ~/Library/Preferences/com.docker...  12 KB  │
│ [ ] Xcode.app     15.3      12.4 GB  │ [X] ~/Library/LaunchAgents/com.docker...  4 KB  │
│                                      │ [X] ~/Library/Containers/com.docker...  380 MB  │
├──────────────────────────────────────┴─────────────────────────────────────────────────┤
│ Mode: (•) Complete Uninstall (.app + remnants)     ( ) Remnants Only (clean orphans)   │
│ Total Selected for Removal: 18.48 GB across 6 items                                    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ [ Refresh Applications ]       [ Cancel ]              [ Uninstall Application (18.5G)│
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Remnant Discovery Locations

When scanning for application components, ATBCmder searches the following standard macOS subsystem locations using exact bundle identifier matching:

1. **Application Bundle**: `/Applications/<Name>.app` and `~/Applications/<Name>.app`.
2. **Application Support**: `~/Library/Application Support/<Name>` and `<BundleID>`.
3. **Application Caches**: `~/Library/Caches/<BundleID>`.
4. **Preferences & Defaults**: `~/Library/Preferences/<BundleID>.plist`.
5. **Saved State**: `~/Library/Saved Application State/<BundleID>.savedState`.
6. **Launch Daemons & Agents**: `~/Library/LaunchAgents/<BundleID>.plist`.
7. **Sandbox Containers**: `~/Library/Containers/<BundleID>/` and `~/Library/Group Containers/`.
8. **Application Logs**: `~/Library/Logs/<Name>/`.

### 6.2 Dual Operational Modes

- **Complete Uninstall (Default)**:
  - Intended for removing an installed application currently present on your Mac.
  - Deletes both the executable `.app` bundle from `/Applications` and all associated auxiliary support files in a single atomic action.
- **Remnants Only**:
  - Intended for cleaning up after applications that were previously deleted manually via Finder or third-party tools.
  - Scans `~/Library/` for orphaned support folders whose parent `.app` bundle is no longer present on the system.

### 6.3 Apple System Integrity & Safety Guardrails

To prevent accidental system destabilization:

- **System App Protection**: Built-in macOS system applications (Safari, Finder, Preview, Music, System Settings, etc.) are protected with a read-only lock icon and cannot be uninstalled.
- **Running Process Detection**: If an application or its helper daemon is currently active, ATBCmder prompts you to quit the application gracefully before uninstallation proceeds.
- **Trash-First Protocol**: All uninstalled items are moved to the macOS Trash by default rather than immediately unlinked from disk, allowing full recovery if needed.

---

## 7. System & Maintenance Alerts

> [!NOTE]
> **Minimal System Resource Overhead**  
> The background status monitor daemon is engineered in native compiled code and runs on a 1.0-second polling interval. It consumes under 0.1% CPU during active file browsing and automatically suspends polling when ATBCmder is minimized or hidden.

> [!TIP]
> **Pairing Disk Usage Analyzer with Dual-Panel Flat Branch View**  
> If the Disk Usage Analyzer flags a directory containing thousands of scattered temporary files, select that directory and press **Reveal in Dual Panel**. Then press **`Cmd+B`** (`cm_DirBranch`) to flatten the entire nested tree into a single listbox where you can sort, select, and batch delete items with keyboard precision.

> [!IMPORTANT]
> **Always Review Cleaner Selections Before Confirming**  
> While the System Cleaner designates caches as **Safe (Green)**, some developer tools (such as Xcode DerivedData or local Docker volumes) may take time to recompile or refetch upon next project launch. Review checked categories to ensure you are not clearing caches for an active sprint.

> [!CAUTION]
> **Force Killing System Processes (`SIGKILL`)**  
> In the System Status Process Manager, sending `SIGKILL` (Force Kill) immediately stops the target process without allowing it to flush open file buffers or save document states. Always attempt a graceful `SIGTERM` termination first.

> [!WARNING]
> **App Sandbox Container Removal**  
> When uninstalling Mac App Store applications, auxiliary files stored under `~/Library/Containers/<BundleID>` often include sandboxed document databases. Ensure you have exported any essential local project files before confirming container deletion.

---

## 8. Master Dual-Matrix System Tools Reference Table

| Category | Action Description | macOS Shortcut | Classic Commander Key | Command ID |
| :--- | :--- | :--- | :--- | :--- |
| **System Monitor** | Open Full System Diagnostics Panel | `Cmd+Shift+M` / `⌘⇧M` | `Ctrl+Shift+M` | `cm_SystemStatus` |
| **System Monitor** | Open Lightweight Status Popover | Click Toolbar Capsule | — | *(UI Action)* |
| **System Monitor** | Filter Process Manager List | `Cmd+F` (in Panel) | `F7` | — |
| **System Monitor** | Terminate Process (`SIGTERM`) | `Delete` / `⌫` | `Delete` | — |
| **System Monitor** | Force Kill Process (`SIGKILL`) | `Shift+Delete` / `⇧⌫`| `Shift+Delete` | — |
| **Disk Analyzer** | Open Disk Usage Analyzer Dialog | `Cmd+Shift+D` / `⌘⇧D` | `Ctrl+Shift+D` | `cm_DiskUsageAnalyzer` |
| **Disk Analyzer** | Drill Down into Selected Folder | `Enter` / `Return` | `Enter` | — |
| **Disk Analyzer** | Zoom Out to Parent Directory | `Backspace` / `⌫` | `Backspace` | — |
| **Disk Analyzer** | Move Highlighted Item to Trash | `Cmd+Delete` / `⌘⌫` | `F8` / `Delete` | — |
| **Disk Analyzer** | Reveal Selected Item in Dual Panel | `Cmd+Return` / `⌘⏎` | `Ctrl+Enter` | — |
| **System Cleaner** | Open Safe System Cleaner Dialog | `Cmd+Shift+C` / `⌘⇧C` | `Ctrl+Shift+C` | `cm_CleanSystem` |
| **System Cleaner** | Run Read-Only Dry Run Scan | `Cmd+R` / `⌘R` | `Ctrl+R` | — |
| **System Cleaner** | Toggle Category Selection | `Space` | `Space` | — |
| **App Uninstaller**| Open Application Uninstaller | `Cmd+Shift+U` / `⌘⇧U` | `Ctrl+Shift+U` | `cm_UninstallApp` |
| **App Uninstaller**| Switch to Remnants Only Mode | `Cmd+2` / `⌘2` | `Alt+2` | — |
| **Preferences** | Toggle Toolbar Status Capsule HUD| Preferences ➔ General| — | *(Config)* |

---

<div align="center">
  <p>Ready to customize hotkeys, panel views, and application behavior?</p>
  <p><strong><a href="preferences_and_customization.md">Proceed to Chapter 8: Preferences & Customization &rarr;</a></strong></p>
</div>
