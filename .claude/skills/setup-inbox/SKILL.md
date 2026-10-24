---
name: setup-inbox
description: Point the computer's screenshots and browser downloads at the workspace Inbox/ so everything new lands where inbox-processing can file it. Changes the macOS screenshot location and the download folder of Chrome, Edge, Brave, Chromium, Arc, and Firefox. Use when the user says "set up my inbox", "save screenshots to the inbox", "send downloads to the inbox", or after cloning this workspace on a new machine.
---

# Setup Inbox

Make `Inbox/` the place new files arrive: screenshots and browser downloads. `inbox-processing` then files them.

Skill folder: `.claude/skills/setup-inbox` (called `$S` below). The script is plain Python 3 with no dependencies.

## Steps

1. **Preview.** Run the script with `--dry-run` from the workspace root and show the user the output:

   ```bash
   python3 -I $S/scripts/setup_inbox.py --dry-run
   ```

   Each line is one setting: `[changed]` will change, `[ok]` is already set, `[blocked]` needs the browser closed, `[skip]` does not apply on this OS. The `Manual:` lines are settings the script cannot change.
2. **Confirm.** These are machine-wide settings outside the workspace. Wait for the user to say yes before applying.
3. **Close browsers.** Chromium browsers rewrite their settings file on exit, so a change made while one is open is lost. For each `[blocked]` line, ask the user to quit that browser. Never quit it for them.
4. **Apply.** Run the same command without `--dry-run`. Run it again if a browser was blocked; it is safe to repeat.
5. **Manual steps.** Walk the user through each `Manual:` line (Safari, or the screenshot tool on Windows and Linux).
6. **Check.** Ask the user to take one screenshot (`Cmd+Shift+4` on macOS) and confirm it appears in `Inbox/`.
7. **Report** one line per setting changed, with the undo for each from the script's output.

## Rules

- The script writes the absolute path of `Inbox/`. If the workspace folder moves, run this skill again.
- Change only the save location. Never touch other browser settings, such as "Ask where to save each file".
- Downloads and screenshots in `Inbox/` are not tracked by git (see `.gitignore`). Files are tracked once `inbox-processing` files them into `Notes/`.
