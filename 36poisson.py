# 36poisson.py by Amina Muhic

import math

def factorial(i):
	if i == 0: return 1
	fac = 1
	for j in range(1, i+1):
		fac = fac * j
	return fac

def poisson_p(n, k):
	prob = n**k * math.e**-n / factorial(k)
	return prob


print(poisson_p(2, 3))
print(poisson_p(5, 5))
print(poisson_p(10, 5))
print(poisson_p(4, 0))
print(poisson_p(1, 1))