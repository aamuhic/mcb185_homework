# 53genomestats.py

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

lengths = []
with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		words = line.split()
		if words[2] != feature: continue		
		beg = int(words[3])
		end = int(words[4])
		l = end - beg +1
		lengths.append(int(l))
	
mini = lengths[0]
maxi = lengths[0]
for length in lengths:
	if length < mini: mini = length
	if length > maxi: maxi = length	

sum_l = 0
for length in lengths:
	sum_l += length
mean = sum_l / len(lengths)

totdv = 0
for length in lengths:
	dv = (length - mean)**2
	totdv += dv
stdv = math.sqrt(totdv / len(lengths))


lengths.sort()
x1 = lengths[len(lengths) // 2 - 1] # fix
x2 = lengths[len(lengths) // 2]     # fix, check
if math.isclose(len(lengths) % 2, 0):
	median = (x1 + x2) / 2
else:
	median = x2


print(len(lengths))     # number of observations
print(mini)             # minimum
print(maxi)             # maximum
print(round(mean))      # mean, rounded
print(round(stdv))      # standard deviation, rounded
print(round(median))    # median, rounded
