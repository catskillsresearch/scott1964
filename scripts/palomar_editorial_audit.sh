#!/usr/bin/env bash
# Editorial audit wrapper: cursor-sdk venv (local or scott1964 fallback).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

venv_ready() {
  local py="$1"
  [[ -x "$py" ]] && "$py" -c "import cursor_sdk" 2>/dev/null
}

pick_python() {
  if venv_ready .venv-editorial/bin/python; then
    echo .venv-editorial/bin/python
    return
  fi
  local sibling="$ROOT/../scott1964/.venv-ocr/bin/python"
  if venv_ready "$sibling"; then
    echo "$sibling"
    return
  fi
  python3 -m venv .venv-editorial
  .venv-editorial/bin/pip install -r scripts/requirements-editorial.txt
  echo .venv-editorial/bin/python
}

load_cursor_api_key() {
  if [[ -n "${CURSOR_API_KEY:-}" ]]; then
    return 0
  fi
  local tokens
  for tokens in "$ROOT/../tokens_ssto.yaml" "$ROOT/tokens_ssto.yaml"; do
    if [[ -f "$tokens" ]]; then
      CURSOR_API_KEY="$(grep -E '^CURSOR_API_KEY:' "$tokens" | head -1 | sed -E 's/^CURSOR_API_KEY:[[:space:]]*//')"
      if [[ -n "$CURSOR_API_KEY" ]]; then
        export CURSOR_API_KEY
        return 0
      fi
    fi
  done
  echo "FAIL: set CURSOR_API_KEY or add it to ../tokens_ssto.yaml" >&2
  return 1
}

load_cursor_api_key
exec "$(pick_python)" scripts/palomar_editorial_audit.py "$@"
