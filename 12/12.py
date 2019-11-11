import sys
from Bio import SeqIO

inFile = sys.argv[1]
k = 3

seq_dict =  SeqIO.to_dict(SeqIO.parse(inFile, "fasta"))

for key in seq_dict.keys():
    pop_dict = seq_dict.copy()
    val = pop_dict.pop(key)
    suffix = val.seq[-k:]
    for sub_key,sub_val in pop_dict.items():
        if suffix == sub_val.seq[:k]:
            print(key, sub_key)
