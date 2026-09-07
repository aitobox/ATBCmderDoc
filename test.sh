#!/usr/bin/env bash

# test.sh - Local build and preview script for ATBCmder Documentation
# Compiles both English and Chinese documentation and runs a local preview server.

set -e

# Ensure we run from the project root directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ANSI text styles
BOLD='\033[1m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Disable color if terminal doesn't support it or NO_COLOR is set
if [ -n "$NO_COLOR" ] || [ ! -t 1 ]; then
    BOLD=''
    GREEN=''
    BLUE=''
    YELLOW=''
    CYAN=''
    RED=''
    NC=''
fi

# Default options
PORT=8000
BUILD_ONLY=false
AUTO_OPEN=true
SERVE_MODE=""

print_usage() {
    cat << EOF
${BOLD}Usage:${NC} ./test.sh [OPTIONS]

${BOLD}Options:${NC}
  -b, --build-only      Only compile the static site to site/, do not start preview server
  -p, --port <PORT>     Specify preview server port (default: 8000)
      --no-open         Do not automatically open default web browser
  -s, --serve <en|zh>   Run zensical live dev server for single language (hot reload)
  -l, --lint            Check Markdown lists blank spacing across docs/
      --fix-lists       Auto-format Markdown lists blank spacing in place
  -h, --help            Show this help message and exit

${BOLD}Examples:${NC}
  ./test.sh             # Compile both EN & ZH sites and start local preview
  ./test.sh -b          # Only compile static files to site/
  ./test.sh -l          # Check Markdown lists formatting
  ./test.sh --fix-lists # Auto-fix Markdown lists formatting
  ./test.sh -p 8080     # Preview on port 8080
  ./test.sh -s en       # Live edit English documentation
  ./test.sh -s zh       # Live edit Chinese documentation
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        -b|--build-only)
            BUILD_ONLY=true
            shift
            ;;
        -l|--lint)
            python3 scripts/format_markdown_lists.py --check
            exit $?
            ;;
        --fix-lists)
            python3 scripts/format_markdown_lists.py --fix
            exit $?
            ;;
        -p|--port)
            if [ -n "$2" ] && [[ "$2" =~ ^[0-9]+$ ]]; then
                PORT="$2"
                shift 2
            else
                echo -e "${RED}Error:${NC} --port requires a numeric argument."
                exit 1
            fi
            ;;
        --no-open)
            AUTO_OPEN=false
            shift
            ;;
        -s|--serve)
            if [ "$2" = "en" ] || [ "$2" = "zh" ]; then
                SERVE_MODE="$2"
                shift 2
            else
                echo -e "${RED}Error:${NC} --serve requires 'en' or 'zh'."
                exit 1
            fi
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            # If a standalone number is passed, treat as port
            if [[ "$1" =~ ^[0-9]+$ ]]; then
                PORT="$1"
                shift
            else
                echo -e "${RED}Unknown option:${NC} $1"
                print_usage
                exit 1
            fi
            ;;
    esac
done

# Detect zensical command
ZENSICAL_CMD=""
if command -v zensical &> /dev/null; then
    ZENSICAL_CMD="zensical"
elif command -v conda &> /dev/null && conda run -n ATBCmderDoc zensical --version &> /dev/null; then
    ZENSICAL_CMD="conda run -n ATBCmderDoc zensical"
else
    echo -e "${RED}Error:${NC} zensical command not found."
    echo -e "Please activate the conda environment or install zensical:"
    echo -e "  ${CYAN}conda activate ATBCmderDoc${NC}"
    echo -e "  or: ${CYAN}pip install zensical${NC}"
    exit 1
fi

# Detect python command for preview server
PYTHON_CMD=""
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
elif command -v conda &> /dev/null && conda run -n ATBCmderDoc python --version &> /dev/null; then
    PYTHON_CMD="conda run -n ATBCmderDoc python"
fi

# Handle live dev server mode for a single language (hot-reload)
if [ -n "$SERVE_MODE" ]; then
    CONFIG_FILE="zensical.${SERVE_MODE}.toml"
    if [ ! -f "$CONFIG_FILE" ]; then
        echo -e "${RED}Error:${NC} Config file $CONFIG_FILE not found."
        exit 1
    fi
    echo -e "${GREEN}==>${NC} ${BOLD}Starting Zensical Live Dev Server (${SERVE_MODE})...${NC}"
    exec $ZENSICAL_CMD serve -f "$CONFIG_FILE"
fi

# Step 1: Compile Static Site
echo -e "${GREEN}==>${NC} ${BOLD}Compiling ATBCmder Documentation (Bilingual)...${NC}"

# Check markdown list spacing before build
if [ -f "scripts/format_markdown_lists.py" ] && [ -n "$PYTHON_CMD" ]; then
    if ! $PYTHON_CMD scripts/format_markdown_lists.py --check > /dev/null 2>&1; then
        echo -e "${YELLOW}!${NC} ${BOLD}Notice:${NC} Some Markdown files have lists without blank line spacing."
        echo -e "  Run ${CYAN}./test.sh --fix-lists${NC} to automatically format them."
    fi
fi

# Build English Documentation
echo -e "${CYAN}-->${NC} Building English documentation (zensical.en.toml)..."
$ZENSICAL_CMD build -f zensical.en.toml

# Build Chinese Documentation
echo -e "${CYAN}-->${NC} Building Chinese documentation (zensical.zh.toml)..."
$ZENSICAL_CMD build -f zensical.zh.toml

# Copy Root Redirect and CNAME
echo -e "${CYAN}-->${NC} Setting up root redirect & CNAME metadata..."
if [ -f root_index.html ]; then
    cp root_index.html site/index.html
fi
if [ -f CNAME ]; then
    cp CNAME site/CNAME
fi

echo -e "${GREEN}✓${NC} ${BOLD}Static site compiled successfully into ${CYAN}site/${NC}!"

if [ "$BUILD_ONLY" = true ]; then
    echo -e "${BLUE}ℹ${NC} Build-only flag specified. Skipping preview server."
    exit 0
fi

# Step 2: Start Preview Server
if [ -z "$PYTHON_CMD" ]; then
    echo -e "${YELLOW}Warning:${NC} Python 3 not found. Cannot start preview server automatically."
    echo -e "You can view the static output directly in the ${CYAN}site/${NC} directory."
    exit 0
fi

# Find available port starting from requested PORT
ORIGINAL_PORT="$PORT"
ACTUAL_PORT=$($PYTHON_CMD -c "
import socket, sys
port = int(sys.argv[1])
while port < 65535:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('127.0.0.1', port))
            print(port)
            break
    except OSError:
        port += 1
" "$PORT" 2>/dev/null || true)

if [ -n "$ACTUAL_PORT" ] && [ "$ACTUAL_PORT" != "$ORIGINAL_PORT" ]; then
    echo -e "${YELLOW}!${NC} Port $ORIGINAL_PORT is in use, using port ${BOLD}$ACTUAL_PORT${NC} instead."
    PORT="$ACTUAL_PORT"
fi

SERVER_URL="http://localhost:${PORT}/"
EN_URL="http://localhost:${PORT}/en/"
ZH_URL="http://localhost:${PORT}/zh/"

echo ""
echo -e "${GREEN}======================================================${NC}"
echo -e "  ${BOLD}ATBCmder Documentation Preview Server Running${NC}"
echo -e "${GREEN}======================================================${NC}"
echo -e "  ${BOLD}Home URL (Redirects to /en/):${NC}  ${CYAN}${SERVER_URL}${NC}"
echo -e "  ${BOLD}English Documentation:${NC}        ${CYAN}${EN_URL}${NC}"
echo -e "  ${BOLD}Chinese Documentation:${NC}        ${CYAN}${ZH_URL}${NC}"
echo -e "${GREEN}======================================================${NC}"
echo -e "  Press ${BOLD}Ctrl + C${NC} to stop the server"
echo ""

cleanup() {
    echo ""
    echo -e "${BLUE}==>${NC} Preview server stopped."
    exit 0
}
trap cleanup SIGINT SIGTERM

# Automatically open browser in background
if [ "$AUTO_OPEN" = true ]; then
    (
        sleep 0.8
        if command -v open &> /dev/null; then
            open "$SERVER_URL" > /dev/null 2>&1
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$SERVER_URL" > /dev/null 2>&1
        fi
    ) &
fi

# Start HTTP server on site directory
$PYTHON_CMD -m http.server "$PORT" --directory site
