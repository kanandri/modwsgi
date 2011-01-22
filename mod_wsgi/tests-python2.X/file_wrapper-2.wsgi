import StringIO
import string

def application(environ, start_response):
    status = '200 OK'

    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)

    filelike = StringIO.StringIO(string.ascii_lowercase)

    return environ['wsgi.file_wrapper'](filelike)
