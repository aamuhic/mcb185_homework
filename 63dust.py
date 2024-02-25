# 63dust.py by Amina Muhic

import sys
import mcb185
import dogma

fastafile = sys.argv[1]
w = int(sys.argv[2])
ht = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(fastafile):
	print(f'>{defline}')

	# coerce sequence into list to mutate nucleotides
	f = list(seq)

	# mask regions of low complexity
	for i in range(len(seq) - w + 1):
		s = seq[i:i+w]
		h = dogma.entropy(s)
		if h < ht: 
			for j in range(w):
				f[i+j] = 'N'
	filt = ''.join(f)

	# wrap lines
	lines = []
	for i in range(0, len(filt) + 60 - 1, 60):
		wrap = filt[i:i+60]
		lines.append(wrap)

	for line in lines: print(line)

