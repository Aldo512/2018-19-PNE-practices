class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print('New empty sequence created!')

        self.strbases = strbases

    def len(self):
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq
    All the objects of class Gene will
    inheritage the methods from Seq Class"""
    pass
s1= Gene("AATCGATCC")
s2= Seq("TTACGGAT")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print('Sequence 1: {}'.format(str1))
print('     Length: {}'.format(l1))
print('Sequence 2: {}'.format(str2))
print('     Length: {}'.format(l2))
print('The end')

