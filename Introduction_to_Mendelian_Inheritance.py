import pandas as pd
import re

with open(r'c:\Users\crobbins\Downloads\rosalind_hamm.txt') as f:
    txt = f.read()

values = txt.split(' ')

homo_dom = int(values[0])
het = int(values[1])
homo_rec = int(values[2])

total = homo_dom + het + homo_rec

DD = (homo_dom / total) * ((homo_dom - 1) / total - 1)
DH = (homo_dom / total) * ((homo_dom - 1) / total - 1)
DD = (homo_dom / total) * ((homo_dom - 1) / total - 1)
DD = (homo_dom / total) * ((homo_dom - 1) / total - 1)
DD = (homo_dom / total) * ((homo_dom - 1) / total - 1)





from sympy import Rational

def calculate_probability(k, m, n):
    total = k + m + n

    # Probabilities of each pair producing offspring with a dominant allele
    pr_DD_DD = 1  # DD × DD
    pr_DD_Dd = 1  # DD × Dd
    pr_DD_dd = 1  # DD × dd
    pr_Dd_Dd = 3/4  # Dd × Dd
    pr_Dd_dd = 1/2  # Dd × dd
    pr_dd_dd = 0   # dd × dd

    # Calculate the probability of each pair occurring
    pr_pair_DD_DD = (k / total) * ((k - 1) / (total - 1))
    pr_pair_DD_Dd = (k / total) * (m / (total - 1)) + (m / total) * (k / (total - 1))
    pr_pair_DD_dd = (k / total) * (n / (total - 1)) + (n / total) * (k / (total - 1))
    pr_pair_Dd_Dd = (m / total) * ((m - 1) / (total - 1))
    pr_pair_Dd_dd = (m / total) * (n / (total - 1)) + (n / total) * (m / (total - 1))
    pr_pair_dd_dd = (n / total) * ((n - 1) / (total - 1))

    # Overall probability of producing offspring with a dominant allele
    overall_pr = (pr_DD_DD * pr_pair_DD_DD +
                  pr_DD_Dd * pr_pair_DD_Dd +
                  pr_DD_dd * pr_pair_DD_dd +
                  pr_Dd_Dd * pr_pair_Dd_Dd +
                  pr_Dd_dd * pr_pair_Dd_dd +
                  pr_dd_dd * pr_pair_dd_dd)

    return Rational(overall_pr).limit_denominator()

# Example values for k, m, n
k = 2  # homozygous dominant
m = 2  # heterozygous
n = 2  # homozygous recessive

calculate_probability(k, m, n)


print(counter)
