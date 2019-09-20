"""Return consensus sequence"""

import sys
from Bio import SeqIO
from Bio import SeqUtils

inFile = sys.argv[1]

file = list(SeqIO.parse(inFile, "fasta"))
file.sort(key=lambda x: SeqUtils.GC(x.seq), reverse=True)

with open(inFile,'r') as i:
    lines = i.read().splitlines()

# this doesn't seem too pythonic
with open(outFile,'w') as o:
    for line in lines:
        mRNA = Seq(line)
        protein = mRNA.translate()[:-1]
        o.write(f"{protein} \n")
        print(protein)
