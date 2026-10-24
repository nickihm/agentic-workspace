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

Your agent sorts your top-of-mind to-dos using the Eisenhower matrix, estimates the time each will take, and blocks out time for them over the next week within your working hours, on your calendar and in your weekly to-do files.

### Long-Term Planning

Each week gets its own to-do file. Say "Start a new week" on Sunday, and your agent builds next week's file, carries over unfinished to-dos, and adds your meetings. The Long Term file is a calendar of weeks for big dates and goals, and each one appears in your weekly file when its week arrives.

### Knowledge Work

Your agent drafts the work, drawing on what your notes already say about the account or project. It researches questions with a source link for every claim, builds PowerPoint decks on your own template, creates Excel models for costs and pricing with live formulas, and draws diagrams of systems and processes that you can edit in draw.io.

### Managing Communication

Email and meetings are where requests arrive and follow-ups get lost. Your agent reads your email for the questions, requests, and deadlines waiting on you, logs each conversation with the right account, project, or area, and marks it read. Before a meeting, it writes a recap, open items, and talking points into the meeting's notes. It drafts emails in your own voice and never sends anything without your approval. When you say "I sent the proposal," it checks the task off everywhere. It also turns your newsletters into a digest with one line per story and its link, and marks them read.

### Building Apps

Build small tools of your own with your agent. Each app gets its own folder and version history in the Apps folder. A large model designs each app and reviews every change, a smaller and cheaper model writes the code, and a QA agent tests it before anything is merged. A ports list records where each app runs so apps don't conflict.

## Workspace Structure

Your agent knows this layout, so you don't need to. Each account, project, and area is a folder holding a note of the same name and an Assets folder for its screenshots and files. Accounts can hold their own projects.

```
workspace/
├── AGENTS.md                      # Context for agents: layout, conventions, workflow
├── .claude/                       # Skills and agents
├── .obsidian/                     # Obsidian settings and plugins
├── Apps/                          # Apps you build, one folder and git repo each
│   ├── PORTS.md                   # Where each app runs
│   └── <app>/
│       ├── README.md              # What it does, how to run and test it
│       ├── ARCHITECTURE.md        # Design, data, and critical flows
│       └── ...                    # The app's code and tests
├── Assets/
│   ├── Templates/                 # Your PowerPoint, Word, and Excel templates
│   └── Samples/                   # Example emails and messages in your voice
├── Inbox/                         # Screenshots and downloads land here, to be filed
├── Notes/                         # Knowledge base
│   ├── Daily/
│   │   ├── YYYY-WN.md             # One to-do file per week
│   │   ├── Long Term.md           # Calendar of weeks for big dates and goals
│   │   ├── Top of Mind.md         # Where everything stands and what needs to be done
│   │   └── Archive/               # Past weeks
│   ├── Accounts/                  # Clients, employers, and organizations
│   │   └── <Account>/
│   │       ├── <Account>.md       # Overview, contacts, interaction log
│   │       ├── Assets/            # Screenshots and files for this account
│   │       └── <Project>/         # A project for this account
│   │           ├── <Project>.md   # Goal, timeline, status, to-dos, log
│   │           └── Assets/
│   ├── Projects/                  # Projects not tied to an account
│   │   └── <Project>/
│   │       ├── <Project>.md
│   │       └── Assets/
│   ├── Areas/                     # Ongoing responsibilities, such as home or health
│   │   └── <Area>/
│   │       ├── <Area>.md
│   │       └── Assets/
│   ├── Resources/                 # Reference material, including newsletter digests
│   └── Archive/                   # Finished projects and inactive areas
└── Outbox/                        # Finished deliverables
```

## Getting Started

You need Obsidian (free), an AI agent that can work with files on your computer (such as Claude Code), and a copy of this workspace.

1. **Get the workspace.** Clone this repository, or click **Code → Download ZIP** and unzip it into your Documents folder.
2. **Open it in Obsidian.** Choose **Open folder as vault**, and select the folder.
3. **Open it in your agent.** Point your agent at the same folder.
4. **Set it up.** Say, "Read AGENTS.md and help me set up this workspace." Your agent walks you through adding your accounts, projects, and areas.
5. **Try it.** Say "Process my inbox," "Update top of mind," or "Prep me for my next meeting with Acme."
