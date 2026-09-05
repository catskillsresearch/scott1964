#!/usr/bin/env bash
# Exec shared Palomar preflight from ../palomar-preflight (or CI checkout / legacy vendor).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

find_toolkit() {
  local root="$1" d
  for d in \
    "${PALOMAR_PREFLIGHT_ROOT:-}" \
    "$(dirname "$root")/palomar-preflight" \
    "$root/palomar-preflight" \
    "$root/vendor/palomar-preflight"; do
    [[ -n "$d" && -f "$d/palomar_preflight.sh" ]] && {
      cd "$d" && pwd
      return 0
    }
  done
  echo "error: palomar-preflight not found; set PALOMAR_PREFLIGHT_ROOT or checkout toolkit" >&2
  return 1
}

toolkit_supports_cli() {
  bash "$1/palomar_preflight.sh" --help 2>&1 | grep -q -- '--project-root'
}

TOOLKIT="$(find_toolkit "$ROOT")"
SORRY_PATHS="Scott1964 Solution.lean"

if toolkit_supports_cli "$TOOLKIT"; then
  exec bash "$TOOLKIT/palomar_preflight.sh" \
    --project-root "$ROOT" \
    --sorry-paths "$SORRY_PATHS" \
    "$@"
fi

export PALOMAR_PROJECT_ROOT="$ROOT"
export PALOMAR_SORRY_PATHS="$SORRY_PATHS"
exec bash "$TOOLKIT/palomar_preflight.sh" "$@"
