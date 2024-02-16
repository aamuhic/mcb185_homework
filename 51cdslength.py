# 51cdslength.py by Amina Muhic

import gzip

path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gg.gz'
with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words =line.split()
		if words[2] != 'CDS': continue
		beg = words[3]
		end = words[4]
		print(end - beg + 1)