---
name: managing-branches
description: Branch, commit, push, open, update, and merge pull requests for an app in Apps/ (or for the workspace itself), following the workspace git rules. Use when the user says "start a branch", "commit this", "open a PR", "push this update", "add this to the PR", "merge it", or "go back to main", and from building-apps.
---

# Managing Branches

Each folder under `Apps/` is its own git repo, and so is the workspace root. `cd` into the right one before every git command. Pass `--repo <owner>/<repo>` to every `gh` command; a repo guessed from the folder can hit the wrong pull request.

## Start a branch

1. `git status`. If there are uncommitted changes that are not part of this work, ask before going on.
2. `git checkout main && git pull` (skip the pull when the repo has no remote yet).
3. `git checkout -b <type>/<short-kebab-name>`, where type is `feature`, `fix`, `refactor`, `docs`, or `chore`.

## Commit

1. Read `git diff` and `git log --oneline -5` to match the commit style.
2. Stage files by name, never `git add -A`. Never stage `.env`, credentials, keys, databases, or data files. Check `git diff --cached`.
3. Write the message to a file and run `git commit -F <file>`. Heredocs inside command substitution break on parentheses.
4. Make a new commit each time. Never amend unless the user asks.

## Push and open a pull request (only when the user says so)

1. `git push -u origin HEAD`.
2. Write the body to a file:

   ```
   ## Summary
   - <one bullet per change>

   ## Test plan
   - <what was run and what it showed>
   ```

3. `gh pr create --repo <owner>/<repo> --base main --title "<title>" --body-file <file>`. Report the URL.

## Add to an open pull request

For a run of related changes in one session, keep committing to the same branch and pull request. After `git push`, if the push is rejected because the remote moved, run `git pull --rebase` and push again. Never force-push unless the user asks. Offer to update the title and body when the scope changed (`gh pr edit`).

## Merge (only when the user says so)

1. Confirm the review and QA from `building-apps` or `reviewing-changes` have no open Critical or High findings. If they do, say so and ask.
2. `gh pr merge <number> --repo <owner>/<repo> --merge --delete-branch`.
3. `git checkout main && git pull && git fetch --prune && git branch -d <branch>`.
4. If the app was running from this folder, restart it so it serves the merged code.

## Go back to main

`git checkout main && git pull`. If there are uncommitted changes, ask whether to commit them to the branch first, set them aside with `git stash`, or discard them; discarding needs the user's explicit yes.

## Safety

- Never commit or push to `main` directly, except the first commit of a new app.
- Never push, open, or merge a pull request without the user's word for that step.
