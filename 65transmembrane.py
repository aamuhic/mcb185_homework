# 65transmembrane.py by Amina Muhic

import sys
import mcb185
import dogma

profile = sys.argv[1]

# function to find proteins with hydrophobic alpha helix
def is_hpa(seq, winsize, threshold):
	alphahelix = False
	for i in range(len(seq) - winsize + 1):
		w = seq[i:i+winsize]
		kd = dogma.kd_hydropathy(w)
		if kd >= threshold and 'P' not in w: 
			return True
	return False

for defline, seq in mcb185.read_fasta(profile):
	# find proteins with ER localization signal and transmembrane domain
	nterm = seq[:30]
	cterm = seq[30:]
	if is_hpa(nterm, 8, 2.5) and is_hpa(cterm, 11, 2):
		print(defline)
