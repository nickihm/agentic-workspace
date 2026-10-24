# Workspace Template

Automate work functions by connecting your favorite AI agent or agents to a unified knowledge workspace.
### Knowledge Management

This workspace acts as a personal knowledge management system or 'second brain' and works with Obsidian.
Everything is stored by projects, area/domain, or account (i.e. client account). Accounts can also have their own projects. All interactions, important files, contacts are stored in this structure.
Agents connected to the base directory understand the structure and save information accordingly. Agents can also search and answer questions against your knowledge base.
- inbox-processing
### Getting Top of Mind

Your activities with accounts, projects, and areas are stored in their interaction logs. Action items, updates can be buried in those interactions. 
The skill 'determining top of mind' will scan all your accounts/projects/areas for latest activity and product an executive summary outline with a 3-5 sentence summary of the account/project/area and action items and todos. This gives you a bird-eye view of where everything stands and what needs to be done.
### Prioritizing and Timeboxing

The 'prioritizing tasks' skill goes through your top of mind todos and helps you prioritizing based on the Eisenhower matrix, estimates required time effort, and timeboxes your calendar and weekly todo file.
### Long Term Planning
- Generate weekly todo file
- Long Term file and integration in to weekly file generation
### Knowledge Work
- research
- build decks
- create excel models
- create diagrams
### Managing Communication
- collect-email-important
- meeting-prepper
- drafting-email
- complete the task
- collect-email-newsletters
### Building Apps
- Apps folder structure
- skills for SDLC -- architecture, build, code review, QA, branch management
- Tracking ports in PORTS

## Workspace Structure

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