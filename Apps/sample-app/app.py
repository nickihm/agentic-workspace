#!/usr/bin/env python3
"""Sample App: a tiny to-do list served on 127.0.0.1. Standard library only."""
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = Path(os.environ.get("SAMPLE_APP_DATA", ROOT / "data")) / "items.json"
PAGE = ROOT / "static" / "index.html"
MAX_TEXT = 200
LOCK = threading.Lock()


def load():
    return json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else []


def save(items):
    DATA.parent.mkdir(parents=True, exist_ok=True)
    tmp = DATA.with_suffix(".tmp")
    tmp.write_text(json.dumps(items, indent=2), encoding="utf-8")
    tmp.replace(DATA)


class Handler(BaseHTTPRequestHandler):
    def send(self, status, body=None, kind="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def body(self):
        length = int(self.headers.get("Content-Length") or 0)
        try:
            return json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return None

    def item_id(self):
        tail = self.path.removeprefix("/api/items/")
        return int(tail) if tail.isdigit() else None

    def do_GET(self):
        if self.path == "/":
            self.send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
        elif self.path == "/api/items":
            with LOCK:
                self.send(200, load())
        else:
            self.send(404, {"error": "not found"})

    def do_POST(self):
        if self.path != "/api/items":
            return self.send(404, {"error": "not found"})
        body = self.body()
        text = body.get("text", "").strip() if isinstance(body, dict) and isinstance(body.get("text"), str) else ""
        if not 1 <= len(text) <= MAX_TEXT:
            return self.send(400, {"error": f"text must be 1-{MAX_TEXT} characters"})
        with LOCK:
            items = load()
            item = {"id": max((i["id"] for i in items), default=0) + 1, "text": text, "done": False}
            save(items + [item])
        self.send(201, item)

    def do_PATCH(self):
        item_id, body = self.item_id(), self.body()
        if item_id is None or not isinstance(body, dict) or not isinstance(body.get("done"), bool):
            return self.send(400, {"error": "send {\"done\": true|false} to /api/items/<id>"})
        with LOCK:
            items = load()
            match = next((i for i in items if i["id"] == item_id), None)
            if match is None:
                return self.send(404, {"error": "no such item"})
            match["done"] = body["done"]
            save(items)
        self.send(200, match)

    def do_DELETE(self):
        item_id = self.item_id()
        with LOCK:
            items = load()
            kept = [i for i in items if i["id"] != item_id]
            if item_id is None or len(kept) == len(items):
                return self.send(404, {"error": "no such item"})
            save(kept)
        self.send(204, b"")


def main():
    port = int(os.environ.get("SAMPLE_APP_PORT", 8400))
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"Sample App on http://127.0.0.1:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
