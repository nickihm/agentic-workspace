#!/usr/bin/env python3
"""Merge newsletter items into a dated digest.

Reads WORK/items.jsonl, one JSON object per line:

    {"title": "...", "url": "https://...", "summary": "One sentence.",
     "newsletter": "Sample Weekly", "topic": "Optional topic",
     "email_id": "message ID from the mail tool", "received": "ISO 8601",
     "subject": "...", "sender": "..."}

Only title, summary, newsletter, and received are required.

Writes, in DIR (default Notes/Resources/Newsletters):

1. YYYY-MM-DD.md for --today, or YYYY-MM-DD-2.md and so on when that exists.
   Items are grouped by newsletter (or by topic with --group-by topic),
   newest first, with a Sources table of every email cited at the bottom.
2. .last-scan.json with the window end, so the next run starts there.

Also writes WORK/mark_read.json: the email IDs that supplied at least one
item. Items whose URL or title already appears in an earlier digest, or
whose email arrived before --start, are dropped.

Usage:
    build_digest.py --work WORK --start ISO --end ISO --today YYYY-MM-DD
                    [--dir DIR] [--group-by newsletter|topic] [--dry-run]
"""

import argparse
import collections
import datetime as dt
import json
import re
from pathlib import Path

DIGEST_NAME = re.compile(r"\d{4}-\d{2}-\d{2}(-\d+)?\.md")


def parse_time(text: str) -> dt.datetime:
    t = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
    return t if t.tzinfo else t.astimezone()


def norm_url(url: str) -> str:
    return (url or "").strip().split("#")[0].split("?")[0].rstrip("/").lower()


def norm_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (title or "").lower()).strip()


def clean(text: str) -> str:
    """Replace em and en dashes, which the digest style does not use."""
    return re.sub(r"\s*[—–]\s*", " - ", text or "").strip()


def prior_keys(folder: Path) -> tuple[set, set]:
    urls, titles = set(), set()
    for f in folder.glob("*.md"):
        if not DIGEST_NAME.fullmatch(f.name):
            continue
        text = f.read_text(encoding="utf-8")
        urls |= {norm_url(u) for u in re.findall(r"\]\((https?://[^)\s]+)\)", text)}
        titles |= {norm_title(t) for t in re.findall(r"^- \*\*\[?([^\]*]+)", text, re.M)}
    return urls, titles


def bullet(item: dict) -> str:
    title = clean(item["title"])
    head = f"**[{title}]({item['url']})**" if item.get("url") else f"**{title}**"
    return f"- {head} - {clean(item['summary'])} *({item['received'][:10]})*"


def build(args) -> dict:
    folder = Path(args.dir)
    work = Path(args.work)
    src = work / "items.jsonl"
    items = [json.loads(l) for l in src.read_text(encoding="utf-8").splitlines() if l.strip()] if src.exists() else []
    start, end = parse_time(args.start), parse_time(args.end)

    seen_urls, seen_titles = prior_keys(folder)
    groups = collections.defaultdict(list)
    emails = {}
    for item in items:
        if not (start <= parse_time(item["received"]) < end):
            continue
        url, title = norm_url(item.get("url")), norm_title(item["title"])
        if (url and url in seen_urls) or title in seen_titles:
            continue
        seen_urls.add(url)
        seen_titles.add(title)
        key = item.get(args.group_by) or "Other"
        groups[key].append(item)
        if item.get("email_id"):
            emails.setdefault(item["email_id"], item)

    window = f"{start.astimezone():%Y-%m-%d %H:%M} to {end.astimezone():%Y-%m-%d %H:%M %Z}"
    total = sum(len(v) for v in groups.values())
    out = ["---", "type: Newsletter Digest", f"title: \"Newsletters: {args.today}\"",
           f"description: \"Newsletter stories received {window}.\"",
           "tags:", "- resources", "- newsletters", "---", "",
           f"# Newsletters: {args.today}", "", f"Window: {window}", "",
           f"{total} item{'' if total == 1 else 's'} from {len(emails)} email{'' if len(emails) == 1 else 's'}.", ""]
    for name in sorted(groups, key=lambda k: (k == "Other", k.lower())):
        out += [f"## {clean(name)}", ""]
        out += [bullet(x) for x in sorted(groups[name], key=lambda x: x["received"], reverse=True)]
        out.append("")
    if emails:
        out += ["## Sources", "", "| Email ID | Received | From | Subject |", "|---|---|---|---|"]
        for eid, x in sorted(emails.items(), key=lambda kv: kv[1]["received"]):
            subject = clean(x.get("subject", "")).replace("|", "/")
            out.append(f"| `{eid}` | {x['received']} | {x.get('sender', '')} | {subject} |")
        out.append("")

    path = folder / f"{args.today}.md"
    n = 2
    while path.exists():
        path = folder / f"{args.today}-{n}.md"
        n += 1
    mark = sorted(emails)
    text = "\n".join(out)

    if args.dry_run:
        (work / "preview.md").write_text(text, encoding="utf-8")
    else:
        folder.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        (work / "mark_read.json").write_text(json.dumps(mark, indent=0), encoding="utf-8")
        (folder / ".last-scan.json").write_text(
            json.dumps({"last_scan_end": args.end, "file": path.name}), encoding="utf-8")

    return {"file": str(path), "items": total, "emails_cited": len(emails),
            "by_group": {k: len(v) for k, v in groups.items()}, "dry_run": args.dry_run}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for name in ("--work", "--start", "--end", "--today"):
        parser.add_argument(name, required=True)
    parser.add_argument("--dir", default="Notes/Resources/Newsletters")
    parser.add_argument("--group-by", choices=["newsletter", "topic"], default="newsletter")
    parser.add_argument("--dry-run", action="store_true", help="write WORK/preview.md and change nothing else")
    print(json.dumps(build(parser.parse_args()), indent=1))


if __name__ == "__main__":
    main()
