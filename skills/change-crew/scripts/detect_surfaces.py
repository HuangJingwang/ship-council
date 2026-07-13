#!/usr/bin/env python3
"""Detect likely app surfaces from repository files."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SIGNALS = {
    "backend": ["pom.xml", "build.gradle", "build.gradle.kts", "src/main/java", "src/main/kotlin", "controllers", "controller"],
    "web": ["package.json", "vite.config.ts", "vite.config.js", "next.config.js", "next.config.mjs", "src/components", "pages", "app"],
    "mobile": ["ios", "android", "pubspec.yaml", "app.json", "expo", "react-native.config.js"],
    "desktop": ["src-tauri", "tauri.conf.json", "electron", "electron-builder.yml"],
    "data": ["migrations", "prisma", "liquibase", "flyway", "db/migration", ".sql"],
    "infra": ["docker-compose.yml", "Dockerfile", ".github/workflows", "k8s", "helm", "terraform"],
    "docs": ["docs", "README.md", "openapi.yaml", "openapi.json"],
    "test": ["tests", "test", "e2e", "playwright.config.ts", "cypress.config.ts"],
}

SKIP_DIRS = {
    ".git",
    ".gradle",
    ".idea",
    ".change-crew",
    ".vite",
    ".vscode",
    "build",
    "dist",
    "node_modules",
    "out",
    "target",
}

def iter_paths(repo: Path, max_depth: int = 5):
    for path in repo.rglob("*"):
        rel = path.relative_to(repo)
        parts = rel.parts
        if any(part in SKIP_DIRS for part in parts):
            continue
        if len(parts) > max_depth:
            continue
        yield rel, path


def matches(signal: str, rel: Path, path: Path) -> bool:
    rel_text = rel.as_posix()
    name = path.name
    if signal.startswith("."):
        return name.endswith(signal)
    return rel_text == signal or rel_text.endswith(f"/{signal}") or name.lower() == signal.lower()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo")
    args = parser.parse_args()
    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        parser.error(f"repo does not exist: {repo}")

    all_paths = list(iter_paths(repo))
    result = {}
    for surface, signals in SIGNALS.items():
        hits = []
        for signal in signals:
            for rel, path in all_paths:
                if matches(signal, rel, path):
                    hits.append(rel.as_posix())
                    break
        if hits:
            result[surface] = {"signals": hits}

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
