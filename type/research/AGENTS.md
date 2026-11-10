---
mode: research
---
# Workspace Agent Directives (Academic Research Paper)

## Governance & Architecture
- **Repository Mode:** Academic empirical research paper repository (`mode: research`).
- **Target Venues:** Rigorous double-blind standards targeting CORE A* and A venues (ISSTA, FSE, ASE, MSR, EDM).
- **Threats to Validity:** Mandatory coverage across 4 quadrants: Internal, External, Construct, and Conclusion validity.
- **Statistical Rigor:** Mandatory non-parametric empirical software engineering statistics:
  - Effect size: Vargha-Delaney A12 or Cliff's delta.
  - Confidence intervals: Wilson score intervals.
  - Multiple hypothesis testing: False Discovery Rate (FDR) control / Benjamini-Hochberg correction.
- **Three-Tier Reproducible Artifact:** Scripts MUST support:
  - `run_all.sh --dry-run` (< 60s sanity check)
  - `run_all.sh --sample` (< 15 min representative validation)
  - `run_all.sh --full` (complete experimental run)
- **Evaluation Metric Placeholders:** Any metric from an unexecuted or pending experimental pipeline MUST be explicitly formatted as `{metric_originTech}` (e.g. `{f1_ASTMatcher}`). Suppressing, inventing, or hardcoding unverified numerical results is STRICTLY FORBIDDEN.
- **Double-Blind Anonymity:** Verify zero author names, institutional affiliations, or absolute local path leaks in public paper artifacts.
- **Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` is a tracked file in Git.

## Operational Constraints
- Preserve exact dataset seeds and random generator configurations across benchmarks.
- Format all equations, tables, and metric plots to meet camera-ready typesetting standards.

