import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_cons (2).txt') as f:
    txt = f.read()

seqs = txt[1:].split('>')

seq_dict = {}
for seq in seqs:
    split_seq = seq.split('\n', 1)
    seq_dict[split_seq[0]] = split_seq[1].replace('\n', '')



df = pd.DataFrame()
for seq in seq_dict:
    df[seq] = [x for x in seq_dict[seq]]

df = df.T

consensus_seq = []
for col in df.columns.to_list():
    consensus_seq.append(df[col].mode()[0])

consensus_seq = ''.join(map(str, consensus_seq))

letters = ['A', 'C', 'G', 'T']

seq_order_dict = {}
for col in df.columns.tolist():
    seq_order_dict[col] = df[col].value_counts().to_dict()
    for letter in letters:
        if letter not in seq_order_dict[col]:
            seq_order_dict[col][letter] = 0


final_letter_count = {}
for letter in letters:
    final_letter_count[letter] = []
    for col in seq_order_dict:
        final_letter_count[letter].append(str(seq_order_dict[col][letter]))

for letter in final_letter_count:
    final_letter_count[letter] = ' '.join(map(str, final_letter_count[letter]))
                       
print(consensus_seq)

final_string = consensus_seq + '\n'

for letter in final_letter_count:
    print(letter + ': ' + str(final_letter_count[letter]))
    final_string = final_string + letter + ': ' + final_letter_count[letter] + '\n'

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(final_string)
