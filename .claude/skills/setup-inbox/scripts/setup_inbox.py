#!/usr/bin/env python3
"""Point screenshots and browser downloads at the workspace Inbox/.

Plain Python 3, no dependencies. Prints what it changed and how to undo it.

  python3 setup_inbox.py --dry-run     # show what would change
  python3 setup_inbox.py               # apply
  python3 setup_inbox.py --inbox PATH  # use another folder

Handles:
  - macOS screenshots (com.apple.screencapture location)
  - Chrome, Edge, Brave, Chromium, Arc: download.default_directory in each
    profile's Preferences file (the browser must be closed)
  - Firefox: browser.download.dir in each profile's user.js
Everything else (Safari, Windows and Linux screenshot tools) is printed as a
manual step.
"""
import argparse
import json
import os
import platform
import subprocess
from pathlib import Path

HOME = Path.home()
SYSTEM = platform.system()

if SYSTEM == "Darwin":
    SUPPORT = HOME / "Library/Application Support"
    CHROMIUM = {
        "Chrome": SUPPORT / "Google/Chrome",
        "Edge": SUPPORT / "Microsoft Edge",
        "Brave": SUPPORT / "BraveSoftware/Brave-Browser",
        "Chromium": SUPPORT / "Chromium",
        "Arc": SUPPORT / "Arc/User Data",
    }
    FIREFOX = SUPPORT / "Firefox/Profiles"
elif SYSTEM == "Windows":
    LOCAL = Path(os.environ.get("LOCALAPPDATA", HOME / "AppData/Local"))
    ROAMING = Path(os.environ.get("APPDATA", HOME / "AppData/Roaming"))
    CHROMIUM = {
        "Chrome": LOCAL / "Google/Chrome/User Data",
        "Edge": LOCAL / "Microsoft/Edge/User Data",
        "Brave": LOCAL / "BraveSoftware/Brave-Browser/User Data",
        "Chromium": LOCAL / "Chromium/User Data",
    }
    FIREFOX = ROAMING / "Mozilla/Firefox/Profiles"
else:
    CONFIG = HOME / ".config"
    CHROMIUM = {
        "Chrome": CONFIG / "google-chrome",
        "Edge": CONFIG / "microsoft-edge",
        "Brave": CONFIG / "BraveSoftware/Brave-Browser",
        "Chromium": CONFIG / "chromium",
    }
    FIREFOX = HOME / ".mozilla/firefox"


def macos_screenshots(inbox, dry):
    if SYSTEM != "Darwin":
        return "skip", "screenshots: not macOS, see manual steps"
    read = subprocess.run(["defaults", "read", "com.apple.screencapture", "location"],
                          capture_output=True, text=True)
    old = read.stdout.strip() if read.returncode == 0 else "(default: Desktop)"
    if old == str(inbox):
        return "ok", f"screenshots: already {inbox}"
    if not dry:
        subprocess.run(["defaults", "write", "com.apple.screencapture", "location",
                        "-string", str(inbox)], check=True)
        subprocess.run(["killall", "SystemUIServer"], capture_output=True)
    undo = ("defaults delete com.apple.screencapture location" if read.returncode
            else f"defaults write com.apple.screencapture location -string '{old}'")
    return "changed", f"screenshots: {old} -> {inbox} (undo: {undo})"


def chromium_profiles(root):
    return [p for p in sorted(root.glob("*/Preferences"))
            if p.parent.name == "Default" or p.parent.name.startswith("Profile ")]


def chromium_downloads(name, root, inbox, dry):
    results = []
    if os.path.lexists(root / "SingletonLock") or (root / "lockfile").exists():
        return [("blocked", f"{name}: running. Quit it and run this again")]
    for prefs in chromium_profiles(root):
        data = json.loads(prefs.read_text(encoding="utf-8"))
        download = data.setdefault("download", {})
        old = download.get("default_directory", "(default: Downloads)")
        label = f"{name} [{prefs.parent.name}]"
        if old == str(inbox):
            results.append(("ok", f"{label}: already {inbox}"))
            continue
        if not dry:
            download["default_directory"] = str(inbox)
            data.setdefault("savefile", {})["default_directory"] = str(inbox)
            prefs.write_text(json.dumps(data, separators=(",", ":")), encoding="utf-8")
        results.append(("changed", f"{label}: {old} -> {inbox} "
                                   "(undo: Settings > Downloads > Location)"))
    return results


def firefox_downloads(inbox, dry):
    results = []
    lines = [f'user_pref("browser.download.dir", {json.dumps(str(inbox))});',
             'user_pref("browser.download.folderList", 2);']
    for profile in sorted(p for p in FIREFOX.glob("*") if (p / "prefs.js").exists()):
        user_js = profile / "user.js"
        text = user_js.read_text(encoding="utf-8") if user_js.exists() else ""
        if all(line in text for line in lines):
            results.append(("ok", f"Firefox [{profile.name}]: already {inbox}"))
            continue
        if not dry:
            kept = [l for l in text.splitlines()
                    if "browser.download.dir" not in l and "browser.download.folderList" not in l]
            user_js.write_text("\n".join(kept + lines) + "\n", encoding="utf-8")
        results.append(("changed", f"Firefox [{profile.name}]: -> {inbox} "
                                   f"(undo: remove the two browser.download lines from {user_js})"))
    return results


def manual_steps(inbox):
    steps = []
    if SYSTEM == "Darwin":
        steps.append(f"Safari: Settings > General > File download location > Other... > {inbox}")
    elif SYSTEM == "Windows":
        steps.append(f"Snipping Tool: Settings > Screenshots folder > Change > {inbox}")
    else:
        steps.append(f"Screenshot tool: set its save folder to {inbox} if it has one "
                     "(GNOME Screenshot always saves to ~/Pictures/Screenshots)")
    steps.append("Any other browser: set its download folder to the path above")
    return steps


def main():
    root = Path(__file__).resolve().parents[4]
    parser = argparse.ArgumentParser(description="Point screenshots and downloads at Inbox/.")
    parser.add_argument("--inbox", default=str(root / "Inbox"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    inbox = Path(args.inbox).expanduser().resolve()
    if not inbox.is_dir():
        raise SystemExit(f"Inbox folder not found: {inbox}")

    results = [macos_screenshots(inbox, args.dry_run)]
    for name, path in CHROMIUM.items():
        if path.is_dir():
            results += chromium_downloads(name, path, inbox, args.dry_run)
    if FIREFOX.is_dir():
        results += firefox_downloads(inbox, args.dry_run)

    print(("DRY RUN, nothing changed\n" if args.dry_run else "") + f"Inbox: {inbox}")
    for status, line in results:
        print(f"[{status}] {line}")
    print("Manual:")
    for step in manual_steps(inbox):
        print(f"- {step}")


if __name__ == "__main__":
    main()
