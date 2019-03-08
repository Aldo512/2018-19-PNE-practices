class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

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

