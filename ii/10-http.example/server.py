from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def application(environ, start_response):
    """Simple WSGI application"""

    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    yield "<b>TEST</b>".encode("utf-8")

if __name__ == '__main__':
    server = make_server('', 8000, application)
    server.serve_forever()
