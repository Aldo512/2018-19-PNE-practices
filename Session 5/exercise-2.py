def count_a(seq):
    """Counting the number of As in the string"""

    As = 0
    Cs = 0
    Ts = 0
    Gs = 0
    for b in range(len(seq)):
        for a in seq[b]:
            if a == 'A':
                As += 1
            if a == 'C':
                Cs += 1
            if a == 'T':
                Ts += 1
            if a == 'G':
                Gs += 1

    return As, Cs, Ts, Gs


# Main program

s = [input('Please enter a DNA string: '), input('Please enter a second DNA string: ')]

bases = 'ACTG'
l = count_a(s)
for ba in range(len(bases)-2):
    print('The number of', bases[ba], 'in both sequences is', count_a(s[ba]))