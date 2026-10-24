---
name: prioritizing-tasks
description: Sort the open to-dos in Notes/Daily/Top of Mind.md with the Eisenhower matrix, estimate how long each takes, and timebox the important ones into free time this week, as bullets under the day in the weekly file and, if a calendar is connected, as focus blocks on the calendar. Use when the user says "prioritize my tasks", "what should I work on", "plan my week", "timebox my to-dos", or "block time for my to-dos".
---

# Prioritizing Tasks

Turn the open to-dos into a plan: what to do first, how long each takes, and when to do it.

## Inputs

- `Notes/Daily/Top of Mind.md`: the open `- [ ]` items under `#### Priorities` and under each account, area, and project. If the file is more than a few days old, offer to run `determining-top-of-mind` first.
- The current week file, `Notes/Daily/YYYY-WN.md`: the day bullets and the meetings already under them.
- The calendar, if a calendar tool is connected: every event this week, so you know which time is free.
- Working hours: a line in `Notes/Daily/Calendars.md` such as `Working hours: Mon-Fri 9am-5pm`. If it is missing, ask the user and add the line (create the file if needed).

## Steps

### 1. Sort with the Eisenhower matrix

Put every open to-do in one quadrant:

| Quadrant | Urgent | Important | Action |
|---|---|---|---|
| Do | yes | yes | Timebox in the next 1-2 working days |
| Schedule | no | yes | Timebox later this week |
| Delegate | yes | no | Suggest who could take it |
| Later | no | no | Leave it; mention it once |

- **Urgent:** a due date within 3 working days, overdue, or someone is waiting on the user. Use the to-do's date and the status line above it; an item older than 2 weeks with someone waiting counts as urgent.
- **Important:** already under `#### Priorities`, tied to a deliverable or a client commitment, or tied to a goal in `Notes/Daily/Long Term.md` for this or next week.
- When the notes do not say, ask instead of guessing. One question for the whole batch, not one per item.
- For Delegate, name a person only if they appear in that note's `### Contacts` or `### People`.

### 2. Estimate time

Give each Do and Schedule item an estimate in 15-minute steps (15m, 30m, 45m, 1h, 1h30m, 2h). Base it on what the item asks for: a reply is 15m, a document or deck is 1-2h. Anything over 2h is split into sessions of up to 2h, not into new to-dos.

### 3. Find free time

From now to the end of the week, inside working hours, take the gaps between calendar events (or between the meetings listed under the day bullets when no calendar is connected). Leave 15 minutes after each meeting and keep lunch (12-1pm unless the user says otherwise) free. Fill the gaps with Do items first, then Schedule items, longest first.

### 4. Show the plan and wait

In chat, show:

1. The matrix: each quadrant with its items, the estimate, and the account, area, or project.
2. The timeboxes, day by day: `Tue 1/5 9-9:45am  Send the revised proposal (Sample Company, Inc.)`.
3. What did not fit, and how much time it needs.

Wait for the user to approve or change it. Never write before approval.

### 5. Write it

After approval:

1. **Priorities.** Replace the open items under `#### Priorities` in `Top of Mind.md` with the Do items, copied word for word with their dates, in order. Keep every `- [x]` line already there.
2. **Weekly file.** Add each timebox under its day bullet in `Notes/Daily/YYYY-WN.md`, one tab deep, in time order with the meetings already there:

   ```
   - Tue 1/5
   	- [ ] Weekly Customer Office Hours 10am
   	- [ ] Focus: Send the revised proposal 9-9:45am
   ```

   Times follow the calendar-sync format: `H:mmam/pm`, `:00` dropped on the hour.
3. **Calendar,** if a calendar tool is connected: one event per timebox, titled `Focus: <to-do>`, shown as busy, with no attendees and the account, area, or project in the description.

### 6. Report

One line each: items per quadrant, timeboxes written to the weekly file, events created on the calendar, and the time still needed for what did not fit.

## Rules

- Every to-do in the plan is an existing one, word for word. Never write a new to-do, split one, or reword it.
- Never mark anything done, and never remove a to-do. Later and Delegate items stay where they are.
- Never move, decline, or edit an existing calendar event, and never invite anyone.
- Running it again replaces your own earlier timeboxes: delete `Focus:` bullets and `Focus:` events you created for days that have not started yet, then write the new ones. Leave past days alone.
- The files may contain non-breaking spaces. When an exact-match edit fails, use a script.
