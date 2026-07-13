#!/usr/bin/env python3
"""Create fix packet drafts from open findings."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-") or "finding"


def load_findings(task_dir: Path) -> list[dict]:
    findings = []
    for file in sorted((task_dir / "findings").glob("*.json")):
        data = json.loads(file.read_text())
        findings.extend(data if isinstance(data, list) else [data])
    return [f for f in findings if f.get("status") == "open"]


def packet_text(finding: dict, loop_index: int) -> str:
    files = "\n".join(f"- {p}" for p in finding.get("files", [])) or "- TBD"
    return f"""# Fix Packet: {finding.get("id", "SC-000")}

## Source Finding

{finding.get("id", "")} ({finding.get("stage", "")})

## Target Surface

{finding.get("target_surface", "unknown")}

## Target Agent

{finding.get("target_surface", "unknown")} developer

## Severity

{finding.get("severity", "medium")}

## Files In Scope

{files}

## Required Changes

{finding.get("required_change", "")}

## Evidence

{finding.get("evidence", "")}

## Out Of Scope

Unrelated refactors and behavior not required by the source finding.

## Acceptance Checks

{finding.get("acceptance", "")}

## Loop Index

{loop_index}
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_dir")
    parser.add_argument("--loop", type=int, default=1)
    args = parser.parse_args()
    task_dir = Path(args.task_dir).expanduser().resolve()
    out_dir = task_dir / "fix-packets"
    out_dir.mkdir(exist_ok=True)

    count = 0
    for finding in load_findings(task_dir):
        name = f"{finding.get('id', 'SC-000')}-{slugify(finding.get('category', 'finding'))}.md"
        (out_dir / name).write_text(packet_text(finding, args.loop))
        count += 1
    print(f"created {count} fix packet(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
