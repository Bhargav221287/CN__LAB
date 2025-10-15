import http.server
import socketserver
import os
import hashlib
import time
from email.utils import formatdate

PORT = 8888
FILE_PATH = "index.html"

class CachingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = FILE_PATH

        if not os.path.exists(self.path):
            self.send_error(404, "File not found")
            return

        with open(self.path, "rb") as f:
            content = f.read()

        etag = hashlib.md5(content).hexdigest()
        last_modified = formatdate(os.path.getmtime(self.path), usegmt=True)

        if (self.headers.get("If-None-Match") == etag or
            self.headers.get("If-Modified-Since") == last_modified):
            self.send_response(304)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("ETag", etag)
        self.send_header("Last-Modified", last_modified)
        self.send_header("Content-Length", len(content))
        self.end_headers()
        self.wfile.write(content)

with socketserver.TCPServer(("", PORT), CachingHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

