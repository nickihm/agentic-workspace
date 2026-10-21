#!/usr/bin/env python3
"""Create the weekly notes file for the next ISO week.

Writes Notes/Daily/YYYY-WN.md with, in this order:

1. Seven day bullets (Mon .. Sun) with month/day.
2. Long Term sections: the row for that week in Notes/Daily/Long Term.md,
   one top-level section per non-empty category column.
3. Carry-forward: top-level non-day sections from the prior week's file,
   keeping only unchecked `- [ ]` items (and anything nested under them).

Usage:
    new_week.py [--root WORKSPACE] [--week YYYY-WN] [--dry-run] [--force]

Defaults: --root is the workspace root (three levels above this script's
skill folder), --week is the ISO week after the current one.
"""

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

DAYS = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
INDENT = "\t"


def monday(year: int, week: int) -> dt.date:
    return dt.date.fromisocalendar(year, week, 1)


def shift_week(year: int, week: int, delta: int) -> tuple[int, int]:
    y, w, _ = (monday(year, week) + dt.timedelta(weeks=delta)).isocalendar()
    return y, w


def parse_week(text: str) -> tuple[int, int]:
    m = re.fullmatch(r"(\d{4})-W(\d{1,2})", text)
    if not m:
        raise SystemExit(f"bad --week {text!r}; expected YYYY-WN")
    return int(m.group(1)), int(m.group(2))


def week_file(daily: Path, year: int, week: int) -> Path:
    return daily / f"{year}-W{week}.md"


def day_bullets(year: int, week: int) -> list[str]:
    start = monday(year, week)
    return [
        f"- {DAYS[i]} {(start + dt.timedelta(days=i)).month}/{(start + dt.timedelta(days=i)).day}"
        for i in range(7)
    ]


def table_rows(path: Path) -> tuple[list[str], list[list[str]]]:
    """Return (header cells, body rows as cell lists) of the first markdown table."""
    rows = [l for l in path.read_text().splitlines() if l.strip().startswith("|")]
    if len(rows) < 2:
        return [], []
    split = lambda l: [c.strip() for c in l.strip().strip("|").split("|")]
    header = split(rows[0])
    body = [split(r) for r in rows[2:]]  # skip the |---| separator
    return header, body


def long_term_sections(long_term: Path, year: int, week: int) -> list[str]:
    if not long_term.exists():
        return []
    header, body = table_rows(long_term)
    if not header:
        return []
    start = monday(year, week)
    row = None
    for cells in body:
        m = re.search(r"(\d+)\s*$", cells[0]) if cells else None
        if not m or int(m.group(1)) != week:
            continue
        # Prefer a row whose Start cell matches this week's Monday (disambiguates years).
        if len(cells) > 1 and cells[1] == start.strftime("%b %d"):
            row = cells
            break
        row = row or cells
    if row is None:
        return []
    out: list[str] = []
    for name, cell in zip(header[3:], row[3:]):
        items = [i.strip() for i in re.split(r"<br\s*/?>", cell) if i.strip()]
        if not items:
            continue
        out.append(f"- {name}")
        out.extend(f"{INDENT}- {i}" for i in items)
    return out


def depth(line: str) -> int:
    stripped = line.lstrip("\t ")
    lead = line[: len(line) - len(stripped)]
    return lead.count("\t") + lead.count(" ") // 4


def is_day_bullet(line: str) -> bool:
    return re.match(r"-\s+(" + "|".join(DAYS) + r")\b", line) is not None


def carry_forward(prior: Path) -> list[str]:
    """Top-level non-day sections from the prior week, unchecked items only."""
    if not prior.exists():
        return []
    lines = prior.read_text().splitlines()
    out: list[str] = []
    section: list[str] = []
    keep_depth: int | None = None  # depth of the last kept `- [ ]` item
    in_section = False

    def flush():
        nonlocal section
        if len(section) > 1:
            out.extend(section)
        section = []

    for line in lines:
        if not line.strip():
            continue
        d = depth(line)
        body = line.strip()
        if d == 0:
            flush()
            in_section = body.startswith("-") and not is_day_bullet(body)
            keep_depth = None
            if in_section:
                section = [line]
            continue
        if not in_section:
            continue
        if keep_depth is not None and d > keep_depth:
            if not body.startswith("- [x]"):
                section.append(line)
            continue
        keep_depth = None
        if body.startswith("- [ ]"):
            section.append(line)
            keep_depth = d
    flush()
    return out


def main() -> int:
    here = Path(__file__).resolve()
    default_root = here.parents[4]  # scripts/ -> skill -> skills -> .claude -> root
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=default_root)
    ap.add_argument("--week", help="target week as YYYY-WN (default: next ISO week)")
    ap.add_argument("--dry-run", action="store_true", help="print instead of writing")
    ap.add_argument("--force", action="store_true", help="overwrite an existing file")
    args = ap.parse_args()

    daily = args.root / "Notes" / "Daily"
    today = dt.date.today()
    year, week = parse_week(args.week) if args.week else shift_week(*today.isocalendar()[:2], 1)
    target = week_file(daily, year, week)
    prior = week_file(daily, *shift_week(year, week, -1))

    if target.exists() and not args.force and not args.dry_run:
        print(f"exists, not overwriting: {target}", file=sys.stderr)
        return 1

    lines = day_bullets(year, week)
    lines += long_term_sections(daily / "Long Term.md", year, week)
    lines += carry_forward(prior)
    content = "\n".join(lines) + "\n"

    if args.dry_run:
        print(content, end="")
        return 0
    daily.mkdir(parents=True, exist_ok=True)
    target.write_text(content)
    print(f"wrote {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
