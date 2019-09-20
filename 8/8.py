"""Return translation of mRNA  sequence"""

import sys
from Bio.Seq import Seq

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

# this doesn't seem too pythonic
with open(outFile,'w') as o:
    for line in lines:
        mRNA = Seq(line)
        protein = mRNA.translate()[:-1]
        o.write(f"{protein} \n")
        print(protein)
