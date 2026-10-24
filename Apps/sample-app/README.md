# Sample App

A tiny to-do list that runs in your browser. It shows the layout every app in `Apps/` follows, so your agent has a working example to copy. Delete it once you have built your own.

## Run

```bash
python3 app.py
```

Then open http://127.0.0.1:8400. Set `SAMPLE_APP_PORT` to use another port.

## Test

```bash
python3 -m unittest -v
```

## Files

- `app.py`: the web server and its small JSON API.
- `static/index.html`: the page.
- `test_app.py`: tests for the critical flows in `ARCHITECTURE.md`.
- `data/items.json`: the saved list, created on first run and not tracked by git.

## Log

The server prints each request to the terminal it runs in.

## Note

In your workspace, each app is its own git repo. This sample is tracked by the template repo so it ships with it. To make it a real app, run `git init -b main` inside this folder.
