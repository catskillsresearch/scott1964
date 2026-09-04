#!/usr/bin/env python3
"""Vendor a plain-file snapshot of palomar-preflight into a Lean project.

This is not a git submodule. Palomar rejects .gitmodules.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

UPSTREAM = "catskillsresearch/palomar-preflight"
DEFAULT_BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{UPSTREAM}"

TOOLKIT_PATHS = [
    "README.md",
    "LICENSE",
    "palomar-lib.sh",
    "palomar_paths.py",
    "palomar_preflight.sh",
    "verify-comparator.sh",
    "compare_challenge_solution_types.sh",
    "fake-landrun.sh",
    "landrun_passthrough.py",
    "palomar_editorial_audit.sh",
    "palomar_editorial_audit.py",
    "palomar_editorial_checks.py",
    "palomar_mechanical_report.py",
    "palomar_policy_sync.py",
    "palomar_preflight_sync.py",
    "requirements-editorial.txt",
]


def fetch_json(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    with urllib.request.urlopen(url, timeout=60) as resp:
        return resp.read().decode("utf-8")


def upstream_head_sha() -> str:
    data = fetch_json(f"https://api.github.com/repos/{UPSTREAM}/commits/{DEFAULT_BRANCH}")
    return data["sha"]


def read_pin(pin_path: Path) -> str | None:
    if not pin_path.is_file():
        return None
    pin = pin_path.read_text(encoding="utf-8").strip()
    return pin or None


def git_head(directory: Path) -> str:
    out = subprocess.check_output(
        ["git", "rev-parse", "HEAD"],
        cwd=directory,
        text=True,
    )
    return out.strip()


def copy_from_dir(source: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for rel in TOOLKIT_PATHS:
        src = source / rel
        if not src.is_file():
            raise SystemExit(f"FAIL: missing toolkit file {src}")
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        if target.suffix in {".sh", ".py"}:
            target.chmod(target.stat().st_mode | 0o111)


def download_from_github(commit: str, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for rel in TOOLKIT_PATHS:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        url = f"{RAW_BASE}/{commit}/{rel}"
        target.write_text(fetch_text(url), encoding="utf-8")
        if target.suffix in {".sh", ".py"}:
            target.chmod(target.stat().st_mode | 0o111)


def write_vendor_readme(root: Path, commit: str) -> None:
    (root / "VENDOR.md").write_text(
        f"""# Vendored palomar-preflight snapshot

Source: https://github.com/{UPSTREAM}
Commit: `{commit}`

This directory is a plain-file copy of the Palomar local preflight toolkit.
It is **not** a git submodule.

Refresh with:

```bash
python3 vendor/palomar-preflight/palomar_preflight_sync.py
```
""",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vendor palomar-preflight into vendor/palomar-preflight."
    )
    parser.add_argument("--root", type=Path, default=Path("vendor/palomar-preflight"))
    parser.add_argument("--pin", type=Path, default=Path("vendor/PALOMAR_PREFLIGHT_PIN"))
    parser.add_argument(
        "--from-dir",
        type=Path,
        help="copy from a local palomar-preflight checkout instead of GitHub",
    )
    parser.add_argument(
        "--no-sync",
        action="store_true",
        help="skip refresh; require an existing vendored snapshot",
    )
    args = parser.parse_args()
    root: Path = args.root
    pin_path: Path = args.pin

    if args.no_sync:
        if not root.is_dir() or not (root / "palomar_preflight.sh").is_file():
            print(f"FAIL: missing vendored preflight under {root}", file=sys.stderr)
            return 1
        pin = read_pin(pin_path)
        if not pin:
            print(f"FAIL: missing pin file {pin_path}", file=sys.stderr)
            return 1
        print(f"OK: using committed preflight pin {pin} (--no-sync)")
        return 0

    if args.from_dir is not None:
        source = args.from_dir.resolve()
        commit = git_head(source)
        copy_from_dir(source, root)
        write_vendor_readme(root, commit)
        pin_path.parent.mkdir(parents=True, exist_ok=True)
        pin_path.write_text(commit + "\n", encoding="utf-8")
        print(f"OK: vendored palomar-preflight from {source} at {commit}")
        return 0

    try:
        latest = upstream_head_sha()
    except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as err:
        print(f"FAIL: could not query upstream {UPSTREAM}: {err}", file=sys.stderr)
        return 1

    current = read_pin(pin_path)
    if current == latest and (root / "palomar_preflight.sh").is_file():
        print(f"OK: preflight pin matches upstream ({latest})")
        return 0

    try:
        download_from_github(latest, root)
        write_vendor_readme(root, latest)
        pin_path.parent.mkdir(parents=True, exist_ok=True)
        pin_path.write_text(latest + "\n", encoding="utf-8")
    except (urllib.error.URLError, TimeoutError, OSError) as err:
        print(f"FAIL: preflight download failed: {err}", file=sys.stderr)
        return 1

    print(f"OK: updated palomar-preflight to {latest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
