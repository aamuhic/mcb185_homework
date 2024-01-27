# 23hydropathy.py by Amina Muhic

import sys

def kd_hydropathy(aa):
	if aa == 'i': return 4.5
	if aa == 'v': return 4.2
	if aa == 'l': return 3.8
	if aa == 'f': return 2.8
	if aa == 'c': return 2.5
	if aa == 'm': return 1.9
	if aa == 'a': return 1.8
	if aa == 'g': return -0.4
	if aa == 't': return -0.7
	if aa == 's': return -0.8
	if aa == 'w': return -0.9
	if aa == 'y': return -1.3
	if aa == 'p': return -1.6
	if aa == 'h': return -3.2
	if aa == 'e': return -3.5
	if aa == 'q': return -3.5
	if aa == 'd': return -3.5
	if aa == 'n': return -3.5
	if aa == 'k': return -3.9
	if aa == 'r': return -4.5
	return sys.exit('unknown amino acid')
	
print(kd_hydropathy('f'))
print(kd_hydropathy('t'))
print(kd_hydropathy('k'))
print(kd_hydropathy('y'))
print(kd_hydropathy('b'))