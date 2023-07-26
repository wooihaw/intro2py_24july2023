# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:15:36 2023

@author: wooihaw
"""

with open("data/Heathrow.txt", "r") as f:
    raw_data = f.readlines()
    # print(raw_data)
    data = [float(i.strip()) for i in raw_data]
    print(data)
    data.sort()
    
    n = len(data)
    mean = sum(data)/n
    
    if n % 2 == 1:
        median = data[n // 2]
    else:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
        
    print(f"Lowest: {data[0]}, highest: {data[-1]}")
    print(f"Mean: {mean}, median: {median}")
    
import statistics as stat

print(f"{stat.mean(data) = }") 
print(f"{stat.median(data) = }") 