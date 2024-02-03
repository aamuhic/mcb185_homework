# 32fibonacci.py by Amina Muhic

f1 = 0
f2 = 1
print(f1)
print(f2)

for i in range(0, 7):
	fn = f1 + f2
	f1 = f2
	f2 = fn
	print(fn)
	