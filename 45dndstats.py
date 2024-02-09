# 45dndstats.py by Amina Muhic

import random

rolls = 10000

# 3D6
total_3d6 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
	total_3d6 += score
print('3D6\t', total_3d6 / rolls)


# 3D6r1
total_3d6r1 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1: d = random.randint(1, 6) 
		score += d
	total_3d6r1 += score
print('3D6r1\t', total_3d6r1 / rolls)

# 3D6x2
total_3d6x2 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: score += d1
		if d1 < d2:  score += d2
	total_3d6x2 += score
print('3D6x2\t', total_3d6x2 / rolls)

# 4D6d1
total_4d6d1 = 0
for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4:   score += d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score += d1 + d3 + d4
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score += d1 + d2 + d4
	else:                                    score += d1 + d2 + d3
	total_4d6d1 += score
print('4D6d1\t', total_4d6d1 / rolls)