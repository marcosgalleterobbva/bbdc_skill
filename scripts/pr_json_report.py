#!/usr/bin/env python3
"""Convert bbdc PR JSON into a concise Markdown report."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Iterable, List


def _read_payload(path: str) -> Any:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _normalize_prs(payload: Any) -> List[dict]:
    if isinstance(payload, list):
        return [p for p in payload if isinstance(p, dict)]
    if isinstance(payload, dict):
        values = payload.get("values")
        if isinstance(values, list):
            return [p for p in values if isinstance(p, dict)]
    return []


def _val(obj: Any, *path: str) -> str:
    cur = obj
    for key in path:
        if not isinstance(cur, dict):
            return ""
        cur = cur.get(key)
    if cur is None:
        return ""
    return str(cur)


def _trim(text: str, max_len: int) -> str:
    if len(text) <= max_len:
        return text
    if max_len <= 1:
        return text[:max_len]
    return text[: max_len - 1] + "…"


def _table(prs: Iterable[dict], max_title: int) -> str:
    rows = [
        "| ID | State | Author | Source -> Target | Title | Link |",
        "|---:|---|---|---|---|---|",
    ]

    for pr in prs:
        pr_id = _val(pr, "id")
        state = _val(pr, "state")
        author = _val(pr, "author", "user", "displayName") or _val(pr, "author", "user", "name")
        source = _val(pr, "fromRef", "displayId") or _val(pr, "fromRef", "id")
        target = _val(pr, "toRef", "displayId") or _val(pr, "toRef", "id")
        title = _trim((_val(pr, "title") or "").replace("|", "\\|"), max_title)

        links = pr.get("links") if isinstance(pr, dict) else None
        href = ""
        if isinstance(links, dict):
            self_links = links.get("self")
            if isinstance(self_links, list) and self_links:
                first = self_links[0]
                if isinstance(first, dict):
                    href = str(first.get("href") or "")

        link_md = f"[open]({href})" if href else ""
        rows.append(f"| {pr_id} | {state} | {author} | {source} -> {target} | {title} | {link_md} |")

    return "\n".join(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build Markdown summary from bbdc PR JSON.")
    parser.add_argument("input", nargs="?", default="-", help="JSON file path or '-' for stdin")
    parser.add_argument("--max-title", type=int, default=90, help="Maximum title length in table")
    args = parser.parse_args()

    payload = _read_payload(args.input)
    prs = _normalize_prs(payload)

    if not prs:
        print("No pull requests found in input payload.")
        return 0

    print(f"Found {len(prs)} pull request(s).\n")
    print(_table(prs, args.max_title))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
