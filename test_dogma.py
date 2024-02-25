# test_dogma.py by Amina Muhic

import dogma

print(dogma.transcribe('ACGT'))

print(dogma.revcomp('AAAACGT'))

print(dogma.translate('ATGTAA')) # should return M*

s = 'ACGTGGGGGGCATATG'
print(dogma.gc_comp(s))
print(dogma.gc_skew(s), dogma.gc_skew(dogma.revcomp(s)))

print(dogma.entropy('ACGT'))
print(dogma.entropy('GGGGGGGCAA'))
print(dogma.entropy('ACCCGGGA'))

print(dogma.kd_hydropathy('MRVLK'))