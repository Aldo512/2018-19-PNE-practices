import socket

# SERVER IP, PORT
IP = "127.0.0.1"
PORT = 8085

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes

while True:
    lolol = input()

    s.send(str.encode(lolol))
    # Receive data from the server
    message = s.recv(2048).decode("utf-8")
    print("MESSAGE FROM THE SERVER:\n")
    print(message)
