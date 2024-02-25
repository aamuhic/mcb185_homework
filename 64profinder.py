# 64profinder.py by Amina Muhic

import sys
import mcb185
import dogma

fastafile = sys.argv[1]
mini = int(sys.argv[2])

# function to find proteins
def get_pro(seq, minsize):
	proteins = []
	for orf in dogma.translate(seq).split('*'):
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			if len(protein) >= minsize: 
				proteins.append(protein)
	return proteins

for defline, seq in mcb185.read_fasta(fastafile):
	defwords = defline.split()
	name = defwords[0]
	
	# store the reverse complement
	rev = dogma.revcomp(seq)

	# find proteins in each reading frame
	id = 0
	for i in range(3):
		for protein in get_pro(seq[i:], mini):
			print(f'>{name}-prot-{id}')
			print(protein)
			id += 1
		for protein in get_pro(rev[i:], mini):
			print(f'>{name}-prot-{id}')
			print(protein)
			id += 1