#!/usr/bin/env python3
"""Simple web server for testing network shell scripts."""

from http.server import HTTPServer, BaseHTTPRequestHandler

class TestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests with header validation."""
        # Check for custom header
        if self.headers.get('X-HolbertonSchool-User-Id') == '98':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'NO')
    
    def log_message(self, format, *args):
        pass

if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), TestHandler)
    server.serve_forever()
