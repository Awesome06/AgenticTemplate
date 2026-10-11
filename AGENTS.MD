# Workspace Agent Directives

## Bootstrap Protocol
- On session initialization:
  1. Check if the local `.agent/skills/` directory contains active domain skills.
  2. If the directory is missing or empty, immediately invoke the global `workspace-initializer` skill.
  3. Analyze the repository structure, `README.md` intent, and dependency files to identify the intended architecture.
  4. Once skills are linked, strictly enforce their constraints during all subsequent code generation and review tasks.

## General Constraints
- Do not add or remove third-party dependencies without explicit user confirmation.
- Keep the context window lean: do not load files into context unless actively modifying them.
