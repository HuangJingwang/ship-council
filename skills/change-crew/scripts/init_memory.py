#!/usr/bin/env python3
"""Create a Change Crew long-term memory directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


MEMORY_FILES = [
    "project-profile.md",
    "coding-constraints.md",
    "surface-map.md",
    "verification-recipes.md",
    "security-constraints.md",
    "decisions.md",
    "lessons-learned.md",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Target repository path")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        parser.error(f"repo does not exist: {repo}")

    skill_dir = Path(__file__).resolve().parents[1]
    templates = skill_dir / "assets" / "templates" / "memory"
    memory_dir = repo / ".change-crew" / "memory"
    memory_dir.mkdir(parents=True, exist_ok=True)

    created = []
    for name in MEMORY_FILES:
        dest = memory_dir / name
        if not dest.exists():
            shutil.copyfile(templates / name, dest)
            created.append(name)

    print(memory_dir)
    if created:
        print("created: " + ", ".join(created))
    else:
        print("memory already initialized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
