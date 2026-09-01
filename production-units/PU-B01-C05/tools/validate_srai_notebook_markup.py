#!/usr/bin/env python3
"""Validate or normalize mathematical Markdown in an SRAI notebook."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tempfile


LEGACY_DELIMITERS = {
    r"\[": "$$",
    r"\]": "$$",
    r"\(": "$",
    r"\)": "$",
}
MATH_SIGNAL = re.compile(r"(?:\\[A-Za-z]+|[_^=]|\\,|\\;|\\qquad)")
UNESCAPED_DOLLAR = re.compile(r"(?<!\\)\$")


def _replace_bracket_blocks(text: str) -> tuple[str, int]:
    """Convert standalone equation-like [ ... ] blocks to $$ ... $$."""
    lines = text.splitlines()
    converted = 0
    index = 0
    while index < len(lines):
        if lines[index].strip() != "[":
            index += 1
            continue
        closing = index + 1
        while closing < len(lines) and lines[closing].strip() != "]":
            closing += 1
        if closing >= len(lines):
            index += 1
            continue
        content = "\n".join(lines[index + 1 : closing])
        if MATH_SIGNAL.search(content):
            lines[index] = "$$"
            lines[closing] = "$$"
            converted += 1
        index = closing + 1
    suffix = "\n" if text.endswith("\n") else ""
    return "\n".join(lines) + suffix, converted


def normalize_markdown(text: str) -> tuple[str, int]:
    changes = 0
    normalized = text
    for old, new in LEGACY_DELIMITERS.items():
        count = normalized.count(old)
        if count:
            normalized = normalized.replace(old, new)
            changes += count
    normalized, bracket_changes = _replace_bracket_blocks(normalized)
    return normalized, changes + bracket_changes


def _active_lines(text: str):
    """Yield lines outside fenced code blocks."""
    fenced = False
    for number, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced:
            yield number, line


def _balanced_braces(expression: str) -> bool:
    depth = 0
    for index, char in enumerate(expression):
        escaped = index > 0 and expression[index - 1] == "\\"
        if char == "{" and not escaped:
            depth += 1
        elif char == "}" and not escaped:
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def validate_markdown(text: str, cell_index: int) -> list[str]:
    errors: list[str] = []
    active = list(_active_lines(text))
    display_open = False
    math_fragments: list[str] = []

    for line_number, line in active:
        for delimiter in LEGACY_DELIMITERS:
            if delimiter in line:
                errors.append(
                    f"Cell {cell_index}, line {line_number}: forbidden legacy delimiter {delimiter!r}"
                )

        stripped = line.strip()
        if stripped in {"[", "]"}:
            errors.append(
                f"Cell {cell_index}, line {line_number}: standalone square bracket may be an unconverted equation delimiter"
            )

        if "$$" in line:
            if stripped != "$$":
                errors.append(
                    f"Cell {cell_index}, line {line_number}: display delimiter $$ must be on its own line"
                )
                continue
            display_open = not display_open
            continue

        if display_open:
            math_fragments.append(line)
            continue

        clean = re.sub(r"`[^`]*`", "", line)
        dollars = list(UNESCAPED_DOLLAR.finditer(clean))
        if len(dollars) % 2:
            errors.append(
                f"Cell {cell_index}, line {line_number}: unbalanced inline $ delimiter"
            )
        for start, end in zip(dollars[0::2], dollars[1::2]):
            math_fragments.append(clean[start.end() : end.start()])

    if display_open:
        errors.append(f"Cell {cell_index}: unclosed $$ display block")
    for fragment in math_fragments:
        if not _balanced_braces(fragment):
            errors.append(f"Cell {cell_index}: unbalanced LaTeX braces in math expression")
    return errors


def audit(notebook: Path, fix: bool = False) -> dict:
    data = json.loads(notebook.read_text(encoding="utf-8-sig"))
    errors: list[str] = []
    changed_cells = 0
    change_count = 0

    for index, cell in enumerate(data.get("cells", [])):
        if cell.get("cell_type") != "markdown":
            continue
        original = "".join(cell.get("source", []))
        current = original
        if fix:
            current, changes = normalize_markdown(current)
            if changes:
                cell["source"] = current.splitlines(keepends=True)
                if current and not current.endswith("\n"):
                    cell["source"][-1] = cell["source"][-1].rstrip("\n")
                changed_cells += 1
                change_count += changes
        errors.extend(validate_markdown(current, index))

    if fix and changed_cells and not errors:
        payload = json.dumps(data, indent=1, ensure_ascii=False) + "\n"
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", newline="\n", delete=False, dir=notebook.parent
        ) as stream:
            stream.write(payload)
            temporary = Path(stream.name)
        temporary.replace(notebook)

    return {
        "status": "PASS" if not errors else "FAIL",
        "notebook": str(notebook.resolve()),
        "mode": "normalize-and-validate" if fix else "validate",
        "changed_cells": changed_cells,
        "delimiter_changes": change_count,
        "errors": errors,
        "standard": {
            "inline_math": "$...$",
            "display_math": "standalone $$ delimiters",
            "forbidden": [r"\(...\)", r"\[...\]", "equation-like standalone [ ... ]"],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--fix", action="store_true")
    args = parser.parse_args()
    result = audit(args.notebook, args.fix)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
