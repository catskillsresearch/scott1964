#!/usr/bin/env bash
# Diff Challenge vs Solution types for every comparator.json name.
# Palomar Comparator looks up those names in two lean4export environments
# and compares ConstantVal (name, levelParams, type, and definition value)
# with pp.all-level fidelity. Instance names in types and values are part of
# the comparison. A green `lake build` does not imply a match.
#
# Gotchas this script is meant to catch:
# - instance-path mismatch (e.g. ConditionallyCompletePartialOrder.toSupSet
#   vs ScottMap.instSupSet)
# - pretty-printer hiding a module prefix (`Challenge.Foo` vs `Foo`)
# - a `def` listed under theorem_names (Comparator then throws
#   "constant kind don't match")
# - a structure listed under definition_names (Comparator then throws
#   "Challenge constant is not a definition")
# - universe parameter names (`IsContinuousLattice.{u_3}` vs `.{u_2}`):
#   Comparator BEqs ConstantVal.levelParams, so auto-generated `u_n`
#   names must agree. Pin compared decls to `Type u` / `Type v`.
set -euo pipefail
cd "$(dirname "$0")/.."

mapfile -t NAMES < <(python3 - <<'PY'
import json
cfg = json.load(open("comparator.json"))
for n in cfg["theorem_names"] + cfg.get("definition_names", []):
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

# grep exits 1 on empty output, which is the normal state while comparator.json
# still lists no names. Do not let that abort the run.
lake env lean "${tmp}/ChallengeTypes.lean" 2>/dev/null \
  | { grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' || true; } \
  >"${tmp}/challenge.txt"
lake env lean "${tmp}/SolutionTypes.lean" 2>/dev/null \
  | { grep -vE 'LEAN_PATH|trace:|warning:|declaration uses' || true; } \
  >"${tmp}/solution.txt"

# Palomar Comparator BEqs ConstantVal.levelParams, so `.{u_3}` vs `.{u_2}`
# is a rejection. Do not strip universe names. A secondary stripped view is
# printed only to make instance-path mismatches easier to read.
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

# Palomar Compare.loop walks every ordinary constant used by compared theorem
# types (and then those constants' types and values). Named theorem_names and
# definition_names are holes: only their types are compared. Everything else
# in the Scott1964.* closure must match, including generated `._proof_N`
# constants. The submitted comparator.json list is not the full comparison.
mapfile -t BODY_NAMES < <(
  python3 - "${tmp}/challenge.txt" "${tmp}/solution.txt" <<'PY'
import json
import re
import sys

cfg = json.load(open("comparator.json"))
holes = set(cfg["theorem_names"]) | set(cfg.get("definition_names", []))
name_re = re.compile(r"Scott1964(?:\.[A-Za-z_][A-Za-z0-9_']*)+")
ordered = []
seen = set()

def add(name: str) -> None:
    if name and name not in seen:
        seen.add(name)
        ordered.append(name)

for name in cfg.get("definition_names", []):
    add(name)
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

# Follow newly printed Scott1964 names until the pretty-print closure is stable.
printf '%s\n' "${BODY_NAMES[@]}" >"${tmp}/known-bodies.txt"
for _ in 1 2 3 4 5 6 7 8; do
  mapfile -t extra < <(
    python3 - "${tmp}/known-bodies.txt" \
      "${tmp}/challenge-definitions.txt" "${tmp}/solution-definitions.txt" <<'PY'
import json
import re
import sys

cfg = json.load(open("comparator.json"))
holes = set(cfg["theorem_names"]) | set(cfg.get("definition_names", []))
known = {
    line.strip()
    for line in open(sys.argv[1], encoding="utf-8", errors="replace")
    if line.strip()
}
name_re = re.compile(r"Scott1964(?:\.[A-Za-z_][A-Za-z0-9_']*)+")
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

# Inline structure proofs elaborate to private constants such as
# `instPartialOrder._proof_4`. Comparator compares those generated constants
# when they appear in a locked value. Matching names can still be accepted;
# mismatched names (EventSpan._proof_1 vs comparisonVector._proof_1) are a
# Palomar rejection. Treat pretty-print identity as the gate, and summarize
# generated proofs as a hint.
proof_names() {
  python3 - "$@" <<'PY'
import re
import sys

pat = re.compile(r"Scott1964(?:\.[A-Za-z_][A-Za-z0-9_']*)+\._proof_[0-9]+")
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
