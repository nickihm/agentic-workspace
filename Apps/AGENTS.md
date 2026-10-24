---
type: Folder Guide
title: Apps Folder Guide
description: Apps you build, one folder each, named in kebab-case (expense-tracker/).
tags:
- folder-guide
- apps
---

# Apps

Apps you build, one folder each, named in kebab-case (`expense-tracker/`). Each app is its own git repo, so the workspace repo ignores everything here except `PORTS.md`, this file, and `sample-app/`.

- Build and change apps with the `building-apps` skill. Review them with `reviewing-changes`.
- Every app has a `README.md` (what it does, how to run and test it, where its log is) and an `ARCHITECTURE.md` (written by the `app-architect` agent).
- `PORTS.md` lists every port an app binds. Pick new ports from its free blocks and update it in the same change.
- `sample-app/` is a working example of this layout. Delete it once you have built your own.
