---
mode: team
---
# Workspace Agent Directives (Team / Hackathon Project)

## Governance & Architecture
- **Repository Mode:** Collaborative team / hackathon repository (`mode: team`).
- **Concurrency & Sanitizers:** Code paths with shared state or async actors MUST pass race sanitizers (`-race` in Go, thread sanitizer in Rust/C++, strict asyncio loop isolation in Python).
- **Demo-First Alignment:** For hackathons or fast product showcases, all features align with the 120-second demo script in `DEMO_VIDEO_SCRIPT.md`.
- **Direct Vault Integration:** Dynamic skills are mounted directly from the central machine vault into `.agents/skills/`. Pinned submodules are eliminated.
- **Exclude Hygiene:** Dynamic agent paths (`.agents/skills/*`, `.agents/.skill-leases.json`, `.agents/.turn-cache.json`, `.agents/mode`) MUST remain in `.git/info/exclude`. `AGENTS.md` is a tracked file in Git.

## Operational Constraints
- Ensure non-blocking async execution across API endpoints and queue workers.
- Avoid branch collision by keeping commits atomic and clearly scoped to specific subsystem modules.
- Run multi-author pre-commit verification before pushing to shared branches.

