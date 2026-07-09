#!/usr/bin/env python3
"""Discover likely install, build, test, and start commands."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".gradle",
    ".ship-council",
    ".vite",
    "build",
    "dist",
    "node_modules",
    "out",
    "target",
}


def is_skipped(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def package_manager_for(path: Path) -> str:
    root = path.parent
    if (root / "pnpm-lock.yaml").exists():
        return "pnpm"
    if (root / "yarn.lock").exists():
        return "yarn"
    return "npm"


def package_json_commands(file: Path) -> list[dict]:
    data = json.loads(file.read_text())
    scripts = data.get("scripts", {})
    pm = package_manager_for(file)
    commands = []
    for key in ["install", "build", "test", "lint", "typecheck", "start", "dev"]:
        if key == "install":
            commands.append({"kind": key, "cwd": str(file.parent), "command": f"{pm} install"})
        elif key in scripts:
            commands.append({"kind": key, "cwd": str(file.parent), "command": f"{pm} run {key}"})
    return commands


def gradle_task(repo: Path, file: Path, task: str) -> tuple[str, str]:
    wrapper = "./gradlew" if (repo / "gradlew").exists() else "gradle"
    if file.parent == repo:
        return str(repo), f"{wrapper} {task}"
    module = ":" + ":".join(file.parent.relative_to(repo).parts)
    return str(repo), f"{wrapper} {module}:{task}"


def java_commands(repo: Path, file: Path) -> list[dict]:
    if file.name == "pom.xml":
        return [
            {"kind": "test", "cwd": str(file.parent), "command": "mvn test"},
            {"kind": "package", "cwd": str(file.parent), "command": "mvn package"},
        ]
    if file.name in {"build.gradle", "build.gradle.kts"}:
        test_cwd, test_cmd = gradle_task(repo, file, "test")
        build_cwd, build_cmd = gradle_task(repo, file, "build")
        return [
            {"kind": "test", "cwd": test_cwd, "command": test_cmd},
            {"kind": "build", "cwd": build_cwd, "command": build_cmd},
        ]
    return []


def github_workflow_commands(file: Path) -> list[dict]:
    commands = []
    for line in file.read_text(errors="ignore").splitlines():
        stripped = line.strip()
        if stripped.startswith("run:"):
            commands.append({"kind": "ci-run", "cwd": str(file.parent), "command": stripped.removeprefix("run:").strip()})
    return commands[:20]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo")
    args = parser.parse_args()
    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        parser.error(f"repo does not exist: {repo}")

    commands = []
    for file in repo.rglob("*"):
        rel = file.relative_to(repo)
        if is_skipped(rel) or not file.is_file():
            continue
        if file.name == "package.json":
            commands.extend(package_json_commands(file))
        elif file.name in {"pom.xml", "build.gradle", "build.gradle.kts"}:
            commands.extend(java_commands(repo, file))
        elif ".github/workflows" in rel.as_posix() and file.suffix in {".yml", ".yaml"}:
            commands.extend(github_workflow_commands(file))

    print(json.dumps(commands, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
