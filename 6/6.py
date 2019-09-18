#!/usr/bin/env python3
"""Return Hamming Distance for two strings of equal length

Hamming Distance - counting the number of bases at which two strings differ
"""

import sys
from Bio import SeqIO
from Bio import SeqUtils

inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

ham = 0
for x,y in zip(lines[0], lines[1]):
    if x != y:
        ham += 1
print(ham)
