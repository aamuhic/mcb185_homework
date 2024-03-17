#!/usr/bin/env python3

import argparse
import gzip

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

features = {}
with gzip.open(arg.gff, 'rt') as fp:
	for line in fp:
		f = line.split()
		chrom = f[0]
		typ = f[2]
		beg = int(f[3])
		end = int(f[4])
		if chrom not in features: features[chrom] = []
		features[chrom].append( (typ, beg, end) )
		
with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		v = line.split()
		chrom = v[0]
		loc = int(v[1])
		
		fts = []
		for t, b, e in features[chrom]:
			if loc >= b and loc <= e +1:
				if t not in fts: 
					fts.append(t)
		if len(fts) < 1: continueq
		
		print(chrom, end='\t')
		print(loc, end='\t')
		for ft in fts: print(ft, end=' ')
		print()
		



