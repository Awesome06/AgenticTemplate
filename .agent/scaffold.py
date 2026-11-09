#!/usr/bin/env python3
"""
.agent/scaffold.py - Workspace Preset Scaffolding Launcher for AgenticTemplate.

Applies project presets (such as 'author-oss' for public open-source releases)
to transform a freshly instantiated template workspace.
"""

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
VAULT_SCAFFOLD = REPO_ROOT / ".agent" / ".registry" / "scripts" / "scaffold-oss.py"


def main():
    parser = argparse.ArgumentParser(description="AgenticTemplate Workspace Preset Scaffolding.")
    parser.add_argument(
        "--preset",
        "-p",
        choices=["personal", "author-oss"],
        default="author-oss",
        help="Workspace preset archetype (default: author-oss)",
    )
    parser.add_argument("--name", "-n", default=None, help="Project name (default: directory name)")
    parser.add_argument("--license", "-l", choices=["apache-2.0", "mit"], default="apache-2.0", help="License type")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without modifying files")
    parser.add_argument("--force", "-f", action="store_true", help="Overwrite existing assets")
    args = parser.parse_args()

    if args.preset == "personal":
        print("[scaffold] Personal preset is the template default. No scaffolding changes required.")
        return

    if not VAULT_SCAFFOLD.is_file():
        # Attempt to initialize submodule
        print("[scaffold] .agent/.registry submodule not initialized. Initializing...")
        try:
            subprocess.run(["git", "submodule", "update", "--init", "--recursive"], cwd=str(REPO_ROOT), check=True)
        except Exception as e:
            print(f"[scaffold] Error initializing submodule: {e}", file=sys.stderr)
            sys.exit(1)

    if not VAULT_SCAFFOLD.is_file():
        print(f"[scaffold] Error: Scaffolding script not found at {VAULT_SCAFFOLD}", file=sys.stderr)
        sys.exit(1)

    cmd = [
        sys.executable,
        str(VAULT_SCAFFOLD),
        "--workspace",
        str(REPO_ROOT),
        "--license",
        args.license,
    ]
    if args.name:
        cmd.extend(["--name", args.name])
    if args.dry_run:
        cmd.append("--dry-run")
    if args.force:
        cmd.append("--force")

    ret = subprocess.call(cmd)
    sys.exit(ret)


if __name__ == "__main__":
    main()
