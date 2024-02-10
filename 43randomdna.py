# 43randomdna.py by Amina Muhic

import random

nseq = 3
for i in range(1, nseq + 1):
	print(f'>seq-{i}')
	
	r = random.randint(50, 60)
	for j in range(r):
		print(random.choice('ACGT'), end='')
	print()