# setup.ps1
Write-Host "Configuring Git hooks for Antigravity Agent..."

$gitHookPath = ".git\hooks\pre-commit"
# Use forward slashes here to prevent Git Bash from swallowing backslashes as escape characters
$agentHookTrigger = "`n# Antigravity Agent Skill Sync`npowershell.exe -ExecutionPolicy Bypass -File .agent/hooks/pre-commit.ps1"

# Ensure the hidden .git/hooks directory exists
if (-Not (Test-Path ".git\hooks")) {
    New-Item -ItemType Directory -Path ".git\hooks" -Force | Out-Null
}

# Check if a pre-commit hook already exists
if (Test-Path $gitHookPath) {
    $currentContents = Get-Content$gitHookPath -Raw
    
    # Only append if we haven't already
    if (-Not ($currentContents -match "Antigravity Agent Skill Sync")) {
        Add-Content -Path $gitHookPath -Value$agentHookTrigger
        Write-Host "Appended Antigravity sync to existing pre-commit hook."
    } else {
        Write-Host "Antigravity sync is already configured in the pre-commit hook."
    }
} else {
    # Create a new pre-commit hook if one didn't exist
    Set-Content -Path $gitHookPath -Value "#!/bin/sh$agentHookTrigger"
    Write-Host "Created new pre-commit hook with Antigravity sync."
}

Write-Host "Workspace ready. The agent will now sync skills on every commit."
