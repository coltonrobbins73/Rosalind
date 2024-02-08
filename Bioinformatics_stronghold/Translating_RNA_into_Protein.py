import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_prot (1).txt') as f:
    txt = f.read()

lookup_table = pd.read_excel(r'C:\Users\crobbins\OneDrive - Fred Hutchinson Cancer Research Center\Python\Rosalind\Codon_lookup.xlsx', engine = 'openpyxl')

lookup_dict = pd.Series(lookup_table.Symbol.values, index = lookup_table.Codon).to_dict()

txt = txt.replace('\n', '')

n = 3
codon_split = [txt[i:i+n] for i in range(0, len(txt), n)]

protein_seq = [lookup_dict[codon] for codon in codon_split]
protein_seq = ''.join(protein_seq)

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(protein_seq)


print(protein_seq)
