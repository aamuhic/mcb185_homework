# 37nilakantha.py by Amina Muhic
 
pi = 3
for i in range(1, 100):
	n1 = i * 2
	n2 = n1 + 1
	n3 = n1 + 2
	d = n1 * n2 * n3
	if i % 2 == 0:  pi = pi - 4 / d
	else:           pi = pi + 4 / d
print(pi)
