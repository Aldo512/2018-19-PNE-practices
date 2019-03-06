def count_a(seq):
    """Counting the number of As in the string"""

    As = 0
    Cs = 0
    Ts = 0
    Gs = 0

    for a in seq:
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

first = input('Enter the first DNA string:')
f = count_a(first)
sec = input('Enter the second DNA string:')
s = count_a(sec)

# Calculate the total length
ft = len(first)

bases = 'ACTG'
for L in range(len(bases)):
    print('The percentages of', bases[L], 'in the first string', 'is {}%'''.format(round((100.0 * f[L]) / ft, 1)))

for L in range(len(bases)):
    print('The percentages of', bases[L], 'in the second string', 'is {}%'''.format(round((100.0 * s[L]) / ft, 1)))