# Workspace Agent Directives

## Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or verify that `.agent/.registry` is present).
  2. Check if the local `.agents/skills/` directory contains active domain skills.
  3. Automatically detect the application stack from repository manifest files (`pyproject.toml`, `package.json`, `go.mod`, etc.) and synchronize skills silently without pausing to ask the user for confirmation to analyze.
  4. Once skills are linked, strictly enforce their constraints during all subsequent code generation and review tasks.
  5. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `security-auditor`, `test-discipline`, `workspace-initializer`, `repo-wiki`) are pre-loaded at the machine level (`~/.gemini/config/skills/`). Do not attempt to symlink them into `.agents/skills/`.
  6. Repository Knowledge Graph: Check for `wiki/`. When architectural decisions, design contracts, or runbooks change, maintain atomic records using the `repo-wiki` protocol (`[[wikilinks]]`, YAML frontmatter). Use `.agent/wiki.ps1 query <topic>` (or `.agent/wiki.sh`) to slice context on demand without bloating the prompt window.

## General Constraints
- The `.agent/` and `.agents/` directories (including `.agent/.registry`) are internal registry, hook, and customization storage. NEVER treat them as application source code, and NEVER allow internal registry files to trigger skills.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` (singular) is permanently DEPRECATED and PROHIBITED. Agents and scripts MUST NEVER create, link, or reference `.agent/skills/`. All active domain skills and local customizations MUST reside strictly in `.agents/skills/`.
- Do not add or remove third-party dependencies without explicit user confirmation.
- Keep the context window lean: do not load files into context unless actively modifying them.

## Self-Upgrading Pipeline & Gated Execution
- When resolving issues, authoring fixes, or proposing pull requests, adhere strictly to the 4-stage pipeline codified in `ops/self-upgrading-pipeline`:
  1. **Context Bootstrapper:** Verify maintainer taste and conventions (local rules in `.agents/rules/maintainer-taste.md` or global cache `~/.gemini/config/repo-tastes/`).
  2. **Dual-Mode Stage 2 (Defect Remediation vs. Feature Creation):**
     - *Mode A (Defect Fix):* Modifying implementation logic before authoring and executing an isolated failing reproduction test (`TestIssueXXXXX`) is STRICTLY FORBIDDEN.
     - *Mode B (Feature Creation & Greenfield):* Creating new files and scaffolding interfaces follows contract-and-specification-first flow; agents are not blocked by defect reproducer tripwires.
  3. **Adversarial Pre-Flight Filter:** Audit diffs for zero formatting noise (<= 5% pure whitespace churn), ensure concurrency sanitizers (`-race`) pass, and eliminate extraneous debug statements.
  4. **Recursive Distiller:** Capture trajectory deltas and record generalizable architectural invariants.
- **Repository Mode Boundary:** External OSS maintainer restrictions, upstream PR taste mimicry, diff noise ceilings, and mandatory red-test reproducer gates are strictly confined to external open-source repositories (`mode == "oss"`). Personal repositories (`mode == "personal"`, identified via `detect_mode.py`, username namespaces like `awesome06`, or explicit `.agents/mode`) are completely exempt from upstream OSS gatekeeping; the user's personal development harness, rapid prototyping, and custom engineering flows govern without interference.
- **Mental Anti-Slop Scrubber Invariant:** All pull request titles, summaries, commit messages, and review comments across all repositories MUST pass the Repo-Agnostic Mental Anti-Slop Scrubber. Corporate jargon (`holistic`, `comprehensive`, `robust`, `seamless`, `surgical`), self-congratulatory boilerplate (`adheres to enterprise standards`), AI hallmarks (`delve`, `tapestry`), and raw terminal log dumps are strictly prohibited.
- **Compile-Signal Upstream Parity Invariant:** During upstream dependency upgrades, compiler errors (unhandled enum variants, new trait methods, restructured fields) MUST be treated as hard diagnostic signals of expanded upstream surface. Suppressing warnings or stubbing dummy returns is strictly forbidden; agents must audit and expose matching capabilities in client-facing APIs.
- **CI Reality & Execution Parity Transparency:** Authoring tests for runtimes or subsystems that compile locally but are omitted from active continuous integration workflows (`.github/workflows/*.yml`) is STRICTLY FORBIDDEN. Agents must verify CI workflow commands before writing tests; unexecuted tests in CI are dead weight that rot silently.
- **One Canonical Home Per Claim & Docstring Mirror Testing:** Technical claims live in exactly one location: callable contracts in docstrings, shared semantics in type docs, and architectural trade-offs in narrative guides. Any executable docstring example marked with skip directives (`# doctest: +SKIP`) MUST have a companion live mirror test preventing doc code rot.

## Chat UI Readability & Output Formatting Protocol
- **Strict Zero-Raw-LaTeX in Chat Streams:** Never stream or output unparsed raw LaTeX math expressions (`$...$`, `$$...$$`, `\beta`, `\to`, `\mathbf{...}`) in conversational chat text. Chat streaming interfaces often fail to parse raw LaTeX blocks, causing visual friction and garbled markdown.
- **Unicode & Native Markdown Math Substitution:**
  - **Greek Letters & Mathematical Symbols:** Use standard UTF-8 Unicode characters directly in the chat body (e.g., `β` instead of `\beta`, `→` instead of `\to`, `±` instead of `\pm`, `Δ` instead of `\Delta`, `μ` instead of `\mu`, `σ` instead of `\sigma`, `≈` instead of `\approx`, `≤` / `≥` instead of `\le` / `\ge`).
  - **Emphasis & Styling:** Use standard Markdown bolding/italics (`**text**`, `*text*`) instead of LaTeX font commands (`\mathbf{...}`, `\mathit{...}`, `\text{...}`).
  - **Code & Variable Names:** Wrap feature names, variable identifiers, and parameters in inline backticks (e.g., `residence_since`, `existing_credits`).
- **Scannable Layouts for Numerical & Comparative Data:** Present multi-cohort metrics, coefficient shifts, and comparative findings using structured bullet points or clean Markdown tables rather than dense inline math formulas.
- **Artifact Isolation for Formal Math/LaTeX:** When formal LaTeX documents or complex multi-line derivations are explicitly requested, confine them strictly to dedicated artifact files (e.g., `.tex` files or structured document artifacts), keeping the conversational stream clean, scannable, and human-friendly.

## Git Staging & Commit Protocol
- **Pre-Staging Verification:** Run active linters and tests via `test-discipline` before staging any changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and formulate structured commit messages adhering to Conventional Commits (via `git-release`) with a comprehensive technical description:
  - Header: `<type>(<scope>): <subject>` (maximum 72 characters, imperative mood, lowercase, no trailing period).
  - Multi-line body: Explicit motivation/intent, bulleted key changes, and verification evidence.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.

