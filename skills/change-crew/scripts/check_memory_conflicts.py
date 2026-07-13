#!/usr/bin/env python3
"""Surface nearby long-term memory rules before writing a new rule.

This helper is intentionally conservative: it finds related existing lines, but
the orchestrator still makes the final semantic conflict judgment.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


MEMORY_FILES = {
    "project-profile.md",
    "coding-constraints.md",
    "surface-map.md",
    "verification-recipes.md",
    "security-constraints.md",
    "decisions.md",
    "lessons-learned.md",
}

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "before",
    "by",
    "do",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "run",
    "should",
    "the",
    "then",
    "this",
    "to",
    "use",
    "when",
    "with",
}


def tokens(text: str) -> set[str]:
    words = {word.lower() for word in re.findall(r"[A-Za-z0-9_.:/-]{3,}", text)}
    return {word for word in words if word not in STOPWORDS}


def read_proposal(args: argparse.Namespace) -> str:
    if args.text:
        return args.text
    if args.proposal_file:
        return Path(args.proposal_file).expanduser().read_text(encoding="utf-8")
    if not sys.stdin.isatty():
        return sys.stdin.read()
    raise SystemExit("provide --text, --proposal-file, or stdin")


def candidate_lines(memory_file: Path, proposal_tokens: set[str]) -> list[dict[str, object]]:
    if not memory_file.exists():
        return []
    results = []
    current_heading = ""
    for line_no, raw_line in enumerate(memory_file.read_text(encoding="utf-8").splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("#"):
            current_heading = line
            continue
        line_tokens = tokens(line)
        overlap = sorted(proposal_tokens & line_tokens)
        score = len(overlap)
        if score:
            results.append(
                {
                    "line": line_no,
                    "heading": current_heading,
                    "text": line,
                    "overlap_terms": overlap,
                    "score": score,
                }
            )
    return sorted(results, key=lambda item: (-int(item["score"]), int(item["line"])))[:12]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", help="Target repository path")
    parser.add_argument("target_memory_file", help="Memory file name, such as verification-recipes.md")
    parser.add_argument("--text", help="Proposed memory rule text")
    parser.add_argument("--proposal-file", help="File containing proposed memory rule")
    args = parser.parse_args()

    repo = Path(args.repo).expanduser().resolve()
    if not repo.exists():
        parser.error(f"repo does not exist: {repo}")
    if args.target_memory_file not in MEMORY_FILES:
        parser.error(f"target_memory_file must be one of: {', '.join(sorted(MEMORY_FILES))}")

    proposal = read_proposal(args).strip()
    if not proposal:
        parser.error("proposed memory rule is empty")

    memory_dir = repo / ".change-crew" / "memory"
    target = memory_dir / args.target_memory_file
    proposal_tokens = tokens(proposal)
    candidates = candidate_lines(target, proposal_tokens)

    payload = {
        "target_file": args.target_memory_file,
        "memory_file": str(target),
        "memory_exists": target.exists(),
        "proposal": proposal,
        "candidate_existing_rules": candidates,
        "requires_semantic_review": True,
        "note": "Candidate rules are lexical neighbors, not automatic conflicts. The orchestrator must decide whether rules conflict.",
    }
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
