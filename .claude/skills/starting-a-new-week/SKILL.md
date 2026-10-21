---
name: starting-a-new-week
description: Full weekly rollover. Creates next week's notes file (new-week-file), archives finished weeks (archive-week), then syncs the calendar into the new file (weekly-calendar-sync). Use when the user says "start a new week", "roll over the week", "set up next week", typically on a Sunday.
---

# Starting a new week

The weekly rollover in `Notes/Daily/`. It chains three skills. Do not reimplement their logic here; read each skill when you run its step.

## Steps

1. **Create the new week file.** Invoke `new-week-file`. It writes `Notes/Daily/YYYY-WN.md` for the upcoming ISO week with day bullets, Long Term items, and carry-forward from the week that is ending. If the file already exists, reconcile instead of stopping (see that skill).
2. **Archive the finished week.** Invoke `archive-week`. It moves the past `Long Term.md` rows to `Notes/Daily/Archive/Long Term.md` and the past week files to `Notes/Daily/Archive/`.
3. **Sync the calendar.** Invoke `weekly-calendar-sync` for the upcoming week. Skip if no calendar tool is connected and say so.
4. **Report.** List the new file path, what was carried forward, what was archived, and how many calendar events were added. One line each.

## Why this order

- `new-week-file` reads the prior week's file for carry-forward. Archive after, not before.
- `new-week-file` reads the upcoming week's row in `Long Term.md`. Archiving only removes earlier rows, so either order works for that file, but keeping one order makes the run predictable.

## Sunday rule

This normally runs on a Sunday. The week ending that Sunday is **past**: archive it. The "current" week for every step is the one whose file you just created.

## Checks before you finish

- `Notes/Daily/` contains the new week file, `Long Term.md`, and `Top of Mind.md`. Older week files are in `Archive/`.
- The first row in `Long Term.md` is the new week.
- Nothing was deleted. `git status` shows only renames and additions under `Notes/Daily/`.
