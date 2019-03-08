import socket

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.253.75"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases, aldo):
        print("New sequence created!")

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        self.aldo = aldo

    def len(self):
        return len(self.strbases)
    def compl(self):
        complement = []
        dict1 = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        for a in self.strbases:
            complement.append(dict1[a])
        compli = ''.join(complement)
        return compli
    def reverse(self):
        return self.strbases[::-1]

try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the conection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the messag
        message = "\n\nHello from the teacher's server"
        send_bytes = str.encode(message)
        # We must write bytes, not a string

        all = al.reverse()
        com = al.compl()
        send_compl = str.encode(com)
        al = Seq(msg, '')
        send_reversed = str.encode(all)
        clientsocket.send(send_reversed)
        clientsocket.send(send_bytes)
        clientsocket.send(send_compl)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
#