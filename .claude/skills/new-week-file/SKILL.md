---
name: new-week-file
description: Create the next week's notes file at Notes/Daily/YYYY-WN.md with Mon-Sun day bullets, scheduled items from Long Term.md, and unfinished work carried forward from the prior week. Use when the user says "new week file", "create next week", or as step 1 of starting-a-new-week.
---

# New week file

Create `Notes/Daily/YYYY-WN.md` for the **next** ISO week (the week after the current one). Monday starts the week. `N` has no zero-padding: `2027-W1.md`, `2027-W19.md`.

## Run it

```bash
python3 .claude/skills/new-week-file/scripts/new_week.py            # next ISO week
python3 .claude/skills/new-week-file/scripts/new_week.py --week 2027-W19
python3 .claude/skills/new-week-file/scripts/new_week.py --dry-run  # print, do not write
```

The script refuses to overwrite an existing file. Do not pass `--force` unless the user asks.

## What the file contains, in order

0. **Frontmatter.** OKF frontmatter with `type: Week`, the week as `title`, and its Monday-to-Sunday dates in `description`.
1. **Day bullets.** Seven top-level dash bullets with the date: `- Mon 1/4` through `- Sun 1/10`. Tabs for indentation, dash bullets, no sub-items yet.
2. **Long Term sections.** `Notes/Daily/Long Term.md` is a markdown table with one row per week: `Week | Start | End | <category columns...>`. For the row whose `Week` matches the new week, every non-empty category cell becomes a top-level section named after the column, and the cell's items (split on `<br>`) become plain `- item` sub-bullets. These are calendar context, not to-dos, so no checkboxes. Empty cells produce no section. No matching row means no Long Term sections.
3. **Carry-forward.** Every top-level bullet in the prior week's file that is not a day bullet is an ongoing work area (`Home`, `Health`, `Paperwork`, ...). Copy each one with only its unchecked `- [ ]` items, keeping anything nested under those items. Drop `- [x]` items. Drop a section that ends up empty. Items under a day bullet stay in the old file even if unchecked: they were scoped to that day and are the record of what slipped.

If a Long Term section and a carry-forward section share a name, keep both, Long Term first.

## Rules

- Never edit the prior week's file or `Long Term.md`. They are source records.
- If the file already exists (the user sometimes creates it mid-week to jot tasks), do not stop at "exists". Run with `--dry-run`, compare the carry-forward sections against the existing file, and add any unchecked items that are missing. Leave the user's own edits alone.
- The files may contain non-breaking spaces. When an exact-match edit fails, use a script, not the editor.

## Example

`Long Term.md` row for week 19 (columns `Week | Start | End | Work | Home | Family | Finance`):

```
| 19 | May 04 | May 10 |   | Plant sale | Birthday dinner |   |
```

Prior week `2026-W18.md` ends with:

```
- Sun 5/3
	- [ ] Post office
- Home
	- [ ] Fix the gate
	- [x] Call plumber
- Health
	- [x] Book checkup
```

Result `2026-W19.md`:

```
- Mon 5/4
- Tue 5/5
- Wed 5/6
- Thur 5/7
- Fri 5/8
- Sat 5/9
- Sun 5/10
- Home
	- Plant sale
- Family
	- Birthday dinner
- Home
	- [ ] Fix the gate
```

`Post office` stays in W18. `Health` is dropped because it was finished. `Work` and `Finance` were empty.
