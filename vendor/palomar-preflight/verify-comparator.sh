#!/usr/bin/env bash
# Run Palomar's pinned Comparator against the current Lean project.
#
# Pins and invocation shape come from PalomarRegistry/PalomarSubmission
# `.github/workflows/submission.yml` (not PalomarTemplate, which may lag or
# lead). Palomar writes a protected comparator.json with enable_nanoda forced
# on; this script does the same in a temp file and does not edit the submitted
# comparator.json.
set -euo pipefail

TOOLKIT_ROOT="$(cd "$(dirname "$0")" && pwd)"
# shellcheck source=palomar-lib.sh
source "$TOOLKIT_ROOT/palomar-lib.sh"
palomar_cd_project
repository_root="$PALOMAR_PROJECT_ROOT"

cache_root=${PALOMAR_COMPARATOR_CACHE:-"$repository_root/.cache/palomar-comparator"}
bin_dir="$cache_root/bin"
comparator_dir="$cache_root/comparator"
lean4export_dir="$cache_root/lean4export"
nanoda_dir="$cache_root/nanoda"

# PalomarRegistry/PalomarSubmission .github/workflows/submission.yml
comparator_commit=575674928e239f5bc452aab72d1dd7b0f1326494
landrun_commit=811cfff51ceaf3d9843708aa6d22e9b84ccac8b4
nanoda_commit=68d5ca9db226849b41a6fff59d796ff19d0a8840

SKIP_NANODA=0
for arg in "$@"; do
  case "$arg" in
    --skip-nanoda) SKIP_NANODA=1 ;;
    -h|--help)
      cat <<'EOF'
Usage: verify-comparator.sh [--skip-nanoda]

Runs Palomar's pinned Comparator (lean4export + Compare.loop + kernel replay).
Palomar always enables NanoDa; omit --skip-nanoda when cargo is available.
EOF
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      exit 2
      ;;
  esac
done

for required_command in git lake python3; do
  if ! command -v "$required_command" >/dev/null 2>&1; then
    echo "error: $required_command is required to run Comparator" >&2
    exit 1
  fi
done

mkdir -p "$cache_root" "$bin_dir"

checkout_exact() {
  local repository=$1
  local destination=$2
  local commit=$3
  if [ ! -d "$destination/.git" ]; then
    git clone --filter=blob:none "$repository" "$destination"
  fi
  git -C "$destination" fetch --depth 1 origin "$commit"
  git -C "$destination" checkout --detach "$commit"
}

project_toolchain=$(tr -d '[:space:]' < "$repository_root/lean-toolchain")
lean4export_commit=$(
  python3 - "$project_toolchain" <<'PY'
import subprocess
import sys

toolchain = sys.argv[1].strip()
prefix = "leanprover/lean4:"
if not toolchain.startswith(prefix):
    raise SystemExit(f"unsupported Lean toolchain: {toolchain}")
tag = toolchain[len(prefix):]
if not tag.startswith("v"):
    raise SystemExit(f"unsupported Lean toolchain: {toolchain}")

def resolve(tag_name: str):
    proc = subprocess.run(
        [
            "git",
            "ls-remote",
            "https://github.com/leanprover/lean4export.git",
            f"refs/tags/{tag_name}^{{}}",
            f"refs/tags/{tag_name}",
        ],
        check=False,
        capture_output=True,
        text=True,
        timeout=120,
    )
    if proc.returncode != 0:
        return None
    commits = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2:
            commits[parts[1]] = parts[0]
    return commits.get(f"refs/tags/{tag_name}^{{}}") or commits.get(f"refs/tags/{tag_name}")

commit = resolve(tag)
if commit is None and tag.count(".") == 2 and "-rc" not in tag:
    major, minor, patch = tag[1:].split(".", 2)
    if patch != "0":
        commit = resolve(f"v{major}.{minor}.0")
if commit is None:
    raise SystemExit(f"leanprover/lean4export has no release tag for {toolchain}")
print(commit)
PY
)

checkout_exact https://github.com/leanprover/lean4export.git "$lean4export_dir" "$lean4export_commit"

if [ ! -f "$lean4export_dir/lean-toolchain" ]; then
  echo "error: pinned lean4export revision $lean4export_commit has no lean-toolchain file" >&2
  exit 1
fi

lean4export_toolchain=$(tr -d '[:space:]' < "$lean4export_dir/lean-toolchain")
python3 - "$project_toolchain" "$lean4export_toolchain" <<'PY'
import re
import sys

TOOLCHAIN_RE = re.compile(
    r"^leanprover/lean4:v(?P<major>[0-9]+)\.(?P<minor>[0-9]+)\.(?P<patch>[0-9]+)"
    r"(?:-rc(?P<rc>[0-9]+))?$"
)

def compatible(submission: str, export: str) -> bool:
    if submission == export:
        return True
    sm = TOOLCHAIN_RE.fullmatch(submission)
    em = TOOLCHAIN_RE.fullmatch(export)
    if sm is None or em is None:
        return False
    return (
        sm.group("rc") is None
        and em.group("rc") is None
        and sm.group("major") == em.group("major")
        and sm.group("minor") == em.group("minor")
        and int(sm.group("patch")) > 0
        and int(em.group("patch")) == 0
    )

if not compatible(sys.argv[1], sys.argv[2]):
    raise SystemExit(
        f"error: project toolchain {sys.argv[1]} is not compatible with "
        f"lean4export toolchain {sys.argv[2]}"
    )
PY

checkout_exact https://github.com/leanprover/comparator.git "$comparator_dir" "$comparator_commit"

have_landrun=0
landrun_bin=""
if command -v go >/dev/null 2>&1; then
  GOBIN="$bin_dir" go install "github.com/zouuup/landrun/cmd/landrun@$landrun_commit"
  landrun_bin="$bin_dir/landrun"
  have_landrun=1
fi

have_nanoda=0
nanoda_bin=""
if [[ "$SKIP_NANODA" -eq 0 ]] && command -v cargo >/dev/null 2>&1; then
  checkout_exact https://github.com/robsimmons/nanoda_lib.git "$nanoda_dir" "$nanoda_commit"
  (cd "$nanoda_dir" && cargo build --release --locked)
  nanoda_bin="$nanoda_dir/target/release/nanoda_bin"
  have_nanoda=1
fi

(cd "$comparator_dir" && lake build comparator)
(cd "$lean4export_dir" && ELAN_TOOLCHAIN="$project_toolchain" lake build lean4export)

protected_config="$cache_root/protected-comparator.json"
python3 - "$repository_root/comparator.json" "$protected_config" "$have_nanoda" <<'PY'
import json
import pathlib
import sys

source = pathlib.Path(sys.argv[1])
destination = pathlib.Path(sys.argv[2])
enable_nanoda = sys.argv[3] == "1"
try:
    config = json.loads(source.read_text(encoding="utf-8"))
except (OSError, UnicodeError, json.JSONDecodeError) as error:
    print(f"error: cannot read valid Comparator config {source}: {error}", file=sys.stderr)
    raise SystemExit(1)
if not isinstance(config, dict):
    raise SystemExit(f"error: {source} must contain one JSON object")
# PalomarSubmission.protected_comparator_config forces NanoDa on. Do not rewrite
# challenge_module; Palomar's PalomarCanonical alias is verifier-only.
if enable_nanoda:
    config["enable_nanoda"] = True
else:
    config.pop("enable_nanoda", None)
destination.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
print(
    f"OK: protected Comparator config at {destination} "
    f"(enable_nanoda={bool(enable_nanoda)})."
)
PY

if [[ "$have_nanoda" -eq 0 ]]; then
  echo "WARNING: NanoDa is not being run (cargo missing or --skip-nanoda)." >&2
  echo "Palomar always forces enable_nanoda true after Const matching." >&2
fi

if [[ "$have_landrun" -eq 1 ]]; then
  export PALOMAR_LANDRUN_REAL="$landrun_bin"
  export COMPARATOR_LANDRUN="$TOOLKIT_ROOT/landrun_passthrough.py"
else
  echo "WARNING: go/landrun is not available; using fake-landrun.sh." >&2
  echo "Const matching, axiom checks, and Lean kernel replay still run." >&2
  chmod +x "$TOOLKIT_ROOT/fake-landrun.sh"
  export COMPARATOR_LANDRUN="$TOOLKIT_ROOT/fake-landrun.sh"
fi

export COMPARATOR_LEAN4EXPORT="$lean4export_dir/.lake/build/bin/lean4export"
if [[ "$have_nanoda" -eq 1 ]]; then
  export COMPARATOR_NANODA="$nanoda_bin"
fi

cd "$repository_root"
lake exe cache get || true

chmod +x "$COMPARATOR_LANDRUN" 2>/dev/null || true
comparator_bin="$comparator_dir/.lake/build/bin/comparator"
set +e
log_file="$cache_root/last-run.log"
lake env "$comparator_bin" "$protected_config" 2>&1 | tee "$log_file"
status=${PIPESTATUS[0]}
set -e

if [[ "$status" -ne 0 ]]; then
  echo ""
  echo "Comparator rejected the project (exit $status)"
  python3 - "$log_file" <<'PY'
import sys

markers = ("uncaught exception", "error:", "error]", "failed")
path = sys.argv[1]
try:
    text = open(path, encoding="utf-8", errors="replace").read()
except OSError:
    raise SystemExit(0)
lines = [line.rstrip() for line in text.splitlines() if line.strip()]
marked = [
    line
    for line in lines
    if any(marker in line.lower() for marker in markers)
]
chosen = (marked or lines)[-10:]
print("\n".join(line[:400] for line in chosen))
PY
  echo ""
  echo "Next: Correct the Lean or Comparator failure quoted above before submitting."
  exit "$status"
fi

echo "OK: Palomar-pinned Comparator accepted Challenge vs Solution."
