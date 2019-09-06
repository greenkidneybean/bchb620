#!/usr/bin/env python3

import sys
from Bio.Seq import Seq

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

with open(outFile,'w') as o:
    for line in lines:
        trans = Seq(line).transcribe()
        o.write(f"{trans} \n")
        print(trans)