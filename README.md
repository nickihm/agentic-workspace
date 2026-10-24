# Workspace Template

Automate work functions by connecting your favorite AI agent or agents to a unified knowledge workspace.

Built for knowledge workers juggling many clients, projects, and responsibilities. No coding required.

## Why

Notes, files, screenshots, and follow-ups are scattered across apps and folders. Action items get buried in old meeting notes. Monday morning goes to figuring out what's on your plate.

With this workspace, every client, project, and area has one home, one page shows what needs to be done, and you ask your agent in plain English ("prep me for my call with Acme") to do the filing, searching, and writing.

## What It Does

### Knowledge Management

This workspace acts as a personal knowledge management system or 'second brain' and works with Obsidian.
Everything is stored by projects, area/domain, or account (i.e. client account). Accounts can also have their own projects. All interactions, important files, contacts are stored in this structure.
Agents connected to the base directory understand the structure and save information accordingly. Agents can also search and answer questions against your knowledge base.
- **Inbox processing:** screenshots and downloads land in one Inbox. Say "process my inbox" and each file is filed to the right account, project, or area, with screenshots matched to the meeting you were in.

### Getting Top of Mind

Your activities with accounts, projects, and areas are stored in their interaction logs. Action items, updates can be buried in those interactions.
The skill 'determining top of mind' will scan all your accounts/projects/areas for latest activity and produce an executive summary outline with a 3-5 sentence summary of the account/project/area and action items and todos. This gives you a bird's-eye view of where everything stands and what needs to be done.

### Prioritizing and Timeboxing

The 'prioritizing tasks' skill goes through your top of mind todos and helps you prioritize based on the Eisenhower matrix, estimates required time effort, and timeboxes your calendar and weekly todo file.

### Long Term Planning
- **Weekly todo file:** say "start a new week" on Sunday. Unfinished todos carry over and your meetings are added.
- **Long Term file:** a calendar of weeks for big dates and goals. Each one shows up in your weekly file when its week arrives.

### Knowledge Work
- **Research** with a source link for every claim.
- **Decks** in PowerPoint, built on your own template.
- **Excel models** for costs and pricing, with live formulas.
- **Diagrams** of systems and processes, editable in draw.io.

### Managing Communication
- **Important email:** pulls out the questions, requests, and deadlines waiting on you.
- **Meeting prep:** recap, open items, and talking points, written into the meeting's notes.
- **Email drafts** in your own voice. Nothing is sent without you.
- **Complete the task:** say "I sent the proposal" and it's checked off everywhere.
- **Newsletter digest:** one line per story, with links.

### Building Apps
- **Apps folder:** each tool you build with your agent gets its own folder and history.
- **Skills for SDLC:** architecture, build, code review, QA, branch management.
- **PORTS:** tracks where each app runs so they don't collide.

## Workspace Structure

Your agent knows this layout; you don't need to.

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

You need Obsidian (free), an AI agent that works with files on your computer (such as Claude Code), and a copy of this workspace.

1. **Download:** click **Code → Download ZIP** and unzip it into your Documents folder.
2. **Open in Obsidian:** choose **Open folder as vault** and pick the folder.
3. **Open in your agent:** point your agent at the same folder.
4. **Say:** "Read AGENTS.md and help me set up this workspace." It walks you through adding your accounts, projects, and areas.
5. **Try:** "Process my inbox", "Update top of mind", "Prep me for my next meeting with Acme".
