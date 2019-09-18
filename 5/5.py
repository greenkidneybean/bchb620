#!/usr/bin/env python3

import sys
from Bio import SeqIO
from Bio import SeqUtils

inFile = sys.argv[1]

file = list(SeqIO.parse(inFile, "fasta"))
file.sort(key=lambda x: SeqUtils.GC(x.seq), reverse=True)

print(file[0].id)
print(SeqUtils.GC(file[0].seq))
