# 30demo.py by Amina Muhic

import math

"""
while True:
	print('hello')
"""

i = 0
while True:
	i = i + 1
	print('hey', i)
	if i == 3: break

i = 0
while i < 3:
	print(i)
	i = i + 1
print('final value of i is', i)


i = 1
while i < 10:
	print(i)
	i = i + 3
print('final value of i is', i)

for i in range(1, 10, 3):
	print(i)

for i in range(0, 5):
	print(i)

for i in range(5):
	print(i)

for char in 'hello':
	print(char)

seq = 'GAATTC'
for nt in seq:
	print(nt)

nts = 'ACGT'	
for nt1 in nts:
	for nt2 in nts:
		if nt1 == nt2: print(nt1, nt2, '+1')
		else:          print(nt1, nt2, '-1')

limit = 4                                 # full matrix
for i in range(0, limit):
	for j in range(0, limit):             # inner loop starts at 0
		print(i+1, j+1)

limit = 4                                 # half matrix + major diagonal
for i in range(0, limit):
	for j in range(i, limit):             # inner loop starts at i
		print(i+1, j+1)

limit = 4                                 # half matrix - major diagonal
for i in range(0, limit):
	for j in range(i+1, limit):           # inner loop starts at i + 1
		print(i+1, j+1)

limit = 4
for i in range(0, limit):                 # full matrix - major diagonal
	for j in range(0, limit):
		if i != j: print(i+1, j+1)

def gc_comp(seq):
	gc_count = 0
	total = 0
	for nt in seq:
		if nt == 'C' or nt == 'G':
			gc_count = gc_count + 1
		total = total + 1
	return gc_count / total

print(gc_comp('ACAGCGAAT'))

# practice

def ntriangular(n):
	number = 0
	for i in range(n+1):
		number = number + i
	return number

print(ntriangular(3))

def factorial(n):
	if n == 0: return 1
	number = 1
	for i in range(1, n+1):
		number = number * i
	return number

print(factorial(4))

limit = 1000
def euler(limit):
	e = 0
	for n in range(limit):
		e = e + 1 / factorial(n)
	return e

print(euler(10))

def is_perfsquare(n):
	root = math.sqrt(n)
	if math.isclose(root, root // 1): return True
	return False
	
print(is_perfsquare(7))
print(is_perfsquare(9))

def is_prime(n):
	if n == 1: return False
	for i in range(2, n//2):
		if n % i == 0: return False
	return True
	
print(is_prime(13))
print(is_prime(14))
print(is_prime(1))

limit = 4
for i in range(0, limit):
	for j in range(0, limit):
		print(i+1, j+1)

