---
name: archive-week
description: Archive finished weeks. Moves past rows out of Notes/Daily/Long Term.md into Notes/Daily/Archive/Long Term.md and moves past Notes/Daily/YYYY-WN.md files into Notes/Daily/Archive/. Use when the user says "archive the week", "archive last week", or as step 2 of starting-a-new-week.
---

# Archive week

Keep `Notes/Daily/` to the current week, the upcoming week, `Long Term.md`, and `Top of Mind.md`. Everything older goes to `Notes/Daily/Archive/`.

## Run it

```bash
python3 .claude/skills/archive-week/scripts/archive_week.py             # cutoff = next ISO week
python3 .claude/skills/archive-week/scripts/archive_week.py --week 2027-W19
python3 .claude/skills/archive-week/scripts/archive_week.py --dry-run
```

`--week` is the **upcoming** week. Every week before it is past.

## What it does

1. **Long Term rows.** Cuts every row in `Notes/Daily/Long Term.md` whose week is before the cutoff and appends it to `Notes/Daily/Archive/Long Term.md`. Creates that file with the same header when missing. The cutoff week and future weeks stay intact.
2. **Week files.** Moves every `Notes/Daily/YYYY-WN.md` whose week is before the cutoff into `Notes/Daily/Archive/`.

## Order matters

Run `new-week-file` **before** this skill. It reads the prior week's file for carry-forward, and that file must still be in `Notes/Daily/`.

When run on a Sunday, the week ending that day is past. Archive it. "Current" means the week whose file you just created.

## Topping up Long Term.md

When the table runs out of future rows, print blank rows and paste them in:

```bash
python3 .claude/skills/archive-week/scripts/long_term_rows.py 2027-W1 2027-W52 --columns "Work,Home,Family,Finance"
```

Pass the same category columns as the table header so the widths line up.

## Rules

- Never delete a row or a file. Everything moves to `Archive/`.
- Never rewrite `Top of Mind.md` here; it is the user's running summary, not a weekly artifact.
