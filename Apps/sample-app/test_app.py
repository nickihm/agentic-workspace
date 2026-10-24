"""Tests for the critical flows in ARCHITECTURE.md. Run: python3 -m unittest -v"""
import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

os.environ["SAMPLE_APP_DATA"] = tempfile.mkdtemp()
import app  # noqa: E402  (reads SAMPLE_APP_DATA at import)


class SampleAppTest(unittest.TestCase):
    def setUp(self):
        app.DATA.unlink(missing_ok=True)
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()
        self.base = f"http://127.0.0.1:{self.server.server_address[1]}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()

    def call(self, method, path, body=None):
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                     headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req) as res:
                raw = res.read()
                return res.status, json.loads(raw) if raw and res.headers.get_content_type() == "application/json" else raw
        except urllib.error.HTTPError as err:
            with err:
                return err.code, json.loads(err.read())

    def test_page_loads(self):
        status, body = self.call("GET", "/")
        self.assertEqual(status, 200)
        self.assertIn(b"<title>Sample App</title>", body)

    def test_add_persists(self):
        status, item = self.call("POST", "/api/items", {"text": "  Call Pat  "})
        self.assertEqual((status, item["text"], item["done"]), (201, "Call Pat", False))
        self.assertEqual(json.loads(Path(app.DATA).read_text())[0]["text"], "Call Pat")
        self.assertEqual(self.call("GET", "/api/items")[1], [item])

    def test_check_off(self):
        item = self.call("POST", "/api/items", {"text": "Send proposal"})[1]
        self.assertEqual(self.call("PATCH", f"/api/items/{item['id']}", {"done": True})[1]["done"], True)
        self.assertTrue(self.call("GET", "/api/items")[1][0]["done"])

    def test_remove_only_that_item(self):
        first = self.call("POST", "/api/items", {"text": "One"})[1]
        second = self.call("POST", "/api/items", {"text": "Two"})[1]
        self.assertEqual(self.call("DELETE", f"/api/items/{first['id']}")[0], 204)
        self.assertEqual(self.call("GET", "/api/items")[1], [second])
        self.assertEqual(self.call("DELETE", f"/api/items/{first['id']}")[0], 404)

    def test_rejects_bad_input(self):
        for body in ({"text": ""}, {"text": "   "}, {"text": "x" * 201}, {"text": 5}, {}):
            self.assertEqual(self.call("POST", "/api/items", body)[0], 400, body)
        self.assertEqual(self.call("PATCH", "/api/items/1", {"done": "yes"})[0], 400)
        self.assertEqual(self.call("GET", "/api/items")[1], [])
        self.assertFalse(Path(app.DATA).exists())


if __name__ == "__main__":
    unittest.main()
