# Workspace Template

A monorepo layout for one person working with AI coding agents: a knowledge base, the code projects, and the files that move in and out, all in one Obsidian vault and one git repo.

```
workspace/
├── AGENTS.md     # Context for agents: layout, conventions, workflow
├── .claude/      # Skills and agent config
├── .obsidian/    # Obsidian vault config and plugins
├── Apps/         # Code projects, one git repo each (ignored except PORTS.md)
├── Inbox/        # Files to process
├── Notes/        # Knowledge base (PARA + Daily + Accounts)
└── Outbox/       # Finished deliverables
```

## Use it

1. Click **Use this template** on GitHub, or clone and `rm -rf .git && git init`.
2. Open the folder in Obsidian as a vault. The bundled plugins and settings load from `.obsidian/`.
3. Read `AGENTS.md`, then follow its **Customizing this template** section.

## Weekly rhythm

On Sunday, tell your agent "start a new week". The `starting-a-new-week` skill creates next week's file in `Notes/Daily/`, carries over unfinished to-dos, pulls in that week's row from `Long Term.md`, archives the finished week, and syncs your calendar.

The scripts behind it are plain Python 3 with no dependencies:

```bash
python3 .claude/skills/new-week-file/scripts/new_week.py --dry-run
python3 .claude/skills/archive-week/scripts/archive_week.py --dry-run
```

## Obsidian plugins included

Outliner (on) and Show Hidden Files (installed, off; turn it on in Settings → Community plugins to see `.claude/` and other dot-folders). Each is the stock release in `.obsidian/plugins/`.
