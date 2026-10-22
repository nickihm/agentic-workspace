---
name: opening-notes
description: Open a note in the Obsidian app. Resolves a name like "Sample Company notes" or "Sample Project" to its file under Notes/ and opens it with an obsidian:// URI. Use when the user says "open <name> notes", "pull up <name>", "open <name> in Obsidian", or asks to open this week's file or Top of Mind.
---

# Opening Notes

Open one note in Obsidian so the user can read and edit it. This skill does not read, summarize, or search the file.

## Steps

### 1. Resolve the name to a file

Look in this order, and stop at the first match:

1. `Notes/Accounts/<Name>/<Name>.md`
2. `Notes/Accounts/*/<Project>/<Project>.md`
3. `Notes/Projects/<Project>/<Project>.md` or `Notes/Projects/<Project>.md`
4. `Notes/Areas/`, `Notes/Resources/`
5. Shortcuts: "this week" is the current `Notes/Daily/YYYY-WN.md`; "top of mind" is `Notes/Daily/Top of Mind.md`; "long term" is `Notes/Daily/Long Term.md`.

Match without regard to case, spaces, or punctuation, and accept partial names ("sample co" matches `Sample Company, Inc.`).

- One match: continue.
- Several matches: ask which one. Do not guess.
- No match: say so and list the 3-5 closest names.

Confirm the `.md` file exists. The file name can differ slightly from the folder name; use the real one.

### 2. Find the vault name

The vault is the workspace root. Obsidian names a vault after its folder by default, so the vault name is the root folder's name:

```bash
basename "$(git rev-parse --show-toplevel)"
```

If the user renamed the vault in Obsidian, use that name instead.

### 3. Open it

```bash
open "obsidian://open?vault=<VaultName>&file=Notes/Accounts/Sample%20Company%2C%20Inc./Sample%20Company%2C%20Inc."
```

- `file=` is the path from the vault root without the `.md` extension.
- URL-encode the vault name and the path: space is `%20`, comma `%2C`, `#` `%23`, `&` `%26`, `?` `%3F`. A short way to do it: `python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "<path>"`.
- Quote the whole URI so the shell does not split it.
- `open` is macOS. On Linux use `xdg-open`; on Windows use `start ""`.

### 4. Confirm in one line

```
Opened Notes/Accounts/Sample Company, Inc./Sample Company, Inc..md in Obsidian.
```

Nothing else.

## Do not

- Read the file into context. The user asked to open it, not to be told what is in it.
- Open the raw path with `open <file>` or `open -a Obsidian <file>`. That can open a different app or skip the vault, which breaks wikilinks.
- Leave `.md` on the `file=` value.
