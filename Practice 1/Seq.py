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


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT", 'tet')
s2 = Seq("CGTAAC", 'ergqrgq')

# Access the attribute strbases for printing the sequence
str1 = s1.strbases
str2 = s2.strbases

print("Sequence 1: {}".format(str1))
print("Sequence 2: {}".format(str2))
print(s1)
print(s2.aldo)
print("Testing the sequence objects")


l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(str1))
print("  Length: {}".format(l1))
print("Sequence 2: {}".format(str2))
print("  Length: {}".format(l2))

al = Seq('AAACCTTGGAA', '')
all = al.compl()
print(all)