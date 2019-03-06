import socket

# SERVER IP, PORT
IP = "212.128.253.75"
PORT = 8080

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes
send = input('Please enter the DNA string that you want to be checked: ')
s.send(str.encode(send))

# Receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)