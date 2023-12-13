import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_subs (2).txt') as f:
    txt = f.read()

query = txt.split('\n')[0]
motif = txt.split('\n')[1]


found_list = []
for m in re.finditer('(?=({}))'.format(motif) ,query):
    found_list.append(m.start() + 1)

list_string = list(map(str, found_list)) 

final_string = ' '.join(list_string)

print(final_string)

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(final_string)

