# 21quadratic.py by Amina Muhic

import math
import sys

def quadratic_formula(a, b, c):
	d = b**2 - 4*a*c
	if d < 0: 
		return None, None
	if d >= 0:
		x1 = (-b + math.sqrt(d)) / (2 * a)
		x2 = (-b - math.sqrt(d)) / (2 * a)
		return x1, x2

print(quadratic_formula(1, 3, -4))
print(quadratic_formula(9, -12, 4))
print(quadratic_formula(1, 2, 1))
print(quadratic_formula(1, 4, 5))
