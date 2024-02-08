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

with open(r'c:\Users\colto\Downloads\rosalind_grph (1).txt') as f:
    txt = f.read()

    seq_dict = parse_fasta(txt)


overlap = 3

prefix = {}
suffix = {}

for seq in seq_dict:
    seq_len = len(seq_dict[seq])
    prefix[seq] = seq_dict[seq][0:overlap]
    suffix[seq] = seq_dict[seq][seq_len-overlap:seq_len]


edge_list = []
for pre in prefix:
    for suf in suffix:
        if pre == suf:
            continue
        if prefix[pre] == suffix[suf]:
            edge_list.append(suf + ' ' + pre)

for i in edge_list:
    print(i)
 