# 84splicesites.py by Amina Muhic

import gzip
import json
import sys

import mcb185

introns = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		if f[2] != 'intron': continue
		chrom = f[0]
		beg = int(f[3]) - 1
		end = int(f[4]) - 1
		strand = f[6]
		n = int(f[5])
		introns.append( (chrom, beg, end, strand, n) )

dons = []
accs = []
dlen = 6
alen = 8
for i in range(dlen):
	dons.append( {'A':0, 'C':0, 'G':0, 'T':0} )
for i in range(alen):
	accs.append( {'A':0, 'C':0, 'G':0, 'T':0} )

for defline, seq in mcb185.read_fasta(sys.argv[2]):
	words = defline.split()
	chrom = words[0]
	for c, b, e, s, n in introns:
		if chrom == c:
			iseq = seq[b:e+1]
			if s == '-': iseq = mcb185.anti_seq(iseq)
			don = iseq[:6]
			acc = iseq[-8:]
			
			for i, nt in enumerate(don):
				dons[i][nt] += n
			for i, nt in enumerate(acc):
				accs[i][nt] += n

def print_pwm(pwm, ac, name, de):
	print('AC', ac)
	print('XX')
	print('ID', name)
	print('XX')
	print('DE', de)
	print('A       ', end='')
	print('C       ', end='')
	print('G       ', end='')
	print('T       ', end='')
	print()
	for i, n in enumerate(pwm):
		a = n['A']
		c = n['C']
		g = n['G']
		t = n['T']
		print(f'{i+1:<8}{a:<8}{c:<8}{g:<8}{t:<8}')

print_pwm(dons, 'DEMO1', 'ACC', 'splice acceptor')
print_pwm(accs, 'DEMO2', 'DON', 'splice donor')
