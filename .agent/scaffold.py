#!/usr/bin/env python3
"""
.agent/scaffold.py - Monorepo Project Archetype Scaffolding for AgenticTemplate.

Applies project archetypes from `type/<type>/` across the 5-tier governance architecture:
1. personal   - Rapid prototyping, private developer harness.
2. team       - Collaborative multi-author development, race sanitizers, 120s demo video.
3. oss        - External open-source contributor rules, red-test reproducer gate.
4. research   - Academic double-blind review rigor, Threats to Validity, statistical rigor.
5. author-oss - Author-maintained public open source, SemVer release tagging, canonical community surface.
"""

import argparse
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TYPE_DIR = REPO_ROOT / "type"
VALID_TYPES = ["personal", "team", "oss", "research", "author-oss"]


def apply_archetype(target_type: str, force: bool = False, update_only: bool = False) -> None:
    if target_type not in VALID_TYPES:
        print(f"[scaffold] Error: Invalid project type '{target_type}'. Valid choices: {', '.join(VALID_TYPES)}", file=sys.stderr)
        sys.exit(1)

    archetype_dir = TYPE_DIR / target_type
    if not archetype_dir.is_dir():
        print(f"[scaffold] Error: Archetype directory not found at {archetype_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"[scaffold] Applying archetype: {target_type}")

    # 1. Update/Write AGENTS.md
    src_agents = archetype_dir / "AGENTS.md"
    dst_agents = REPO_ROOT / "AGENTS.md"
    if src_agents.is_file():
        if not dst_agents.exists() or force or update_only:
            shutil.copy2(src_agents, dst_agents)
            print(f"[scaffold] Synced AGENTS.md for {target_type}")
        else:
            # Ensure frontmatter mode is updated if AGENTS.md exists
            content = dst_agents.read_text(encoding="utf-8")
            if not content.startswith(f"---\nmode: {target_type}\n---"):
                if content.startswith("---"):
                    # Replace frontmatter
                    parts = content.split("---", 2)
                    if len(parts) >= 3:
                        new_content = f"---\nmode: {target_type}\n---" + parts[2]
                    else:
                        new_content = f"---\nmode: {target_type}\n---\n" + content
                else:
                    new_content = f"---\nmode: {target_type}\n---\n" + content
                dst_agents.write_text(new_content, encoding="utf-8")
                print(f"[scaffold] Updated mode to '{target_type}' in AGENTS.md frontmatter")

    # 2. Write mode marker
    agents_dir = REPO_ROOT / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    mode_file = agents_dir / "mode"
    mode_file.write_text(target_type, encoding="utf-8")
    print(f"[scaffold] Wrote .agents/mode -> {target_type}")

    # 3. Copy archetype assets (README, community files, scripts)
    for src_file in archetype_dir.rglob("*"):
        if src_file.is_file() and src_file.name != "AGENTS.md":
            rel_path = src_file.relative_to(archetype_dir)
            target_dest = REPO_ROOT / rel_path

            if target_dest.exists() and not force:
                continue

            target_dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, target_dest)
            print(f"[scaffold] Scaffolding {rel_path}")

    print(f"[scaffold] Project successfully initialized with {target_type} governance rules.")


def main():
    parser = argparse.ArgumentParser(description="AgenticTemplate Monorepo Project Archetype Scaffolder.")
    parser.add_argument(
        "--type",
        "-t",
        choices=VALID_TYPES,
        default="personal",
        help="Project governance type (default: personal)",
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Overwrite existing workspace files",
    )
    parser.add_argument(
        "--update",
        "-u",
        action="store_true",
        help="Update rules in-place from archetype without replacing custom files",
    )
    args = parser.parse_args()

    apply_archetype(args.type, force=args.force, update_only=args.update)


if __name__ == "__main__":
    main()
