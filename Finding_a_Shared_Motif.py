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

with open(r'c:\Users\colto\Downloads\rosalind_iev.txt') as f:
    txt = f.read()

seq_dict = parse_fasta(txt)

def build_suffix_array(s):
    """Builds a suffix array for the given string."""
    return sorted(range(len(s)), key=lambda k: s[k:])

def build_lcp_array(s, suffix_array):
    """Builds the LCP array for the given string and its suffix array."""
    n = len(s)
    rank = [0] * n
    lcp = [0] * (n - 1)

    for i in range(n):
        rank[suffix_array[i]] = i

    k = 0
    for i in range(n):
        if rank[i] == n - 1:
            k = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k:
            k -= 1

    return lcp

def longest_common_substring(strings):
    """Finds the longest common substring among the given strings."""
    if not strings:
        return ""

    concat_str = '\0'.join(strings) + '\0'  # Unique delimiter
    suffix_array = build_suffix_array(concat_str)
    lcp = build_lcp_array(concat_str, suffix_array)

    # Finding the longest common substring
    longest_common = ''
    n = len(concat_str)

    for i in range(len(lcp)):
        if lcp[i] > len(longest_common):
            substr = concat_str[suffix_array[i]:suffix_array[i] + lcp[i]]
            if all(substr in string for string in strings):
                longest_common = substr

    return longest_common

# Example usage
strings = ["ABABC", "BABC", "BABCA", "CABAB"]
print(longest_common_substring(strings))  # Outputs the longest common substring


>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA