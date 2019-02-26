def count_a(seq):
    """Counting the number of As in the string"""

    As = 0
    Cs = 0
    Ts = 0
    Gs = 0
    for b in seq:
        if b == 'A':
            As += 1
        if b == 'C':
            Cs += 1
        if b == 'T':
            Ts += 1
        if b == 'G':
            Gs += 1

    return As, Cs, Ts, Gs


# Main program

s = input('Please enter a DNA string: ')
na = count_a(s)
print("The are {} As in the sequence".format(na))

# Calculate the total length
tl = len(s)

print("This sequence is {} bases in length".format(tl))

bases = 'ACTG'
for L in range(len(bases)):
    print('The percentages of', bases[L], 's', 'is {}%'''.format(round(100.0 * na[L] / tl, 1)))
