#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application  #/ this creates our app
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__': #/ this runs a server, it requires 3 things, hostname, port, and application, in this case, the app above
    from werkzeug.serving import run_simple
    run_simple(
        hostname='localhost',
        port=5555,
        application=application
    )