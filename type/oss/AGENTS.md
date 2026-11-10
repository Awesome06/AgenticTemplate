---
mode: oss
---
# Workspace Agent Directives (External Open-Source Contribution)

## 1. Governance & Architecture
- **Repository Mode:** External open-source repository contribution (`mode: oss`).
- **Maintainer Precedence:** Upstream `CONTRIBUTING.md`, issue/PR templates, and maintainer architectural conventions govern with absolute priority. Contributor preferences are subservient to project taste.
- **Red-Test Reproducer Gate (Mode A vs. Mode B):**
  - *Mode A (Defect Fix):* Modifying existing implementation logic before authoring and executing an isolated failing reproduction test (`TestIssueXXXXX`) is STRICTLY FORBIDDEN. The reproduction test must fail before the fix and pass after.
  - *Mode B (Feature Creation & Greenfield):* Creating new files and scaffolding interfaces follows contract-and-specification-first flow; agents are not blocked by defect reproducer tripwires.
- **Diff Noise Ceiling:** All PR diffs must have <= 5% pure whitespace or stylistic churn. Never reformat unrelated lines, sort imports needlessly, or inject conversational comments into upstream code.
- **Closed PR Non-Reopening Invariant:** Reopening a closed pull request (`gh pr reopen`) is STRICTLY FORBIDDEN. Maintainer closures signify architectural disagreement or design obsolescence; reopening forces unwanted notifications. If the work remains viable, seek alignment on the tracking issue first or submit a fresh, cleanly rebased PR from a new branch.
- **Mandatory PR Template Conformance:** Agents MUST discover and adhere strictly to repository PR templates (`.github/PULL_REQUEST_TEMPLATE.md`). Discarding repository templates is STRICTLY FORBIDDEN. All required sections and checklist items (`[x]`) MUST be preserved.
- **Mental Anti-Slop Scrubber Invariant:** All PR titles, summaries, commits, and review comments MUST pass the Mental Anti-Slop Scrubber. Corporate jargon (`holistic`, `comprehensive`, `robust`, `seamless`), self-congratulatory boilerplate, AI hallmarks (`delve`, `tapestry`), and raw terminal log dumps are strictly prohibited.
- **Direct Vault Integration:** Dynamic skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/`. Pinned submodules are permanently eliminated.
- **Universal Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` MUST remain a tracked file in Git.

## 2. Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or `.agent/setup.sh` on POSIX).
  2. Verify that dynamic agent artifacts (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) are registered in `.git/info/exclude`.
  3. Inspect upstream repo manifests and link required domain skills into `.agents/skills/`.
  4. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`) are pre-loaded at machine level (`~/.gemini/config/skills/`). Never symlink them into `.agents/skills/`.
  5. Inspect upstream `CONTRIBUTING.md`, style guides, and PR templates before proposing changes.

## 3. General Constraints & Upstream Quality Invariants
- **Compile-Signal Upstream Parity Invariant:** During upstream dependency upgrades or refactors, compiler errors MUST be treated as hard diagnostic signals of expanded upstream surface. Suppressing warnings or stubbing dummy returns is strictly forbidden.
- **CI Reality & Execution Parity Transparency:** Authoring tests for runtimes or subsystems that compile locally but are omitted from active continuous integration workflows (`.github/workflows/*.yml`) is STRICTLY FORBIDDEN. Unexecuted tests in CI rot silently.
- **Enumerate the Family Before Modifying Invariant:** Before extending or modifying an interface method, trait implementation, FFI getter, or dunder protocol, agents MUST run a pre-flight grep enumerating all existing sibling implementations. Modifying one without verifying parity across the family is STRICTLY FORBIDDEN.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` is permanently DEPRECATED and PROHIBITED.

## 4. Chat Output Readability & Anti-LaTeX Invariant
- **Zero-Tolerance for Broken Math Delimiters:** In conversational chat turns and assistant messages, agents MUST prioritize immediate visual clarity and plain-text markdown formatting. The Chat UI renders standard GitHub-Flavored Markdown (GFM) WITHOUT a KaTeX/MathJax engine. Unescaped LaTeX causes broken formatting, raw dollar signs, and syntax noise.
- **Rule A (Zero Dollar Delimiters):** NEVER wrap equations, numbers, units, or variables in single (`$...$`) or double (`$$...$$`) dollar signs. Dollar signs are ONLY allowed in code blocks for shell variables (`echo $PATH`), shell prompts (`$ command`), or monetary values (`$50`).
- **Rule B (Zero LaTeX Math Commands):** NEVER use LaTeX math macros in chat responses. Always use ASCII / Unicode equivalents: `*` or `x` instead of `\times`, `/` instead of `\div`, `µs` instead of `\mu s`, `O(N)` instead of `\mathcal{O}(N)`, `<=`, `>=`, `!=` instead of `\le`, `\ge`, `\neq`, `~` instead of `\approx`, `->` instead of `\to`, `A / B` instead of `\frac{A}{B}`, `+/-` instead of `\pm`, `<->` instead of `\leftrightarrow`.
- **Pre-Emission Mental Scan Gate:** Before outputting ANY response, the agent MUST run a mandatory verification check:
  - *"Does this response contain any `$` enclosing math or variables?"* -> Strip immediately.
  - *"Does this response contain `\times`, `\div`, `\text{`, `\mu`, or `\mathcal`?"* -> Replace with `*`, `/`, plain text, `µs`, or `O(...)`.

## 5. Git Staging & Commit Review Protocol
- **Pre-Staging Verification Gate:** Run upstream test suites and linters locally before staging changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and craft structured commit messages adhering to upstream project conventions and `globals/git-release`.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.
