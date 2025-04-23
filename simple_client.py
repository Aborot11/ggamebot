import socket
import time
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (replace 'localhost' with the server's IP address if needed)
# temporary set firewalls to off
# ping the server/client and it should reply, otherwise 
# 
client_socket.connect(('localhost', 12345))

time.sleep(3)
# Send a message to the server
message = 'Hello, Server! This is the client.'
client_socket.send(message.encode())

# Receive and print the server's response
response = client_socket.recv(1024)
print('Received from server: {}'.format(response.decode()))

# Close the client socket
client_socket.close()
