# 56birthdays.py by Amina Muhic

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0
for t in range(trials):

	# collect all birthdays from class
	birthdays = []
	for b in range(people):
		bd = random.randint(1, days)
		birthdays.append(bd)

	# check birthdays for duplicates
	shared = False
	for i in range(len(birthdays)):
		for j in range(i + 1, len(birthdays)):
			if birthdays[i] == birthdays[j]:
				shared = True
				break
	if shared: success += 1
		
print(success / trials)