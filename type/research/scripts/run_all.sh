#!/usr/bin/env sh
# scripts/run_all.sh - Three-Tier Empirical Replication Runner (POSIX wrapper).
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_CMD="python3"
if ! command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python"
fi

case "$1" in
    --dry-run|--sample|--full)
        "$PYTHON_CMD" "$SCRIPT_DIR/run_all.py" "$@"
        ;;
    *)
        echo "Usage: $0 {--dry-run|--sample|--full} [--seed <int>]" >&2
        echo "  --dry-run : Fast sanity check on toy data (< 60s)" >&2
        echo "  --sample  : Representative validation on 5-10% slice (< 15 min)" >&2
        echo "  --full    : Complete experimental benchmark replication" >&2
        exit 1
        ;;
esac

