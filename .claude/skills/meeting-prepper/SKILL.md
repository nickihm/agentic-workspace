---
name: meeting-prepper
description: Prepare for a meeting by reading the account or project note, recent log entries, and open to-dos, then write a dated (prep) entry at the top of the note's log with the Prep section filled in. Use when the user says "prep me for", "prepare for my meeting with", "meeting prep", or asks for talking points before a call.
---

# Meeting Prepper

Write the prep for an upcoming meeting directly into the note it belongs to, as a new entry at the top of the log. During the meeting the user adds notes under the same entry, so prep and record stay together.

## Inputs

Ask for anything missing:

- **Who or what**: the account, area, or project. It must match a folder in `Notes/Accounts/`, `Notes/Areas/`, or `Notes/Projects/`.
- **Meeting title**: for example "Weekly Customer Office Hours" or "Quarterly Review".
- **Date**: `YYYY-MM-DD`. Default to the next occurrence on the calendar, if one is connected.
- **Anything the user wants raised**: agenda items, asks, deliverables.

## Sources, in order

1. **The note itself**: `Notes/Accounts/<Name>/<Name>.md`, or the project note. Read `### Overview`, `### Contacts` (or `### People`), and the last 1-3 log entries on the same topic or series.
2. **Project notes** under the account, when the meeting is about a project: `### Status`, `### Timeline`, and `### Todos`.
3. **`Notes/Daily/Top of Mind.md`**: open to-dos and the status line for this account or project.
4. **Calendar**, if a calendar tool is connected: attendees, time, and location.
5. **`Inbox/`** and email, if connected: recent items on the same topic.

## Steps

### 1. Gather

From the sources, pull out:

- Attendees and their roles.
- Open `==highlights==` from earlier entries, especially overdue ones.
- Decisions and progress from the last 2-3 entries.
- Blockers and risks.
- Anything the organizer or the user asked to cover.

### 2. Write the prep entry

Insert it at the top of `### Interaction Log` (account or area note) or `### Log` (project note). Match the note's existing format. The title ends in `(prep)` so it reads as forward-looking:

```markdown
- **YYYY-MM-DD - Meeting title (prep)**
	- Attendees:
		- Name - role
	- Prep:
		- Recap from last cadence: what was covered on YYYY-MM-DD and what was decided
		- Current status: where things stand now, from the notes
		- Talking Points:
			- Topic and what to say about it
			- Open item from YYYY-MM-DD: the highlight text, quoted
		- Questions:
			- A question for a named attendee
	- Notes:
```

- Leave `Notes:` empty for the meeting itself.
- Quote open items as they appear in the source. Do not write new `==highlights==` in the prep; prep suggestions are not the user's to-dos until the user marks them.
- Add only the sections the meeting needs. A first meeting needs background and discovery questions; a recurring sync needs recap, status, and open items.
- Add personal or rapport details only if they are already in `### Contacts`.

### 3. Confirm

In chat, give:

- The file and position you wrote to.
- The 2-3 most important talking points.
- Any fact you were unsure about (dates, attendees, numbers), so the user can fix it before the meeting.

## After the meeting

The user, or `inbox-processing` when raw notes arrive in `Inbox/`, fills in `Notes:`, removes `(prep)` from the title, and highlights the new action items.
