# 70demo.py by Amina Muhic

import itertools

emptyd = {}
emptyd = dict()

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat'])

d['pig'] = 'oink'
print(d)

d['cat'] = 'mew'
print(d)

del d['cat']
print(d)

"""
print(d['rat']) # gives error, not in dict
"""

if 'dog' in d: print(d['dog'])

for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v)        # always unpack tuples

for thing in d.items(): print(thing[0], thing[1]) # unpacked and ugly

print(d.keys(), d.values(), list(d.values()))

kdtable = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M':  1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
	kd = 0
	for aa in seq: kd += kdtable[aa]
	return kd / len(seq)

print(kd_dict('MHKL'))

"""
count = {}
for nt in seq:
	if nt not in count: count[nt] = 0
	count[nt] += 1
"""
	
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)