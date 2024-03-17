#!/usr/bin/env python3

import argparse

import dogma
import mcb185

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	print(f'>{defline}')
	f = list(seq)
	
	for i in range(len(seq) -arg.size +1):
		s = seq[i:i+arg.size]
		h = dogma.entropy(s)
		if h < arg.entropy:
			for j in range(arg.size):
				if arg.lower: f[i+j] = f[i+j].lower()
				else:         f[i+j] = 'N'
	filt = ''.join(f)
	
	for i in range(0, len(filt), 60):
		wrap = filt[i:i+60]
		print(wrap)