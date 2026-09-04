#!/usr/bin/env bash
# Borrowed from leanprover/comparator scripts/fake-landrun.sh (Palomar pin
# 575674928e239f5bc452aab72d1dd7b0f1326494). Development shim: Comparator's
# Const/axiom/kernel checks still run; Landlock sandboxing does not.
set -euo pipefail

flags_with_value=(
  --ro --rox --rw --rwx
  --bind-tcp --connect-tcp
  --log-level
  --env
)

is_value_flag() {
  local f="$1"
  for vf in "${flags_with_value[@]}"; do
    [[ "$f" == "$vf" ]] && return 0
  done
  return 1
}

case "${1:-}" in
  -h|--help)
    cat <<'EOF'
fake landrun shim/fake/stub - does nothing, runs your command unsandboxed

Usage: landrun [flags] <command> [args...]

Flags are accepted and ignored.
EOF
    exit 0
    ;;
  -V|--version)
    echo "XXX NOT LANDRUN, FAKE SHIM XXX" >&2
    exit 0
    ;;
esac

while [[ $# -gt 0 ]]; do
  case "$1" in
    --) shift; break ;;
    -*)
      is_value_flag "$1" && shift
      shift
      ;;
    *) break ;;
  esac
done

if [[ $# -eq 0 ]]; then
  echo "landrun shim: no command given" >&2
  exit 2
fi

echo "WARNING: THIS IS NOT REAL LANDRUN! UNSAFELY RUNNING exec $*" >&2
exec "$@"
