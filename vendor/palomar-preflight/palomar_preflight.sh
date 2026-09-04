#!/usr/bin/env bash
# Palomar local preflight: mechanical Comparator checks + editorial LLM audit.
# Mechanical runs Palomar's pinned Comparator so local/CI rejection matches
# registry verification. Use --mechanical-only for CI without API calls.
set -euo pipefail

TOOLKIT_ROOT="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=palomar-lib.sh
source "$TOOLKIT_ROOT/palomar-lib.sh"
palomar_cd_project
export PYTHONPATH="$TOOLKIT_ROOT${PYTHONPATH:+:$PYTHONPATH}"

MECHANICAL_ONLY=0
NO_POLICY_SYNC=0
for arg in "$@"; do
  case "$arg" in
    --mechanical-only) MECHANICAL_ONLY=1 ;;
    --no-policy-sync) NO_POLICY_SYNC=1 ;;
    -h|--help)
      cat <<'EOF'
Usage: palomar_preflight.sh [--mechanical-only] [--no-policy-sync]

  --mechanical-only   Skip PalomarPolicy sync and LLM editorial audit.
                      Still runs Palomar-pinned Comparator.
  --no-policy-sync    Audit against committed vendor/palomar-policy only.

Project wrappers should set PALOMAR_PROJECT_ROOT and PALOMAR_SORRY_PATHS.
Optional scripts/palomar_preflight_local.sh runs extra mechanical checks.

Full preflight requires CURSOR_API_KEY (or ../tokens_ssto.yaml) and runs
Cursor editorial review: gpt-5.6-sol for substantive passes, composer-2.5 for lighter checks.
EOF
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 2
      ;;
  esac
done

step() {
  printf '\n== %s ==\n' "$1"
}

step "Validate Comparator configuration"
python3 - <<'PY'
import json
import re

with open("comparator.json", encoding="utf-8") as f:
    cfg = json.load(f)

allowed_keys = {
    "challenge_module",
    "solution_module",
    "theorem_names",
    "definition_names",
    "permitted_axioms",
    "enable_nanoda",
}
unknown = sorted(set(cfg) - allowed_keys)
if unknown:
    raise SystemExit(f"Unknown comparator.json keys: {', '.join(unknown)}")

for key in ("challenge_module", "solution_module", "theorem_names", "definition_names", "permitted_axioms"):
    if key not in cfg:
        raise SystemExit(f"Missing comparator.json key: {key}")

challenge = cfg["challenge_module"]
solution = cfg["solution_module"]
theorems = cfg["theorem_names"]
definitions = cfg.get("definition_names", [])
axioms = cfg["permitted_axioms"]

if challenge == solution:
    raise SystemExit("challenge_module and solution_module must differ")

module_part = re.compile(r"[A-Za-z_][A-Za-z0-9_']*")
for key in ("challenge_module", "solution_module"):
    name = cfg[key]
    if not isinstance(name, str) or not name:
        raise SystemExit(f"{key} must be a nonempty string")
    if not all(module_part.fullmatch(part) for part in name.split(".")):
        raise SystemExit(f"{key} is not a safe dotted Lean module name: {name!r}")

if not isinstance(theorems, list) or not theorems or not all(
    isinstance(name, str) and name for name in theorems
):
    raise SystemExit("theorem_names must be a nonempty array of nonempty strings")

if not isinstance(definitions, list) or not all(
    isinstance(name, str) and name for name in definitions
):
    raise SystemExit("definition_names must be an array of nonempty strings")

allowed_axioms = {"propext", "Quot.sound", "Classical.choice"}
if not isinstance(axioms, list) or not all(isinstance(x, str) for x in axioms):
    raise SystemExit("permitted_axioms must be an array of strings")
extra = sorted(set(axioms) - allowed_axioms)
if extra:
    raise SystemExit(
        "permitted_axioms exceeds Palomar allowlist "
        f"(forbidden: {', '.join(extra)})"
    )

declarations = theorems + definitions
duplicates = sorted({name for name in declarations if declarations.count(name) > 1})
if duplicates:
    raise SystemExit(f"Duplicate Comparator names: {', '.join(duplicates)}")

print(
    f"OK: challenge_module={challenge}, solution_module={solution}, "
    f"{len(theorems)} theorems, {len(definitions)} definitions, "
    f"{len(declarations)} declarations."
)
PY

step "Challenge import discipline (Mathlib only)"
python3 - <<'PY'
import json
import os
import re
from pathlib import Path

text = Path("Challenge.lean").read_text(encoding="utf-8")
imports = re.findall(r"^import\s+(\S+)", text, re.MULTILINE)
cfg = json.loads(Path("comparator.json").read_text(encoding="utf-8"))
forbidden = {"Solution"}
for name in cfg["theorem_names"] + cfg.get("definition_names", []):
    head = name.split(".", 1)[0]
    if head:
        forbidden.add(head)
for extra in os.environ.get("PALOMAR_CHALLENGE_FORBIDDEN_PREFIXES", "").split():
    forbidden.add(extra)
for imp in imports:
    head = imp.split(".", 1)[0]
    if head in forbidden or imp.startswith("Solution"):
        raise SystemExit(f"Forbidden Challenge import: {imp}")
    if not (imp.startswith("Init") or imp.startswith("Std")
            or imp.startswith("Lean") or imp.startswith("Mathlib")):
        raise SystemExit(
            f"Challenge import not allowlisted (Init/Mathlib/Std/Lean): {imp}"
        )
print(f"OK: Challenge has {len(imports)} explicit import(s).")
PY

step "Challenge surface size limits"
python3 - <<'PY'
from pathlib import Path

path = Path("Challenge.lean")
lines = path.read_text(encoding="utf-8").count("\n") + 1
size = path.stat().st_size
if lines >= 1000:
    raise SystemExit(f"Challenge.lean too long: {lines} lines (limit 1000)")
if size >= 100 * 1024:
    raise SystemExit(f"Challenge.lean too large: {size} bytes (limit 100 KiB)")
print(f"OK: Challenge.lean is {lines} lines, {size} bytes.")
PY

step "Exactly one Lake manifest at repository root"
if [[ -f lakefile.toml && -f lakefile.lean ]]; then
  echo "FAIL: both lakefile.toml and lakefile.lean present."
  exit 1
fi
if [[ ! -f lakefile.toml && ! -f lakefile.lean ]]; then
  echo "FAIL: no lakefile.toml or lakefile.lean at repository root."
  exit 1
fi
if [[ ! -f lake-manifest.json ]]; then
  echo "FAIL: lake-manifest.json is missing."
  exit 1
fi
if [[ ! -f lean-toolchain ]]; then
  echo "FAIL: lean-toolchain is missing."
  exit 1
fi
echo "OK: Lake config, manifest, and toolchain present."

step "Reject git submodules (Palomar cannot preserve them)"
if [[ -e .gitmodules ]]; then
  echo "FAIL: .gitmodules is present; Palomar cannot preserve submodules."
  exit 1
fi
echo "OK: no .gitmodules."

if [[ -f scripts/palomar_preflight_local.sh ]]; then
  step "Project-specific mechanical checks"
  bash scripts/palomar_preflight_local.sh
fi

step "Build Lean project"
lake build 2>&1 | grep -vE 'LEAN_PATH|trace:' | tail -20

step "Compare Challenge/Solution types and declaration-closure values"
compare_status=0
PALOMAR_QUIET=1 bash "$TOOLKIT_ROOT/compare_challenge_solution_types.sh" || compare_status=$?

step "Run Palomar-pinned Comparator"
bash "$TOOLKIT_ROOT/verify-comparator.sh"
if [[ "$compare_status" -ne 0 ]]; then
  echo "Pretty-print declaration-closure check also failed (exit ${compare_status})."
  exit "$compare_status"
fi

step "Reject proof holes in Solution sources"
python3 - <<'PY'
import os
import re
from pathlib import Path

pattern = re.compile(
    r"(^|:=|by)[[:space:]]+(?:sorry|admit)([[:space:];]|$)|^[[:space:]]*(?:sorry|admit)([[:space:];]|$)",
    re.MULTILINE,
)
raw = os.environ.get("PALOMAR_SORRY_PATHS", "Solution.lean").split()
if not raw:
    raw = ["Solution.lean"]
files = []
for item in raw:
    path = Path(item)
    if path.is_dir():
        files.extend(sorted(path.rglob("*.lean")))
    elif path.is_file():
        files.append(path)
    else:
        raise SystemExit(f"FAIL: PALOMAR_SORRY_PATHS entry missing: {item}")
hits = []
for path in files:
    text = path.read_text(encoding="utf-8")
    for match in pattern.finditer(text):
        line = text.count("\n", 0, match.start()) + 1
        hits.append(f"{path}:{line}")
if hits:
    print("FAIL: Solution proof sources contain sorry/admit:")
    print("\n".join(f"  {hit}" for hit in hits))
    raise SystemExit(1)
print(f"OK: scanned {len(files)} Solution proof file(s); no sorry/admit.")
PY

step "Check permitted theorem axioms"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
python3 - "$tmp/Axioms.lean" <<'PY'
import json
import sys

with open("comparator.json", encoding="utf-8") as f:
    cfg = json.load(f)
with open(sys.argv[1], "w", encoding="utf-8") as out:
    out.write(f"import {cfg['solution_module']}\n")
    for name in cfg["theorem_names"]:
        out.write(f"#print axioms {name}\n")
PY
lake env lean "$tmp/Axioms.lean" >"$tmp/axioms.txt"
python3 - "$tmp/axioms.txt" <<'PY'
import json
import re
import sys

with open("comparator.json", encoding="utf-8") as f:
    cfg = json.load(f)
allowed = set(cfg["permitted_axioms"])
theorems = cfg["theorem_names"]
text = open(sys.argv[1], encoding="utf-8").read()
reports = re.findall(
    r"^'(.+)' depends on axioms: \[([^\]]*)\]$", text, re.MULTILINE
)
no_axioms = re.findall(
    r"^'(.+)' does not depend on any axioms$", text, re.MULTILINE
)
reported = {name for name, _ in reports} | set(no_axioms)
expected = set(theorems)
if reported != expected:
    missing = sorted(expected - reported)
    extra = sorted(reported - expected)
    raise SystemExit(f"Axiom report mismatch; missing={missing}, extra={extra}")
for name, raw in reports:
    used = {item.strip() for item in raw.split(",") if item.strip()}
    forbidden = sorted(used - allowed)
    if forbidden:
        raise SystemExit(f"{name} uses forbidden axioms: {', '.join(forbidden)}")
print(f"OK: all theorem targets use only {sorted(allowed)} (or no axioms).")
PY

step "Check patch formatting"
git diff --check

if [[ "$MECHANICAL_ONLY" -eq 1 ]]; then
  echo ""
  echo "OK: mechanical preflight passed (--mechanical-only; editorial audit skipped)."
  echo "NOTE: full Palomar preflight also runs vendored-policy sync and Cursor editorial audit (gpt-5.6-sol + composer-2.5)."
  exit 0
fi

SYNC_ARGS=(--root vendor/palomar-policy --pin vendor/PALOMAR_POLICY_PIN)
if [[ "$NO_POLICY_SYNC" -eq 1 ]]; then
  SYNC_ARGS+=(--no-sync)
fi

step "Sync PalomarPolicy to upstream latest"
python3 "$TOOLKIT_ROOT/palomar_policy_sync.py" "${SYNC_ARGS[@]}"

step "Palomar editorial pre-checks"
python3 "$TOOLKIT_ROOT/palomar_editorial_checks.py"

step "Build local mechanical report"
mkdir -p .cache/palomar-editorial
python3 "$TOOLKIT_ROOT/palomar_mechanical_report.py" --out .cache/palomar-editorial/mechanical-report.json

if [[ -z "${CURSOR_API_KEY:-}" ]]; then
  for TOKENS in ../tokens_ssto.yaml tokens_ssto.yaml; do
    if [[ -f "$TOKENS" ]]; then
      CURSOR_API_KEY="$(grep -E '^CURSOR_API_KEY:' "$TOKENS" | head -1 | sed -E 's/^CURSOR_API_KEY:[[:space:]]*//')"
      if [[ -n "$CURSOR_API_KEY" ]]; then
        export CURSOR_API_KEY
        break
      fi
    fi
  done
fi

step "Palomar editorial audit (LLM, gpt-5.6-sol + composer-2.5)"
bash "$TOOLKIT_ROOT/palomar_editorial_audit.sh" \
  --policy-dir vendor/palomar-policy \
  --policy-pin "$(tr -d '[:space:]' < vendor/PALOMAR_POLICY_PIN)" \
  --mechanical-report .cache/palomar-editorial/mechanical-report.json \
  --out .cache/palomar-editorial/review-draft.json

echo ""
echo "OK: full Palomar preflight passed (mechanical + editorial neutral)."
