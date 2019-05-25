# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:40:33 2019

@author: Thomaz
"""

n = int(input())
arr = map(int, input().split())
arr = list(arr)
c = arr.count(max(arr))
for i in range(c):
    arr.remove(max(arr))
print(max(arr))