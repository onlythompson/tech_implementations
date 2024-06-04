"""Basic web server using Python's built-in socket module."""

# Required tool for network programming
import socket

"""
HOST = '': The server will listen on all available network interfaces 
(e.g., both your local network and the internet if your machine is publicly accessible).
PORT = 8888: The server will listen for incoming connections on port 8888.
"""
HOST, PORT = '', 8888

"""
create a new socket object using the socket.socket() function.
the first argument is the address family (AF_INET) and the second argument is the socket type (SOCK_STREAM).
AF_INET is the address family for IPv4, and SOCK_STREAM is the socket type for TCP connections.
socket.AF_INET: Specifies that we're using IPv4 addresses.
socket.SOCK_STREAM: Indicates we want a TCP socket (for reliable, connection-oriented communication).
"""
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
setsockopt() method to set the SO_REUSEADDR option on the socket.
This allows you to restart the server without waiting for the socket to timeout.
This option lets the socket be reused immediately after the server is closed, preventing the "address already in use" error.

"""
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
"""
bind() method to bind the socket to the address and port.
The first argument is the host, and the second argument is the port.
"""
listen_socket.bind((HOST, PORT))
"""
listen() method to start listening for incoming connections.
The argument is the maximum number of queued connections (usually 1).
The socket starts waiting for incoming connections. The argument 1 limits the number of queued connections to 1.
"""
listen_socket.listen(1)
"""
print() function to print a message to the console.
This message tells you that the server is running and listening for incoming connections.

"""
print(f'Serving HTTP on port {PORT} ...')

"""
The server is now running and listening for incoming connections.
The server will run indefinitely until you stop it manually.
The server will accept incoming connections and print the request data to the console."""
while True:
    """
    accept() method to accept an incoming connection.
    The method returns a new socket object representing the connection and the address of the client.
    The server waits for a client to connect.
    When a client connects, a new socket (client_connection) is created for communication with that client.
    client_address stores the client's IP address and port.
    """
    client_connection, client_address = listen_socket.accept()
    """
    recv() method to receive data from the client.
    The argument is the maximum number of bytes to receive.
    The method returns the data received from the client.
    The server receives the request data from the client.
    The server reads the request data from the client and prints it to the console.
    
    The server receives up to 1024 bytes of data from the client (this would be the HTTP request).
    The request is printed to the console for debugging (not typically done in a production server).
    
    """
    request = client_connection.recv(1024)
    print(request.decode('utf-8'))

    """
    http_response: The response data that the server sends to the client.
    The server sends the response data to the client.

    The b prefix in front of the string (b"""...""") indicates that the string
    is a byte string, not a regular Unicode string (which is the default in Python 3).

    Data transmitted over a network is fundamentally in bytes.
    A byte string represents raw binary data, which is the appropriate format for sending over the socket.

    The HTTP protocol expects data to be transmitted in bytes. Headers and message bodies are all byte-oriented.

    Using byte strings ensures compatibility with different character encodings that clients might use.

    """
    http_response = b"""\
    HTTP/1.1 200 OK

    Hello, World!
    """
    
    """
    The server sends the response data to the client.
    """
    client_connection.sendall(http_response)
    #The connection with this client is closed.
    client_connection.close()