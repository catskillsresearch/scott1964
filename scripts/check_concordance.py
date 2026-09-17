#!/usr/bin/env python3
"""Validate the source-to-Lean concordance embedded in ``arxiv.md``.

The checker covers marker structure, exact physical-line coverage, verbatim
Scott panels, and referenced Lean declarations.  Card C16 is intentionally
excepted from quote comparison because it discloses editorial OCR metadata;
its source range remains part of the required contiguous coverage.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


SOURCE_FIRST = 7
SOURCE_LAST = 507
SCOTT_LABEL = "**Scott 1964 (verbatim).**"
LEAN_LABEL = "**Lean 4 correspondence (exact source).**"
RECONSTRUCTION_LABEL = "**Mathematical reconstruction from Lean.**"

OPEN_PATTERN = (
    r"^<!-- scott-concordance: card=(?P<card>[^\s]+) "
    r"source-lines=(?P<start>[0-9]+)-(?P<end>[0-9]+) "
    r"lean=(?P<lean>[^\r\n]*?) -->$"
)
CLOSE_PATTERN = r"^<!-- /scott-concordance -->$"
OPEN_RE = re.compile(OPEN_PATTERN, re.MULTILINE)
CLOSE_RE = re.compile(CLOSE_PATTERN, re.MULTILINE)
TOKEN_RE = re.compile(
    rf"(?P<open>{OPEN_PATTERN})|(?P<close>{CLOSE_PATTERN})", re.MULTILINE
)
MARKER_LIKE_RE = re.compile(
    r"^.*<!--[^\r\n]*scott-concordance[^\r\n]*(?:-->)?.*$", re.MULTILINE
)
PAGE_COMMENT_RE = re.compile(r"<!--\s*page\b.*?-->", re.IGNORECASE | re.DOTALL)
TRANSCRIPTION_HEADING_RE = re.compile(
    r"^# Transcription \(LLM vision OCR\)\s*$", re.MULTILINE
)
DECLARATION_RE = re.compile(
    r"^(?:(?:noncomputable|private|protected|unsafe)\s+)*"
    r"(?:def|theorem|structure|abbrev|class|inductive)\s+"
    r"(?P<name>[^\s({:\[]+)",
    re.MULTILINE,
)


@dataclass(frozen=True)
class Card:
    card_id: str
    source_start: int
    source_end: int
    lean_field: str
    body: str
    marker_line: int
    marker_offset: int


def line_number(text: str, offset: int) -> int:
    """Return the one-based physical line containing ``offset``."""
    return text.count("\n", 0, offset) + 1


def parse_cards(text: str, errors: list[str]) -> list[Card]:
    """Parse exact marker tokens and diagnose malformed nesting or ordering."""
    exact_spans = {
        match.span() for regex in (OPEN_RE, CLOSE_RE) for match in regex.finditer(text)
    }
    for match in MARKER_LIKE_RE.finditer(text):
        if match.span() not in exact_spans:
            errors.append(
                f"arxiv.md:{line_number(text, match.start())}: malformed "
                "scott-concordance marker"
            )

    stack: list[tuple[re.Match[str], int]] = []
    cards: list[Card] = []
    for token in TOKEN_RE.finditer(text):
        if token.group("open") is not None:
            if stack:
                outer = stack[-1][0]
                errors.append(
                    f"arxiv.md:{line_number(text, token.start())}: nested opening "
                    f"marker inside card {outer.group('card')}"
                )
            stack.append((token, token.end()))
            continue

        if not stack:
            errors.append(
                f"arxiv.md:{line_number(text, token.start())}: closing marker "
                "without a preceding opening marker"
            )
            continue

        opening, body_start = stack.pop()
        cards.append(
            Card(
                card_id=opening.group("card"),
                source_start=int(opening.group("start")),
                source_end=int(opening.group("end")),
                lean_field=opening.group("lean"),
                body=text[body_start : token.start()],
                marker_line=line_number(text, opening.start()),
                marker_offset=opening.start(),
            )
        )

    for opening, _ in stack:
        errors.append(
            f"arxiv.md:{line_number(text, opening.start())}: card "
            f"{opening.group('card')} has no closing marker"
        )

    cards.sort(key=lambda card: card.marker_offset)
    if not cards:
        errors.append("arxiv.md: no complete scott-concordance cards found")
    return cards


def compact_ranges(numbers: list[int]) -> str:
    """Format sorted integers as compact inclusive ranges."""
    if not numbers:
        return ""
    ranges: list[str] = []
    start = previous = numbers[0]
    for number in numbers[1:]:
        if number == previous + 1:
            previous = number
            continue
        ranges.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = number
    ranges.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(ranges)


def validate_ranges(cards: list[Card], source_count: int, errors: list[str]) -> None:
    """Require ordered, nonoverlapping coverage of physical lines 7 through 507."""
    if source_count < SOURCE_LAST:
        errors.append(
            f"sources/ScottMeasurement1964_vision.md: has {source_count} physical "
            f"lines; line {SOURCE_LAST} is required"
        )

    seen_ids: dict[str, int] = {}
    for card in cards:
        if card.card_id in seen_ids:
            errors.append(
                f"arxiv.md:{card.marker_line}: duplicate card ID {card.card_id} "
                f"(first used at line {seen_ids[card.card_id]})"
            )
        else:
            seen_ids[card.card_id] = card.marker_line
        if card.source_start > card.source_end:
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} has reversed "
                f"source range {card.source_start}-{card.source_end}"
            )
        if card.source_start < SOURCE_FIRST or card.source_end > SOURCE_LAST:
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} range "
                f"{card.source_start}-{card.source_end} lies outside "
                f"{SOURCE_FIRST}-{SOURCE_LAST}"
            )

    for previous, current in zip(cards, cards[1:]):
        if current.source_start < previous.source_start:
            errors.append(
                f"arxiv.md:{current.marker_line}: source ranges are out of order: "
                f"{current.card_id} starts at {current.source_start} after "
                f"{previous.card_id} starts at {previous.source_start}"
            )
        if current.source_start <= previous.source_end:
            errors.append(
                f"arxiv.md:{current.marker_line}: source ranges overlap: "
                f"{previous.card_id} ends at {previous.source_end}, while "
                f"{current.card_id} starts at {current.source_start}"
            )
        elif current.source_start > previous.source_end + 1:
            errors.append(
                f"arxiv.md:{current.marker_line}: gap in source ranges between "
                f"{previous.card_id} ({previous.source_end}) and "
                f"{current.card_id} ({current.source_start})"
            )

    coverage = {line: 0 for line in range(SOURCE_FIRST, SOURCE_LAST + 1)}
    for card in cards:
        for physical_line in range(
            max(card.source_start, SOURCE_FIRST),
            min(card.source_end, SOURCE_LAST) + 1,
        ):
            coverage[physical_line] += 1
    missing = [line for line, count in coverage.items() if count == 0]
    repeated = [line for line, count in coverage.items() if count > 1]
    if missing:
        errors.append(
            f"source coverage has gaps at physical lines {compact_ranges(missing)}"
        )
    if repeated:
        errors.append(
            "source coverage is not unique at physical lines "
            f"{compact_ranges(repeated)}"
        )

    c16_cards = [card for card in cards if card.card_id == "C16"]
    if not c16_cards:
        errors.append("arxiv.md: missing required editorial exclusion card C16")
    elif len(c16_cards) == 1 and (
        c16_cards[0].source_start,
        c16_cards[0].source_end,
    ) != (155, 165):
        errors.append(
            f"arxiv.md:{c16_cards[0].marker_line}: C16 must cover source lines "
            f"155-165, not {c16_cards[0].source_start}-{c16_cards[0].source_end}"
        )


def label_matches(body: str, label: str) -> list[re.Match[str]]:
    """Find exact panel-label occurrences, including labels with inline content."""
    return list(re.finditer(re.escape(label), body, flags=re.MULTILINE))


def normalized_content(text: str) -> str:
    """Drop editorial markers and blank lines, then normalize all whitespace."""
    without_pages = PAGE_COMMENT_RE.sub("", text)
    without_editorial_heading = TRANSCRIPTION_HEADING_RE.sub("", without_pages)
    nonblank = [line for line in without_editorial_heading.splitlines() if line.strip()]
    return re.sub(r"\s+", " ", "\n".join(nonblank)).strip()


def quoted_panel_content(
    card: Card, scott_label: re.Match[str], lean_label: re.Match[str], errors: list[str]
) -> str:
    """Extract and remove Markdown blockquote prefixes from a Scott panel."""
    panel = card.body[scott_label.end() : lean_label.start()]
    stripped_lines: list[str] = []
    for relative_line, line in enumerate(panel.splitlines(), start=1):
        if not line.strip():
            stripped_lines.append("")
            continue
        quote = re.match(r"^[ \t]*>[ \t]?(.*)$", line)
        if quote is None:
            panel_line = (
                card.marker_line
                + card.body[: scott_label.end()].count("\n")
                + relative_line
            )
            errors.append(
                f"arxiv.md:{panel_line}: card {card.card_id} Scott panel contains "
                "a non-blockquote line"
            )
            stripped_lines.append(line)
        else:
            stripped_lines.append(quote.group(1))
    return normalized_content("\n".join(stripped_lines))


def validate_panels_and_quotes(
    cards: list[Card], source_lines: list[str], errors: list[str]
) -> int:
    """Validate panel labels and compare each non-C16 quotation to its source."""
    quote_checks = 0
    labels = (SCOTT_LABEL, LEAN_LABEL, RECONSTRUCTION_LABEL)
    for card in cards:
        matches = {label: label_matches(card.body, label) for label in labels}
        for label, found in matches.items():
            if len(found) != 1:
                errors.append(
                    f"arxiv.md:{card.marker_line}: card {card.card_id} requires "
                    f"exactly one {label!r} label; found {len(found)}"
                )
        if any(len(found) != 1 for found in matches.values()):
            continue

        scott_match = matches[SCOTT_LABEL][0]
        lean_match = matches[LEAN_LABEL][0]
        reconstruction_match = matches[RECONSTRUCTION_LABEL][0]
        if not (
            scott_match.start() < lean_match.start() < reconstruction_match.start()
        ):
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} panel labels "
                "are not in Scott, Lean, reconstruction order"
            )
            continue

        if card.card_id == "C16":
            continue
        if not (
            SOURCE_FIRST <= card.source_start <= card.source_end <= len(source_lines)
        ):
            continue

        actual = quoted_panel_content(card, scott_match, lean_match, errors)
        expected = normalized_content(
            "\n".join(source_lines[card.source_start - 1 : card.source_end])
        )
        quote_checks += 1
        if actual != expected:
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} Scott quote "
                f"does not match source lines {card.source_start}-{card.source_end}"
            )
    return quote_checks


def parse_lean_references(cards: list[Card], errors: list[str]) -> list[tuple[Card, str]]:
    """Split each lean field, accepting only ``none`` or nonempty references."""
    references: list[tuple[Card, str]] = []
    for card in cards:
        parts = [part.strip() for part in card.lean_field.split(",")]
        if card.lean_field.strip() == "none":
            continue
        if not card.lean_field.strip():
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} has an empty "
                "lean field; use none or one or more references"
            )
            continue
        if any(not part for part in parts):
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} has an empty "
                "Lean reference between commas"
            )
            continue
        if "none" in parts:
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} mixes none "
                "with Lean references"
            )
            continue
        references.extend((card, part) for part in parts)
    return references


def mask_lean_comments_and_strings(text: str) -> str:
    """Mask Lean comments and strings while preserving lines and columns."""
    result = list(text)
    index = 0
    block_depth = 0
    in_string = False
    while index < len(text):
        if block_depth:
            if text.startswith("/-", index):
                result[index : index + 2] = "  "
                block_depth += 1
                index += 2
            elif text.startswith("-/", index):
                result[index : index + 2] = "  "
                block_depth -= 1
                index += 2
            else:
                if text[index] != "\n":
                    result[index] = " "
                index += 1
            continue

        if in_string:
            if text[index] == "\\" and index + 1 < len(text):
                if text[index] != "\n":
                    result[index] = " "
                if text[index + 1] != "\n":
                    result[index + 1] = " "
                index += 2
            else:
                if text[index] == '"':
                    in_string = False
                if text[index] != "\n":
                    result[index] = " "
                index += 1
            continue

        if text.startswith("--", index):
            while index < len(text) and text[index] != "\n":
                result[index] = " "
                index += 1
        elif text.startswith("/-", index):
            result[index : index + 2] = "  "
            block_depth = 1
            index += 2
        elif text[index] == '"':
            result[index] = " "
            in_string = True
            index += 1
        else:
            index += 1
    return "".join(result)


def lean_declarations(lean_files: list[Path], errors: list[str]) -> set[str]:
    """Collect terminal identifiers of supported top-level Lean declarations."""
    declarations: set[str] = set()
    for path in lean_files:
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            errors.append(f"{path}: cannot read Lean source: {exc}")
            continue
        masked = mask_lean_comments_and_strings(text)
        for match in DECLARATION_RE.finditer(masked):
            declarations.add(match.group("name").split(".")[-1])
    return declarations


def validate_lean_references(
    references: list[tuple[Card, str]], declarations: set[str], errors: list[str]
) -> None:
    """Require every reference's terminal name to be a declared identifier."""
    for card, reference in references:
        terminal = reference.rsplit(".", 1)[-1]
        if terminal not in declarations:
            errors.append(
                f"arxiv.md:{card.marker_line}: card {card.card_id} references "
                f"missing Lean declaration {reference!r} (terminal identifier "
                f"{terminal!r})"
            )


def run() -> int:
    root = Path(__file__).resolve().parent.parent
    arxiv_path = root / "arxiv.md"
    source_path = root / "sources" / "ScottMeasurement1964_vision.md"
    lean_root = root / "Scott1964"
    errors: list[str] = []

    try:
        arxiv_text = arxiv_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"concordance check failed: cannot read {arxiv_path}: {exc}", file=sys.stderr)
        return 1
    try:
        source_text = source_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(
            f"concordance check failed: cannot read {source_path}: {exc}",
            file=sys.stderr,
        )
        return 1

    source_lines = source_text.splitlines()
    cards = parse_cards(arxiv_text, errors)
    validate_ranges(cards, len(source_lines), errors)
    quote_checks = validate_panels_and_quotes(cards, source_lines, errors)
    references = parse_lean_references(cards, errors)

    lean_files = sorted(lean_root.rglob("*.lean")) if lean_root.is_dir() else []
    if not lean_files:
        errors.append(f"{lean_root}: no Scott1964/**/*.lean files found")
    declarations = lean_declarations(lean_files, errors)
    validate_lean_references(references, declarations, errors)

    if errors:
        print(
            f"concordance check failed with {len(errors)} error(s):",
            file=sys.stderr,
        )
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        f"concordance OK: {len(cards)} cards, source lines "
        f"{SOURCE_FIRST}-{SOURCE_LAST}, {quote_checks} quote checks, "
        f"{len(references)} Lean refs"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
