# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:01:10 2019

@author: Thomaz
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
STDIN = input()
a = []
b = []
c = []
d = []
for i in STDIN:
    if i.islower():
        a.append(i)
    if i.isupper():
        b.append(i)
    if i.isdigit() and int(i)%2 == 1:
        c.append(i)
    if i.isdigit() and int(i)%2 == 0:
        d.append(i)
a.sort()
b.sort()
c.sort()
d.sort()
out = ''.join(a+b+c+d)
print(out)