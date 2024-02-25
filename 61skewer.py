# 61skewer.py by Amina Muhic

import sys
import mcb185
import dogma

fastafile = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fastafile):
	print(f'>{defline}')

	for i in range(len(seq) -w + 1):
		s = seq[i:i+w]
		print(f'{i}\t{dogma.gc_comp(s):.3f}\t{dogma.gc_skew(s):.3f}')
