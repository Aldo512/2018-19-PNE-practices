import socket
import termcolor
PORT = 8080
IP = '212.128.253.110'
MAX_OPEN_REQUEST = 5


def process_client(cs):

    #Reading the message from the client
    msg = cs.recv(2048).decode('utf-8')

    termcolor.cprint('Message from the client: {}'.format(msg), 'blue')

    #Sending the message back to the client
    #(because we are an echo server)
    cs.send(str.encode(msg))
    cs.close()


#A socket for connecting to the client
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

while True:

    print('Waiting for connections at: {}, {}'.format(IP, PORT))

    (clientsocket, address) = serversocket.accept()

    process_client(clientsocket)
