"""Return consensus sequence"""

import sys
from Bio import SeqIO
from Bio import SeqUtils
from Bio import AlignIO
from Bio.Align import AlignInfo

inFile = sys.argv[1]

alignment = AlignIO.read(inFile, "fasta")

summary_align = AlignInfo.SummaryInfo(alignment)

consensus = summary_align.dumb_consensus(threshold=.01)


my_pssm = summary_align.pos_specific_score_matrix(consensus,
                                                  chars_to_ignore = ['N'])
final_dict = {'A':[],'C':[],'G':[],'T':[]}
consensus = []

for i in my_pssm:
    consensus.append(max(i, key=i.get))
    for key,val in i.items():
        final_dict[key].append(int(val))

print("".join(consensus))

for key,val in final_dict.items():
    print(f'{key}: {" ".join(list(map(str,val)))}')
