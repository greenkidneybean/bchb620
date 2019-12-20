

from Bio import SeqIO
import os
import re
import sys
from urllib.request import urlopen

inFile = sys.argv[1]

# lines is the  list
with open(inFile,'r') as i:
   ID = i.read().splitlines()



for i in range(len(ID)):
   URL = 'http://www.uniprot.org/uniprot/' + ID[i] + '.fasta'
   data = urlopen(URL)
   fasta = data.read().decode('utf-8', 'ignore')
   with open('seq_file.fasta', 'a') as text_file:
       text_file.write(fasta)

handle = open('seq_file.fasta', 'r')
motifs = re.compile(r'(?=(N[^P][ST][^P]))')

for id, record in zip(ID, SeqIO.parse(handle, 'fasta')):
   seq = str(record.seq)
   positions = []
   for m in re.finditer(motifs, seq):
       positions.append(m.start() + 1)
   if len(positions) > 0:
       print(id)
       print(" ".join(str(x) for x in positions))
