# Sample App Architecture

## Goal

A single person keeps a short to-do list in a browser tab on their own computer. Done means items can be added, checked off, and removed, and they are still there after a restart.

## Stack

- Python 3 standard library only (`http.server`, `json`). No packages to install.
- One static HTML page with plain JavaScript. No build step.
- A JSON file for storage. A list this small does not need a database.

## Structure

```
sample-app/
├── app.py              # Server: serves the page and the /api/items routes
├── static/index.html   # The page
├── test_app.py         # Tests for the critical flows
├── data/items.json     # Saved items (created on first run, not tracked)
├── README.md
└── ARCHITECTURE.md
```

## Data

`data/items.json` is a list of items:

| Field | Type | Meaning |
|---|---|---|
| `id` | integer | Unique, increasing |
| `text` | string | The to-do, 1-200 characters |
| `done` | boolean | Checked off |

## Flows

1. **Load:** the page calls `GET /api/items` and shows the list.
2. **Add:** the user types and presses Enter; the page calls `POST /api/items` with `{"text": ...}` and reloads the list.
3. **Check off:** clicking the box calls `PATCH /api/items/<id>` with `{"done": true|false}`.
4. **Remove:** clicking × calls `DELETE /api/items/<id>`.

## Critical flows

1. The page loads and shows saved items.
2. Adding an item saves it, and it survives a server restart.
3. Checking off an item saves its state.
4. Removing an item deletes only that item.
5. Empty or over-long text is rejected with a 400 and nothing is saved.

## Ports

8400, bound to `127.0.0.1` (see `Apps/PORTS.md`). Override with `SAMPLE_APP_PORT`.

## Risks

- **Exposure:** binds to `127.0.0.1` only, so other computers cannot reach it.
- **Script injection:** the page inserts item text with `textContent`, never as HTML.
- **Data loss:** writes go to a temporary file that replaces `items.json` in one step, so a crash mid-write cannot corrupt the list.
