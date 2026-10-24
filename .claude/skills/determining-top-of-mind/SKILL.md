---
name: determining-top-of-mind
description: Rebuild Notes/Daily/Top of Mind.md from recent notes. Collects every open ==highlight== from account, area, and project notes, adds a short status line per account, area, and project, and records what was finished since the last run. Use when the user says "update top of mind", "what's on my plate", "rebuild my task list", or before weekly planning.
---

# Determining Top of Mind

Scan recent notes across every account, area, and project and rewrite `Notes/Daily/Top of Mind.md`: priorities first, then one block per account, then an `Areas` group and a `Projects` group, each with a status line and the open to-dos per item.

## Where things are

- `Notes/Accounts/<Name>/<Name>.md`: one note per account. Dated entries live under `### Interaction Log`, newest first.
- `Notes/Accounts/<Name>/<Project>/<Project>.md`: one note per account project. Dated entries live under `### Log`.
- `Notes/Areas/<Area>/<Area>.md`: one note per area (ongoing responsibility). Dated entries live under `### Interaction Log`, like an account. Projects inside an area live in `Notes/Areas/<Area>/<Project>/<Project>.md`.
- `Notes/Projects/<Project>/<Project>.md` or `Notes/Projects/<Project>.md`: projects not tied to an account or area. Same format as an account project.
- Action items in any of these notes are marked `==like this==`. A highlight may be unclosed (`==text` to end of line). It is still open.
- A finished item is struck: `==~~text~~== (completed YYYY-MM-DD)`. An unclosed `==~~text` is also finished.
- `Notes/Daily/Top of Mind.md`: the output.

## Hard rule: transcribe, never author

Every `- [ ]` you write must be an existing `==highlight==` from a note, copied near-verbatim. Nothing else becomes a to-do.

- Never write a `==highlight==` into a note.
- Never invent a to-do, reword one into a different ask, or split one into several.
- If something looks missing, say so in chat. Do not write it to a file.

This rule covers checkboxes only. Every account, area, and project block still starts with a plain status bullet (step 5). Status, silence, overdue counts, dates, and context go there.

## Never undo the user's checkmarks

A `- [x]` in `Top of Mind.md` is the user's. Never turn it back into `- [ ]`. Keep any note the user appended to the line, word for word.

- Read the existing file before you rebuild it, and carry every `- [x]` line across with its trailing note.
- The same applies to `#### Priorities`. The user writes that section, or `prioritizing-tasks` does with the user's approval. Copy it across unchanged, except for the strike in step 3.

## Steps

1. **Back up.** Copy `Notes/Daily/Top of Mind.md` to `Notes/Daily/Archive/Top of Mind YYYY-MM-DD.md` with today's date. Overwrite a backup from earlier the same day.
2. **Read the current file.** Note every `- [x]` line and which account, area, or project block it sits under.
3. **Strike finished items at the source.** For each `- [x]` item, open the note it came from and find the matching highlight. The item ends with its entry date in parentheses, for example `(2027-01-05)`; use it to pick the right entry. Match on distinctive fragments, since the text may be shortened.
   - `==text==` or `==text` becomes `==~~text~~== (completed YYYY-MM-DD)` with today's date.
   - If the line is `- [ ] ==text==`, also change `- [ ]` to `- [x]`.
   - One clear match: edit it. No match or several matches: list them in chat and ask. Never guess.
4. **Collect open items.** In every account, account project, area, area project, and standalone project note, read the dated entries from the last 90 days (or the window the user asks for). Collect each highlight that is not struck. Record the entry date with it.
5. **Write the file** in this layout, with tabs for indentation. Keep the frontmatter block at the top of the file unchanged:

   ```markdown
   #### Priorities

   - [ ] (copied from the existing file, unchanged)

   ---

   - **[[Sample Company, Inc.]]**
   	- Weekly office hours on 2027-01-05 covered the rollout plan. Pat Ryder owns the next step; nothing is scheduled yet.
   	- [ ] Highlighted action item / followup (2027-01-05)
   	- **[[Sample Project]]**
   		- Kickoff held 2027-01-04; target delivery 2027-02-15. No blockers recorded.
   		- [ ] Highlighted action item / followup (2027-01-05)
   - **Areas**
   	- **[[Sample Home Maintenance]]**
   		- Contractor quote received 2027-01-05. Waiting on a decision about the start date.
   		- [ ] Highlighted action item / followup (2027-01-05)
   - **Projects**
   	- **[[Sample Website Refresh]]**
   		- Working session held 2027-01-06; launch targeted for 2027-03-01.
   		- [ ] Highlighted action item / followup (2027-01-06)

   ### Completed Last Time

   - Send the revised proposal (Sample Company, Inc.)
   ```

   - Accounts are top-level bullets, as bold wikilinks. Account projects nest one level under their account.
   - After the accounts come two plain bold group bullets, `**Areas**` then `**Projects**` (no wikilink). Each area or standalone project is a bold wikilink one level under its group, built the same way as an account. Area projects nest under their area.
   - The first bullet under every account, area, and project is a status summary of 1-3 sentences: what happened last and when, the current state, who is involved, and the next date if one exists. Summarize only what the notes say. Never make it a checkbox.
   - Then the checkboxes: carried-over `- [x]` lines, then open `- [ ]` items, each ending with its entry date.
   - Items that do not belong to a project go directly under the account or area, before any project blocks.
   - Leave out accounts, areas, and projects with no open items and no `- [x]` lines. Leave out the `Areas` or `Projects` group when nothing is left under it.
6. **Completed Last Time.** List every item that was `- [x]` in the previous file as `- Item text (Account, Area, or Project)`. Replace the previous run's list.
7. **Report** in chat: the number of open items per account, area, or project, the items you struck at the source, and anything you could not match.

## Rules

- Only the user marks things done. This skill records the user's checkmarks; it never decides a task is finished.
- Obsidian may write non-breaking spaces. When an exact-match edit fails, use a script.
- Keep dates in `YYYY-MM-DD`.
