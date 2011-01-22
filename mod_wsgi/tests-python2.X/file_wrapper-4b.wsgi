import os
import string

def application(environ, start_response):
    status = '200 OK' 
    
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-length', str(len(string.ascii_lowercase)/4))]
    start_response(status, response_headers)
    
    filelike = file('/tmp/filetest.txt', 'w+')
    filelike.write(string.ascii_lowercase)
    filelike.flush()
    
    filelike.seek(len(string.ascii_lowercase)/2, os.SEEK_SET)

    return environ['wsgi.file_wrapper'](filelike)
