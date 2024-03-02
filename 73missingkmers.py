# 73missingkmers.py by Amina Muhic

import sys
import mcb185
import dogma
import itertools

kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	print(f'>{defline}')
	rev = dogma.revcomp(seq)
	
	for k in range(len(seq)):
		for i in range(len(seq) -k +1):
			kmerpos = seq[i:i+k]
			if kmerpos not in kcount: kcount[kmerpos] = 0
			kcount[kmerpos] += 1
			
			kmerneg = rev[i:i+k]
			if kmerneg not in kcount: kcount[kmerneg] = 0
			kcount[kmerneg] += 1
		
		n = 0
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount: n += 1
			
		if n >= 1:
			print(f'k={k} n={n}')
			break