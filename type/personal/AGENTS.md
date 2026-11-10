---
mode: personal
---
# Workspace Agent Directives (Personal Project)

## 1. Governance & Architecture
- **Repository Mode:** Personal repository (`mode: personal`).
- **Autonomy & Velocity:** Rapid prototyping, developer harness, and private app velocity govern. The agent is exempt from external open-source gatekeeping, upstream maintainer taste mimicry, or mandatory red-test reproducer gates.
- **Direct Vault Integration:** Dynamic skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/` via directory junctions or POSIX symlinks. Pinned git submodules are permanently eliminated.
- **Universal Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude` to guarantee a clean Git status. `AGENTS.md` MUST remain a tracked file in Git.

## 2. Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or `.agent/setup.sh` on POSIX).
  2. Verify that dynamic agent artifacts (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) are registered in `.git/info/exclude`.
  3. Inspect repository manifests (`pyproject.toml`, `package.json`, `go.mod`, `Cargo.toml`) and ensure matching domain skills are active in `.agents/skills/`.
  4. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`) are pre-loaded at the machine level (`~/.gemini/config/skills/`). Never attempt to symlink them into `.agents/skills/`.
  5. Repository Knowledge Graph: Check for `wiki/`. When architectural contracts or ADRs change, maintain records using `repo-wiki` protocol (`[[wikilinks]]`). Use `.agent/wiki.ps1 query <topic>` (or `.agent/wiki.sh`) to slice context on demand.

## 3. General Constraints & Development Discipline
- **Customization Isolation:** The `.agent/` and `.agents/` directories are internal registry, hook, and customization storage. NEVER treat them as application source code, and NEVER allow internal files to trigger stack detection.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` (singular) is permanently DEPRECATED and PROHIBITED. All active domain skills and local customizations MUST reside strictly in `.agents/skills/`.
- **Context Economy:** Keep context lean: do not load multi-thousand line files in bulk. Inspect targeted symbols and 1-hop neighborhoods.
- **Preserve Documentation:** Preserve existing comments and docstrings unless explicitly asked to modify them.
- **Local Verification:** Run active linters and automated tests locally via package runners (`pytest`, `cargo test`, `vitest`, `go test`) before staging code.

## 4. Chat Output Readability & Anti-LaTeX Invariant
- **Zero-Tolerance for Broken Math Delimiters:** In conversational chat turns and assistant messages, agents MUST prioritize immediate visual clarity and plain-text markdown formatting. The Chat UI renders standard GitHub-Flavored Markdown (GFM) WITHOUT a KaTeX/MathJax engine. Unescaped LaTeX causes broken formatting, raw dollar signs, and syntax noise.
- **Rule A (Zero Dollar Delimiters):** NEVER wrap equations, numbers, units, or variables in single (`$...$`) or double (`$$...$$`) dollar signs. Dollar signs are ONLY allowed in code blocks for shell variables (`echo $PATH`), shell prompts (`$ command`), or monetary values (`$50`).
- **Rule B (Zero LaTeX Math Commands):** NEVER use LaTeX math macros in chat responses. Always use ASCII / Unicode equivalents: `*` or `x` instead of `\times`, `/` instead of `\div`, `µs` instead of `\mu s`, `O(N)` instead of `\mathcal{O}(N)`, `<=`, `>=`, `!=` instead of `\le`, `\ge`, `\neq`, `~` instead of `\approx`, `->` instead of `\to`, `A / B` instead of `\frac{A}{B}`, `+/-` instead of `\pm`, `<->` instead of `\leftrightarrow`.
- **Pre-Emission Mental Scan Gate:** Before outputting ANY response, the agent MUST run a mandatory verification check:
  - *"Does this response contain any `$` enclosing math or variables?"* -> Strip immediately.
  - *"Does this response contain `\times`, `\div`, `\text{`, `\mu`, or `\mathcal`?"* -> Replace with `*`, `/`, plain text, `µs`, or `O(...)`.

## 5. Git Staging & Commit Review Protocol
- **Pre-Staging Verification Gate:** Run active linters and tests locally before staging any changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and craft structured commit messages adhering to `globals/git-release`:
  - **Header:** `<type>(<scope>): <subject>` (maximum 72 characters, imperative mood, lowercase, no trailing period).
  - **Multi-Line Body:** Structured description with Motivation & Intent, Key Changes, and Verification Evidence.
- **Documentation Lockstep Gate (`AGENTS.md` <-> `README.md`):** Verify that changes altering tools, scripts, or workflows are reflected consistently in both `README.md` and `AGENTS.md`.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.
