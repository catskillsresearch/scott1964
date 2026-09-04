#!/usr/bin/env python3
"""Resolve the Lean project root versus this toolkit directory."""

from __future__ import annotations

import os
from pathlib import Path

TOOLKIT_ROOT = Path(__file__).resolve().parent


def project_root() -> Path:
    env = os.environ.get("PALOMAR_PROJECT_ROOT", "").strip()
    if env:
        return Path(env).resolve()
    here = Path.cwd().resolve()
    for path in [here, *here.parents]:
        if (path / "comparator.json").is_file() and (path / "lean-toolchain").is_file():
            return path
    raise SystemExit(
        "FAIL: not in a Palomar Lean project (need comparator.json and lean-toolchain).\n"
        "Set PALOMAR_PROJECT_ROOT or run from the project directory."
    )
