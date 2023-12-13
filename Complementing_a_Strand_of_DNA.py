import pandas as pd

with open(r'c:\Users\crobbins\Downloads\rosalind_revc.txt') as f:
    txt = f.read()

txt = txt.strip('\n')

reverse = txt[::-1]

lookup = {
        'A' : 'T',
        'G' : 'C',
        'C' : 'G',
        'T' : 'A'
}

rev_compliment = [lookup.get(i) for i in reverse]
rev_compliment = ''.join(rev_compliment)

with open(r'c:\Users\crobbins\Downloads\output.txt', 'w') as f:
    f.write(rev_compliment)
