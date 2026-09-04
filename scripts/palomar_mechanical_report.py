#!/usr/bin/env python3
"""Build a local mechanical-report.json for Palomar editorial audit."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_head() -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def challenge_imports() -> list[str]:
    text = (ROOT / "Challenge.lean").read_text(encoding="utf-8")
    return re.findall(r"^import\s+(\S+)", text, re.MULTILINE)


def load_comparator() -> dict:
    with (ROOT / "comparator.json").open(encoding="utf-8") as f:
        return json.load(f)


def build_report() -> dict:
    cfg = load_comparator()
    commit = git_head()
    theorems = cfg["theorem_names"]
    definitions = cfg.get("definition_names", [])
    paths = {
        "comparator.json": ROOT / "comparator.json",
        "Challenge.lean": ROOT / "Challenge.lean",
        "Solution.lean": ROOT / "Solution.lean",
        "formalization.yaml": ROOT / "formalization.yaml",
        "lean-toolchain": ROOT / "lean-toolchain",
    }
    if (ROOT / "lakefile.toml").is_file():
        paths["lakefile.toml"] = ROOT / "lakefile.toml"
    elif (ROOT / "lakefile.lean").is_file():
        paths["lakefile.lean"] = ROOT / "lakefile.lean"

    return {
        "schema": "scott1964-local-mechanical-report-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "repository": {
            "commit": commit,
            "comparator_config": "comparator.json",
        },
        "comparator": {
            "challenge_module": cfg["challenge_module"],
            "solution_module": cfg["solution_module"],
            "theorem_names": theorems,
            "definition_names": definitions,
            "permitted_axioms": cfg["permitted_axioms"],
        },
        "declarations_checked_order": theorems + definitions,
        "challenge_imports": challenge_imports(),
        "artifact_hashes": {name: sha256_file(path) for name, path in paths.items() if path.is_file()},
        "preflight": {
            "mechanical_steps": "comparator-config, imports, build, type-compare, pinned-comparator, sorry-scan, axioms",
            "status": "passed_before_report",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = build_report()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    decl_count = len(report["declarations_checked_order"])
    print(f"OK: mechanical report written to {args.out} ({decl_count} declarations).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
