# scripts/check-race.ps1
# Automates race and concurrency sanitizer execution for team repositories.
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
Write-Host "[check-race] Executing concurrency sanitizers..." -ForegroundColor Cyan

$passed = $true

# 1. Go Race Detector
if (Test-Path "go.mod") {
    Write-Host "[check-race] Running 'go test -race ./...'..." -ForegroundColor Cyan
    & go test -race ./...
    if ($LASTEXITCODE -ne 0) { $passed = $false }
}

# 2. Rust ThreadSanitizer / Tests
if (Test-Path "Cargo.toml") {
    Write-Host "[check-race] Running 'cargo test'..." -ForegroundColor Cyan
    & cargo test
    if ($LASTEXITCODE -ne 0) { $passed = $false }
}

# 3. Python Asyncio & Strict Concurrency Tests
if ((Test-Path "pyproject.toml") -or (Test-Path "requirements.txt")) {
    Write-Host "[check-race] Running pytest concurrency checks..." -ForegroundColor Cyan
    if (Get-Command uv -ErrorAction SilentlyContinue) {
        & uv run pytest -v
    } elseif (Get-Command pytest -ErrorAction SilentlyContinue) {
        & pytest -v
    }
    if ($LASTEXITCODE -ne 0) { $passed = $false }
}

# 4. Node.js Concurrency / Test Suite
if (Test-Path "package.json") {
    Write-Host "[check-race] Running package test suite..." -ForegroundColor Cyan
    & npm test
    if ($LASTEXITCODE -ne 0) { $passed = $false }
}

if (-not $passed) {
    Write-Error "[check-race] Race sanitizer or concurrency test failed. Fix data races before pushing."
    exit 1
}

Write-Host "[check-race] All concurrency checks passed cleanly." -ForegroundColor Green
exit 0

