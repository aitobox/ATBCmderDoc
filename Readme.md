# ATBCmder Help Docs


ATBCmder: The Ultimate Keyboard-Driven File Manager for macOS

Welcome to your new command center. If you are tired of clicking through endless folders, dragging files, and losing your flow, ATBCmder is built specifically for you. Designed for developers, system administrators, and VIM enthusiasts, ATBCmder resurrects the legendary dual-panel file management paradigm and supercharges it for the modern macOS environment.

Keep your hands on the keyboard and take absolute control of your data.

Core Features:

100% Keyboard-Native Workflow: Never reach for your mouse again. Navigate, copy, move, delete, and batch-rename files using classic, battle-tested hotkeys.

Local AI Semantic Search: Find files using natural language. Our privacy-first, on-device AI engine translates your intent into lightning-fast semantic filters without relying on cloud APIs.

Instant Quick Search: Simply start typing anywhere in the active panel to instantly lock your cursor onto the exact file you need.

Branch View (Flat Directory): Press a single key to flatten complex, deeply nested directory trees into a single list. Perfect for batch processing files scattered across multiple subfolders.

Built-In Geek PDF Reader: Read documentation without breaking your flow. Features a blazing-fast PDF viewer with Vim-style navigation (j/k), instant scaling, and distraction-free reading.

Asynchronous I/O Queue: Transfer massive directories without freezing your UI. Queue up heavy copy or move tasks and let them run silently in the background.

Stop managing files. Start commanding them.


## Download

- **Mac App Store**: [Download on Mac App Store](https://apps.apple.com/app/atbcmder/id6792398333)
- **Documentation & DMG**: [Download Page](https://cmder.aitobox.com/en/download/)


## Test

The repository includes a comprehensive CLI helper script, `test.sh`, to build, test, lint, and preview the documentation locally.

### Prerequisites

Ensure you have Python 3.12+ and [Zensical](https://github.com/zensical/zensical) installed:

```bash
pip install zensical
```

### Basic Usage

Build all language editions, start the local preview server, and automatically open your default browser:

```bash
./test.sh
```

By default, the preview server runs at `http://localhost:8000`.

### Command-Line Options

| Option | Description |
| :--- | :--- |
| `-b, --build-only` | Compile the static site to `site/` without launching the preview server |
| `-p, --port <PORT>` | Specify a custom port for the preview server (default: `8000`) |
| `--no-open` | Start the preview server without automatically opening the browser |
| `-s, --serve <LANG>` | Run Zensical's live development server with hot-reload for a single language (`en`, `zh`, `ja`, etc.) |
| `-l, --lint` | Check Markdown list blank-line spacing (MD032) across `docs/` |
| `--fix-lists` | Automatically format and fix Markdown list blank-line spacing in place |
| `--check-parity` | Verify 1:1 structural and heading translation parity against the English benchmark |
| `-h, --help` | Display the help message and exit |

### Common Examples

- **Build static files only (e.g., for CI/CD or local validation):**

  ```bash
  ./test.sh -b
  ```

- **Run preview server on a custom port without opening browser:**

  ```bash
  ./test.sh -p 8080 --no-open
  ```

- **Live development with hot-reloading for a specific language:**

  ```bash
  ./test.sh -s en    # English
  ./test.sh -s zh    # Simplified Chinese
  ```

- **Lint and format Markdown lists:**

  ```bash
  ./test.sh -l          # Check list formatting
  ./test.sh --fix-lists # Auto-fix formatting issues
  ```

- **Verify multilingual 1:1 translation parity:**

  ```bash
  ./test.sh --check-parity
  ```

