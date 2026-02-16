#!/usr/bin/env python3
"""Generate a Markdown inventory of Typer commands from bbdc_cli source."""

from __future__ import annotations

import argparse
import ast
from pathlib import Path
from typing import List, Tuple

APP_PREFIX = {
    "app": "",
    "pr_app": "pr",
    "participants_app": "pr participants",
    "comments_app": "pr comments",
    "blockers_app": "pr blockers",
    "review_app": "pr review",
    "auto_merge_app": "pr auto-merge",
}


def _is_typer_call(node: ast.AST) -> Tuple[str, List[str], bool] | None:
    if not isinstance(node, ast.Call):
        return None
    func = node.func
    if not isinstance(func, ast.Attribute):
        return None
    if not isinstance(func.value, ast.Name) or func.value.id != "typer":
        return None
    kind = func.attr
    if kind not in {"Option", "Argument"}:
        return None

    flags: List[str] = []
    required = False

    for arg in node.args:
        if isinstance(arg, ast.Constant):
            if isinstance(arg.value, str):
                if arg.value.startswith("-"):
                    flags.append(arg.value)
            elif arg.value is Ellipsis:
                required = True
    return kind, flags, required


def _parameter_cells(fn: ast.FunctionDef) -> str:
    args = fn.args.args
    defaults = fn.args.defaults
    default_start = len(args) - len(defaults)

    cells: List[str] = []
    for index, arg in enumerate(args):
        default = defaults[index - default_start] if index >= default_start else None
        parsed = _is_typer_call(default) if default is not None else None
        if parsed is None:
            cells.append(arg.arg)
            continue

        kind, flags, required = parsed
        if kind == "Argument":
            label = f"<{arg.arg}>"
            if required:
                label += "*"
            cells.append(label)
            continue

        if not flags:
            flags = [f"--{arg.arg.replace('_', '-')}"]
        label = "/".join(flags)
        if required:
            label += "*"
        cells.append(label)

    return ", ".join(cells)


def _command_rows(module: ast.Module) -> List[Tuple[str, str, str, str]]:
    rows: List[Tuple[str, str, str, str]] = []
    for node in module.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        for dec in node.decorator_list:
            if not isinstance(dec, ast.Call):
                continue
            if not isinstance(dec.func, ast.Attribute):
                continue
            if dec.func.attr != "command":
                continue
            if not isinstance(dec.func.value, ast.Name):
                continue

            app_name = dec.func.value.id
            prefix = APP_PREFIX.get(app_name)
            if prefix is None:
                continue

            cmd_name = ""
            if dec.args and isinstance(dec.args[0], ast.Constant) and isinstance(dec.args[0].value, str):
                cmd_name = dec.args[0].value
            if not cmd_name:
                cmd_name = node.name

            full_command = (f"{prefix} {cmd_name}").strip()
            group = prefix or "root"
            params = _parameter_cells(node)
            rows.append((group, full_command, node.name, params))

    rows.sort(key=lambda r: (r[0], r[1]))
    return rows


def generate_markdown(source: Path, rows: List[Tuple[str, str, str, str]]) -> str:
    lines = [
        "# bbdc CLI Command Inventory",
        "",
        f"Source: `{source}`",
        "",
        "`*` marks required option/argument.",
        "",
        "| Group | Command | Function | Parameters |",
        "|---|---|---|---|",
    ]
    for group, command, function, params in rows:
        lines.append(f"| {group} | `{command}` | `{function}` | `{params}` |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate command inventory from bbdc Typer source.")
    parser.add_argument("--source", required=True, help="Path to bbdc_cli/__main__.py")
    parser.add_argument("--output", default="", help="Optional output markdown path")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Source file not found: {source}")

    module = ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    rows = _command_rows(module)
    markdown = generate_markdown(source, rows)

    if args.output:
        output = Path(args.output).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(markdown, encoding="utf-8")
        print(f"Wrote {len(rows)} commands to {output}")
    else:
        print(markdown)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
