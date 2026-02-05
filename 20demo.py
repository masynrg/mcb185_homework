import math

#strings

s = 'hello world'
print(len(s))
print(s.upper())
print(s)
print(f'{1e6 * math.pi:e}')
print(f'{"hello world":>20}')
print(f'{"hello world":.>20}')
print(f'{20:<10} {15}')

#indexing

seq = 'GAATTC'

#prints seq out right to left & ends line:
for nt in seq:
    print(nt, end='')
print()

#each nt a new line:
for nt in seq:
    print(nt)

#goes for length of sequence
#prints number of loop cycle and what is at that position number
for i in range(len(seq)):
    print(i, seq[i])

#slicing

dna = 'ATGCTGTAA'
for i in range(0, len(dna), 3):
    print(i, dna[i:i+3])

#tuples

tax = ('Homo', 'sapiens', 9606)
print(tax)
print(tax[0])
print(tax[::-1])

#enumerate & zip

nts = 'ACGT'
for i in range (len(nts)):
    print(i, nts[i])
for i, nt in enumerate(nts):
    print(i, nt)
names = ('adenine', 'cytosine', 'guanine', 'thymine')
for i in range(len(names)):
    print(nts[i], names[i])
for nt, name in zip(nts, names):
    print(nt, name)