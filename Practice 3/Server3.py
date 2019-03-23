import socket
import termcolor
import sets

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.56.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class P3:
    def __init__(self, bases):
        self.bases = bases

    def len(self):
        return len(self.bases)

    def count(self, bases):
        count = 0
        for a in self.bases:
            if a == bases:
                count += 1
        return count

    def perc(self, bases):
        As = 0
        Ts = 0
        Gs= 0
        Cs= 0
        for a in self.bases:
            a = a.lower()
            if a == 'a':
                As += 1
            elif a == 't':
                Ts += 1
            elif a == 'g':
                Gs += 1
            elif a == 'c':
                Cs += 1

        if bases == 'A':
            percA = (As/len(self.bases))*100
            return percA
        elif bases == 'T':
            percT = (Ts/len(self.bases))*100
            return percT
        elif bases == 'G':
            percG = (Gs/len(self.bases))*100
            return percG
        elif bases == 'C':
            percC = (Cs/len(self.bases))*100
            return percC
        else:
            print('As, Cs, Gs, Ts')
            return (As/len(self.bases))*100, (Cs/len(self.bases))*100, (Gs/len(self.bases))*100, (Ts/len(self.bases))*100

    def compl(self):
        complement = []
        dict1 = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        for a in self.bases:
            complement.append(dict1[a])
        compli = ''.join(complement)
        return compli

    def reverse(self):
        return self.bases[::-1]

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

        if msg == '\n':
            answer = 'ALIVE'
            ans = str.encode(answer)
            clientsocket.send(ans)

        n_msg = msg.splitlines()
        bases = n_msg[0]
        bas = 'AGCT'
        if Set(n_msg).issubset(bas):



        

        # Send the messag
        message = "\n\nHello from the teacher's server\n"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()
