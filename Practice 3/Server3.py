import socket
import termcolor

class P3:
    def __init__(self, bases):
        self.bases = bases

    def len(self):
        return len(self.bases)

    def find(self, bases):
        found = 0
        for a in self.bases:
            if a == bases:
                found += 1
        return found
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
        percA = (As/len(bases))*100
        return percA





r = P3('AAC').perc('')
print(r)