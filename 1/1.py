#!/usr/bin/env python3

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

# this doesn't seem too pythonic
with open(outFile,'w') as o:
    for line in lines:
        a = line.count("A")
        c = line.count("C")
        g = line.count("G")
        t = line.count("T")
        o.write(f"{a} {c} {g} {t} \n")