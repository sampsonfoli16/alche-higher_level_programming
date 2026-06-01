#!/usr/bin/env python3
"""Web server with 5 redirects and multiple status codes for testing."""

from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests with multiple redirects."""
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', 'http://localhost:8000/r1')
            self.end_headers()
        elif self.path == '/r1':
            self.send_response(302)
            self.send_header('Location', 'http://localhost:8000/r2')
            self.end_headers()
        elif self.path == '/r2':
            self.send_response(303)
            self.send_header('Location', 'http://localhost:8000/r3')
            self.end_headers()
        elif self.path == '/r3':
            self.send_response(304)
            self.send_header('Location', 'http://localhost:8000/r4')
            self.end_headers()
        elif self.path == '/r4':
            self.send_response(307)
            self.send_header('Location', 'http://localhost:8000/r5')
            self.end_headers()
        elif self.path == '/r5':
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
