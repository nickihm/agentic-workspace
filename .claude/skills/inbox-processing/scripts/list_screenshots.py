#!/usr/bin/env python3
"""List the screenshots in Inbox/ with the local time each was taken.

Plain Python 3, no dependencies. Prints one JSON object per screenshot:
  {"file": ..., "taken": "YYYY-MM-DDTHH:MM:SS", "source": "name" | "file",
   "week_file": "Notes/Daily/YYYY-WN.md", "day": "Mon 1/4"}

The time comes from the file name when it has one (macOS "Screenshot 2027-01-05
at 10.15.32 AM.png", Windows "Screenshot 2027-01-05 101532.png", GNOME
"Screenshot From 2027-01-05 10-15-32.png"), otherwise from the file's creation
time.

  python3 -I list_screenshots.py [INBOX]
"""
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

IMAGE = {".png", ".jpg", ".jpeg", ".heic", ".gif", ".webp", ".tiff"}
NAME = re.compile(r"(?i)(?:screen ?shot|screen capture|capture d.écran|bildschirmfoto)")
STAMP = re.compile(
    r"(\d{4})-(\d{2})-(\d{2})\D{1,6}?(\d{1,2})[.\-:]?(\d{2})[.\-:]?(\d{2})"
    r"(?:\s*([AaPp])\.?[Mm]\.?)?")
DAYS = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]


def taken_from_name(name):
    match = STAMP.search(name.replace("\u202f", " "))
    if not match:
        return None
    y, mo, d, h, mi, s, ampm = match.groups()
    hour = int(h)
    if ampm:
        hour = hour % 12 + (12 if ampm.lower() == "p" else 0)
    try:
        return datetime(int(y), int(mo), int(d), hour, int(mi), int(s))
    except ValueError:
        return None


def taken_from_file(path):
    st = path.stat()
    return datetime.fromtimestamp(getattr(st, "st_birthtime", st.st_mtime))


def main():
    root = Path(__file__).resolve().parents[4]
    inbox = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "Inbox"
    for path in sorted(inbox.iterdir()):
        if path.suffix.lower() not in IMAGE or not NAME.search(path.name):
            continue
        taken, source = taken_from_name(path.name), "name"
        if taken is None:
            taken, source = taken_from_file(path), "file"
        year, week, weekday = taken.isocalendar()
        print(json.dumps({
            "file": str(path.relative_to(root) if path.is_relative_to(root) else path),
            "taken": taken.isoformat(timespec="seconds"),
            "source": source,
            "week_file": f"Notes/Daily/{year}-W{week}.md",
            "day": f"{DAYS[weekday - 1]} {taken.month}/{taken.day}",
        }, ensure_ascii=False))


if __name__ == "__main__":
    main()
