"""
Make sure to check the basic_web_server.py file first.
This is a basic http server that can handle GET requests.
"""

import socket

"""
HOST: The host name or IP address of the server.
PORT: The port number that the server listens on.
The host is not specified, so the server will accept connections on 
any available network interface.
In this case, we are developing within a device, so we use the standard loopback address. a.k.a localhost.
"""
HOST, PORT = '', 8000

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f'Serving HTTP on port {PORT} ...')

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))
    
    #Parse the HTTP request headers
    """
    TCP is a stream protocol, so the data is not sent in fixed-size packets.
    The data is sent in a continuous stream.
    The data has headers and a body.
    The headers contain metadata about the data.
    The body contains the actual data.
    The headers and body are separated by a blank line.
    The headers are separated by a newline character.
    The first line of the headers is the request line.
    The request line contains the request method, the requested resource, and the HTTP version.
    The request line is followed by the request headers.
    """
    #Parse the request data
    #The request is decoded from bytes to a string.
    #split() method to split the request data into lines.
    #The first line of the request data contains the request line.
    headers = request.decode('utf-8').split('\n')
    filename = headers[0].split()[1]

    #Check if the requested file is the root
    #If it is, set the filename to index.html
    if filename == '/':
        filename = '/index.html'

    """
    htdocs: The folder that contains the HTML files.
    index.html: The default file that the server will serve.
    fin: The file object that reads the content of the index.html file.
    """
    #Get the content of the htdocs/index.html file
    #fin = open('htdocs/index.html')

    """
    Wrap the file reading code in a try-except block.
    This is to handle the case where the requested file does not exist.
    If the file does not exist, the server will return a 404 Not Found response.
    """
    try:
        #Check if the file exists in the htdocs folder
        #If it does, open the file and read its contents
        fin = open('htdocs' + filename)
        content = fin.read()
        fin.close()

        #If the file exists, return a 200 OK response
        #http_response = 'HTTP/1.1 200 OK\n\nHello, World!'
        http_response = 'HTTP/1.1 200 OK\n\n' + content
    except FileNotFoundError:
        http_response = 'HTTP/1.1 404 Not Found\n\nFile Not Found'

    #Send the HTTP response to the client
    client_connection.sendall(http_response.encode())
    client_connection.close()