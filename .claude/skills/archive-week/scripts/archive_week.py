#!/usr/bin/env python3
"""Archive finished weeks.

Given the upcoming week (default: the ISO week after the current one):

1. Cut every row in Notes/Daily/Long Term.md whose week is before the
   upcoming week and append it to Notes/Daily/Archive/Long Term.md
   (created with the same header if missing).
2. Move every Notes/Daily/YYYY-WN.md whose week is before the upcoming
   week into Notes/Daily/Archive/.

Run new_week.py first; it reads the prior week's file for carry-forward.

Usage:
    archive_week.py [--root WORKSPACE] [--week YYYY-WN] [--dry-run]
"""

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path


def monday(year: int, week: int) -> dt.date:
    return dt.date.fromisocalendar(year, week, 1)


def next_week(today: dt.date) -> tuple[int, int]:
    y, w, _ = (monday(*today.isocalendar()[:2]) + dt.timedelta(weeks=1)).isocalendar()
    return y, w


def parse_week(text: str) -> tuple[int, int]:
    m = re.fullmatch(r"(\d{4})-W(\d{1,2})", text)
    if not m:
        raise SystemExit(f"bad --week {text!r}; expected YYYY-WN")
    return int(m.group(1)), int(m.group(2))


def row_monday(cells: list[str], around: dt.date) -> dt.date | None:
    """Resolve a row's Monday from its Week and Start cells.

    Start has no year ("Oct 19"); try the years around the target and keep
    the one that lands on a Monday of the stated ISO week.
    """
    if len(cells) < 2:
        return None
    m = re.search(r"(\d+)\s*$", cells[0])
    if not m:
        return None
    week = int(m.group(1))
    for year in (around.year - 1, around.year, around.year + 1):
        try:
            d = dt.datetime.strptime(f"{cells[1]} {year}", "%b %d %Y").date()
        except ValueError:
            continue
        if d.weekday() == 0 and d.isocalendar()[1] == week:
            return d
    for year in (around.year - 1, around.year, around.year + 1):
        try:
            return monday(year, week) if abs((monday(year, week) - around).days) < 200 else None
        except ValueError:
            continue
    return None


def archive_long_term(daily: Path, cutoff: dt.date, dry_run: bool) -> int:
    src = daily / "Long Term.md"
    if not src.exists():
        return 0
    lines = src.read_text().splitlines()
    table_idx = [i for i, l in enumerate(lines) if l.strip().startswith("|")]
    if len(table_idx) < 2:
        return 0
    header, sep = lines[table_idx[0]], lines[table_idx[1]]
    past: list[str] = []
    keep: list[str] = []
    for i, line in enumerate(lines):
        if i in table_idx[2:]:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            d = row_monday(cells, cutoff)
            if d is not None and d < cutoff:
                past.append(line)
                continue
        keep.append(line)
    if not past:
        return 0
    dest = daily / "Archive" / "Long Term.md"
    if dry_run:
        print(f"would move {len(past)} row(s) to {dest}")
        return len(past)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.write_text(f"\n{header}\n{sep}\n")
    with dest.open("a") as f:
        f.write("\n".join(past) + "\n")
    src.write_text("\n".join(keep) + "\n")
    print(f"moved {len(past)} row(s) to {dest}")
    return len(past)


def archive_week_files(daily: Path, cutoff: dt.date, dry_run: bool) -> int:
    moved = 0
    for path in sorted(daily.glob("*-W*.md")):
        m = re.fullmatch(r"(\d{4})-W(\d{1,2})", path.stem)
        if not m:
            continue
        try:
            start = monday(int(m.group(1)), int(m.group(2)))
        except ValueError:
            continue
        if start >= cutoff:
            continue
        dest = daily / "Archive" / path.name
        if dry_run:
            print(f"would move {path.name} -> Archive/")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(dest))
            print(f"moved {path.name} -> Archive/")
        moved += 1
    return moved


def main() -> int:
    here = Path(__file__).resolve()
    default_root = here.parents[4]
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=default_root)
    ap.add_argument("--week", help="upcoming week as YYYY-WN (default: next ISO week)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    daily = args.root / "Notes" / "Daily"
    year, week = parse_week(args.week) if args.week else next_week(dt.date.today())
    cutoff = monday(year, week)
    n = archive_long_term(daily, cutoff, args.dry_run)
    n += archive_week_files(daily, cutoff, args.dry_run)
    if n == 0:
        print("nothing to archive")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
