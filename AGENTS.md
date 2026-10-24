# AGENTS.md

This file gives AI coding agents the context they need to work in this workspace. Read it first, every time.

## What this workspace is

One folder, one git repo, one Obsidian vault. It holds a personal knowledge base, the code projects you work on, and an inbox/outbox for files that move in and out.

```
workspace/
├── AGENTS.md          # This file
├── .claude/           # Agent config: skills, agents, settings
├── .obsidian/         # Obsidian vault config (the vault root is this folder)
├── Apps/              # Code projects, one git repo per subdirectory
│   └── PORTS.md       # Port inventory for every app and service on this machine
├── Assets/            # Reusable material: Templates/ for documents (see its AGENTS.md), Samples/ for example emails and messages
├── Inbox/             # Files dropped here for processing (downloads, exports, screenshots)
├── Notes/             # Knowledge base (PARA method, Obsidian markdown)
│   ├── AGENTS.md      # Index of the knowledge base; read it before working in Notes/
│   ├── Daily/         # Weekly notes, Long Term.md, Top of Mind.md
│   ├── Accounts/      # One folder per client, employer, or organization
│   ├── Projects/      # Work with an end date and an outcome
│   ├── Areas/         # Ongoing responsibilities with no end date
│   ├── Resources/     # Reference material by topic
│   └── Archive/       # Finished or inactive items from the other folders
└── Outbox/            # Files produced for someone else (reports, exports, deliverables)
```

The workspace root is a git repo. It tracks `AGENTS.md`, `.claude/`, `.obsidian/`, `Notes/`, `Inbox/`, `Outbox/`, and `Apps/PORTS.md`. Each directory under `Apps/` is its own git repo with its own remote; the root `.gitignore` excludes them.

## Notes

`Notes/` is an Obsidian vault organized by the PARA method. The index is `Notes/AGENTS.md`. It lists every top-level folder and what it is for.

- Weekly notes live in `Notes/Daily/`, one file per ISO week (`YYYY-WN.md`, no zero-padding).
- `Notes/Daily/Long Term.md` is a table with one row per week and one column per life area. It is the week-level calendar.
- `Notes/Daily/Top of Mind.md` is the running summary: priorities first, then one block per account, area, and project with the latest activity and open to-dos.
- Name new folders and documents in Title Case with spaces, not kebab-case.
- Obsidian may write non-breaking spaces into files. When an exact-match edit fails, use a script instead of the editor.

## Apps

Each directory under `Apps/` is a separate code project and a separate git repo. Navigate into the right one before running git commands. Document each app in its own `README.md`; add a short entry below when it is stable enough to describe.

| App | Folder | Stack | Run | Test |
|---|---|---|---|---|
| (none yet) | | | | |

## Ports

`Apps/PORTS.md` lists every TCP port an app or service on this machine binds, and the free blocks for new ones. Keep it current:

- Before choosing a port for anything new, read `Apps/PORTS.md` and pick from a free block. Confirm with `lsof -nP -iTCP -sTCP:LISTEN`.
- Any change that adds, removes, or moves a port updates `Apps/PORTS.md` in the same commit.
- When you find a port in use that `Apps/PORTS.md` does not list, add it.

## Inbox and Outbox

- `Inbox/` is where files arrive. Process them into `Notes/` or `Apps/`, then delete or archive the original. An empty inbox is the goal.
- `Outbox/` is where finished deliverables go so they are easy to find and send. Do not use it as working storage.

## Skills

Skills live in `.claude/skills/<name>/SKILL.md`. Load the matching skill before starting a task it covers.

| Skill | Use when |
|---|---|
| `starting-a-new-week` | Weekly rollover, usually on a Sunday. Runs the three below in order. |
| `new-week-file` | Create next week's `Notes/Daily/YYYY-WN.md` with carry-forward and Long Term items. |
| `archive-week` | Move finished week files and Long Term rows into `Notes/Daily/Archive/`. |
| `weekly-calendar-sync` | Add the week's calendar events under the day bullets. |
| `determining-top-of-mind` | Rebuild `Notes/Daily/Top of Mind.md` from open highlights in account, area, and project notes. |
| `completing-tasks` | Mark a task done in `Top of Mind.md` and strike its highlight in the source note. |
| `inbox-processing` | File everything in `Inbox/` into the right note, account, or calendar. |
| `meeting-prepper` | Write a dated prep entry in an account, area, or project note before a meeting. |
| `opening-notes` | Open a note in Obsidian by name. |
| `drafting-email` | Draft an email in the user's voice, matched to `Assets/Samples/Emails/`. |
| `collect-email-newsletters` | Digest newsletters that arrived since the last run into a dated note. |
| `researching` | Answer a question from primary sources with citations. |
| `architecture-diagram` | Draw architecture, data flow, network, and deployment diagrams as draw.io files. |
| `building-decks` | Build a `.pptx` from a template in `Assets/Templates/`. |
| `financial-modeling` | Build a cost, price, or financial model as an Excel workbook with live formulas. |

## Git workflow

The root repo and every app repo use the same rules.

- Never push directly to `main` unless the user asks for it on a specific change. Use feature branches and pull requests.
- Branch names: `feature/`, `fix/`, `refactor/`, `docs/`, `chore/` plus a short kebab-case description.
- Write commit messages and PR bodies to a file and pass them with `git commit -F` or `--body-file`. Heredocs inside command substitution break on parentheses.
- Pass `--repo` to every `gh` command.
- For a run of small related changes in one session, keep them on one branch and one PR.
- Merge with a merge commit, then check out `main` and pull.
- Never commit secrets, credentials, `.env` files, databases, or personal data about other people.

## Coding guidelines

Make only the requested changes and do not alter other functionality. Implement a simple solution with as few lines modified as possible. Do not implement workarounds. Use best practices and native standards where applicable.

## Customizing this template

1. Replace the sample content in `Notes/Accounts/`, `Notes/Areas/`, `Notes/Projects/`, and `Notes/Daily/` with your own.
2. Fill the Apps table above and `Apps/PORTS.md` as you add projects.
3. Set the category columns in `Notes/Daily/Long Term.md` to your own life areas and extend the table with `.claude/skills/archive-week/scripts/long_term_rows.py`.
4. Create `Notes/Daily/Calendars.md` if you use `weekly-calendar-sync`.
5. Add your document templates (`.pptx`, `.docx`, `.xlsx`) to `Assets/Templates/`.
