#!/usr/bin/python3
import http.server
import socketserver
import json

PORT = 8000


class Request(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {"Endpoint not found"}
            self.wfile.write(json.dumps(error).encode('utf-8'))
