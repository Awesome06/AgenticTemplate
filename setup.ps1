# setup.ps1 - Hardened Git Hook Installer for Antigravity
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
Write-Host "Configuring Git hooks for Antigravity Agent..." -ForegroundColor Cyan

$hooksDir = ".git/hooks"
$gitHookPath = "$hooksDir/pre-commit"

# Ensure .git exists
if (-not (Test-Path ".git")) {
    Write-Error "Not a git repository. Run 'git init' before configuring hooks."
    exit 1
}

# Ensure .git/hooks directory exists
if (-not (Test-Path $hooksDir)) {
    New-Item -ItemType Directory -Path $hooksDir -Force | Out-Null
}

# POSIX-compliant trigger block with LF endings, -NoProfile, and exit code propagation
$agentTrigger = @"
# --- Antigravity Agent Hook Start ---
if command -v powershell.exe >/dev/null 2>&1; then
    powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File .agent/hooks/pre-commit.ps1 || exit 1
elif command -v pwsh >/dev/null 2>&1; then
    pwsh -NoProfile -NonInteractive -File .agent/hooks/pre-commit.ps1 || exit 1
elif [ -f .agent/hooks/pre-commit.sh ]; then
    sh .agent/hooks/pre-commit.sh || exit 1
fi
# --- Antigravity Agent Hook End ---
"@ -replace "`r`n", "`n"

if (Test-Path $gitHookPath) {
    # Read existing content using LF normalization
    $existing = (Get-Content $gitHookPath -Raw) -replace "`r`n", "`n"
    if ($existing -notmatch "Antigravity Agent Hook") {
        $updated = "$existing`n$agentTrigger`n"
        [System.IO.File]::WriteAllText((Convert-Path $gitHookPath), $updated, (New-Object System.Text.UTF8Encoding($false)))
        Write-Host "Appended Antigravity sync to existing pre-commit hook." -ForegroundColor Green
    } else {
        Write-Host "Antigravity sync is already configured in the pre-commit hook." -ForegroundColor Yellow
    }
} else {
    # Create new file starting with standard POSIX shebang and pure LF endings
    $newHook = "#!/bin/sh`n$agentTrigger`n"
    [System.IO.File]::WriteAllText((Join-Path (Get-Location) $gitHookPath), $newHook, (New-Object System.Text.UTF8Encoding($false)))
    Write-Host "Created new pre-commit hook with Antigravity sync (LF encoded)." -ForegroundColor Green
}

Write-Host "Workspace ready. Skills will validate with sub-second execution on every commit." -ForegroundColor Cyan
