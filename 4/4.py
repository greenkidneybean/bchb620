#!/usr/bin/env python3

import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def rabbits(n,k):
    if n <= 1:
        return n
    else:
        return(rabbits(n-1,k) + (rabbits(n-2,k)*k))
 

with open(inFile,'r') as i:
    lines = i.read().splitlines()

# this doesn't seem too pythonic
with open(outFile,'w') as o:
    for line in lines:
        elements = line.split(" ")
        n = int(elements[0])
        k = int(elements[1])
        value = str(rabbits(n,k))
        o.write(f"{value} \n")
        print(value)