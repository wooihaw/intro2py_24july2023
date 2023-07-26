# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:51:40 2023

@author: wooihaw
"""
from collections import Counter

with open("data/alice.txt", "r") as f:
    s = f.read()
    
    # Cleaning and normalize the text
    t = [c.lower() if c.isalpha() else ' ' for c in s]
    w = ''.join(t).split()
    # print(w)
    c = Counter(w)
    
    print(f"Number of unique words: {len(c)}")
    print(f"Ten most common words: {c.most_common(10)}")
    print(f"The word 'alice' appears {c['alice']} in the text file")