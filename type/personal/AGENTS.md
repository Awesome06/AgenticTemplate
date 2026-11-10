---
mode: personal
---
# Workspace Agent Directives (Personal Project)

## Governance & Architecture
- **Repository Mode:** Personal repository (`mode: personal`).
- **Autonomy & Velocity:** Rapid prototyping and personal harness govern. Exempt from external OSS gatekeeping, maintainer taste mimicry, or red-test reproducer gates.
- **Direct Vault Integration:** Dynamic skills are mounted directly from the central machine vault into `.agents/skills/`. Pinned submodules are eliminated.
- **Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` is a tracked file in Git.

## Operational Constraints
- Keep the context window lean: do not load files into context unless actively inspecting or modifying them.
- Preserve existing comments and docstrings unless explicitly asked to modify them.
- Run active linters and tests locally before proposing commits.

