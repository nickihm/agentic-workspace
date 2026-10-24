# Workspace Template

Automate your work by connecting your favorite AI agents to a unified knowledge workspace. Built for knowledge workers juggling many clients, projects, and responsibilities. No coding required.

## Why

Notes, files, screenshots, and follow-ups are scattered across apps and folders. Action items get buried in old meeting notes, and Monday morning goes to figuring out what's on your plate.

This workspace gives every client, project, and area one home and keeps a single page that shows what needs to be done. You ask your agent in plain English, such as "Prep me for my call with Acme," and it handles the filing, searching, and writing.

## What It Does

### Knowledge Management

The workspace is a personal knowledge management system, or "second brain," that works with Obsidian. Everything is organized by account (such as a client), project, or area of responsibility, and accounts can have their own projects. Each holds its interactions, important files, and contacts. Your agent understands this structure, saves information in the right place, and answers questions from your knowledge base.

Screenshots and downloads land in one inbox. Say "Process my inbox," and your agent files each item with the right account, project, or area, matching screenshots to the meeting you were in when you took them.

### Getting Top of Mind

Your activity with each account, project, and area is recorded in its interaction log, where action items and updates are easy to lose. Say "Update top of mind," and your agent scans everything for the latest activity and writes an executive summary: a three- to five-sentence status for each account, project, and area, followed by its open to-dos. You get a bird's-eye view of where everything stands and what needs to be done.

### Prioritizing and Timeboxing

Your agent sorts your top-of-mind to-dos using the Eisenhower matrix, estimates the time each will take, and blocks out time for them on your calendar and in your weekly to-do file.

### Long-Term Planning

Two files keep you looking ahead.

- **Weekly to-do file.** Say "Start a new week" on Sunday. Unfinished to-dos carry over, and your meetings are added.
- **Long Term file.** A calendar of weeks for big dates and goals. Each one appears in your weekly file when its week arrives.

### Knowledge Work

Your agent drafts the work, drawing on what your notes already say about the account or project.

- **Research.** Answers with a source link for every claim.
- **Presentations.** PowerPoint decks built on your own template.
- **Financial models.** Excel workbooks for costs and pricing, with live formulas.
- **Diagrams.** Systems and processes, editable in draw.io.

### Managing Communication

Email and meetings are where requests arrive and follow-ups get lost.

- **Important email.** Pulls out the questions, requests, and deadlines waiting on you.
- **Meeting prep.** Writes a recap, open items, and talking points into the meeting's notes.
- **Email drafts.** Written in your own voice. Nothing is sent without your approval.
- **Task completion.** Say "I sent the proposal," and it's checked off everywhere.
- **Newsletter digest.** One line per story, with links.

### Building Apps

Build small tools of your own with your agent.

- **Apps folder.** Each tool gets its own folder and version history.
- **Software development skills.** Architecture, building, code review, QA, and branch management.
- **Port tracking.** A ports list records where each app runs so apps don't conflict.

## Workspace Structure

Your agent knows this layout, so you don't need to.

```
workspace/
├── AGENTS.md     # Context for agents: layout, conventions, workflow
├── .claude/      # Skills and agent config
├── .obsidian/    # Obsidian vault config and plugins
├── Apps/         # Code projects, one git repo each (ignored except PORTS.md)
├── Inbox/        # Screenshots and downloads land here, to be filed (not tracked)
├── Notes/        # Knowledge base (PARA + Daily + Accounts)
└── Outbox/       # Finished deliverables
```

## Getting Started

You need Obsidian (free), an AI agent that can work with files on your computer (such as Claude Code), and a copy of this workspace.

1. **Get the workspace.** Clone this repository, or click **Code → Download ZIP** and unzip it into your Documents folder.
2. **Open it in Obsidian.** Choose **Open folder as vault**, and select the folder.
3. **Open it in your agent.** Point your agent at the same folder.
4. **Set it up.** Say, "Read AGENTS.md and help me set up this workspace." Your agent walks you through adding your accounts, projects, and areas.
5. **Try it.** Say "Process my inbox," "Update top of mind," or "Prep me for my next meeting with Acme."
