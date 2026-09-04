# Palomar editorial audit (local dry-run)

This repository vendors [PalomarPolicy](https://github.com/PalomarRegistry/PalomarPolicy)
under `vendor/palomar-policy/` and runs the same editorial prompt rubric locally
before Palomar registry submission.

## Full preflight

```bash
# CURSOR_API_KEY in env, or in ../tokens_ssto.yaml (shared with sibling repos)
bash scripts/palomar_preflight.sh
```

Full preflight runs:

1. Mechanical Comparator checks (build, type/value match, Palomar-pinned Comparator, sorry scan, axioms, …)
2. **Policy sync** — compares `vendor/PALOMAR_POLICY_PIN` to upstream `main` and
   refreshes the vendored tree when newer
3. Deterministic editorial pre-checks (`scripts/palomar_editorial_checks.py`)
4. Local `mechanical-report.json` stub
5. **LLM editorial audit** via **Cursor SDK** (`scripts/palomar_editorial_audit.sh`)
   - **Substantive passes**: **`gpt-5.6-sol`**
     — `statement_alignment`, `definition_fidelity`, `literature_notability`, `synthesis`
   - **Lighter passes**: **`composer-2.5`**
     — `classification`, `metadata`, optional `proof_account`

Output: `.cache/palomar-editorial/review-draft.json` (gitignored).

Preflight is green only when synthesis outcome is **`neutral`**.

## Mechanical-only (CI / day-to-day development)

```bash
bash scripts/palomar_preflight.sh --mechanical-only
```

Skips policy sync and LLM audit. GitHub Actions uses this on every push/PR.

Run **full** preflight locally before a Palomar submission commit.

Full editorial audit cost: about **six sequential LLM calls**
(two `composer-2.5`, four `gpt-5.6-sol`), roughly **$1–1.50** and several
minutes wall time per run.

## Submission packaging checklist

Before running full preflight on a submission candidate, confirm:

1. **Research interest** — compared theorems are Scott 1964 headline results
   (plus any separately labelled reconstructions), not incidental lemmas.
2. **Definition pinning** — every material symbol in each compared theorem type
   is either primitive, defined without `sorry` in Challenge.lean, or listed in
   `comparator.json` → `definition_names` with its defining or semantic law also
   compared. Opaque `sorry` stubs make the theorem unauditable.
3. **Metadata sync** — `formalization.yaml` `status.scope`, `main_results`,
   `limitations`, and `alignment` match `comparator.json` and Challenge/Solution.
4. **Sources** — `formalization.yaml` `sources:` records the primary paper and
   any extra literature for separately labelled compared results.
5. **Mechanical green** — `bash scripts/palomar_preflight.sh --mechanical-only`
   passes. That now includes Palomar's pinned Comparator
   (`scripts/verify-comparator.sh`), which walks the declaration closure
   Comparator actually compares. Then `bash scripts/compare_challenge_solution_types.sh`.

Deterministic packaging checks live in `scripts/palomar_editorial_checks.py`
(main_results coverage, sorry-definition pinning, scope sync). They run during
**full** preflight and fail fast before the LLM audit.

Comparator elaboration rules (inline proofs, instance paths, universe names):
`docs/PALOMAR_STYLE.md`.

## Policy sync and revert

- Pin file: `vendor/PALOMAR_POLICY_PIN`
- Sync script: `scripts/palomar_policy_sync.py`
- Skip upstream check: `bash scripts/palomar_preflight.sh --no-policy-sync`

If a bad upstream draft is pulled, revert before committing:

```bash
git checkout -- vendor/palomar-policy vendor/PALOMAR_POLICY_PIN
```

After a good audit that updated policy, commit the vendored snapshot and pin
together so GitHub records which editorial contract was in effect.

## Models and auth

| Pass | Model | Notes |
|------|-------|-------|
| statement_alignment, definition_fidelity, literature_notability, synthesis | `gpt-5.6-sol` | Palomar production editorial model |
| classification, metadata, proof_account | `composer-2.5` | cheaper ancillary checks |

Override via `PALOMAR_EDITORIAL_PRIMARY_MODEL` / `PALOMAR_EDITORIAL_ECONOMY_MODEL`.

Auth: `CURSOR_API_KEY` environment variable, or `CURSOR_API_KEY` in
`../tokens_ssto.yaml`.

First run creates `.venv-editorial/` with `cursor-sdk` and `pyyaml`, or reuses
`../scott1964/.venv-ocr/bin/python` when cursor-sdk is already installed there.

## Files

| Path | Role |
|------|------|
| `vendor/palomar-policy/` | Vendored prompts, rubric, CONTRIBUTING, schemas |
| `vendor/PALOMAR_POLICY_PIN` | Upstream PalomarPolicy commit SHA |
| `scripts/palomar_policy_sync.py` | Upstream check + auto-update |
| `scripts/palomar_editorial_checks.py` | Fast deterministic pre-checks |
| `scripts/palomar_mechanical_report.py` | Local mechanical report JSON |
| `scripts/palomar_editorial_audit.py` | LLM rubric orchestrator |
| `scripts/palomar_editorial_audit.sh` | Venv wrapper for cursor-sdk |
| `scripts/palomar_preflight.sh` | Mechanical + editorial gate |
| `scripts/verify-comparator.sh` | Palomar-pinned Comparator (declaration closure) |
