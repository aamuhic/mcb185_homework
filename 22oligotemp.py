# 22oligotemp.py by Amina Muhic

import math
import sys

def oligotm(a, c, g, t):                                   
	tot = a + t + g + c
	if tot > 13 and g + c < 16.4: sys.exit('low GC content')
	
	if tot <= 13:
		tm1 = (a + t) * 2 + (g + c) * 4
		return tm1
	if tot > 13 and g + c > 16.4:
		tm2 = (64.9 + 41 * (g + c - 16.4)) / tot 
		return tm2
		
print(oligotm(2, 3, 5, 3))
print(oligotm(30, 80, 60, 40))
print(oligotm(9, 8, 9, 8))
print(oligotm(2, 3, 5, 4))
