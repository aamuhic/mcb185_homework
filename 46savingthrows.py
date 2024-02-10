# 46savingthrows.py by Amina Muhic

import random

print('\tDC5\tDC10\tDC15')

trials = 10000

# normal
print('normal', end='\t')
for dc in range(5, 16, 5):
	success = 0
	for i in range(trials):
		d = random.randint(1, 20)
		if d >= dc: success += 1
	print(success / trials, end='\t')
print()

# advantage
print('adv', end='\t')
for dc in range(5, 16, 5):
	success = 0
	score = 0
	for i in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 >= d2: score = d1
		else:        score = d2
		if score >= dc: success += 1
	print(success / trials, end='\t')
print()

# disadvantage
print('disadv', end='\t')
for dc in range(5, 16, 5):
	success = 0
	score = 0
	for i in range(trials):
		d1 = random.randint(1, 20)
		d2 = random.randint(1, 20)
		if d1 <= d2: score = d1
		else:        score = d2
		if score >= dc: success += 1
	print(success / trials, end='\t')
print()
		