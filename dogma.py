# dogma.py by Amina Muhic

import math

def transcribe(dna):
	return dna.replace('T', 'U')

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else:           rc.append('N')
	return ''.join(rc)

def translate(dna):
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if   codon == 'ATG': aas.append('M')
		elif codon == 'TTT': aas.append('F')
		elif codon == 'TTC': aas.append('F')
		elif codon == 'TTA': aas.append('L')
		elif codon == 'TTG': aas.append('L')
		elif codon == 'CTT': aas.append('L')
		elif codon == 'CTC': aas.append('L')
		elif codon == 'CTA': aas.append('L')
		elif codon == 'CTG': aas.append('L')
		elif codon == 'TCT': aas.append('S')
		elif codon == 'TCC': aas.append('S')
		elif codon == 'TCA': aas.append('S')
		elif codon == 'TCG': aas.append('S')
		elif codon == 'AGT': aas.append('S')
		elif codon == 'AGC': aas.append('S')
		elif codon == 'TAT': aas.append('Y')
		elif codon == 'TAC': aas.append('Y')
		elif codon == 'TGT': aas.append('C')
		elif codon == 'TGC': aas.append('C')
		elif codon == 'TGG': aas.append('W')
		elif codon == 'CCT': aas.append('P')
		elif codon == 'CCC': aas.append('P')
		elif codon == 'CCA': aas.append('P')
		elif codon == 'CCG': aas.append('P')
		elif codon == 'CAT': aas.append('H')
		elif codon == 'CAC': aas.append('H')
		elif codon == 'CAA': aas.append('Q')
		elif codon == 'CAG': aas.append('Q')
		elif codon == 'CGT': aas.append('R')
		elif codon == 'CGC': aas.append('R')
		elif codon == 'CGA': aas.append('R')
		elif codon == 'CGG': aas.append('R')
		elif codon == 'AGA': aas.append('R')
		elif codon == 'AGG': aas.append('R')
		elif codon == 'ATT': aas.append('I')
		elif codon == 'ATC': aas.append('I')
		elif codon == 'ATA': aas.append('I')
		elif codon == 'ACT': aas.append('T')
		elif codon == 'ACC': aas.append('T')
		elif codon == 'ACA': aas.append('T')
		elif codon == 'ACG': aas.append('T')
		elif codon == 'AAT': aas.append('N')
		elif codon == 'AAC': aas.append('N')
		elif codon == 'AAA': aas.append('K')
		elif codon == 'AAG': aas.append('K')
		elif codon == 'GTT': aas.append('V')
		elif codon == 'GTC': aas.append('V')
		elif codon == 'GTA': aas.append('V')
		elif codon == 'GTG': aas.append('V')
		elif codon == 'GCT': aas.append('A')
		elif codon == 'GCC': aas.append('A')
		elif codon == 'GCA': aas.append('A')
		elif codon == 'GCG': aas.append('A')
		elif codon == 'GAT': aas.append('D')
		elif codon == 'GAC': aas.append('D')
		elif codon == 'GAA': aas.append('E')
		elif codon == 'GAG': aas.append('E')
		elif codon == 'GGT': aas.append('G')
		elif codon == 'GGC': aas.append('G')
		elif codon == 'GGA': aas.append('G')
		elif codon == 'GGG': aas.append('G')
		elif codon == 'TAA': aas.append('*')
		elif codon == 'TAG': aas.append('*')
		elif codon == 'TGA': aas.append('*')
		else:                aas.append('X')
	return ''.join(aas)

def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)

def entropy(seq):
	counts = [0] * 4
	counts[0] = seq.count('A')
	counts[1] = seq.count('C')
	counts[2] = seq.count('G')
	counts[3] = seq.count('T')

	h = 0
	for i in range(len(counts)):
		p = counts[i] / sum(counts)
		if p != 0: h -= p * math.log2(p)
	return h

def kd_hydropathy(seq):
	score = 0
	for i in range(len(seq)):
		if seq[i] == 'I': score += 4.5
		if seq[i] == 'V': score += 4.2
		if seq[i] == 'L': score += 3.8
		if seq[i] == 'F': score += 2.8
		if seq[i] == 'C': score += 2.5
		if seq[i] == 'M': score += 1.9
		if seq[i] == 'A': score += 1.8
		if seq[i] == 'G': score += -0.4
		if seq[i] == 'T': score += -0.7
		if seq[i] == 'S': score += -0.8
		if seq[i] == 'W': score += -0.9
		if seq[i] == 'Y': score += -1.3
		if seq[i] == 'P': score += -1.6
		if seq[i] == 'H': score += -3.2
		if seq[i] == 'E': score += -3.5
		if seq[i] == 'Q': score += -3.5
		if seq[i] == 'D': score += -3.5
		if seq[i] == 'N': score += -3.5
		if seq[i] == 'K': score += -3.9
		if seq[i] == 'R': score += -4.5
		else:             score += 0
	return score / len(seq)
