# 33triples.py by Amina Muhic

import math

limit = 100
for a in range(1, limit):
	for b in range(a, limit):
		c = math.sqrt(a**2 + b**2)
		if c // 1 == c: print(a, b, c)
