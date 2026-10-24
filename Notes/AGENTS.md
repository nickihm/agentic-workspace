---
type: Folder Guide
title: Notes Folder Guide
description: 'Knowledge base index: what each Notes folder holds, note conventions, frontmatter, and where a new note goes.'
tags:
- folder-guide
- notes
---

# Notes

The knowledge base. An Obsidian vault organized by the PARA method: Projects, Areas, Resources, Archive, plus two folders this workspace adds: Daily and Accounts.

## Folders

- `Daily/` — weekly notes and the two files that drive them.
  - `YYYY-WN.md` — one file per ISO week. Seven day bullets at the top, then ongoing sections (`Home`, `Health`, `Paperwork`, ...) with checkbox to-dos. Items under a day bullet belong to that day and do not carry forward. Items under a section carry forward until checked.
  - `Long Term.md` — a table with one row per week and one column per life area. The week-level calendar. `new-week-file` pulls the upcoming row into the new week file.
  - `Top of Mind.md` — the running summary. Priorities first, then one block per account, then an `Areas` group and a `Projects` group: a short summary of the latest activity and the open to-dos for each.
  - `Calendars.md` — the calendars to read and your working hours, for `weekly-calendar-sync` and `prioritizing-tasks`.
  - `Important Email.md` — your email addresses, senders to ignore, and the last scan time, for `collect-email-important`.
  - `Archive/` — finished week files and past `Long Term.md` rows, moved here by `archive-week`.
- `Accounts/` — one folder per client, employer, or organization, named after it. Each has a note with the same name (overview, locations, contacts, projects, interaction log), an `Assets/` folder, and one subfolder per project. Finished accounts move to `Accounts/Archive/`.
- `Projects/` — work with a goal and an end date that is not tied to one account. One folder per project with a note of the same name (overview, goal, timeline, status, todos, log) and an `Assets/` folder.
- `Areas/` — ongoing responsibilities with no end date: health, finance, home, career. One folder per area with a note of the same name (overview, projects, interaction log) and an `Assets/` folder, like an account.
- `Resources/` — reference material by topic: articles, clippings, prompts, how-tos. `Resources/Newsletters/` holds the digests from `collect-email-newsletters`. Stale material moves to `Resources/Archive/`.
- `Archive/` — anything from Projects or Areas that is finished or inactive.

## Conventions

- Every note starts with OKF frontmatter (see Frontmatter below).
- Every folder has an `AGENTS.md` saying what it holds. Create one with each new folder, following the one in a sibling folder.
- Title Case with spaces for folder and file names. `Sample Company, Inc.md`, not `sample-company-inc.md`.
- One idea per note. Link with `[[wikilinks]]`.
- Tabs for indentation in bullet lists. Dash bullets. Checkboxes (`- [ ]`) only for things that get done.
- Dates as `YYYY-MM-DD` in file names and interaction logs, newest first in logs.
- Highlight follow-ups and action items in interaction logs with `==double equals==` so they stand out in Obsidian.
- Images and screenshots go in the `Assets/` folder of the account, area, or project they belong to (a project's own `Assets/`, not its account's), named `YYYY-MM-DD HH.MM.SS <Short Description>.png`. Embed them in the log entry they belong to with the full vault path: `![[Notes/Accounts/<Name>/Assets/<file>]]`. `Assets` is a reserved folder name; never name a project `Assets`.
- Obsidian may write non-breaking spaces into files. When an exact-match edit fails, use a script.

## Frontmatter

Every note starts with a YAML frontmatter block in the Open Knowledge Format (OKF v0.2), the format OpenWiki reads and writes. Obsidian shows it as the note's properties.

```yaml
---
type: Account
title: Acme Corp
description: Logistics client; quarterly business reviews and the warehouse rollout project.
tags:
- account
---
```

- `type` is required. Use one of: `Account`, `Project`, `Area`, `Week`, `Long Term Plan`, `Top of Mind`, `Newsletter Digest`, `Resource`, `Settings`, `Folder Guide`, `Email Sample`, `Message Sample`, `Architecture`, `Port Inventory`.
- `title` is the note's name. `description` is one sentence saying what the note is about, written with the names and terms someone would search for. `tags` is a list of lowercase words.
- Optional: `resource`, a URL or ID for the thing the note describes (a website, a shared drive folder, a CRM record).
- Keep the frontmatter when you edit a note. When you rewrite a note whole, carry it over and update `description` if the note's scope changed.
- Create it with every new note. Copy it from a sibling note of the same type and change the values.

## Where a new note goes

1. About a client, employer, or organization: `Accounts/<Name>/`.
2. Has an end date and an outcome: `Projects/`.
3. Something you maintain indefinitely: `Areas/`.
4. Reference you did not write or do not act on: `Resources/`.
5. Not sure: `Daily/` in this week's file, and sort it later.
