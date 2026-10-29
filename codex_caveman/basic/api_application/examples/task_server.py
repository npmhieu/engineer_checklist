"""Local learning demo. Single process, volatile data, no authentication."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlsplit


TASKS = {}
NEXT_ID = 1
MAX_BODY = 4096


def representation(task):
    return {
        **task,
        "links": {"self": f"/tasks/{task['id']}", "collection": "/tasks"},
    }


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def setup(self):
        super().setup()
        self.connection.settimeout(5)

    def reply(self, status, body=None, **headers):
        payload = b"" if body is None else json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        if body is not None:
            self.send_header("Content-Type", "application/json")
        for name, value in headers.items():
            self.send_header(name, value)
        self.end_headers()
        self.wfile.write(payload)
        self.close_connection = True

    def error(self, status, code, **headers):
        self.reply(status, {"error": {"code": code}}, **headers)

    def route(self):
        path = urlsplit(self.path).path
        if path == "/tasks":
            return "collection", None
        parts = path.split("/")
        if len(parts) == 3 and parts[1] == "tasks" and parts[2].isascii() and parts[2].isdigit():
            if 1 <= len(parts[2]) <= 9 and not parts[2].startswith("0"):
                return "item", int(parts[2])
        return "unknown", None

    def do_GET(self):
        kind, task_id = self.route()
        if kind == "collection":
            self.reply(200, {"items": [representation(t) for t in TASKS.values()]})
        elif kind == "item" and task_id in TASKS:
            self.reply(200, representation(TASKS[task_id]))
        else:
            self.error(404, "NOT_FOUND")

    def do_POST(self):
        global NEXT_ID
        kind, _ = self.route()
        if kind == "unknown":
            return self.error(404, "NOT_FOUND")
        if kind != "collection":
            return self.error(405, "METHOD_NOT_ALLOWED", Allow="GET, DELETE")
        if self.headers.get("Transfer-Encoding") is not None:
            return self.error(400, "TRANSFER_ENCODING_UNSUPPORTED")
        lengths = self.headers.get_all("Content-Length", [])
        if not lengths:
            return self.error(411, "LENGTH_REQUIRED")
        if len(lengths) != 1 or not lengths[0].isascii() or not lengths[0].isdigit():
            return self.error(400, "INVALID_CONTENT_LENGTH")
        size = int(lengths[0])
        if size > MAX_BODY:
            return self.error(413, "BODY_TOO_LARGE")
        media_type = self.headers.get("Content-Type", "").split(";", 1)[0].strip().lower()
        if media_type != "application/json":
            return self.error(415, "UNSUPPORTED_MEDIA_TYPE")
        raw = self.rfile.read(size)
        if len(raw) != size:
            return self.error(400, "INCOMPLETE_BODY")
        try:
            data = json.loads(raw.decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            return self.error(400, "INVALID_JSON")
        if not isinstance(data, dict) or set(data) != {"title"} or not isinstance(data["title"], str):
            return self.error(422, "INVALID_TITLE")
        title = data["title"].strip()
        if not 1 <= len(title) <= 120:
            return self.error(422, "INVALID_TITLE")
        task = {"id": NEXT_ID, "title": title, "completed": False}
        TASKS[NEXT_ID] = task
        NEXT_ID += 1
        self.reply(201, representation(task), Location=f"/tasks/{task['id']}")

    def do_DELETE(self):
        kind, task_id = self.route()
        if kind == "collection":
            return self.error(405, "METHOD_NOT_ALLOWED", Allow="GET, POST")
        if kind != "item" or task_id not in TASKS:
            return self.error(404, "NOT_FOUND")
        del TASKS[task_id]
        self.reply(204)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), Handler)
    print("Learning demo: http://127.0.0.1:8000/tasks", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
