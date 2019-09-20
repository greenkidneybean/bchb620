"""Return probability of progeny with dominant allele"""

import sys

inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.read().splitlines()

# probability function
def dom_allele_prob(k,m,n):
    pop = (k+m+n)
    tot_prog = (pop * (pop -1)) * 4

    # Aa x Aa
    Aa_Aa = ((m * (m-1)) * 4) * .25
    # Aa x aa
    Aa_aa = (((m * n) * 4) * 2 ) * .5
    # aa x aa
    aa_aa = ((n * (n-1)) * 4) * 1

    dom_allele = tot_prog - (Aa_Aa + Aa_aa + aa_aa)
    dom_prob = dom_allele/tot_prog
    print(dom_prob)

# iterate thru input file
for line in lines:
    k,m,n = [int(i) for i in line.split(" ")]
    dom_allele_prob(k,m,n)
