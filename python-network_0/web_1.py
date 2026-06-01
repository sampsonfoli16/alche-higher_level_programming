#!/usr/bin/env python3
"""Web server with 1 redirect for testing."""

from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests with one redirect."""
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', 'http://localhost:8000/redirected')
            self.end_headers()
        elif self.path == '/redirected':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), TestHandler)
    server.serve_forever()
