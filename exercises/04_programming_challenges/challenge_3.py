# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:09:56 2023

@author: wooihaw
"""

s1 = set(range(5, 101, 5))  # set of numbers divisible by 5
s2 = set(range(7, 101, 7))  # set of number divisible by 7
s3 = set(range(1, 101))  # set of number from 1 to 100

ans = s3 - (s1 | s2)

print(ans)