# 45dndstats.py by Amina Muhic

import random

trials = 10000

# 3D6
total_3d6 = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		score += d
	total_3d6 += score
print('3D6\t', total_3d6 / trials)


# 3D6r1
total_3d6r1 = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1: d = random.randint(1, 6) 
		score += d
	total_3d6r1 += score
print('3D6r1\t', total_3d6r1 / trials)

# 3D6x2
total_3d6x2 = 0
for i in range(trials):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 >= d2: score += d1
		if d1 < d2:  score += d2
	total_3d6x2 += score
print('3D6x2\t', total_3d6x2 / trials)

# 4D6d1
total_4d6d1 = 0
for i in range(trials):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	sum_d = d1 + d2 + d3 + d4
	if d1 <= d2 and d1 <= d3 and d1 <= d4:   score += sum_d - d1
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: score += sum_d - d2
	elif d3 <= d1 and d3 <= d2 and d3 <= d4: score += sum_d - d3
	else:                                    score += sum_d - d4
	total_4d6d1 += score
print('4D6d1\t', total_4d6d1 / trials)