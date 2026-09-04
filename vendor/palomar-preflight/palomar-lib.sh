# Shared bash helpers for Palomar local preflight. Source from toolkit scripts.
# shellcheck shell=bash

palomar_toolkit_root() {
  cd "$(dirname "${BASH_SOURCE[0]}")" && pwd
}

palomar_project_root() {
  if [[ -n "${PALOMAR_PROJECT_ROOT:-}" ]]; then
    printf '%s\n' "$PALOMAR_PROJECT_ROOT"
    return 0
  fi
  local dir="$PWD"
  while true; do
    if [[ -f "$dir/comparator.json" && -f "$dir/lean-toolchain" ]]; then
      printf '%s\n' "$dir"
      return 0
    fi
    [[ "$dir" == / ]] && break
    dir="$(dirname "$dir")"
  done
  echo "error: run from a Palomar Lean project (comparator.json + lean-toolchain)" >&2
  echo "Set PALOMAR_PROJECT_ROOT or invoke via the project's scripts/palomar_preflight.sh." >&2
  return 1
}

palomar_cd_project() {
  local root
  root="$(palomar_project_root)" || return 1
  export PALOMAR_PROJECT_ROOT="$root"
  cd "$root"
}
