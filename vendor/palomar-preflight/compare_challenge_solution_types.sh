#!/usr/bin/env bash
# Diff Challenge vs Solution types for every comparator.json name, then walk
# the project-namespace declaration closure the way Palomar Compare.loop does.
#
# Named theorem_names / definition_names are holes (types only). Everything
# else in the project's namespace prefix(es) must match as a full constant,
# including generated `._proof_N` names.
set -euo pipefail

TOOLKIT_ROOT="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=palomar-lib.sh
source "$TOOLKIT_ROOT/palomar-lib.sh"
palomar_cd_project

mapfile -t NAMES < <(python3 - <<'PY'
import json
cfg = json.load(open("comparator.json"))
for n in cfg["theorem_names"] + cfg.get("definition_names", []):
    print(n)
PY
)

mapfile -t THEOREM_NAMES < <(python3 - <<'PY'
import json
cfg = json.load(open("comparator.json"))
for n in cfg["theorem_names"]:
    print(n)
PY
)

mapfile -t DEFINITION_NAMES < <(python3 - <<'PY'
import json
cfg = json.load(open("comparator.json"))
for n in cfg.get("definition_names", []):
    print(n)
PY
)

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

write_lean() {
  local module="$1" out="$2"
  {
    echo "import ${module}"
    echo "set_option pp.all true"
    echo "set_option pp.explicit true"
    echo "set_option pp.universes true"
    echo "set_option pp.fullNames true"
    echo "set_option pp.funBinderTypes true"
    for n in "${NAMES[@]}"; do
      echo "#check ${n}"
    done
  } >"${out}"
}

write_lean Challenge "${tmp}/ChallengeTypes.lean"
write_lean Solution "${tmp}/SolutionTypes.lean"

if [[ "${PALOMAR_CHECK_DECL_KINDS:-1}" != 0 ]]; then
  write_kind_lean() {
    local module="$1" out="$2"
    {
      echo "import ${module}"
      cat <<'LEAN'
open Lean Elab Command
elab "#assert_theorem " n:ident : command => do
  match (← getEnv).find? n.getId with
  | some (.thmInfo _) => pure ()
  | some _ => throwError "{n.getId} is not a theorem"
  | none => throwError "unknown declaration {n.getId}"
elab "#assert_definition " n:ident : command => do
  match (← getEnv).find? n.getId with
  | some (.defnInfo _) => pure ()
  | some _ => throwError "{n.getId} is not a definition"
  | none => throwError "unknown declaration {n.getId}"
LEAN
      for n in "${THEOREM_NAMES[@]}"; do
        echo "#assert_theorem ${n}"
      done
      for n in "${DEFINITION_NAMES[@]}"; do
        echo "#assert_definition ${n}"
      done
    } >"${out}"
  }
  write_kind_lean Challenge "${tmp}/ChallengeKinds.lean"
  write_kind_lean Solution "${tmp}/SolutionKinds.lean"
  for module in Challenge Solution; do
    if ! lake env lean "${tmp}/${module}Kinds.lean" >"${tmp}/${module}-kinds.raw" 2>&1; then
      echo "FAIL: Comparator declaration-kind check failed in ${module}."
      cat "${tmp}/${module}-kinds.raw"
      exit 1
    fi
  done
  echo "OK: theorem_names and definition_names have the required declaration kinds."
fi

if ! lake env lean "${tmp}/ChallengeTypes.lean" >"${tmp}/challenge.raw" 2>&1; then
  echo "FAIL: could not inspect Challenge declarations."
  cat "${tmp}/challenge.raw"
  exit 1
fi
if ! lake env lean "${tmp}/SolutionTypes.lean" >"${tmp}/solution.raw" 2>&1; then
  echo "FAIL: could not inspect Solution declarations."
  cat "${tmp}/solution.raw"
  exit 1
fi
grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' \
  <"${tmp}/challenge.raw" >"${tmp}/challenge.txt" || true
grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' \
  <"${tmp}/solution.raw" >"${tmp}/solution.txt" || true

# Palomar Comparator BEqs ConstantVal.levelParams. Do not strip universe names
# for the primary diff. A stripped view is a hint for instance-path mismatches.
normalize_instances() {
  sed -E 's/\.\{u_[0-9]+(,[ ]*u_[0-9]+)*\}//g; s/u_[0-9]+/u/g'
}

if [[ "${PALOMAR_QUIET:-0}" != 1 ]]; then
  echo "== Challenge (pp.all + pp.fullNames) =="
  cat "${tmp}/challenge.txt"
  echo
  echo "== Solution (pp.all + pp.fullNames) =="
  cat "${tmp}/solution.txt"
  echo
fi
if diff -u "${tmp}/challenge.txt" "${tmp}/solution.txt"; then
  echo "OK: Challenge and Solution names, universes, and types match."
else
  echo "FAIL: type/universe/instance/name mismatch — Palomar Comparator will reject this."
  echo
  echo "== Universe-stripped hint (instance paths only) =="
  normalize_instances <"${tmp}/challenge.txt" >"${tmp}/challenge.norm"
  normalize_instances <"${tmp}/solution.txt" >"${tmp}/solution.norm"
  diff -u "${tmp}/challenge.norm" "${tmp}/solution.norm" || true
  exit 1
fi

mapfile -t BODY_NAMES < <(
  python3 - "${tmp}/challenge.txt" "${tmp}/solution.txt" <<'PY'
import json
import os
import re
import sys

cfg = json.load(open("comparator.json"))
holes = set(cfg["theorem_names"]) | set(cfg.get("definition_names", []))
prefixes = {name.split(".", 1)[0] for name in holes if name}
for extra in os.environ.get("PALOMAR_CLOSURE_PREFIXES", "").split():
    if extra:
        prefixes.add(extra)
if not prefixes:
    raise SystemExit(0)
alt = "|".join(re.escape(p) for p in sorted(prefixes))
name_re = re.compile(rf"(?:{alt})(?:\.[A-Za-z_][A-Za-z0-9_']*)*")
ordered = []
seen = set()

def add(name: str) -> None:
    if name and name not in seen:
        seen.add(name)
        ordered.append(name)

for name in cfg.get("definition_names", []):
    add(name)
for extra in os.environ.get("PALOMAR_EXTRA_PRINT_NAMES", "").split():
    add(extra)
for path in sys.argv[1:]:
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for match in name_re.finditer(text):
        name = match.group(0)
        if "._proof_" in name:
            continue
        if name not in holes:
            add(name)
print("\n".join(ordered))
PY
)

if [[ ${#BODY_NAMES[@]} -eq 0 ]]; then
  echo "OK: no definition bodies to compare yet."
  exit 0
fi

write_definition_dump() {
  local module="$1" out="$2"
  {
    echo "import ${module}"
    echo "set_option pp.all true"
    echo "set_option pp.explicit true"
    echo "set_option pp.universes true"
    echo "set_option pp.fullNames true"
    echo "set_option pp.funBinderTypes true"
    for n in "${BODY_NAMES[@]}"; do
      echo "#print ${n}"
    done
  } >"${out}"
}

dump_bodies() {
  write_definition_dump Challenge "${tmp}/ChallengeDefinitions.lean"
  write_definition_dump Solution "${tmp}/SolutionDefinitions.lean"
  lake env lean "${tmp}/ChallengeDefinitions.lean" 2>/dev/null \
    | { grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' || true; } \
    >"${tmp}/challenge-definitions.txt"
  lake env lean "${tmp}/SolutionDefinitions.lean" 2>/dev/null \
    | { grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' || true; } \
    >"${tmp}/solution-definitions.txt"
}

dump_bodies

printf '%s\n' "${BODY_NAMES[@]}" >"${tmp}/known-bodies.txt"
for _ in 1 2 3 4 5 6 7 8; do
  mapfile -t extra < <(
    python3 - "${tmp}/known-bodies.txt" \
      "${tmp}/challenge-definitions.txt" "${tmp}/solution-definitions.txt" <<'PY'
import json
import os
import re
import sys

cfg = json.load(open("comparator.json"))
holes = set(cfg["theorem_names"]) | set(cfg.get("definition_names", []))
prefixes = {name.split(".", 1)[0] for name in holes if name}
for item in os.environ.get("PALOMAR_CLOSURE_PREFIXES", "").split():
    if item:
        prefixes.add(item)
if not prefixes:
    raise SystemExit(0)
alt = "|".join(re.escape(p) for p in sorted(prefixes))
name_re = re.compile(rf"(?:{alt})(?:\.[A-Za-z_][A-Za-z0-9_']*)*")
known = {
    line.strip()
    for line in open(sys.argv[1], encoding="utf-8", errors="replace")
    if line.strip()
}
ordered = []
seen = set(known)

def add(name: str) -> None:
    if name and name not in seen and name not in holes:
        seen.add(name)
        ordered.append(name)

for path in sys.argv[2:]:
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for match in name_re.finditer(text):
        name = match.group(0)
        if "._proof_" in name:
            continue
        add(name)
print("\n".join(ordered))
PY
  )
  if [[ ${#extra[@]} -eq 0 || -z "${extra[0]:-}" ]]; then
    break
  fi
  BODY_NAMES+=("${extra[@]}")
  printf '%s\n' "${BODY_NAMES[@]}" >"${tmp}/known-bodies.txt"
  dump_bodies
done

proof_names() {
  python3 - "$@" <<'PY'
import os
import re
import sys
import json

cfg = json.load(open("comparator.json"))
holes = set(cfg["theorem_names"]) | set(cfg.get("definition_names", []))
prefixes = {name.split(".", 1)[0] for name in holes if name}
for item in os.environ.get("PALOMAR_CLOSURE_PREFIXES", "").split():
    if item:
        prefixes.add(item)
if not prefixes:
    raise SystemExit(0)
alt = "|".join(re.escape(p) for p in sorted(prefixes))
pat = re.compile(rf"(?:{alt})(?:\.[A-Za-z_][A-Za-z0-9_']*)*\._proof_[0-9]+")
found = []
seen = set()
for path in sys.argv[1:]:
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    for match in pat.finditer(text):
        name = match.group(0)
        if name not in seen:
            seen.add(name)
            found.append(name)
print("\n".join(found))
PY
}

if diff -u "${tmp}/challenge-definitions.txt" "${tmp}/solution-definitions.txt" \
    >"${tmp}/definitions.diff"; then
  mapfile -t proofs < <(proof_names \
    "${tmp}/challenge-definitions.txt" "${tmp}/solution-definitions.txt")
  if [[ ${#proofs[@]} -gt 0 && -n "${proofs[0]:-}" ]]; then
    echo "WARNING: locked dumps mention generated proofs (Comparator will compare them):"
    printf '  %s\n' "${proofs[@]}"
  fi
  echo "OK: compared and transitively locked definition values match."
else
  echo "FAIL: a compared or transitively locked definition value differs."
  echo "Palomar Comparator will reject the mismatching constant."
  mapfile -t proofs < <(proof_names \
    "${tmp}/challenge-definitions.txt" "${tmp}/solution-definitions.txt")
  if [[ ${#proofs[@]} -gt 0 && -n "${proofs[0]:-}" ]]; then
    echo "Generated proofs mentioned in the dumps:"
    printf '  %s\n' "${proofs[@]}"
  fi
  echo
  echo "== First 80 lines of the pretty-print diff =="
  head -n 80 "${tmp}/definitions.diff"
  exit 1
fi
