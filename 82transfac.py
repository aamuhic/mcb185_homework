# 82transfac.py by Amina Muhic

import gzip
import json
import re
import sys

tf_list = []
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		
		if f[0] == 'ID': 
			tf = f[1]
			record = {
				'id': tf,
				'pwm': []
			}
			tf_list.append(record)
			
		if re.search('[0123456789]', f[0]):
			a = float(f[1])
			c = float(f[2])
			g = float(f[3])
			t = float(f[4])
			counts = {
				'A': a,
				'C': c,
				'G': g,
				'T': t
			}
			record['pwm'].append(counts)

print(json.dumps(tf_list, indent=4))
	
	