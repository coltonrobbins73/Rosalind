import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_gc (5).txt') as f:
    txt = f.read()

samples = txt[1:].split('>')

sample_dict = {}
for sample in samples:
    split_string = sample.split('\n', 1)
    sample_dict[split_string[0]] = split_string[1]

def gc_counter(input_str):
    g_count = input_str.count('G')
    c_count = input_str.count('C')
    total = (g_count + c_count)/len(input_str) * 100

    return total

gc_content_dict = {}
for sample in sample_dict:
    sample_dict[sample] = sample_dict[sample].replace('\n', '')
    gc_content_dict[sample] = gc_counter(sample_dict[sample])

max_value = max(gc_content_dict.values())

for key, value in gc_content_dict.items():
    if value == max_value:
        max_sample_id = key

output_txt = max_sample_id + '\n' + str(max_value)

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(output_txt)


print(output_txt)
