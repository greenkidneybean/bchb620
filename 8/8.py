"""Return translation of mRNA  sequence"""

import sys
from Bio.Seq import Seq

inFile = sys.argv[1]
#outFile = sys.argv[2]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

for line in lines:
    mRNA = Seq(line)
    print(mRNA.translate()[:-1])
    print()
