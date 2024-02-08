import pandas as pd

df = pd.read_csv(r'c:\Users\crobbins\Downloads\rosalind_dna (2).txt')

test = df.columns.tolist()

letters  = ['A', 'T', 'C', 'G']
count_dict = {}
for letter in letters:
    count_dict[letter] = test[0].count(letter)

count_dict
