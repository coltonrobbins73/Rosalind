import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_prot (1).txt') as f:
    txt = f.read()


seqs = txt[1:].split('>')

seq_dict = {}
for seq in seqs:
    split_seq = seq.split('\n', 1)
    seq_dict[split_seq[0]] = split_seq[1].replace('\n', '')


with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(protein_seq)


print(protein_seq)
