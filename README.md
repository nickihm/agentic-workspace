# Workspace Template

Automate work functions by connecting your favorite AI agent or agents to a unified knowledge workspace.

## The Problem

If you juggle several clients, projects, or responsibilities at once, the information about each one is scattered. Meeting notes live in one app, files in your Downloads folder, screenshots on your desktop, and follow-ups in your email. Action items get buried in the notes of a meeting from two weeks ago. Before a call you dig through old emails to remember what was promised. On Monday morning it takes an hour just to work out what is on your plate.

## What You Get

- Every client, project, and area of your life has one home, with its meeting history, files, contacts, and screenshots in one place.
- One page shows where everything stands and every open action item, kept up to date for you.
- Meeting prep takes a minute instead of half an hour.
- Downloads and screenshots find their way to the right client or project.
- Each week starts with a plan instead of a blank page.
- Emails drafted in your own voice, decks in your own template, research with sources.

You ask in plain English, such as "prep me for my call with Sample Company" or "what's on my plate?", and the agent does the filing, searching, and writing.

## Who It's For

Knowledge workers who keep many things moving at once: account managers, consultants, project managers, office managers, executive assistants, and founders. You do not need to know how to code. If you can install an app and type a request to an AI assistant, you can use this workspace.

## What It Does

### Knowledge Management

This workspace acts as a personal knowledge management system or 'second brain' and works with Obsidian.
Everything is stored by projects, area/domain, or account (i.e. client account). Accounts can also have their own projects. All interactions, important files, contacts are stored in this structure.
Agents connected to the base directory understand the structure and save information accordingly. Agents can also search and answer questions against your knowledge base.

Files come at you all day: downloads, screenshots, exported meeting notes. In this workspace they all land in one Inbox folder. The 'setup-inbox' skill points your computer's screenshots and downloads there, so you never have to think about where they go. When you say "process my inbox", the 'inbox-processing' skill sorts each file to where it belongs. Rough meeting notes become a clean entry in the right client's or project's log, with the action items highlighted. Documents are filed next to the notes they belong to. Screenshots are matched to the meeting you were in when you took them and to what they show, then saved with that client, project, or area and added to that meeting's notes. Anything it is unsure about, it asks you first.

### Getting Top of Mind

Your activities with accounts, projects, and areas are stored in their interaction logs. Action items, updates can be buried in those interactions.
The skill 'determining top of mind' will scan all your accounts/projects/areas for latest activity and produce an executive summary outline with a 3-5 sentence summary of the account/project/area and action items and todos. This gives you a bird's-eye view of where everything stands and what needs to be done.

### Prioritizing and Timeboxing

The 'prioritizing tasks' skill goes through your top of mind todos and helps you prioritize based on the Eisenhower matrix, estimates required time effort, and timeboxes your calendar and weekly todo file.

### Long Term Planning

Most to-do lists only show today. Bigger things, like a launch next month, a contract renewal in the spring, or a vacation in August, get forgotten until they are urgent. The Long Term file is a simple calendar of weeks: one row per week and one column for each part of your life, such as work, home, health, and family. You note big dates and goals in the week they belong to, and they come back to you at the right time.

Each week gets its own to-do file, with a spot for each day and a section for each part of your life. On Sunday, say "start a new week". The 'starting-a-new-week' skill creates next week's file, carries over everything you did not finish, brings in what you planned for that week in the Long Term file, adds your meetings from your calendar, and puts last week away in the archive. You start Monday knowing what the week holds.

### Knowledge Work

Much of office work is producing things: an answer to a question, a presentation, a cost estimate, a diagram. Your agent can do the first draft of each, using what it already knows about the client or project from your notes.

The 'researching' skill answers a question from original sources, such as official websites, documentation, and public filings, with a link for every claim so you can check it yourself.

The 'building-decks' skill turns an outline or a page of notes into a PowerPoint deck built on your own company template, so the fonts, colors, and logos match. It shows you the outline for approval before it builds a single slide.

The 'financial-modeling' skill builds cost estimates, pricing, and budget models in Excel with working formulas, so you can change an input and watch the totals update.

The 'architecture-diagram' skill draws how systems, data, and processes fit together, as diagrams you can open and edit in draw.io.

### Managing Communication

Email is where most requests arrive and where most follow-ups get lost.

The 'collect-email-important' skill reads the email that arrived since you last checked and pulls out what needs you: questions waiting for an answer, requests, deadlines, and decisions, each tied to the client or project it concerns.

Before a meeting, say "prep me for my call with Sample Company". The 'meeting-prepper' skill reads that client's notes, the last few meetings, and the open action items, then writes a prep section into the meeting's entry: a recap of last time, where things stand, talking points, and questions to ask. During the call you take notes in the same place, so prep and record stay together.

The 'drafting-email' skill writes emails that sound like you. It learns your greeting, sign-off, and tone from a few of your own emails saved as samples, and it saves the result as a draft for you to review. It never sends anything on its own.

When something is done, just say so: "I sent the proposal." The 'completing-tasks' skill checks it off on your Top of Mind page and marks it done in the original meeting notes, so it does not come back.

Newsletters pile up unread. The 'collect-email-newsletters' skill reads the ones that arrived since the last time and writes a one-page digest: one line per story with its link, and nothing repeated from an earlier digest.

### Building Apps

Sometimes the fastest fix is a small tool of your own: a tracker, a form, or a script that cleans up a weekly report. With an AI agent you can build these without being a programmer, and this workspace gives them a home.

Each tool lives in its own folder under Apps, kept apart from your notes, with its own history so every change can be reviewed and undone. Skills for the software development lifecycle walk the agent through the steps a careful developer would follow: planning how the tool fits together, building it, reviewing the code, testing it, and keeping each change separate until you approve it. A simple list called PORTS records where each tool runs on your computer, so two tools never get in each other's way.

## Getting Started

You need three things: Obsidian, a free note-taking app; an AI agent that can work with the files on your computer, such as Claude Code in the Claude desktop app; and your own copy of this workspace.

1. **Get your copy.** On this page, click **Code**, then **Download ZIP**, and unzip it somewhere you will keep it, such as your Documents folder. Rename the folder if you like. If you use GitHub, click **Use this template** instead.
2. **Open it in Obsidian.** Install Obsidian from obsidian.md, choose **Open folder as vault**, and pick your workspace folder. When Obsidian asks whether you trust the author of this vault, choose to trust it so the bundled outliner plugin turns on.
3. **Open it in your agent.** Start your AI agent and point it at the same folder. Most agents ask you to choose a folder when you start a session.
4. **Ask it to set you up.** Type: "Read AGENTS.md and help me set up this workspace." Then make it yours, one request at a time:
	- "Set up my inbox", so your screenshots and downloads land in the Inbox.
	- "Add an account for Acme Corp", "Add a project for the office move", "Add an area for Home". Add the clients, projects, and parts of your life you want to track.
	- "Save these as my sample emails", and paste in three to five emails you have written. Drafts will match your style.
	- Drop your company's PowerPoint, Word, and Excel templates into the Assets/Templates folder.
	- Connect your email and calendar in your agent's settings, if it offers connectors. Everything still works without them; the agent will ask you for what it needs.
	- "Remove the sample notes", once you have added your own.
5. **Try it.** Each of these works on day one:
	- "Process my inbox"
	- "Prep me for my next meeting with Acme Corp"
	- "Update top of mind"
	- "Start a new week", on a Sunday

## Workspace Structure

For the curious, here is how the folder is laid out. You do not need to know this to use it; your agent does.

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
