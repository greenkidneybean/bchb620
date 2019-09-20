"""Find all positions of motif in string (including overlap)

`$ python 9.py input.txt > output.txt`

"""

import sys
import re

inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

s = lines[0]
t = lines[1]

print(*[m.start() + 1 for m in re.finditer(f'(?={t})', s)])
