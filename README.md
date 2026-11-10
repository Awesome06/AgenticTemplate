# AgenticTemplate (Monorepo Project Archetypes)

[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-blue.svg)]()
[![Antigravity](https://img.shields.io/badge/agent-Google%20Antigravity-purple.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An opinionated, agent-first scaffolding monorepo for **Google Antigravity**. It houses the 5-tier governance archetypes under `type/`, links dynamically with the centralized machine `agent-skills-vault` without Git submodules, and enforces strict governance through [`AGENTS.md`](AGENTS.md).

---

## 5-Tier Governance Architecture (`type/`)

Each project archetype maintains its own dedicated template rules and starter assets in `type/<tier>/`:

| Tier | Directory | Governance Focus | Key Invariants |
| :--- | :--- | :--- | :--- |
| **Personal** | `type/personal/` | Rapid prototyping & private tools | Velocity-first, local test parity, exempt from artificial reproducer gates |
| **Team / Hackathon** | `type/team/` | Collaborative multi-author systems | Concurrency sanitizers (`-race`), 120s demo video script (`DEMO_VIDEO_SCRIPT.md`), non-blocking async |
| **External OSS** | `type/oss/` | Upstream contribution & PRs | Mandatory red-test reproducer gate (`TestIssueXXXXX`), maintainer taste mimicry, diff noise ceiling <= 5%, no closed PR reopening |
| **Research** | `type/research/` | Academic empirical papers | CORE A*/A rigor, 4-quadrant Threats to Validity, non-parametric stats (A12, Cliff's delta, Wilson CI, FDR), 3-tier replication runner (`--dry-run`, `--sample`, `--full`), `{metric_originTech}` placeholders |
| **Author-OSS** | `type/author-oss/` | Public author-maintained libraries | Full maintainer authority, SemVer releases, multi-OS CI matrix parity (Linux/macOS/Windows), canonical community assets |

---

## Monorepo Workflow & Main Branch Updates

Because archetypes reside together in `type/`:
1. **List Available Governance Tiers:**
   ```bash
   python .agent/scaffold.py --list
   ```
2. **Initialize a Project Type:**
   ```powershell
   # Windows (PowerShell)
   .\.agent\setup.ps1 -Type <personal|team|oss|research|author-oss>
   ```
   ```bash
   # POSIX Shell (Linux / macOS / DevContainers)
   ./.agent/setup.sh --type <personal|team|oss|research|author-oss>
   ```
3. **Easy Updates from Main:**
   When the base template or archetype rules are refined on `main`, projects can pull updates cleanly from the main branch and re-run:
   ```bash
   python .agent/scaffold.py --type <mode> --update
   ```
4. **Workspace Initializer Mode Skip Gate:**
   - If the governance mode is already declared in `AGENTS.md` (e.g. `mode: personal`), `workspace-initializer` skips prompting and immediately applies the tier's invariants.
   - If undeclared, the initializer prompts the user, awaits confirmation, and writes the choice to `AGENTS.md`.

---

## Submodule Elimination & Local Machine Vault

Git submodules for `agent-skills-vault` are completely eliminated:
- Skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/` via NTFS directory junctions (Windows) or POSIX symlinks (Linux/macOS).
- Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) remain registered in `.git/info/exclude`.
- [`AGENTS.md`](AGENTS.md) is committed and tracked across all repositories.

---

## Directory Structure

```text
AgenticTemplate/
├── type/
│   ├── personal/              # Personal app / rapid prototype rules & templates
│   ├── team/                  # Team / Hackathon directives, demo script & race checks
│   ├── oss/                   # Upstream OSS contributor rules, reproducer gates & PR template
│   ├── research/              # Academic research directives, 3-tier runner & stats engine
│   └── author-oss/            # Public library authoring, SemVer, CI matrix & community assets
├── .agent/
│   ├── hooks/
│   │   ├── pre-commit.ps1     # Dynamic skill detection from central vault (PowerShell)
│   │   └── pre-commit.sh      # Dynamic skill detection from central vault (POSIX sh)
│   ├── scaffold.py            # Archetype scaffolding & update orchestrator
│   ├── setup.ps1              # Workspace initialization & hook configuration (PowerShell)
│   ├── setup.sh               # Workspace initialization & hook configuration (POSIX sh)
│   ├── wiki.ps1               # Quick CLI launcher for wiki-engine (PowerShell)
│   └── wiki.sh                # Quick CLI launcher for wiki-engine (POSIX sh)
├── .agents/skills/            # Active Antigravity customization discovery root (dynamic junctions)
├── AGENTS.md                  # Workspace agent governance directives (tracked)
├── README.example.md          # Scaffolding template README for downstream projects
├── README.md                  # System documentation for AgenticTemplate
├── rules.md                   # Quick reference rules
├── .gitattributes             # Git normalization (LF line endings for cross-platform parity)
├── .gitignore                 # Root-anchored binary ignores & build artifacts
└── wiki/                      # Bidirectional knowledge graph records
    ├── index.md               # Root knowledge graph entrypoint
    ├── architecture.md        # High-level architecture specification
    └── adr/                   # Architecture Decision Records
        └── 001-initial-architecture.md
```

---

## Quick Start

### 1. Initialize Workspace
Run the automated setup script from PowerShell (Windows):

```powershell
.\.agent\setup.ps1 -Type personal
```

Or from a POSIX shell (Linux/macOS/DevContainers):
```bash
./.agent/setup.sh --type personal
```

The setup script will:
1. Ensure the workspace is a valid Git repository and set the root directory.
2. Locate the central `agent-skills-vault` on the machine (via standard paths or `AGENT_SKILLS_VAULT_PATH`).
3. Configure vault exclusions in `.git/info/exclude` to keep Git working tree 100% clean.
4. Verify global skills in `~/.gemini/config/skills/`.
5. Configure the Git `.git/hooks/pre-commit` hook to run synchronization on commit.
6. Apply the selected archetype rules from `type/<type>/` and run initial skill synchronization.

### 2. Archetype Presets

| Command | Applied Governance |
| :--- | :--- |
| `.\.agent\setup.ps1 -Type personal` | Rapid prototyping, personal harness, zero gatekeeping |
| `.\.agent\setup.ps1 -Type team` | Race sanitizers, 120s demo video choreography (`DEMO_VIDEO_SCRIPT.md`) |
| `.\.agent\setup.ps1 -Type oss` | Upstream contributor rules, red-test reproducer gate, diff noise <= 5% |
| `.\.agent\setup.ps1 -Type research` | Academic paper package, 4-quadrant threats, 3-tier replication runner |
| `.\.agent\setup.ps1 -Type author-oss` | Full maintainer authority, SemVer releases, CI matrix, community assets |

Cross-platform scaffolding via Python:
```bash
python .agent/scaffold.py --type <tier>
```

### 3. Fresh Repository Setup & Cleanup
When scaffolding a new application from this template into a fresh repository:
1. **Scaffold Archetype:** Run `.agent/setup.ps1 -Type <tier>` or `python .agent/scaffold.py --type <tier>`.
2. **Replace Root README:** Replace `README.md` using `README.example.md` as your starter specification, delete `README.example.md`, and remove the template disclaimer block.
3. **Populate Stack & Commit:** Add your application code and stack manifests (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`). The pre-commit hook automatically mounts matching domain skills from the local vault into `.agents/skills/`. If the machine lacks the vault, hooks cleanly no-op without blocking Git.

---

## Global Skills vs. Workspace Domain Skills

Antigravity operates with a two-tier skill model:

1. **Global Skills** (`~/.gemini/config/skills/`):
   Always available across all workspaces on the machine (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`). These are never linked into `.agents/skills/`.
2. **Workspace Domain Skills** (`.agents/skills/`):
   Language-, framework-, and stack-specific skills (e.g., `langs/go-systems`, `frameworks/fastapi`, `db/sql-redis`, `ops/docker`) dynamically mounted into `.agents/skills/` from the central machine vault via NTFS junctions or POSIX symlinks based on active repository manifests.
