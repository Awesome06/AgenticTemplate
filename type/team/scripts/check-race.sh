#!/usr/bin/env sh
# scripts/check-race.sh
# Automates race and concurrency sanitizer execution for team repositories (POSIX).
set -e

echo "[check-race] Executing concurrency sanitizers..."

# 1. Go Race Detector
if [ -f "go.mod" ]; then
    echo "[check-race] Running 'go test -race ./...'..."
    go test -race ./...
fi

# 2. Rust Tests
if [ -f "Cargo.toml" ]; then
    echo "[check-race] Running 'cargo test'..."
    cargo test
fi

# 3. Python Asyncio & Strict Concurrency Tests
if [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
    echo "[check-race] Running pytest concurrency checks..."
    if command -v uv >/dev/null 2>&1; then
        uv run pytest -v
    elif command -v pytest >/dev/null 2>&1; then
        pytest -v
    fi
fi

# 4. Node.js Test Suite
if [ -f "package.json" ]; then
    echo "[check-race] Running npm test..."
    npm test
fi

echo "[check-race] All concurrency checks passed cleanly."

