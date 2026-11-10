---
mode: oss
---
# Workspace Agent Directives (External Open-Source Contribution)

## Governance & Architecture
- **Repository Mode:** External open-source repository contribution (`mode: oss`).
- **Maintainer Precedence:** Upstream `CONTRIBUTING.md`, PR templates, and maintainer architectural conventions govern with absolute precedence. Personal preferences are subservient to project taste.
- **Red-Test Reproducer Gate (Mode A):** Modifying existing source code before authoring and executing an isolated failing reproduction test (`TestIssueXXXXX`) is STRICTLY FORBIDDEN.
- **Diff Noise Ceiling:** All PR diffs must have <= 5% pure whitespace or stylistic churn. Never reformat unrelated lines or inject unnecessary comments.
- **Closed PR Non-Reopening Invariant:** Reopening a closed pull request (`gh pr reopen`) is STRICTLY FORBIDDEN. Seek alignment on issues or open a fresh branch.
- **Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` is a tracked file in Git.

## Operational Constraints
- Preserve exact project naming and architectural patterns.
- Follow the repository's native PR template completely without omitting required checklist items.
- Mental Anti-Slop Scrubber: Prohibit corporate jargon, AI hallmarks ("delve", "tapestry"), and raw terminal log dumps.

