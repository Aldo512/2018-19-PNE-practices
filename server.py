import socket

PORT = 8080
IP = '212.128.253.110'
MAX_OPEN_REQUEST = 5

#A socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

while True:

    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Process the client request
    clientsocket.close()