import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_prot (1).txt') as f:
    txt = f.read()


with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(protein_seq)


print(protein_seq)
