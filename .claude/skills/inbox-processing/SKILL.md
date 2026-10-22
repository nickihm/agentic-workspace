---
name: inbox-processing
description: Process the files in Inbox/. Rewrites meeting notes into the right account or project log, files documents next to the note they belong to, adds calendar files to the week file, and clears the inbox. Use when the user says "process my inbox", "file these", "triage the inbox", or drops files in Inbox/.
---

# Inbox Processing

Move every file in `Inbox/` to where it belongs in `Notes/`. An empty inbox is the goal.

## Where things go

Follow the placement rules in `Notes/AGENTS.md`:

1. About a client, employer, or organization: `Notes/Accounts/<Name>/`, or `Notes/Accounts/<Name>/<Project>/` when it is about one project.
2. Has an end date and an outcome, not tied to one account: `Notes/Projects/`.
3. Something maintained indefinitely: `Notes/Areas/`.
4. Reference the user did not write or does not act on: `Notes/Resources/`.
5. Not sure: ask the user.

Code goes in `Apps/`, not `Notes/`. Finished deliverables go in `Outbox/`.

## Steps

### 1. List the inbox and classify each file

| Kind | How to tell | Go to |
|---|---|---|
| Meeting notes | Rough notes, a transcript, or minutes | Step 2 |
| Calendar file | `.ics` | Step 3 |
| Document | PDF, Office file, image, export, clipping | Step 4 |
| Unknown | Anything else | Ask |

For each file, work out which account or project it is about by matching names against the folders in `Notes/Accounts/` and `Notes/Projects/`. If you cannot tell, ask.

Show the user the plan as a table (file, kind, destination) and wait for confirmation before you change anything.

### 2. Meeting notes

1. Read the raw file.
2. Rewrite it as one entry in the format the destination note already uses:

   ```markdown
   - **YYYY-MM-DD - Meeting title**
   	- Attendees:
   		- Name - title, if known
   	- Notes:
   		- Short, plain statements of what was said and decided
   		- ==Action item or follow-up, as stated in the source==
   ```

   - Use tabs for indentation and dash bullets.
   - Highlight only action items and follow-ups that the source states. Do not invent new ones or turn a discussion point into a task.
   - Keep names, numbers, and dates exactly as they appear in the source. If something is unclear, keep the original wording and flag it to the user.
3. Insert the entry under `### Interaction Log` in an account note, or `### Log` in a project note, in date order with the newest first. If a `(prep)` entry for the same meeting exists (see `meeting-prepper`), fill in its `Notes:` and remove `(prep)` from the title instead of adding a duplicate.
4. If a new attendee appears, offer to add them to the note's `### Contacts` or `### People` section. Do not add them without asking.

### 3. Calendar files (`.ics`)

1. Parse the events, including recurring ones, with Python's standard library or a short script.
2. Add each event under its day bullet in `Notes/Daily/YYYY-WN.md`, using the bullet format and skip rules in the `weekly-calendar-sync` skill. If the week file does not exist, run `new-week-file` for that week first.
3. Skip events that are already listed with the same name and time.

### 4. Documents

1. Move the file into the account, project, area, or resource folder it belongs to. Keep the original file name unless it is unreadable; then rename it in Title Case with spaces.
2. If the destination folder does not exist, ask before creating it.
3. If the document has action items or decisions, say so in chat. Do not write highlights from it on your own.

### 5. Clear the inbox

After a file's content is filed, delete the original from `Inbox/`, except `Inbox/.gitkeep`. Leave any file you could not process.

### 6. Report

One line per file: what it was and where it went. List anything left in the inbox and why.
