#!/usr/bin/python3

from wsgiref.simple_server import make_server

def application(environ, start_response):
    """Simple WSGI application"""

    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "<b>TEST</b>".encode("utf-8")

if __name__ == '__main__':
    # TODO: IPv6 apparently not used by default.
    server = make_server('', 8000, application)
    server.serve_forever()
