#!/usr/bin/env python3
"""Deterministic editorial pre-checks before Palomar LLM audit."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parent.parent

AI_NAME_PATTERNS = re.compile(
    r"(?i)\b("
    r"gpt[-\s]?\d|claude|codex|openai|anthropic|chatgpt|"
    r"auto[-\s]?review|language model|llm|cursor agent|"
    r"copilot|gemini|deepseek"
    r")\b"
)

QUALIFIED_NAME = re.compile(r"[A-Za-z][A-Za-z0-9_']*\.[A-Za-z_][A-Za-z0-9_']*")

# Optional per-theorem source hints when a compared result needs an extra
# formalization.yaml sources entry beyond the primary paper record.
THEOREM_SOURCE_HINTS: dict[str, tuple[str, ...]] = {}

SORRY_DEF = re.compile(
    r"^(?:noncomputable\s+)?def\s+(\w+)\b[\s\S]*?:=\s*sorry",
    re.MULTILINE,
)

THEOREM_BODY = re.compile(
    r"(?:/--[\s\S]*?-/\s*\n\s*)?"
    r"theorem\s+{name}\b([\s\S]*?):=\s*by\s+sorry",
    re.MULTILINE,
)


def load_formalization(path: Path) -> dict:
    if yaml is None:
        raise SystemExit("PyYAML is required: pip install pyyaml")
    text = path.read_text(encoding="utf-8")
    doc = yaml.safe_load(text)
    if not isinstance(doc, dict):
        raise SystemExit(f"{path} must contain one top-level mapping")
    return doc


def load_comparator(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def check_human_only(names: list[str], field: str) -> list[str]:
    errors: list[str] = []
    for name in names:
        if not isinstance(name, str) or not name.strip():
            errors.append(f"{field} contains empty name")
        elif AI_NAME_PATTERNS.search(name):
            errors.append(f"{field} must name humans only; suspicious entry: {name!r}")
    return errors


def check_license(formalization: dict) -> list[str]:
    errors: list[str] = []
    declared = formalization.get("project", {}).get("license")
    licence_files = list(ROOT.glob("LICENSE*")) + list(ROOT.glob("Licence*"))
    if not licence_files:
        errors.append("missing root licence file")
        return errors
    if declared != "Apache-2.0":
        errors.append(f"project.license must be Apache-2.0, got {declared!r}")
    return errors


def check_required_fields(formalization: dict) -> list[str]:
    errors: list[str] = []
    if formalization.get("version") != "v0.4":
        errors.append(f"formalization.yaml version must be v0.4, got {formalization.get('version')!r}")
    project = formalization.get("project", {})
    for key in ("name", "description", "authors", "license", "responsible_maintainers"):
        if key not in project:
            errors.append(f"missing project.{key}")
    desc = project.get("description", "")
    if not isinstance(desc, str) or not desc.strip():
        errors.append("project.description must be nonempty")
    classification = formalization.get("classification", {})
    arxiv = classification.get("arxiv")
    if not isinstance(arxiv, list) or not arxiv:
        errors.append("classification.arxiv must be a nonempty list")
    automation = formalization.get("automation", {})
    methods = automation.get("methods")
    if not isinstance(methods, list) or not methods:
        errors.append("automation.methods must be a nonempty list")
    review = formalization.get("review", {})
    if not review.get("status"):
        errors.append("review.status must be nonempty")
    sources = formalization.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a nonempty list")
    return errors


def comparator_declarations(cfg: dict) -> list[str]:
    return list(cfg.get("theorem_names", [])) + list(cfg.get("definition_names", []))


def short_name(full: str) -> str:
    return full.split(".")[-1]


def main_result_declaration(entry: object) -> str | None:
    if isinstance(entry, dict):
        decl = entry.get("declaration")
        return decl if isinstance(decl, str) and decl else None
    if isinstance(entry, str) and entry.strip():
        return entry.strip()
    return None


def check_main_results(formalization: dict, cfg: dict) -> list[str]:
    errors: list[str] = []
    compared = set(comparator_declarations(cfg))
    for entry in formalization.get("status", {}).get("main_results", []) or []:
        decl = main_result_declaration(entry)
        if decl and decl not in compared:
            errors.append(f"main_results declaration {decl!r} not in comparator.json")
    return errors


def check_alignment(formalization: dict, challenge_text: str, cfg: dict) -> list[str]:
    errors: list[str] = []
    compared_short = {short_name(name) for name in comparator_declarations(cfg)}
    for entry in formalization.get("alignment", {}).get("statements", []) or []:
        lean = entry.get("lean")
        if not isinstance(lean, str) or not lean.strip():
            continue
        if " through " in lean.lower() or ";" in lean:
            continue
        token = lean.strip().split()[-1]
        if token not in compared_short:
            continue
        if token not in challenge_text:
            errors.append(
                f"alignment statement lean name {lean!r} (token {token!r}) not found in Challenge.lean"
            )
    return errors


def sorry_qualified_defs(challenge_text: str) -> set[str]:
    """Fully qualified names of Challenge definitions whose body is `sorry`."""
    result: set[str] = set()
    for ns_match in re.finditer(r"^namespace\s+(\S+)\s*$", challenge_text, re.MULTILINE):
        ns = ns_match.group(1)
        start = ns_match.end()
        end_match = re.search(rf"^end\s+{re.escape(ns)}\s*$", challenge_text[start:], re.MULTILINE)
        if not end_match:
            continue
        block = challenge_text[start : start + end_match.start()]
        for dm in SORRY_DEF.finditer(block):
            result.add(f"{ns}.{dm.group(1)}")
    return result


def theorem_statement(challenge_text: str, name: str) -> str | None:
    pattern = THEOREM_BODY.pattern.format(name=re.escape(name))
    match = re.search(pattern, challenge_text, re.MULTILINE)
    return match.group(0) if match else None


def compared_definition_names(cfg: dict) -> set[str]:
    return set(cfg.get("definition_names", []))


def check_sorry_definition_pinning(cfg: dict, challenge_text: str) -> list[str]:
    """Every sorry'd Challenge def referenced by a compared theorem must be compared."""
    errors: list[str] = []
    sorry_defs = sorry_qualified_defs(challenge_text)
    pinned = compared_definition_names(cfg)
    for full_name in cfg.get("theorem_names", []):
        short = short_name(full_name)
        statement = theorem_statement(challenge_text, short)
        if statement is None:
            errors.append(
                f"compared theorem {full_name!r} not found as `sorry` theorem in Challenge.lean"
            )
            continue
        referenced = set(QUALIFIED_NAME.findall(statement))
        opaque = sorted(q for q in referenced if q in sorry_defs and q not in pinned)
        if opaque:
            errors.append(
                f"{full_name} references opaque Challenge definitions not listed in "
                f"comparator.json definition_names: {', '.join(opaque)}"
            )
    return errors


def check_scope_comparator_sync(formalization: dict, cfg: dict) -> list[str]:
    """formalization.yaml must not contradict comparator.json."""
    errors: list[str] = []
    scope = str(formalization.get("status", {}).get("scope", ""))
    theorems = cfg.get("theorem_names", [])
    main_results = [
        main_result_declaration(entry)
        for entry in formalization.get("status", {}).get("main_results", []) or []
    ]
    main_results = [name for name in main_results if name]
    missing_from_main = sorted(set(theorems) - set(main_results))
    if missing_from_main:
        errors.append(
            "comparator theorem_names not listed in status.main_results: "
            + ", ".join(missing_from_main)
        )

    count_match = re.search(r"(\d+)\s+compared (?:theorem|result)", scope.lower())
    if count_match:
        claimed = int(count_match.group(1))
        actual = len(theorems)
        if claimed != actual:
            errors.append(
                f"status.scope claims {claimed} compared results but comparator.json lists {actual}"
            )

    limitations = " ".join(str(x) for x in formalization.get("limitations", []) or [])
    if "Solution.lean imports" in limitations and "Scott1964" not in limitations:
        errors.append("limitations should mention Solution.lean imports Scott1964 proofs")
    return errors


def check_compared_sources(formalization: dict, cfg: dict) -> list[str]:
    """Each hinted compared theorem needs a matching formalization.yaml source."""
    errors: list[str] = []
    sources_blob = json.dumps(formalization.get("sources", []), ensure_ascii=False).lower()
    for full_name in cfg.get("theorem_names", []):
        hints = THEOREM_SOURCE_HINTS.get(full_name)
        if not hints:
            continue
        if not any(h.lower() in sources_blob for h in hints):
            errors.append(
                f"compared theorem {full_name!r} requires a formalization.yaml sources entry "
                f"mentioning one of: {', '.join(hints)}"
            )
    return errors


def main() -> int:
    formalization_path = ROOT / "formalization.yaml"
    comparator_path = ROOT / "comparator.json"
    challenge_path = ROOT / "Challenge.lean"

    formalization = load_formalization(formalization_path)
    cfg = load_comparator(comparator_path)
    challenge_text = challenge_path.read_text(encoding="utf-8")

    errors: list[str] = []
    errors.extend(check_required_fields(formalization))
    errors.extend(
        check_human_only(formalization.get("project", {}).get("authors", []), "project.authors")
    )
    errors.extend(
        check_human_only(
            formalization.get("project", {}).get("responsible_maintainers", []),
            "project.responsible_maintainers",
        )
    )
    errors.extend(check_license(formalization))
    errors.extend(check_main_results(formalization, cfg))
    errors.extend(check_alignment(formalization, challenge_text, cfg))
    errors.extend(check_sorry_definition_pinning(cfg, challenge_text))
    errors.extend(check_scope_comparator_sync(formalization, cfg))
    errors.extend(check_compared_sources(formalization, cfg))

    if errors:
        print("FAIL: editorial pre-checks:")
        for err in errors:
            print(f"  {err}")
        return 1

    print(
        f"OK: editorial pre-checks passed "
        f"({len(comparator_declarations(cfg))} compared declarations)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
