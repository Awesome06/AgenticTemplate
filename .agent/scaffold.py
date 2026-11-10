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

ARCHETYPE_METADATA = {
    "personal": {
        "title": "Personal Project (mode: personal)",
        "scope": "Private applications, scripts, personal harness, rapid prototyping.",
        "invariants": [
            "Velocity-first engineering with local test parity",
            "Exempt from external OSS gatekeeping and artificial reproducer gates",
            "Direct machine vault dynamic links in .agents/skills/",
            "Universal .git/info/exclude hygiene with tracked AGENTS.md",
        ],
    },
    "team": {
        "title": "Team / Hackathon Project (mode: team)",
        "scope": "Collaborative multi-author repos, competition submissions, fast product showcases.",
        "invariants": [
            "Mandatory concurrency race sanitizers (-race in Go, TSAN in C++/Rust, asyncio loop isolation)",
            "Demo-first alignment with 120-second choreography in DEMO_VIDEO_SCRIPT.md",
            "Non-blocking asynchronous execution and atomic modular commits",
            "Multi-author pre-commit verification before pushing to shared branches",
        ],
    },
    "oss": {
        "title": "External Open-Source Contribution (mode: oss)",
        "scope": "Guest contributions, bug fixes, and feature proposals to upstream OSS repositories.",
        "invariants": [
            "Maintainer precedence: upstream CONTRIBUTING.md and maintainer taste govern with absolute priority",
            "Red-Test Reproducer Gate (Mode A): modifying source before an isolated failing TestIssueXXXXX is FORBIDDEN",
            "Diff Noise Ceiling: all PR diffs must have <= 5% whitespace or stylistic churn",
            "Closed PR Non-Reopening Invariant: gh pr reopen is strictly forbidden on closed pull requests",
            "Mental Anti-Slop Scrubber: zero corporate jargon, AI hallmarks, or raw terminal dumps",
        ],
    },
    "research": {
        "title": "Academic Research Paper (mode: research)",
        "scope": "Empirical software engineering papers, benchmark suites, artifact evaluation packages.",
        "invariants": [
            "Targeting CORE A* and A venues (ISSTA, FSE, ASE, MSR, EDM) with double-blind anonymity audits",
            "4-quadrant Threats to Validity coverage: Internal, External, Construct, Conclusion",
            "Non-parametric SE statistics: Vargha-Delaney A12, Cliff's delta, Wilson CI, Benjamini-Hochberg FDR",
            "Three-tier reproducible artifact runner: run_all.sh --dry-run (<60s), --sample (<15m), --full",
            "Strict {metric_originTech} placeholder formatting for unavailable or pending evaluation metrics",
        ],
    },
    "author-oss": {
        "title": "Author-Maintained Open-Source Library (mode: author-oss)",
        "scope": "Public libraries, tools, and runtimes authored and maintained by the user.",
        "invariants": [
            "Full maintainer authority: author sets architectural contracts and conventions",
            "Exempt from guest-contributor reproducer gates; author may reopen PRs and direct evolution",
            "Public CI/CD matrix parity across Linux, macOS, and Windows",
            "Strict SemVer releases adhering to globals/git-release",
            "Canonical community surface: LICENSE, CONTRIBUTING.md, SECURITY.md, CODE_OF_CONDUCT.md, issue/PR templates",
            "Clean AGENTS.md with zero local machine path leaks and root-anchored .gitignore exclusions",
        ],
    },
}


def list_archetypes() -> None:
    print("\n" + "=" * 78)
    print("AgenticTemplate - 5-Tier Governance Archetypes")
    print("=" * 78)
    for mode, meta in ARCHETYPE_METADATA.items():
        print(f"\n[Tier] {meta['title']}")
        print(f"  Scope:      {meta['scope']}")
        print("  Invariants:")
        for inv in meta["invariants"]:
            print(f"    - {inv}")
    print("\n" + "=" * 78)
    print("Usage:")
    print("  python .agent/scaffold.py --type <tier> [--update] [--force] [--workspace <path>]")
    print("  .\\.agent\\setup.ps1 -Type <tier>")
    print("=" * 78 + "\n")


def apply_archetype(
    target_type: str,
    force: bool = False,
    update_only: bool = False,
    workspace_path: Path = REPO_ROOT,
) -> None:
    if target_type not in VALID_TYPES:
        print(
            f"[scaffold] Error: Invalid project type '{target_type}'. Valid choices: {', '.join(VALID_TYPES)}",
            file=sys.stderr,
        )
        sys.exit(1)

    archetype_dir = TYPE_DIR / target_type
    if not archetype_dir.is_dir():
        print(
            f"[scaffold] Error: Archetype directory not found at {archetype_dir}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"[scaffold] Applying archetype '{target_type}' to workspace: {workspace_path}")

    # 1. Update/Write AGENTS.md
    src_agents = archetype_dir / "AGENTS.md"
    dst_agents = workspace_path / "AGENTS.md"
    if src_agents.is_file():
        if not dst_agents.exists() or force or update_only:
            shutil.copy2(src_agents, dst_agents)
            print(f"[scaffold] Synced AGENTS.md for {target_type}")
        else:
            # Ensure frontmatter mode is updated if AGENTS.md exists
            content = dst_agents.read_text(encoding="utf-8")
            if not content.startswith(f"---\nmode: {target_type}\n---"):
                if content.startswith("---"):
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
    agents_dir = workspace_path / ".agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    mode_file = agents_dir / "mode"
    mode_file.write_text(target_type, encoding="utf-8")
    print(f"[scaffold] Wrote .agents/mode -> {target_type}")

    # 3. Copy archetype assets (README, community files, scripts, workflows)
    scaffolded_count = 0
    for src_file in archetype_dir.rglob("*"):
        if src_file.is_file() and src_file.name != "AGENTS.md":
            rel_path = src_file.relative_to(archetype_dir)
            target_dest = workspace_path / rel_path

            if target_dest.exists() and not force and not update_only:
                continue

            target_dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, target_dest)
            scaffolded_count += 1
            print(f"[scaffold] Scaffolding {rel_path}")

    print(
        f"[scaffold] Workspace successfully configured with '{target_type}' governance rules ({scaffolded_count} assets processed)."
    )


def main():
    parser = argparse.ArgumentParser(
        description="AgenticTemplate Monorepo Project Archetype Scaffolder."
    )
    parser.add_argument(
        "--type",
        "-t",
        "--preset",
        "-p",
        dest="target_type",
        choices=VALID_TYPES,
        default=None,
        help="Project governance type (personal, team, oss, research, author-oss)",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List all 5 governance archetypes and their key invariants",
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
    parser.add_argument(
        "--workspace",
        "-w",
        type=Path,
        default=REPO_ROOT,
        help="Target workspace directory (default: current repository root)",
    )
    args = parser.parse_args()

    if args.list:
        list_archetypes()
        return

    target_type = args.target_type or "personal"
    apply_archetype(
        target_type,
        force=args.force,
        update_only=args.update,
        workspace_path=args.workspace,
    )


if __name__ == "__main__":
    main()
