import http.server
import socketserver
import termcolor
import re

# Define the Server's port
PORT = 8001

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

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        srl = self.requestline
        # Open the form1.html file
        f = open("Main6.html", 'r')
        contents = f.read()
        f.close()
        print(srl)
        if '&' in srl:
            docuini = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DNA results</title>
</head>
<body style="background-color: lightblue">\n'''

            results = [docuini,]
            dnatemp = srl[srl.find('dna')+4:srl.find('&')]
            dna = dnatemp.upper()
            dnaop= open('Testresult.html', 'w+')
            dnastr = P3(dna)
            if allowed_char(dna) == True:
                if 'ln=on' in srl:
                    ln = dnastr.len()
                    results.append('Lenght: ' + str(ln) + '</br>' + '\n')

                if 'rvr=on' in srl:
                    rvr = dnastr.reverse()
                    results.append('Reverse: ' + rvr + '</br>' + '\n')

                if 'operation=slct' not in srl:

                    if 'prc' in srl and 'base' in srl:
                        base = srl[srl.find('base')+5]
                        prc = dnastr.perc(base)
                        results.append('Percentage of ' + base + 's '+ str(prc) + '%' + '</br>' + '\n')
                    elif 'cnt' in srl and 'base' in srl:
                        base = srl[srl.find('base') + 5]
                        cnt = dnastr.count(base)
                        results.append('Number of '+ base + 's is: ' + str(cnt) + '</br>' + '\n')
                    elif 'base' not in srl:
                        results.append('You didn\'t select a base to operate...')
                else:
                    results.append('You didn\'t select an operation...')
            else:
                errormsg = 'ERROR: Not all characters inside the sequence are bases of DNA'
                docuini = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ERROR</title>
</head>
<body style="background-color: red">\n'''
                results = [docuini,]
                results.append(errormsg)
            docufinal= '''\n</body>
</html> \n  <br> <a href="Main6.html">[Main page]</a>'''
            results.append(docufinal)
            for lines in range(len(results)):
                dnaop.write(results[lines])
            dnaop.close()
            newdnaop = open('Testresult.html', 'r')
            contents = newdnaop.read()
        elif 'favicon' not in srl:
            dna =srl[srl.find('dna')+4:srl.find('H')-1]


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")