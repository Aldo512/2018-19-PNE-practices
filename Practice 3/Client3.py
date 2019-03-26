import socket

# SERVER IP, PORT
IP = "192.168.56.1"
PORT = 8080

# First, create the socket
# We will always use this parameters: AF_INET y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

# Send data. No strings can be send, only bytes
# It necesary to encode the string into bytes

#PLACE HERE YOUR MESSAGE
lolol = '''AACGATCGACTTGACGATCGATCGCTasATCGCGCGCTAATATAAAACGACTCGCATCGACTCGACTAGCTAGCATCA
reverse
len
perca
percc
percg
perct
complement
counta
countg
countc
countt
'''


s.send(str.encode(lolol))
# Receive data from the server
msg = s.recv(2048).decode("utf-8")
print("MESSAGE FROM THE SERVER:\n")
print(msg)
