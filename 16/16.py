from Bio import SeqIO
import os
import re
import sys

inFile = sys.argv[1]

# lines is the  list
with open(inFile,'r') as i:
    lines = i.read().splitlines()

for i in lines:
    os.system(f'wget http://www.uniprot.org/uniprot/{i}.fasta')

for i in lines:
    for record in SeqIO.parse(f"{i}.fasta", "fasta"):
        match = 0
        match = [m.start()+1 for m in re.finditer('(?=(N[^P][ST][^P]))', str(record.seq))]
        if len(match) > 0:
            print(i)
            print(" ".join(str(x) for x in match))
