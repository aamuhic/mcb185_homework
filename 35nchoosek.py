# 35nchoosek.py by Amina Muhic

def factorial(i):
	if i == 0: return 1
	fac = 1
	for j in range(1, i+1):
		fac = fac * j
	return fac

def nchoosek(n, k):
	nck = factorial(n) / (factorial(k) * factorial(n - k))
	return nck

print(nchoosek(0, 0))
print(nchoosek(1, 0))
print(nchoosek(1, 1))
print(nchoosek(2, 1))
print(nchoosek(3, 2))
print(nchoosek(4, 3))
print(nchoosek(4, 2))
