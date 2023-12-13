import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_hamm.txt') as f:
    txt = f.read()

strings = txt.split('\n')

counter = 0
for i in range(len(strings[0])):
    if strings[0][i] != strings[1][i]:
        counter = counter + 1

print(counter)
