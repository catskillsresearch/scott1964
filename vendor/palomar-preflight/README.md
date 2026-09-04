# Palomar local preflight

Local/CI replica of Palomar registry mechanical verification, plus the
editorial LLM audit used before submission.

This repository is **vendored by copy** into Lean formalization projects
(`vendor/palomar-preflight/`). It is not a git submodule. Palomar rejects
`.gitmodules`, and Palomar itself runs Comparator from PalomarSubmission —
it does not call this repo.

## Use from a Lean project

Keep a thin wrapper at `scripts/palomar_preflight.sh`:

```bash
#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PALOMAR_PROJECT_ROOT="$ROOT"
export PALOMAR_SORRY_PATHS="YourLib Solution.lean"
exec bash "$ROOT/vendor/palomar-preflight/palomar_preflight.sh" "$@"
```

Optional `scripts/palomar_preflight_local.sh` runs extra mechanical checks
(after the submodule ban, before `lake build`).

Environment:

| Variable | Meaning |
| --- | --- |
| `PALOMAR_SORRY_PATHS` | Files or directories scanned for `sorry`/`admit` |
| `PALOMAR_CLOSURE_PREFIXES` | Extra Lean namespace prefixes for the pretty-print closure walk |
| `PALOMAR_EXTRA_PRINT_NAMES` | Extra constants to `#print` during the closure walk |
| `PALOMAR_CHECK_DECL_KINDS` | Set to `0` if `theorem_names` includes defs (Mizar-style) |
| `PALOMAR_CHALLENGE_FORBIDDEN_PREFIXES` | Extra Challenge import bans |

Vendor / refresh:

```bash
python3 /path/to/palomar-preflight/palomar_preflight_sync.py --from-dir /path/to/palomar-preflight
# or, after this repo is on GitHub:
python3 vendor/palomar-preflight/palomar_preflight_sync.py
```

Pin file: `vendor/PALOMAR_PREFLIGHT_PIN`.

## Commands

```bash
bash scripts/palomar_preflight.sh --mechanical-only   # CI
bash scripts/palomar_preflight.sh                     # before Palomar submit
```

Mechanical includes Palomar-pinned Comparator (`verify-comparator.sh`):
declaration-closure Const matching, axiom checks, and Lean kernel replay.

## License

Apache-2.0.
