#!/usr/bin/python3
"""
Simple HTTP server with basic API endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    Handler for simple API endpoints.
    """

    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_not_found()

    def handle_root(self):
        """
        Respond with a welcome message.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        """
        Respond with sample JSON data.
        """
        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def handle_status(self):
        """
        Respond with a status message.
        """
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_not_found(self):
        """
        Respond with a 404 error for unknown endpoints.
        """
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Endpoint not found")


def run_server():
    """
    Start the HTTP server.
    """
    port = 8000
    server_adress = ('', port)
    httpd = HTTPServer(server_adress, SimpleAPIHandler)
    print("Server running on port {}".format(port))
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
