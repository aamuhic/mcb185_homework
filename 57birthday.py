# 57birthday.py by Amina Muhic

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0
for t in range(trials):

	# create an empty calendar
	cal = []
	for i in range(days):
		cal.append(0)

	# fill with dates
	shared = False
	for j in range(people):
		d = random.randint(0, days - 1)
		cal[d] += 1
		if cal[d] >= 2:
			shared = True
			break
	if shared: success += 1

print(success / trials)


	
