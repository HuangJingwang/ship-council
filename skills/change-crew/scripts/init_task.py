#!/usr/bin/env python3
"""Create a Change Crew task workspace from bundled templates."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import date
from pathlib import Path


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "task"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Target repository path")
    parser.add_argument("title", help="Task title")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        parser.error(f"repo does not exist: {repo}")

    skill_dir = Path(__file__).resolve().parents[1]
    templates = skill_dir / "assets" / "templates"
    task_id = f"{date.today().isoformat()}-{slugify(args.title)}"
    task_dir = repo / ".change-crew" / "tasks" / task_id
    task_dir.mkdir(parents=True, exist_ok=True)
    (task_dir / "findings").mkdir(exist_ok=True)
    (task_dir / "fix-packets").mkdir(exist_ok=True)

    for name in [
        "prd.md",
        "surface-map.md",
        "impact-analysis.md",
        "research.md",
        "deliberation.md",
        "proposal-critique.md",
        "contract.md",
        "test-plan.md",
        "environment-report.md",
        "implementation-plan.md",
        "git-pr-plan.md",
        "verification-report.md",
        "retrospective.md",
        "memory-suggestions.md",
        "final-report.md",
    ]:
        dest = task_dir / name
        if not dest.exists():
            shutil.copyfile(templates / name, dest)

    manifest = task_dir / "change-crew.json"
    if not manifest.exists():
        data = json.loads((templates / "change-crew.json").read_text())
        data["task_id"] = task_id
        data["created_at"] = date.today().isoformat()
        manifest.write_text(json.dumps(data, indent=2) + "\n")

    print(task_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
