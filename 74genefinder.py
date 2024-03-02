# 74genefinder.py by Amina Muhic

import sys
import dogma
import mcb185

def get_cds(seq, mini):
	# create dictionary to store gene coordinates
	genes = {}
	
	# find genes in each reading frame (single strand)
	for frame in range(3):
		fseq = seq[frame:]
		i = 0
		while i < len(seq):
			# get start codon
			codon = fseq[i:i+3]
			if codon != 'ATG':
				i += 3
				continue
			start = i + 1 + frame
			# look for stop codon
			for j in range(i, len(seq) - 2, 3):
				codon = fseq[j:j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					stop = j + 3 + frame
					if (stop - start) >= mini:
						genes[start] = stop
					i = j
					break
			i += 3
	return genes

orf = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	rev = dogma.revcomp(seq)
	
	for start, stop in get_cds(seq, orf).items():
		print(f'{name}\t{start}\t{stop}\t+')
	
	for start, stop in get_cds(rev, orf).items():
		beg = len(seq) - stop + 1
		end = len(seq) - start + 1
		print(f'{name}\t{beg}\t{end}\t-')