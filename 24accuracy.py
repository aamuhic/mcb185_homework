# 24accuracy.py by Amina Muhic

import math
import sys

def performance(tp, fp, tn, fn):
	acc = (tp + tn) / (tp + tn + fp + fn)
	p = tp / (tp + fp)
	r = tp / (tp + fn)
	f1 = (2 * p * r) / (p + r)
	return acc, f1
	
print(performance(15, 20, 25, 30))
print(performance(160, 80, 70, 210))
print(performance(200, 0, 62, 30))
print(performance(11, 12, 0, 9))
print(performance(2, 45, 800, 0))

