import pandas as pd
import re

"""
Let d: dominant, h: hetero, r: recessive
Let a = k+m+n
Let X = the r.v. associated with the first person randomly selected
Let Y = the r.v. associated with the second person randomly selected without replacement
Then:
k = f_d => p(X=d) = k/a => p(Y=d| X=d) = (k-1)/(a-1) ,
                           p(Y=h| X=d) = (m)/(a-1) ,
                           p(Y=r| X=d) = (n)/(a-1)
                           
m = f_h => p(X=h) = m/a => p(Y=d| X=h) = (k)/(a-1) ,
                           p(Y=h| X=h) = (m-1)/(a-1)
                           p(Y=r| X=h) = (n)/(a-1)
                           
n = f_r => p(X=r) = n/a => p(Y=d| X=r) = (k)/(a-1) ,
                           p(Y=h| X=r) = (m)/(a-1) ,
                           p(Y=r| X=r) = (n-1)/(a-1)
Now the joint would be:
                            |    offspring possibilites given X and Y choice
-------------------------------------------------------------------------
X Y |  P(X,Y)               |   d(dominant)     h(hetero)   r(recessive)
-------------------------------------------------------------------------
d d     k/a*(k-1)/(a-1)     |    1               0           0
d h     k/a*(m)/(a-1)       |    1/2            1/2          0
d r     k/a*(n)/(a-1)       |    0               1           0
                            |
h d     m/a*(k)/(a-1)       |    1/2            1/2          0
h h     m/a*(m-1)/(a-1)     |    1/4            1/2         1/4
h r     m/a*(n)/(a-1)       |    0              1/2         1/2
                            |
r d     n/a*(k)/(a-1)       |    0               0           0
r h     n/a*(m)/(a-1)       |    0               1/2        1/2
r r     n/a*(n-1)/(a-1)     |    0               0           1

Here what we don't want is the element in the very last column where the offspring is completely recessive.
so P = 1 - those situations as follow
"""


path = r'c:\Users\colto\Downloads\rosalind_iprb.txt'

with open(path, 'r') as file:
    lines = file.readlines()
k, m, n = [int(i) for i in lines[0].split(' ')]
a = k + m + n

p_recessive = (1/4*m*(m-1) + 1/2*m*n + 1/2*m*n + n*(n-1))/(a*(a-1))
p_wanted = 1 - p_recessive
p_wanted = round(p_wanted, 5)
print(p_wanted)