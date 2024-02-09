# 47deathsaves.py by Amina Muhic

import random

trials = 10000

stable = 0
death = 0
revive = 0
for i in range(trials):
	failure = 0
	success = 0
	while True: 
		d = random.randint(1, 20)
		if d == 1:
			failure += 2
		elif d < 10:
			failure += 1
		elif d < 20:
			success += 1
		else: 
			revive += 1
			break
			
		if failure >= 3:
			death += 1
			break
		
		if success >= 3:
			stable += 1
			break
		
print('death\t', death / trials)
print('stable\t', stable / trials)
print('revive\t', revive / trials)
