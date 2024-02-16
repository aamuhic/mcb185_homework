# 50demo.py by Amina Muhic

import math

seq = 'GAATTC'
print(seq[0], seq[1])
print(seq[-1])

for nt in seq: print(nt, end='')
print()

for i in range(len(seq)):
	print(i, seq[i])

s = 'ABCDEFGHIJ'
print(s[0:5])
print(s[0:8:2])
print(s[0:5], s[:5])      # both ABCDE
print(s[5:len(s)], s[5:]) # both FGHIJ

print(s, s[::], s[::1], s[::-1])

tax = ('Homo', 'sapiens', 9606)
print(tax)

"""
s[0] = 'C'
tax[0] = 'human'
# can't change contents of tuples/strings by poking indices
"""

print(tax[0])
print(tax[::-1])

def quadratic(a, b, c):
	x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
	x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
	return x1, x2

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)                       # pretty
intercepts = quadratic(5, 6, 1)
print(intercepts[0], intercepts[1]) # ugly

nts = 'ACGT'
for i in range(len(nts)):    # messier
	print(i, nts[i])

for i, nt in enumerate(nts): # tidier
	print(i, nt)

i = 0
for nt in nts:               # messiest
	print(i, nt)
	i += 1

names = ('adenine', 'cytosine', 'guanine', 'thymine') # messier
for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names):                      # tidier
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)):
	print(i, nt, name)

nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C')
print(nts)

last = nts.pop()
print(last)

nts.sort()
print(nts)
nts.sort(reverse=True)
print(nts)

nucleotides = nts
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides)

items = list()
print(items)
items.append('eggs')
print(items)

stuff = []
stuff.append(3)
print(stuff)

alph = 'ABCDEFGHIJKLMNOPQRSTUVW'
print(alph)
aas = list(alph)
print(aas)

text = 'good day    to you'
words = text.split()
print(words)

line = '1.41,2.72,3.14'
print(line.split(','))

s = '-'.join(aas)
print(s)
s = ''.join(aas)
print(s)

if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
# print('index Z?', alph.index('Z'))

print('find G?', alph.find('G'))
print('find Z?', alph.find('Z'))

# if thing in list: idx = list.index(thing)

# Practice Problems

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
print(minimum([3, 1, 2]))

def minimaxi(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
print(minimaxi([3, 1, 2]))

def mean(vals):
	sum = 0
	for val in vals:
		sum += val
	mean = sum / len(vals)
	return mean

def entropy(probs):
	h = 0
	for prob in probs:
		h -= probs * math.log2(probs)
	return h

def kullbackleibler(P, Q):
	dist = 0
	for p, q in zip(P, Q):
		dist += p * math.log2(p / q)
	return dist
p1 =[0.4, 0.3, 0.2, 0.1]
p2 = (0.1, 0.3, 0.4, 0.2)
print(kullbackleibler(p1, p2))

"""
with open(path) as fp:
	for line in fp:
		do_something_with(line)
"""

"""
import gzip
with gzip.open(path, 'rt') as fp:
	for line in fp:
		print(line, end='')
"""

i = int('42')
x = float('0.61803')