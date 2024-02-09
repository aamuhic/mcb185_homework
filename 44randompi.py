# 44randompi.py by Amina Muhic

import random
import math

incircle = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	d = math.sqrt(x**2 + y**2)
	
	total += 1
	if d < 1: incircle += 1
	print(4 * incircle / total)
