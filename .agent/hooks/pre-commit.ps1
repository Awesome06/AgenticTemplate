#!/usr/bin/env pwsh
# .agent/hooks/pre-commit.ps1
# Analyzes the repo for new language signatures and syncs agent skills before committing.

# Ensure we are operating from the repository root
$repoRoot = git rev-parse --show-toplevel
if ($LASTEXITCODE -ne 0) { exit 0 }
Set-Location -Path $repoRoot

$registryMapPath = ".agent\.registry\skill-map.json"
$activeSkillsPath = ".agent\.active-skills.json"
$skillsDir = ".agent\skills"

# Exit silently if the vault isn't vendored yet
if (-Not (Test-Path $registryMapPath)) { exit 0 }

$map = Get-Content $registryMapPath | ConvertFrom-Json
$currentSkills = @()
if (Test-Path $activeSkillsPath) {
    $currentSkills = Get-Content $activeSkillsPath | ConvertFrom-Json
}

$requiredSkills = @()

# Scan repo for trigger files (e.g., go.mod, package.json)
foreach ($signature in $map.signatures.psobject.properties) {
    if (Test-Path $signature.Name) {
        $requiredSkills += $signature.Value
    }
}
$requiredSkills = $requiredSkills | Select-Object -Unique

$driftDetected = $false

# Identify missing skills and create symlinks
foreach ($req in $requiredSkills) {
    if ($req -notin $currentSkills) {
        Write-Host "Antigravity Sync: Linking new skill -> $req"
        
        $folderName = Split-Path $req -Leaf
        $targetPath = "..\.registry\$req"
        $linkPath = "$skillsDir\$folderName"
        
        if (-Not (Test-Path $skillsDir)) { 
            New-Item -ItemType Directory -Path $skillsDir -Force | Out-Null 
        }
        
        # Create Windows symlink (Requires Developer Mode enabled in Windows Settings)
        New-Item -ItemType SymbolicLink -Path $linkPath -Target $targetPath -Force | Out-Null
        
        $currentSkills += $req
        $driftDetected = $true
    }
}

# Apply and stage updates if drift occurred
if ($driftDetected) {
    $currentSkills | ConvertTo-Json | Set-Content $activeSkillsPath
    Write-Host "Antigravity Sync: Agent skills updated. Staging tracker..."
    
    # Stage the hidden state file so it is included in the commit that triggered this hook
    git add $activeSkillsPath
}

exit 0
