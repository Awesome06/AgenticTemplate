# AgenticTemplate (Monorepo Project Archetypes)

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue.svg)]()
[![Antigravity](https://img.shields.io/badge/agent-Google%20Antigravity-purple.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An opinionated, agent-first scaffolding monorepo for **Google Antigravity**. It houses the 5-tier governance archetypes under `type/`, links dynamically with the centralized machine `agent-skills-vault` without Git submodules, and enforces strict governance through [`AGENTS.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/AGENTS.md).

---

## 5-Tier Governance Architecture (`type/`)

Each project archetype maintains its own dedicated template rules and starter assets in `type/<tier>/`:

| Tier | Directory | Governance Focus | Key Invariants |
| :--- | :--- | :--- | :--- |
| **Personal** | `type/personal/` | Rapid prototyping & private tools | Velocity-first, local test parity, no artificial reproducer gates |
| **Team / Hackathon** | `type/team/` | Collaborative multi-author systems | Concurrency sanitizers (`-race`), 120s demo video script (`DEMO_VIDEO_SCRIPT.md`) |
| **External OSS** | `type/oss/` | Upstream contribution & PRs | Mandatory red-test reproducer gate (`TestIssueXXXXX`), maintainer taste mimicry, diff noise ceiling <= 5% |
| **Research** | `type/research/` | Academic empirical papers | Double-blind review rigor, Threats to Validity, non-parametric stats, 3-tier replication runner |
| **Author-OSS** | `type/author-oss/` | Public author-maintained libraries | Full maintainer authority, SemVer releases, public CI matrix, canonical community assets (`CONTRIBUTING.md`, etc.) |

---

## Monorepo Workflow & Main Branch Updates

Because archetypes reside together in `type/`:
1. **Initialize a Project Type:**
   ```powershell
   .\.agent\setup.ps1 -Type <personal|team|oss|research|author-oss>
   ```
2. **Easy Updates from Main:**
   When the base template or archetype rules are refined on `main`, projects can pull updates cleanly from the main branch and re-run:
   ```bash
   python .agent/scaffold.py --type <mode> --update
   ```
3. **Workspace Initializer Mode Skip Gate:**
   - If the governance mode is already declared in `AGENTS.md` (e.g. `mode: personal`), `workspace-initializer` skips prompting and immediately applies the tier's invariants.
   - If undeclared, the initializer prompts the user, awaits confirmation, and writes the choice to `AGENTS.md`.

---

## Submodule Elimination & Local Machine Vault

Git submodules for `agent-skills-vault` are completely eliminated:
- Skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/` via NTFS junctions / POSIX symlinks.
- Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) remain registered in `.git/info/exclude`.
- [`AGENTS.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/AGENTS.md) is committed and tracked across all repositories.

---

## Directory Structure

```text
AgenticTemplate/
├── type/
│   ├── personal/              # Personal app / rapid prototype rules & templates
│   ├── team/                  # Team / Hackathon directives & demo script
│   ├── oss/                   # Upstream OSS contributor rules & reproducer gates
│   ├── research/              # Academic empirical research directives & replication package
│   └── author-oss/            # Public library authoring, SemVer, & community assets
├── .agent/
│   ├── hooks/
│   │   ├── pre-commit.ps1     # Dynamic skill detection from central vault (PowerShell)
│   │   └── pre-commit.sh      # Dynamic skill detection from central vault (POSIX sh)
│   ├── scaffold.py            # Archetype scaffolding & update orchestrator
│   ├── setup.ps1              # Workspace initialization & hook configuration
│   ├── wiki.ps1               # Quick CLI launcher for wiki-engine (Windows)
│   └── wiki.sh                # Quick CLI launcher for wiki-engine (Linux/macOS)
├── .agents/skills/            # Active Antigravity customization discovery root
├── AGENTS.md                  # Workspace agent governance directives (tracked)
└── wiki/                      # Bidirectional knowledge graph records
```
│   ├── setup.ps1              # One-command workspace bootstrap & hook installer (Windows)
│   └── setup.sh               # One-command workspace bootstrap & hook installer (Linux/macOS)
├── .agents/
│   └── skills/                # Antigravity customization discovery root (symlinks gitignored)
│       └── .gitkeep
├── wiki/                      # Repository Knowledge Graph & ADRs (Markdown)
│   ├── index.md               # Root knowledge graph entrypoint
│   ├── architecture.md        # High-level architecture specification
│   └── adr/                   # Architecture Decision Records
│       └── 001-initial-architecture.md
├── AGENTS.md                  # Antigravity agent directives & bootstrap protocol
├── README.example.md          # Scaffolding template README for downstream projects
├── README.md                  # System documentation for AgenticTemplate
├── .gitattributes             # Git normalization (LF line endings for scripts)
├── .gitmodules                # Submodule registration for .agent/.registry
└── .gitignore                 # Standard ignores for build outputs & dynamic links
```

---

## Quick Start

### 1. Initialize Workspace
Run the automated setup script from PowerShell (Windows):

```powershell
.\.agent\setup.ps1
```

Or from a POSIX shell (Linux/macOS/DevContainers):
```bash
./.agent/setup.sh
```

The setup script will:
1. Ensure the workspace is a valid Git repository and set the root directory.
2. Initialize and pull the `.agent/.registry` submodule from the skills vault.
3. Configure the Git `.git/hooks/pre-commit` hook to run synchronization on every commit.
4. Execute an immediate initial synchronization pass into `.agents/skills/`.

### 2. Fresh Repository Setup & Cleanup
When scaffolding a new application from this template into a fresh repository:
1. **Remove Template Disclaimer**:
   - Permanently delete the `> [!WARNING]` block at the very top of [`README.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/README.md).
   - Alternatively, replace [`README.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/README.md) entirely using [`README.example.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/README.example.md) as your starter specification, and delete [`README.example.md`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/README.example.md).
2. **Private Skills Vault Check**:
   - If you do not have access to the private `agent-skills-vault`, either link your own submodule to `.agent/.registry` or remove `.agent/hooks/` and the pre-commit hook triggers.
3. **Populate Stack & Commit**:
   - Add your application source code and stack manifest files (e.g., `package.json`, `go.mod`, `Cargo.toml`, `requirements.txt`).
   - Commit your changes—the pre-commit hook will automatically detect your project stack and symlink matching domain skills into [`.agents/skills/`](file:///c:/Users/Bhatn/OneDrive/Desktop/Projects/AgenticTemplate/.agents/skills).

### 3. Workspace Archetype Presets (Personal vs. Author-Maintained Open-Source)
AgenticTemplate supports both private personal development and public author-maintained open-source releases on `main`:
- **Personal Default (`mode: personal`):** Standard setup for private applications, experiments, and rapid prototyping:
  ```powershell
  .\.agent\setup.ps1
  ```
- **Author-Maintained OSS Preset (`mode: author-oss`):** Transforms the workspace for public community release:
  ```powershell
  .\.agent\setup.ps1 -Preset author-oss
  ```
  Or cross-platform via Python:
  ```bash
  python .agent/scaffold.py --preset author-oss
  ```
  This automatically scaffolds the complete open-source community surface (`LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/` issue forms, PR template, CI matrix workflow, and `.gitignore` dynamic junction exclusions) while configuring `mode: author-oss` in `AGENTS.md`.

---

## Global Skills vs. Workspace Domain Skills

Antigravity operates with a two-tier skill model:

1. **Global Skills** (`~/.gemini/config/skills/`):
   Always available across all workspaces on the machine (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`). These are never linked into `.agents/skills/`.
2. **Workspace Domain Skills** (`.agents/skills/`):
   Language-, framework-, and stack-specific skills (e.g., `go`, `react`, `rust`, `python`) dynamically linked from the vendored `.agent/.registry` based on active repository files.
