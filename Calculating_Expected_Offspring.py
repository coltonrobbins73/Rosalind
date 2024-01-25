import pandas as pd
import re

def parse_fasta(txt):
    """Parse FASTA formatted data and return a dictionary of sequences."""
    seqs = txt[1:].split('>')

    seq_dict = {}
    for seq in seqs:
        split_seq = seq.split('\n', 1)
        seq_dict[split_seq[0]] = split_seq[1].replace('\n', '')
    
    return seq_dict

with open(r'c:\Users\colto\Downloads\rosalind_iev.txt') as f:
    txt = f.read()

geno_pairs = txt.split(' ')

geno_pairs = [int(item) for item in geno_pairs]

projected_dom_offspring_rate = {
    0 : 2,
    1 : 2,
    2 : 2,
    3 : 1.5,
    4 : 1,
    5 : 0,
}

total_dom_offspring_list = []
for count, geno_value in enumerate(geno_pairs):
    total_dom_offspring_list.append(projected_dom_offspring_rate[count] * geno_pairs[count])

print(sum(total_dom_offspring_list))

