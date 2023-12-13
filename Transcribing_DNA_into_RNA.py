import pandas as pd

with open(r'c:\Users\crobbins\Downloads\rosalind_rna.txt') as f:
    txt = f.read()

rna = txt.replace('T', 'U')

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(rna)
