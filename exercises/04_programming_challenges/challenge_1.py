# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:53:00 2023

@author: wooihaw
"""

# c - number of chicken
# r - number of rabbit
# c + r = 35
# 2*c + 4*r = 94

for c in range(36):
    r = 35 - c
    if 2*c + 4*r == 94:
        print(f"There are {r} rabbits and {c} chickens.")