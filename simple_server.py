### code for server
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to a specific address and port

server_socket.bind(('localhost', 12345))

# Listen for incoming connections (maximum 5 queued connections)
server_socket.listen(5)

print('Server listening on port 12345...')

while True:
    # Accept incoming client connections
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))

    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break
    # Print received data and send a response back to the client
    print('Received data: {}'.format(data.decode()))
    response = 'Hello, Client! Thank you for your message.'
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
