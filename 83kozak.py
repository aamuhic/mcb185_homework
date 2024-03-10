# 83kozak.py by Amina Muhic

import gzip
import sys

import mcb185

genome = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('ORIGIN'): break
	for line in fp:
		words = line.split()
		for word in words[1:]:
			genome.append(word.upper())
seq = ''.join(genome)

		
kozaks = []
klen = 14
for i in range(klen):
	kozaks.append({'A':0, 'C':0, 'G':0, 'T':0})

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[0] != 'CDS': continue
		if 'join' in f[1]: continue
		
		if 'complement' in f[1]:
			p1 = f[1].index('(') + 1
			p2 = f[1].index(')')
			coor = f[1][p1:p2]
			beg = int(coor.split('..')[1])
			kseq = mcb185.anti_seq(seq[beg-5:beg+9])
		else:
			coor = f[1]
			beg = int(coor.split('..')[0])
			kseq = seq[beg-10:beg+4]

		for i, nt in enumerate(kseq):
			kozaks[i][nt] += 1

print('AC IMTSU001')
print('XX')
print('ID ECKOZ')
print('XX')
print('DE E. coli Kozak sequence')
print('PO      ', end='')
print('A       ', end='')
print('C       ', end='')
print('G       ', end='')
print('T       ', end='')
print()
for i, n in enumerate(kozaks):
	a = n['A']
	c = n['C']
	g = n['G']
	t = n['T']
	print(f'{i+1:<8}{a:<8}{c:<8}{g:<8}{t:<8}')