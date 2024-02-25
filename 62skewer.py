# 62skewer.py by Amina Muhic & Alexandria Skinner

import sys
import mcb185

fastafile = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(fastafile):
	print(f'>{defline}')
	
	# G and C counts in the first window
	g = seq[:w].count('G')
	c = seq[:w].count('C')
	gc_comp = (g + c) / w
	gc_skew = (g - c) / (g + c)
	print(f'0\t{gc_comp:.3f}\t{gc_skew:.3f}')

	# adjust G and C counts for after each window
	for i in range(len(seq) - w):
		off = seq[i]
		on = seq[i+w]
		if off == 'G': g -= 1
		if off == 'C': c -= 1
		if  on == 'G': g += 1
		if  on == 'C': c += 1
		
		# evaluate GC composition and skew at each window
		gc_comp = (g + c) / w
		if g + c == 0: gc_skew = 0
		else:          gc_skew = (g - c) / (g + c)
		print(f'{i+1}\t{gc_comp:.3f}\t{gc_skew:.3f}')