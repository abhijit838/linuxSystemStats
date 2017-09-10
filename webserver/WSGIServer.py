"""
Python WSGI web server
"""
import socket
try:
    from io import StringIO
except ImportError:
    from StringIO import StringIO
import sys

class WSGIServer(object):
    """
    Wsgi server
    """
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        # Create and listen socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family, self.socket_type
        )
        # Reuse address
        listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Bind
        listen_socket.bind(server_address)
        # Listen
        listen_socket.listen(self.request_queue_size)
        # Get server host and port
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        # Return headers set by Web framework/Web application
        self.headers_set = []

    def set_app(self, application):
        """ Set application """
        self.application = application

    def server_forever(self):
        """ Run the server forever to listen requests"""
        listen_socket = self.listen_socket
        while True:
            # New client request wait
            self.client_connection, client_address = listen_socket.accept()
            # Handle the request and wait for another
            self.handle_one_request()

    def handle_one_request(self):
        """ Handle request """
        self.request_data = request_data = self.client_connection.recv(1024)
        # Print formatted request
        print(''.join(
            '< {line}\n'.format(line=line)
            for line in request_data.splitlines()
        ))
        
        self.parse_request(request_data)

        # Construct environment dict using request data
        env = self.get_environment()

        # Now call our application callable and get back a result
        # that will become HTTP response
        result = self.application(env, self.start_response)

        # Construct a response and send it back to the client
        self.finish_response(result)

    def parse_request(self, text):
        """ Parse the request """
        request_line = text.splitlines()[0]
        request_line = request_line.rstrip('\r\n')
        # Break down the request line to components
        (self.request_method,
        self.path,
        self.request_version
        ) = request_line.split()

    def get_environment(self):
        """ Environment variables"""
        env = {}
        # Required WSGI variables
        env['wsgi.version'] = (1, 0)
        env['wsgi.url_scheme'] = 'http'
        #env['wsgi.input'] = StringIO(self.request_data)
        env['wsgi.errors'] = sys.stderr
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = False
        # Required CGI bariables
        env['REQUEST_METHOD'] = self.request_method
        env['PATH_INFO'] = self.path
        env['SERVER_NAME'] = self.server_name
        env['SERVER_PORT'] = str(self.server_port)   
        return env

    def start_response(self, status, response_headers, exc_info=None):
        """ Start preparing response"""
        # Add necessary headers
        from datetime import datetime
        server_headers = [
            ('Date', datetime.date),
            ('Server', 'WSGIServer 0.2'),
        ]
        self.headers_set = [status, response_headers + server_headers]

    def finish_response(self, result):
        """ Prepare the response with body """
        try:
            status, response_headers = self.headers_set
            response = 'HTTP/1.1 {status}\r\n'.format(status=status)
            for header in response_headers:
                response += '{0}: {1}\r\n'.format(*header)
            response + '\r\n'
            for data in result:
                response += data
            # Print formatted response
            print(''.join(
                '> {line}\n'.format(line=line)
                for line in response.splitlines()
            ))
            self.client_connection.sendall(response)
        finally:
            self.client_connection.close()

class HTTPServer():
    """ WSGI server runner """
    def run_server(self, server_address):
        """ Create server with application
        server_address: (HOST, PORT)
        application: application callable
        """
        if len(sys.argv) < 2:
            sys.exit('Provide a WSGI application object as module:callable')
        app_path = sys.argv[1]
        module, application = app_path.split(':')
        module = __import__(module)
        application = getattr(module, application)
        server = WSGIServer(server_address)
        server.set_app(application)
        server.server_forever()

# If you are running this module directly
if __name__ == '__main__':
    HTTPServer().run_server(('', 8888))
