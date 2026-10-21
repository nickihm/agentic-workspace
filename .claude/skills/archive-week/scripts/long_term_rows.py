#!/usr/bin/env python3
"""Print empty Long Term.md table rows for a range of ISO weeks.

Append the output to Notes/Daily/Long Term.md when the table runs out of
future weeks. Pass the category columns from your table so the row widths match.

Usage:
    long_term_rows.py 2027-W1 2027-W52 [--columns "Work,Home,Family,Finance"] [--header]
"""

import argparse
import datetime as dt
import re


def parse_week(text: str) -> tuple[int, int]:
    m = re.fullmatch(r"(\d{4})-W(\d{1,2})", text)
    if not m:
        raise SystemExit(f"bad week {text!r}; expected YYYY-WN")
    return int(m.group(1)), int(m.group(2))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("start")
    ap.add_argument("end")
    ap.add_argument("--columns", default="Work,Home,Family,Finance")
    ap.add_argument("--header", action="store_true", help="also print the table header")
    args = ap.parse_args()

    cols = [c.strip() for c in args.columns.split(",") if c.strip()]
    if args.header:
        print("| " + " | ".join(["Week  ", "Start ", "End   "] + cols) + " |")
        print("| " + " | ".join(["------", "------", "------"] + ["-" * len(c) for c in cols]) + " |")

    d = dt.date.fromisocalendar(*parse_week(args.start), 1)
    last = dt.date.fromisocalendar(*parse_week(args.end), 1)
    while d <= last:
        week = d.isocalendar()[1]
        cells = [f"{week:<6}", d.strftime("%b %d"), (d + dt.timedelta(days=6)).strftime("%b %d")]
        cells += [" " * len(c) for c in cols]
        print("| " + " | ".join(cells) + " |")
        d += dt.timedelta(weeks=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
