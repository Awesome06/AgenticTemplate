---
mode: author-oss
---
# Workspace Agent Directives (Author-Maintained Open-Source Library)

## 1. Governance & Architecture
- **Repository Mode:** Public open-source library authored and maintained by the user (`mode: author-oss`).
- **Maintainer Authority:** Full maintainer architectural authority without upstream contributor subservience. The author sets coding conventions, public API contracts, and roadmap priorities. Exempt from guest-contributor reproducer gates. The author may reopen closed PRs and guide evolution.
- **Public Open-Source Hygiene:**
  - Mandatory public CI/CD matrix parity across Linux, macOS, and Windows.
  - Strict SemVer releases adhering to `globals/git-release`.
  - Clean `AGENTS.md` and public documentation with zero local machine path leaks.
  - Root-anchored `.gitignore` exclusions preventing local dynamic agent junctions from leaking into public Git tracking.
  - Canonical community assets committed: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/` issue forms, and structured PR template.
- **Direct Vault Integration:** Dynamic skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/`. Pinned submodules are permanently eliminated.
- **Universal Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` MUST remain a tracked file in Git.

## 2. Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or `.agent/setup.sh` on POSIX).
  2. Verify that dynamic agent artifacts (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) are registered in `.git/info/exclude`.
  3. Inspect library manifests (`pyproject.toml`, `Cargo.toml`, `package.json`, `go.mod`) and link matching domain skills into `.agents/skills/`.
  4. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`) are pre-loaded at machine level (`~/.gemini/config/skills/`). Never symlink them into `.agents/skills/`.
  5. Repository Knowledge Graph: Check for `wiki/`. When architectural decisions, design contracts, or runbooks change, maintain atomic records using `repo-wiki` protocol (`[[wikilinks]]`).

## 3. General Constraints & Maintainer Invariants
- **Public API Contract Stability:** Every public export, type definition, and function signature must have explicit type annotations and docstrings. Breaking changes require major SemVer increments.
- **CI Parity & Reality:** All tests must pass in local test runners and across the active GitHub Actions matrix (`.github/workflows/ci.yml`). Never write tests for unexecuted CI configurations.
- **Customization Isolation:** The `.agent/` and `.agents/` directories are internal registry, hook, and customization storage. NEVER treat them as application source code.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` is permanently DEPRECATED and PROHIBITED.

## 4. Chat Output Readability & Anti-LaTeX Invariant
- **Zero-Tolerance for Broken Math Delimiters:** In conversational chat turns and assistant messages, agents MUST prioritize immediate visual clarity and plain-text markdown formatting. The Chat UI renders standard GitHub-Flavored Markdown (GFM) WITHOUT a KaTeX/MathJax engine. Unescaped LaTeX causes broken formatting, raw dollar signs, and syntax noise.
- **Rule A (Zero Dollar Delimiters):** NEVER wrap equations, numbers, units, or variables in single (`$...$`) or double (`$$...$$`) dollar signs. Dollar signs are ONLY allowed in code blocks for shell variables (`echo $PATH`), shell prompts (`$ command`), or monetary values (`$50`).
- **Rule B (Zero LaTeX Math Commands):** NEVER use LaTeX math macros in chat responses. Always use ASCII / Unicode equivalents: `*` or `x` instead of `\times`, `/` instead of `\div`, `µs` instead of `\mu s`, `O(N)` instead of `\mathcal{O}(N)`, `<=`, `>=`, `!=` instead of `\le`, `\ge`, `\neq`, `~` instead of `\approx`, `->` instead of `\to`, `A / B` instead of `\frac{A}{B}`, `+/-` instead of `\pm`, `<->` instead of `\leftrightarrow`.
- **Pre-Emission Mental Scan Gate:** Before outputting ANY response, the agent MUST run a mandatory verification check:
  - *"Does this response contain any `$` enclosing math or variables?"* -> Strip immediately.
  - *"Does this response contain `\times`, `\div`, `\text{`, `\mu`, or `\mathcal`?"* -> Replace with `*`, `/`, plain text, `µs`, or `O(...)`.

## 5. Git Staging & Commit Review Protocol
- **Pre-Staging Verification Gate:** Run full test suite and linters locally before staging changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and craft structured commit messages adhering to `globals/git-release`:
  - **Header:** `<type>(<scope>): <subject>` (maximum 72 characters, imperative mood, lowercase, no trailing period).
  - **Multi-Line Body:** Structured description with Motivation & Intent, Key Changes, and Verification Evidence.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.
