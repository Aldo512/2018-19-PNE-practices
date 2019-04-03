import socket
import termcolor
import re

# Configure the Server's IP and PORT
PORT = 8080
IP = "192.168.56.1"
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def allowed_char(string):
    charRe = re.compile(r'[^ACTG.]')
    string = charRe.search(string)
    return not bool(string)


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
            percA = round((As/len(self.bases))*100,2)
            return percA
        elif bases == 'T':
            percT = round((Ts/len(self.bases))*100,2)
            return percT
        elif bases == 'G':
            percG = round((Gs/len(self.bases))*100,2)
            return percG
        elif bases == 'C':
            percC = round((Cs/len(self.bases))*100,2)
            return percC
        else:
            print('As, Cs, Gs, Ts')
            return round((As/len(self.bases))*100, (Cs/len(self.bases))*100, (Gs/len(self.bases))*100, (Ts/len(self.bases))*100,2)

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
        termcolor.cprint("Message from client: {}".format(msg), 'blue')

        if msg == '\n':
            answer = 'ALIVE'
            ans = str.encode(answer)
            clientsocket.send(ans)

        n_msg = msg.splitlines()
        bases = n_msg[0]

        if allowed_char(bases) == True:
            ok = str.encode('OK\n')
            Rans = str.encode('')

            Lans = str.encode('')

            Cans = str.encode('')

            AAans = str.encode('')
            CCans = str.encode('')
            GGans = str.encode('')
            TTans = str.encode('')

            PAAns = str.encode('')
            PGAns = str.encode('')
            PTAns = str.encode('')
            PCAns = str.encode('')


            for comand in range(len(n_msg)):

                if n_msg[comand].lower() == 'len':
                    Lanswer = str(P3(bases).len())
                    Lans = str.encode(termcolor.colored('Length: '+ Lanswer + '\n', 'red'))

                if n_msg[comand].lower() == 'reverse':
                    Ranswer = P3(bases).reverse()
                    Rans = str.encode(termcolor.colored('Reverse: ' + Ranswer+ '\n', 'blue'))

                if n_msg[comand].lower() == 'complement':
                    Canswer = P3(bases).compl()
                    Cans = str.encode(termcolor.colored('Complement: ' + Canswer + '\n', 'yellow'))

                if n_msg[comand].lower() == 'counta':
                    AAanswer = str(bases.count('A'))
                    AAans = str.encode(termcolor.colored('Number of As; ' + AAanswer + '\n', 'white'))

                if n_msg[comand].lower() == 'countc':
                    CCanswer = str(bases.count('C'))
                    CCans = str.encode(termcolor.colored('Number of Cs: ' + CCanswer + '\n', 'cyan'))

                if n_msg[comand].lower() == 'countg':
                    GGanswer = str(bases.count('G'))
                    GGans = str.encode(termcolor.colored('Number of Gs: ' + GGanswer + '\n', 'magenta'))

                if n_msg[comand].lower() == 'countt':
                    TTanswer = str(bases.count('T'))
                    TTans = str.encode(termcolor.colored('Number of Ts: ' + TTanswer + '\n', 'green'))

                if n_msg[comand].lower() == 'perca':
                    PAAnswer = str(P3(bases).perc('A'))
                    PAAns = str.encode(termcolor.colored('As represent ' + PAAnswer + '%' + '\n', 'white'))

                if n_msg[comand].lower() == 'percg':
                    PGAnswer = str(P3(bases).perc('G'))
                    PGAns = str.encode(termcolor.colored('Gs represent ' + PGAnswer + '%' + '\n','magenta'))

                if n_msg[comand].lower() == 'percc':
                    PCAnswer = str(P3(bases).perc('C'))
                    PCAns = str.encode(termcolor.colored('Cs represent ' + PCAnswer + '%' + '\n', 'cyan'))

                if n_msg[comand].lower() == 'perct':
                    PTAnswer = str(P3(bases).perc('T'))
                    PTAns = str.encode(termcolor.colored('Ts represent ' + PTAnswer + '%' + '\n', 'green'))




            clientsocket.send(ok + Lans + Rans + Cans + AAans + CCans + GGans + TTans + PAAns + PGAns + PCAns + PTAns)
        else:
            error = 'ERROR: Looks like your DNA string contains not only bases, please check and try again'
            emsg = str.encode(termcolor.colored(error, 'red'))
            clientsocket.send(emsg)
        clientsocket.close()

except socket.error:
    print("Problems using port {}. Do you have permission?".format(PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()

