---
title: Initial Architectural Baseline
type: adr
status: active
tags: [adr, baseline, setup]
---

# ADR 001: Initial Architectural Baseline

## Context
Establishes the foundational project layout, agentic skill integration, and repository wiki knowledge graph.

## Decision
1. Organize project components around modular boundaries.
2. Link the repository to the centralized agent skills vault for hardened engineering directives.
3. Maintain atomic architectural decision records (ADRs) and domain specifications in `wiki/`.

## Consequences
- Every new architectural pivot MUST be captured in a sequential ADR in `wiki/adr/`.
- Cross-references use bidirectional `[[target-note]]` wikilink syntax.

## References
- Root Knowledge Graph: [[wiki/index]]
- System Architecture: [[wiki/architecture]]
