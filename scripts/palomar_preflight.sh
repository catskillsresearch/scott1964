#!/usr/bin/env bash
# Thin wrapper: Palomar local preflight lives in vendor/palomar-preflight.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PALOMAR_PROJECT_ROOT="$ROOT"
export PALOMAR_SORRY_PATHS="Scott1964 Solution.lean"
exec bash "$ROOT/vendor/palomar-preflight/palomar_preflight.sh" "$@"
