#!/usr/bin/env python3

import argparse

import dogma
import mcb185

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
	help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true',
	help='also examine the anti-parallel strand')
arg = parser.parse_args()

def get_pro(seq, minsize):
	proteins = []
	for frame in range(3):
		fseq = seq[frame:]
		for orf in dogma.translate(fseq).split('*'):
			if 'M' in orf:
				start = orf.find('M')
				protein = orf[start:]
				if len(protein) >= minsize:
					proteins.append(protein)
	return proteins

for defline, seq in mcb185.read_fasta(arg.file):
	rev = mcb185.anti_seq(seq)
	proteins = []
	for pro in get_pro(seq, arg.min):
		proteins.append(pro)
	if arg.anti:
		for pro in get_pro(rev, arg.min): 
			proteins.append(pro)
	
	if len(proteins) < 1: continue
	
	print(f'>{defline}')
	maxpro = proteins[0]
	for protein in proteins[1:]:
		if len(protein) > len(maxpro): 
			maxpro = protein
	for i in range(0, len(maxpro), 60):
		wrap = maxpro[i:i+60]
		print(wrap)
	
	