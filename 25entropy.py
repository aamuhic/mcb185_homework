# 25entropy.py by Amina Muhic

import math
import sys

def shannon_nt(a, c, g, t):
	tot = a + t + g + c
	if a > 0 and t > 0 and g > 0 and c > 0:
		ai = (a / tot) * math.log2(a / tot)                         
		ci = (c / tot) * math.log2(c / tot)
		gi = (g / tot) * math.log2(g / tot)
		ti = (t / tot) * math.log2(t / tot)
		h = (ai + ci + gi + ti) * -1
		return h
	elif a == 0 or t == 0 or g == 0 or c == 0:
		ap = ((a + 1) / (tot + 4)) * math.log2((a + 1) / (tot + 4)) # pseudo-count
		cp = ((c + 1) / (tot + 4)) * math.log2((c + 1) / (tot + 4))
		gp = ((g + 1) / (tot + 4)) * math.log2((g + 1) / (tot + 4))
		tp = ((t + 1) / (tot + 4)) * math.log2((t + 1) / (tot + 4))
		hp = (ap + cp + gp + tp) * -1
		return hp
	else: sys.exit('error: invalid count(s)')

print(shannon_nt(1, 1, 1, 1))
print(shannon_nt(2, 2, 0, 0))
print(shannon_nt(3, 3, 1, 1))
print(shannon_nt(1, 4, 2, 1))
