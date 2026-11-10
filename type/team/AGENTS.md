---
mode: team
---
# Workspace Agent Directives (Team / Hackathon Project)

## 1. Governance & Architecture
- **Repository Mode:** Collaborative team / hackathon repository (`mode: team`).
- **Mandatory Concurrency Sanitizers:** Code paths handling shared concurrency, threads, or asynchronous state MUST pass race sanitizers:
  - Go: `go test -race ./...`
  - Rust / C++: ThreadSanitizer (`-Zsanitizer=thread` or `TSAN_OPTIONS`)
  - Python: Strict asyncio loop isolation (`pytest-asyncio` strict mode or zero unawaited coroutines)
- **Demo-First Alignment:** For hackathons or fast product showcases, all features align with the 120-second demo script in `DEMO_VIDEO_SCRIPT.md`. Every architectural capability must directly advance the demo walkthrough or sponsor track requirements.
- **Non-Blocking Asynchronous Execution:** Network I/O, LLM inference calls, and background workers must never block main application event loops.
- **Atomic Modular Collaboration:** Keep commits atomic and tightly scoped to specific subsystem modules. Never reformat or introduce stylistic churn into files actively edited by teammates.
- **Direct Vault Integration:** Dynamic skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/`. Pinned submodules are permanently eliminated.
- **Universal Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` MUST remain a tracked file in Git.

## 2. Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or `.agent/setup.sh` on POSIX).
  2. Verify that dynamic agent artifacts (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) are in `.git/info/exclude`.
  3. Inspect repository manifests and link required domain skills into `.agents/skills/`.
  4. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`) are pre-loaded at machine level (`~/.gemini/config/skills/`). Never symlink them into `.agents/skills/`.
  5. Check `DEMO_VIDEO_SCRIPT.md` to ensure any proposed feature aligns with the competition presentation storyboard.

## 3. General Constraints & Team Collaboration Invariants
- **Customization Isolation:** The `.agent/` and `.agents/` directories are internal registry, hook, and customization storage. NEVER treat them as application source code.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` is permanently DEPRECATED and PROHIBITED.
- **Multi-Author Conflict Prevention:** Avoid giant monolithic PRs. Break features into small, cohesive PRs with clear interfaces defined in `wiki/`.
- **Pre-Push Sanitizer Gate:** Run race sanitizers (`scripts/check-race.ps1` or `scripts/check-race.sh`) before pushing shared branches.

## 4. Chat Output Readability & Anti-LaTeX Invariant
- **Zero-Tolerance for Broken Math Delimiters:** In conversational chat turns and assistant messages, agents MUST prioritize immediate visual clarity and plain-text markdown formatting. The Chat UI renders standard GitHub-Flavored Markdown (GFM) WITHOUT a KaTeX/MathJax engine. Unescaped LaTeX causes broken formatting, raw dollar signs, and syntax noise.
- **Rule A (Zero Dollar Delimiters):** NEVER wrap equations, numbers, units, or variables in single (`$...$`) or double (`$$...$$`) dollar signs. Dollar signs are ONLY allowed in code blocks for shell variables (`echo $PATH`), shell prompts (`$ command`), or monetary values (`$50`).
- **Rule B (Zero LaTeX Math Commands):** NEVER use LaTeX math macros in chat responses. Always use ASCII / Unicode equivalents: `*` or `x` instead of `\times`, `/` instead of `\div`, `µs` instead of `\mu s`, `O(N)` instead of `\mathcal{O}(N)`, `<=`, `>=`, `!=` instead of `\le`, `\ge`, `\neq`, `~` instead of `\approx`, `->` instead of `\to`, `A / B` instead of `\frac{A}{B}`, `+/-` instead of `\pm`, `<->` instead of `\leftrightarrow`.
- **Pre-Emission Mental Scan Gate:** Before outputting ANY response, the agent MUST run a mandatory verification check:
  - *"Does this response contain any `$` enclosing math or variables?"* -> Strip immediately.
  - *"Does this response contain `\times`, `\div`, `\text{`, `\mu`, or `\mathcal`?"* -> Replace with `*`, `/`, plain text, `µs`, or `O(...)`.

## 5. Git Staging & Commit Review Protocol
- **Pre-Staging Verification Gate:** Run active linters, tests, and race sanitizers before staging changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and craft structured commit messages adhering to `globals/git-release`:
  - **Header:** `<type>(<scope>): <subject>` (maximum 72 characters, imperative mood, lowercase, no trailing period).
  - **Multi-Line Body:** Structured description with Motivation & Intent, Key Changes, and Verification Evidence.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.
