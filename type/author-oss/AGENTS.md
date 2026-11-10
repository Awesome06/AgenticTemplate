---
mode: author-oss
---
# Workspace Agent Directives (Author-Maintained Open-Source Library)

## Governance & Architecture
- **Repository Mode:** Public open-source library authored and maintained by the user (`mode: author-oss`).
- **Maintainer Authority:** Full maintainer architectural authority without upstream contributor subservience. Author sets coding conventions and architectural contracts. Exempt from guest-contributor reproducer gates.
- **Public Open-Source Hygiene:**
  - Mandatory public CI/CD matrix parity across Linux, macOS, and Windows.
  - SemVer release tagging adhering to `globals/git-release`.
  - Clean `AGENTS.md` and repository text with zero local machine path leaks.
  - Root-anchored `.gitignore` exclusions preventing local dynamic agent junctions from leaking into public Git tracking.
  - Canonical community assets committed: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue/PR templates.
- **Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` is a tracked file in Git.

## Operational Constraints
- Run local CI parity gates before creating releases.
- Ensure all public APIs have accompanying docstrings, type annotations, and regression tests.

