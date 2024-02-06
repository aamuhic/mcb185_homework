# 38quiz.py by Amina Muhic, Francesa C. Gasperini, and Isha Suba

for i in range(1, 7, 2):
	d = i + 2
	print(d)

sign = 1
for i in range(1, 7, 2):
	sign = sign * -1
	print(sign)
	
pi = 1
sign = 1
for i in range(1, 3, 2):
	sign = sign * -1
	d = i + 2
	pi = pi + (1 / d) * sign
print(4 * pi)
