---
mode: research
---
# Workspace Agent Directives (Academic Research Paper)

## 1. Governance & Architecture
- **Repository Mode:** Academic empirical research paper repository (`mode: research`).
- **Target Venues:** Rigorous double-blind standards targeting CORE A* and A venues (ISSTA, FSE, ASE, MSR, EDM).
- **Threats to Validity:** Mandatory coverage across 4 quadrants in `docs/THREATS_TO_VALIDITY_TEMPLATE.md`:
  1. *Internal Validity:* Confounding factors, instrument calibration, prompt leakage, training contamination.
  2. *External Validity:* Generalizability across repositories, languages, project sizes, and realistic developer workloads.
  3. *Construct Validity:* Alignment between theoretical concepts and empirical metrics (e.g. AST edit distance vs syntactic accuracy).
  4. *Conclusion Validity:* Statistical test assumptions, sample sizes, and error rate controls.
- **Statistical Rigor Invariant:** Mandatory non-parametric empirical software engineering statistics:
  - *Effect size:* Vargha-Delaney A12 or Cliff's delta (never assume normal distributions).
  - *Confidence intervals:* Wilson score intervals for proportions.
  - *Multiple hypothesis testing:* False Discovery Rate (FDR) control / Benjamini-Hochberg correction.
- **Three-Tier Reproducible Artifact:** Evaluation scripts MUST support:
  - `run_all.sh --dry-run` (< 60s sanity check on toy dataset).
  - `run_all.sh --sample` (< 15 min representative validation on 5-10% sample).
  - `run_all.sh --full` (complete experimental replication).
- **Evaluation Metric Placeholders:** Any metric from an unexecuted or pending experimental pipeline MUST be explicitly formatted as `{metric_originTech}` (e.g. `{f1_ASTMatcher}`, `{p95_Latency}`). Suppressing, inventing, or hardcoding unverified numerical results is STRICTLY FORBIDDEN.
- **Double-Blind Anonymity:** Strict pre-flight audit: verify zero author names, institutional affiliations, grant identifiers, or absolute local machine paths leak into public paper artifacts, manuscript sources, or replication scripts.
- **Direct Vault Integration:** Dynamic skills mount directly from the central machine vault (`agent-skills-vault`) into `.agents/skills/`. Pinned submodules are permanently eliminated.
- **Universal Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` MUST remain a tracked file in Git.

## 2. Bootstrap Protocol
- On session initialization:
  1. Verify Git hook configuration by checking if `.git/hooks/pre-commit` exists. If missing, execute `.agent/setup.ps1` (or `.agent/setup.sh` on POSIX).
  2. Verify that dynamic agent artifacts (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) are in `.git/info/exclude`.
  3. Inspect research dependencies and link required domain skills into `.agents/skills/`.
  4. Note: Global skills (`code-review`, `doc-sync`, `error-discipline`, `git-release`, `incident-triaging`, `intent-discipline`, `repo-wiki`, `script-optimization`, `security-auditor`, `strategic-reconnaissance`, `test-discipline`, `workspace-initializer`) are pre-loaded at machine level (`~/.gemini/config/skills/`). Never symlink them into `.agents/skills/`.
  5. Audit scripts in `scripts/` to ensure all three replication tiers (`--dry-run`, `--sample`, `--full`) are supported.

## 3. General Constraints & Research Rigor Invariants
- **Deterministic Evaluation Seeds:** Preserve exact dataset seeds and random generator configurations across all benchmark runs.
- **Zero-Unverified-Numbers Guardrail:** Any claim made in paper markdown, LaTeX, or Typst files must have corresponding raw log files in `results/`.
- **Anonymity Audit Gate:** Search repository for any hardcoded username (e.g. local machine paths like `C:\Users\...` or `/home/...`), institutional emails, or GitHub user handles before committing paper assets.
- **Strict Zero-Legacy-Skills Invariant:** Antigravity IDE discovers workspace skills exclusively from `.agents/skills/` (plural). The legacy directory `.agent/skills/` is permanently DEPRECATED and PROHIBITED.

## 4. Chat Output Readability & Anti-LaTeX Invariant
- **Zero-Tolerance for Broken Math Delimiters:** In conversational chat turns and assistant messages, agents MUST prioritize immediate visual clarity and plain-text markdown formatting. The Chat UI renders standard GitHub-Flavored Markdown (GFM) WITHOUT a KaTeX/MathJax engine. Unescaped LaTeX causes broken formatting, raw dollar signs, and syntax noise.
- **Rule A (Zero Dollar Delimiters):** NEVER wrap equations, numbers, units, or variables in single (`$...$`) or double (`$$...$$`) dollar signs in chat messages. Dollar signs are ONLY allowed in code blocks for shell variables (`echo $PATH`), shell prompts (`$ command`), or monetary values (`$50`).
- **Rule B (Zero LaTeX Math Commands in Chat):** NEVER use LaTeX math macros in chat responses. Always use ASCII / Unicode equivalents: `*` or `x` instead of `\times`, `/` instead of `\div`, `µs` instead of `\mu s`, `O(N)` instead of `\mathcal{O}(N)`, `<=`, `>=`, `!=` instead of `\le`, `\ge`, `\neq`, `~` instead of `\approx`, `->` instead of `\to`, `A / B` instead of `\frac{A}{B}`, `+/-` instead of `\pm`, `<->` instead of `\leftrightarrow`.
- **Scope Boundaries:** Formal LaTeX syntax (`$...$`, `$$...$$`, `\begin{equation}`) is STRICTLY RESERVED for `.ipynb` notebook cells, `.tex` source documents, and PDF report templates. Outside of those specific file types, ALL outputs MUST be 100% clean plain-text/Unicode GFM.
- **Pre-Emission Mental Scan Gate:** Before outputting ANY response, the agent MUST run a mandatory verification check:
  - *"Does this response contain any `$` enclosing math or variables?"* -> Strip immediately.
  - *"Does this response contain `\times`, `\div`, `\text{`, `\mu`, or `\mathcal`?"* -> Replace with `*`, `/`, plain text, `µs`, or `O(...)`.

## 5. Git Staging & Commit Review Protocol
- **Pre-Staging Verification Gate:** Run replication smoke tests (`bash scripts/run_all.sh --dry-run` or `python scripts/run_all.py --dry-run`) before staging paper changes.
- **Autonomous Staging & Commit Formulation:** Agents are authorized to stage modified files (`git add`) and craft structured commit messages adhering to `globals/git-release`.
- **Review Gate (Not Committed Until Review):** Commits MUST NOT be executed autonomously. Always leave changes staged and present the drafted commit message and diff summary to the user for review. Execute `git commit` ONLY after explicit user review and approval.
- **Strict Zero-Unprompted-Push Guardrail:** NEVER run `git push` without explicit user instruction.
