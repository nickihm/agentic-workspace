---
name: weekly-calendar-sync
description: Pull the week's calendar events and add them as short checkbox bullets under the matching day in Notes/Daily/YYYY-WN.md. Use when the user says "sync my calendar", "add this week's meetings to my notes", or as step 3 of starting-a-new-week.
---

# Weekly calendar sync

Add the week's events to the week file so the day bullets show what is scheduled.

## Setup (once)

List the calendars to read in `Notes/Daily/Calendars.md`, one per line, with the calendar ID and a short label:

```
- Personal: you@example.com
- Work: you@company.com
```

If the file is missing, ask the user which calendars to read and create it. Never hard-code calendar IDs in this skill.

## Steps

1. **Pick the week.** Monday to Sunday, ISO week. On a Sunday, target the **upcoming** week, not the one ending today. The file is `Notes/Daily/YYYY-WN.md` (no zero-padding). If it does not exist, run `new-week-file` first.
2. **Fetch events** from every calendar in `Calendars.md`, in parallel if the tool allows. Range: Monday 00:00 to the next Monday 00:00 in the user's time zone. Order by start time.
3. **Read the week file first.** It has day bullets and may already have other items. You are inserting, not replacing.
4. **Write one checkbox bullet per event** under the matching day, one tab deep:

   ```
   - Mon 5/4
   	- [ ] Team sync 10am
   	- [ ] Design review 2:30pm
   ```

   - Short names: drop organization prefixes and boilerplate.
   - Time as `H:mmam/pm`; drop `:00` on the hour (`10am`, `2:30pm`).
   - Overlapping or back-to-back events: list both.
   - All-day events: skip unless they matter (travel, out of office, holiday).
   - Events before 7am or after 9pm: skip unless notable.
5. **Skip duplicates.** If a bullet with the same name and time is already under that day, do not add it again.
6. **Report** the count added per day in one line.

## Rules

- Never delete or reorder existing bullets.
- Calendar event bullets are checkboxes (`- [ ]`) because the user ticks them off as the day goes.
- The files may contain non-breaking spaces. When an exact-match edit fails, use a script.
