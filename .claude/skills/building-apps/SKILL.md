---
name: building-apps
description: Build a new app or change an existing one in Apps/, end to end, with the right model at each step. The app-architect agent (large model) designs it, the app-developer agent (small or medium model) builds it step by step on a feature branch, the pr-reviewer agent (large model) reviews the diff, the qa-reviewer agent tests it, and managing-branches opens and merges the pull request. Use when the user says "build me an app", "make a tool that", "add a feature to <app>", or "fix <bug> in <app>".
---

# Building Apps

Every app lives in its own folder under `Apps/`, with its own git repo. The root workspace repo ignores everything in `Apps/` except `PORTS.md`.

## Who does what

| Step | Agent | Model | Why |
|---|---|---|---|
| Design | `app-architect` | large (`opus`) | Design mistakes are the most expensive to fix later. |
| Build | `app-developer` | medium (`sonnet`); small (`haiku`) for one-file edits, copy, and config | The plan already made the hard decisions. |
| Code review | `pr-reviewer` | large (`opus`) | Security and architecture problems are easy to miss. |
| Test | `qa-reviewer` | medium (`sonnet`) | Running tests and flows needs care, not deep design. |

The agents are defined in `.claude/agents/`, each with its model set. When a build step is marked `[large model]` in the plan, run `app-developer` with the model overridden to `opus` for that step. When the agent tool supports it, pass `haiku` for small edits. If your agent tool cannot pick a model, run every step anyway and say which steps ran on which model.

## Steps

### 1. Set up the app folder

- **New app:** pick a kebab-case folder name, create `Apps/<app>/`, run `git init -b main` inside it, add a `README.md` with one line on what it is and a `.gitignore` that covers `.env`, data files, databases, virtual environments, and build output. Commit that on `main`. Ask the user whether to create a GitHub repository for it; never make one public without asking.
- **Existing app:** run `git status` in `Apps/<app>/`. If there are uncommitted changes, ask before going on.

### 2. Design

Run `app-architect` with the user's request in their own words and the app folder. Show the user the goal, the stack, and the build plan in plain language. Wait for approval. Answer the architect's questions with the user, not on their behalf.

### 3. Branch

Use `managing-branches` to create a feature branch from an up-to-date `main` in `Apps/<app>/`.

### 4. Build, one step at a time

For each plan step, run `app-developer` with the step, the branch, and the app folder. Check its report: if it stopped or something failed, fix the cause (re-plan with the architect when the plan was wrong) before the next step. Independent steps that touch different files may run in parallel.

### 5. Review

Run `pr-reviewer` on the branch diff against `main` (`git diff main...HEAD` in `Apps/<app>/`).

- Fix every Critical and High finding with `app-developer`, then ask `pr-reviewer` to check each fix, giving it the earlier findings.
- Show Medium and Low findings to the user and ask which to fix.

### 6. Test

Run `qa-reviewer` on the app at the branch. Fix anything broken in a critical flow with `app-developer` and run QA again.

### 7. Finish

Tell the user in plain language what now works and how to open or run it. Then use `managing-branches` to open a pull request, and merge only when the user says so. Update the Apps table in the workspace `AGENTS.md` (folder, stack, run, test) when the app is new or its run or test command changed.

## Rules

- No code before the user approves the design.
- Never commit on `main` after the first commit of a new app. Every change goes through a branch, review, and QA.
- Never test against the user's real data. QA uses a scratch copy.
- Ports come from a free block in `Apps/PORTS.md`, and `PORTS.md` is updated in the same change.
- Report progress after each step in one line: "Step 3 of 6 built: CSV import. Next: the summary page."
