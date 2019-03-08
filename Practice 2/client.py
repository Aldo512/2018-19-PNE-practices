import socket
from Seq2 import Seq
# SERVER IP, PORT
IP = "212.128.253.79"
PORT = 8080

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created!')

inpt = input('Please enter the sequence to be analyzed: ')
cmp = Seq(inpt).compl()
rvs = Seq(inpt).reverse()

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

sequence = [inpt, cmp, rvs]
# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes


s.send(str.encode(str(sequence)))

# Receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)