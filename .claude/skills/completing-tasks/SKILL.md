---
name: completing-tasks
description: Mark a task complete when the user says it is done. Checks the box in Notes/Daily/Top of Mind.md and strikes the matching ==highlight== in the source note as ==~~text~~== (completed YYYY-MM-DD). Use when the user says "X is done", "done with X", "finished X", "mark X complete", "X was approved", "I sent X", or "check off X".
---

# Completing Tasks

When the user says a task is done, record it in two places:

1. `Notes/Daily/Top of Mind.md`: change `- [ ]` to `- [x]`.
2. The source note: strike the matching highlight as `==~~text~~== (completed YYYY-MM-DD)`.

Only the user decides a task is done. This skill records that decision. It never marks a task complete on its own judgment.

## Steps

### 1. Find the task in Top of Mind

Search `Notes/Daily/Top of Mind.md` for open checkboxes (`- [ ]`) that match the user's words. Search by short, distinctive fragments, because the user paraphrases.

Each to-do ends with the date of the entry it came from, for example `(2027-01-05)`. The bold wikilink above it (`- **[[Sample Company, Inc.]]**`, and a nested `**[[Sample Project]]**` if present) tells you which note it came from. The same task can appear more than once, for example under `#### Priorities` and under its account. Check every copy.

- Exactly one task matches: continue.
- More than one task, or no clear match: show each candidate line and ask. Never guess.
- No match: say so, and show the closest lines you found.

### 2. Find the source highlight

Resolve the wikilink to a file:

- Account: `Notes/Accounts/<Name>/<Name>.md`
- Account project: `Notes/Accounts/<Name>/<Project>/<Project>.md`
- Standalone project: `Notes/Projects/<Project>/<Project>.md` or `Notes/Projects/<Project>.md`

Search the file for a fragment of the to-do text. Highlights are often unclosed, so a line may start with `==` and have no closing `==`. Use the to-do's date to pick the right entry when the same text appears more than once.

- Exact or near-verbatim match: continue.
- The highlight is already struck (it starts with `==~~`, closed or not): it is already done. Only check the box in Top of Mind, and tell the user.
- No match, or more than one possible match: ask. A failed search does not prove the item is absent, so say the search failed.

### 3. Show the edit, then apply it

Show the before and after for each line, with file and line number:

```
Notes/Daily/Top of Mind.md:9
-	- [ ] Send the revised proposal (2027-01-05)
+	- [x] Send the revised proposal (2027-01-05)

Notes/Accounts/Sample Company, Inc./Sample Company, Inc..md:31
-		- ==Send the revised proposal
+		- ==~~Send the revised proposal~~== (completed 2027-01-08)
```

Wait for the user to confirm, then make the edits.

### Strike-through rules

- Strike only the highlighted text. Keep the indent, list marker, and any text after the highlight.
- Closed `==text==` and unclosed `==text` both become `==~~text~~== (completed YYYY-MM-DD)`.
- If a line has more than one highlight, strike only the one that matches.
- Use today's date unless the user gives one.

### 4. Report

One line per file changed. Stop there.

## Rules

- Never write a new `==highlight==`, and never add a to-do.
- Never reword the task text when you strike it.
- Never remove the checked line from Top of Mind. Keep it as `- [x]`; `determining-top-of-mind` moves it to `### Completed Last Time` on its next run.
- If the user says only part of a task is done, ask how to record it. Do not split the task.
- If the user names several tasks, handle each one and show all the edits together before applying them.
- Obsidian may write non-breaking spaces. When an exact-match edit fails, use a script.
