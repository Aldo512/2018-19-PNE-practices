import requests, sys, re, termcolor

server = "http://rest.ensembl.org"
ext = "/lookup/symbol/homo_sapiens"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
symbol = requests.post(server + ext, headers=headers, data='{ "symbols" : ["CACHD1"] }')

if not symbol.ok:
    symbol.raise_for_status()
    sys.exit()

decoded = symbol.json()

geneid = "/sequence/id/"
id = decoded['CACHD1']['id']
r = requests.get(server + geneid + id + '?', headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()
filein = repr(decoded)

done = filein.split(',')
writing = open('Jsoninfo.json', 'w+')

for info in range(len(done)):

    if info < len(done)-1:
        writing.write(done[info].replace("'", '"') + ',' + '\n')

    elif info == len(done)-1:
        writing.write(done[info].replace("'", '"'))

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

writing.close()


a = P3(decoded['seq']).count('A')
c = P3(decoded['seq']).count('C')
t = P3(decoded['seq']).count('T')
g = P3(decoded['seq']).count('G')
bas = ['A', 'C', 'T', 'G']
bases = [a,c,t,g]
maxbase = bas[bases.index(max(bases))]
perc = P3(decoded['seq']).perc(maxbase)
perca = P3(decoded['seq']).perc('A')
percc = P3(decoded['seq']).perc('C')
perct = P3(decoded['seq']).perc('T')
percg = P3(decoded['seq']).perc('G')
cprint = termcolor.cprint

print()
cprint('The ensembl id name for the gene is: ' + id, 'yellow')
print()
cprint('There are ' + str(len(decoded['seq'])) + ' total bases in the requested gene', 'blue')
print()
cprint('In total, there are ' + str(t) + ' T bases in the gene', 'red')
print()
cprint('The most popular base in the gene is ' + maxbase, 'magenta')
print()
cprint(maxbase + ' represents ' + str(perc) + '% of the total bases in the gene', 'cyan')
print()

r = 0
for nit in bases:
    if max(bases) != nit:
        print('The percentage of ' + bas[r] + ' is ' + str(P3(decoded['seq']).perc(bas[r])) + '%')
    r += 1

