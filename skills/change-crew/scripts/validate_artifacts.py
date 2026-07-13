#!/usr/bin/env python3
"""Validate a Change Crew task workspace."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = [
    "change-crew.json",
    "prd.md",
    "surface-map.md",
    "impact-analysis.md",
    "proposal-critique.md",
    "contract.md",
    "test-plan.md",
    "environment-report.md",
    "implementation-plan.md",
    "verification-report.md",
    "memory-suggestions.md",
    "final-report.md",
]

FINDING_FIELDS = {
    "id",
    "stage",
    "target_surface",
    "severity",
    "category",
    "files",
    "evidence",
    "required_change",
    "acceptance",
    "status",
}

MANIFEST_STATES = {
    "INTAKE",
    "SURFACE_DISCOVERY",
    "IMPACT_ANALYSIS",
    "RESEARCH",
    "DELIBERATION",
    "PROPOSAL_CRITIQUE",
    "CONTRACT",
    "TEST_STRATEGY",
    "ENVIRONMENT_DISCOVERY",
    "IMPLEMENTATION",
    "REVIEW",
    "SECURITY",
    "DOCUMENTATION",
    "VERIFICATION",
    "FIX",
    "MEMORY_CAPTURE",
    "DONE",
    "BLOCKED",
}

HEADINGS = {
    "proposal-critique.md": ["## PRD Critique", "## Contract And Plan Critique"],
    "contract.md": ["## Interfaces", "## Permissions", "## Testing Obligations"],
    "test-plan.md": ["## Behaviors To Prove", "## Not Testing And Why"],
    "environment-report.md": ["## Commands", "## Environment Variables"],
    "verification-report.md": ["## Commands Run", "## Results"],
    "memory-suggestions.md": ["## Proposed Updates", "## Conflicts With Existing Memory"],
    "final-report.md": ["## Verification Status", "## Remaining Risks Or Gaps"],
}


def validate_findings(path: Path) -> list[str]:
    errors = []
    for file in path.glob("findings/*.json"):
        try:
            data = json.loads(file.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"{file}: invalid JSON: {exc}")
            continue
        items = data if isinstance(data, list) else [data]
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"{file}[{index}]: finding must be an object")
                continue
            missing = FINDING_FIELDS - set(item)
            if missing:
                errors.append(f"{file}[{index}]: missing fields {sorted(missing)}")
    return errors


def validate_manifest(task_dir: Path) -> list[str]:
    file = task_dir / "change-crew.json"
    if not file.exists():
        return ["missing change-crew.json"]
    try:
        data = json.loads(file.read_text())
    except json.JSONDecodeError as exc:
        return [f"change-crew.json: invalid JSON: {exc}"]
    errors = []
    if data.get("state") not in MANIFEST_STATES:
        errors.append("change-crew.json: invalid state")
    if data.get("mode") not in {"semi-auto", "auto"}:
        errors.append("change-crew.json: mode must be semi-auto or auto")
    if not isinstance(data.get("loop_index"), int) or not isinstance(data.get("loop_limit"), int):
        errors.append("change-crew.json: loop_index and loop_limit must be integers")
    if data.get("memory_update_policy") not in {"suggest-only", "auto-approved"}:
        errors.append("change-crew.json: memory_update_policy must be suggest-only or auto-approved")
    return errors


def validate_headings(task_dir: Path) -> list[str]:
    errors = []
    for name, headings in HEADINGS.items():
        file = task_dir / name
        if not file.exists():
            continue
        text = file.read_text()
        for heading in headings:
            if heading not in text:
                errors.append(f"{name}: missing heading {heading}")
    return errors


def validate_blockers(task_dir: Path) -> list[str]:
    errors = []
    for file in (task_dir / "findings").glob("*.json"):
        data = json.loads(file.read_text())
        items = data if isinstance(data, list) else [data]
        for item in items:
            if item.get("status") == "open" and item.get("severity") in {"critical", "high"}:
                errors.append(f"{file}: open blocker finding {item.get('id', '<missing id>')}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task_dir")
    args = parser.parse_args()
    task_dir = Path(args.task_dir).expanduser().resolve()

    errors = []
    for name in REQUIRED:
        if not (task_dir / name).exists():
            errors.append(f"missing {name}")
    errors.extend(validate_manifest(task_dir))
    errors.extend(validate_headings(task_dir))
    errors.extend(validate_findings(task_dir))
    errors.extend(validate_blockers(task_dir))

    if errors:
        print("\n".join(errors))
        return 1
    print("Change Crew artifacts valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
