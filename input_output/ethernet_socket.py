# Purpose:  Demonstrate how to open a socket
#           Connect to different IP address

# Import statement
import socket

# IP Address
TCP_IP_ADDRESS = "192.168.1.1"
# Port to connect to
TCP_PORT = 18572
# Message to send
message = "Message"
# Buffer size of incoming messages
BUFFER_SIZE = 500

# Establish the socket connection
connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set the parameters of the socket and connect
connection_socket.connect((TCP_IP_ADDRESS, TCP_PORT))
# Send the message on the connection
connection_socket.send(message)
# Receive a message on the connection
received_message = connection_socket.recv(BUFFER_SIZE)
# Close the connection
connection_socket.close()