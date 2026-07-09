#!/usr/bin/env python3
"""Validate Ship Council packaging without machine-local dependencies."""

from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ship-council"


def fail(message: str) -> None:
    raise SystemExit(message)


def load_json(path: Path) -> dict:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - script should print a concise failure
        fail(f"{path}: invalid JSON: {exc}")
    if not isinstance(payload, dict):
        fail(f"{path}: expected JSON object")
    return payload


def validate_skill() -> None:
    skill_md = SKILL / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    frontmatter = text[4:end]
    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"SKILL.md missing frontmatter field {field}")
    line_count = len(text.splitlines())
    if line_count > 120:
        fail(f"SKILL.md is too heavy for a frequently-triggered skill: {line_count} lines > 120")
    required_phrases = (
        "Stay context-light by default",
        "Default to `quick`",
        "Do not read all references",
    )
    for phrase in required_phrases:
        if phrase not in text:
            fail(f"SKILL.md missing context-budget rule: {phrase}")
    for path in (
        SKILL / "references" / "memory-policy.md",
        SKILL / "references" / "agent-topology.md",
        SKILL / "references" / "context-loading.md",
        SKILL / "references" / "grill-gate.md",
        SKILL / "assets" / "templates" / "proposal-critique.md",
        SKILL / "scripts" / "init_task.py",
        SKILL / "scripts" / "check_memory_conflicts.py",
    ):
        if not path.exists():
            fail(f"missing expected skill file: {path.relative_to(ROOT)}")
    expected_briefs = {
        "research-agent.md",
        "proposal-critic-agent.md",
        "surface-developer-agent.md",
        "review-agent.md",
        "security-agent.md",
        "verification-agent.md",
        "dependency-agent.md",
        "data-migration-agent.md",
        "external-service-agent.md",
        "rollout-observability-agent.md",
        "memory-agent.md",
    }
    briefs_dir = SKILL / "references" / "agent-briefs"
    existing_briefs = {path.name for path in briefs_dir.glob("*.md")}
    missing_briefs = sorted(expected_briefs - existing_briefs)
    if missing_briefs:
        fail(f"missing agent briefs: {', '.join(missing_briefs)}")
    for path in briefs_dir.glob("*.md"):
        brief_lines = len(path.read_text(encoding="utf-8").splitlines())
        if brief_lines > 24:
            fail(f"{path.relative_to(ROOT)} is too verbose for an agent brief: {brief_lines} lines > 24")
        brief_text = path.read_text(encoding="utf-8")
        for phrase in ("Mission:", "Read:", "Do:", "Output"):
            if phrase not in brief_text:
                fail(f"{path.relative_to(ROOT)} missing high-density section: {phrase}")
    topology = SKILL / "references" / "agent-topology.md"
    topology_lines = len(topology.read_text(encoding="utf-8").splitlines())
    if topology_lines > 70:
        fail(f"{topology.relative_to(ROOT)} is too verbose: {topology_lines} lines > 70")
    reference_limits = {
        "context-loading.md": 60,
        "grill-gate.md": 40,
    }
    for name, limit in reference_limits.items():
        ref = SKILL / "references" / name
        ref_lines = len(ref.read_text(encoding="utf-8").splitlines())
        if ref_lines > limit:
            fail(f"{ref.relative_to(ROOT)} is too verbose: {ref_lines} lines > {limit}")
    for phrase in ("references/context-loading.md", "references/grill-gate.md"):
        if phrase not in text:
            fail(f"SKILL.md missing route: {phrase}")


def validate_plugin_manifest() -> None:
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)
    required = ("name", "version", "description", "author", "skills", "interface")
    for field in required:
        if field not in manifest:
            fail(f"{manifest_path}: missing {field}")
    if manifest["name"] != "ship-council":
        fail("plugin name must be ship-council")
    if manifest["skills"] != "./skills/":
        fail("plugin skills path must be ./skills/")
    if not (ROOT / manifest["skills"]).is_dir():
        fail("plugin skills path does not exist")
    interface = manifest["interface"]
    for field in ("displayName", "shortDescription", "longDescription", "defaultPrompt"):
        if field not in interface:
            fail(f"{manifest_path}: missing interface.{field}")


def validate_marketplace(path: Path, *, codex: bool) -> None:
    data = load_json(path)
    if data.get("name") != "ship-council":
        fail(f"{path}: marketplace name must be ship-council")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail(f"{path}: expected one plugin entry")
    plugin = plugins[0]
    if plugin.get("name") != "ship-council":
        fail(f"{path}: plugin entry must be ship-council")
    source = plugin.get("source")
    rel = source.get("path") if isinstance(source, dict) else source
    if rel != "./":
        fail(f"{path}: source path must be ./")
    if codex:
        policy = plugin.get("policy")
        if not isinstance(policy, dict):
            fail(f"{path}: missing policy")
        for field in ("installation", "authentication"):
            if field not in policy:
                fail(f"{path}: missing policy.{field}")


def run_smoke_tests() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        repo.mkdir()
        task_title = "distribution smoke"
        task_output = subprocess.check_output(
            ["python3", str(SKILL / "scripts" / "init_task.py"), str(repo), task_title],
            text=True,
        ).strip()
        subprocess.check_call(
            ["python3", str(SKILL / "scripts" / "validate_artifacts.py"), task_output]
        )
        subprocess.check_call(["python3", str(SKILL / "scripts" / "init_memory.py"), str(repo)])
        memory_file = repo / ".ship-council" / "memory" / "verification-recipes.md"
        with memory_file.open("a", encoding="utf-8") as handle:
            handle.write("\n## Integration Tests\n\n- Before e2e tests, start backend before frontend.\n")
        conflict = subprocess.check_output(
            [
                "python3",
                str(SKILL / "scripts" / "check_memory_conflicts.py"),
                str(repo),
                "verification-recipes.md",
                "--text",
                "From now on, start frontend before backend for e2e.",
            ],
            text=True,
        )
        payload = json.loads(conflict)
        if not payload["candidate_existing_rules"]:
            fail("memory conflict smoke test did not find a candidate rule")
    shutil.rmtree(ROOT / ".ship-council", ignore_errors=True)


def main() -> None:
    validate_skill()
    validate_plugin_manifest()
    validate_marketplace(ROOT / ".agents" / "plugins" / "marketplace.json", codex=True)
    validate_marketplace(ROOT / ".claude-plugin" / "marketplace.json", codex=False)
    load_json(ROOT / ".claude-plugin" / "plugin.json")
    run_smoke_tests()
    print("Ship Council distribution valid")


if __name__ == "__main__":
    main()
