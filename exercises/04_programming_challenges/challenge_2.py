# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:59:33 2023

@author: wooihaw
"""

try:
    investment = float(input("Enter the initial investment: "))
    interest = float(input("Enter the annual rate (percentage): "))
    years = int(input("Enter the years of investment: "))
except:
    print("Invalid input")
else:
    print(f"Initial investment: ${investment:.2f}, annual rate: {interest:.2f}%, years of investment: {years}")

    for i in range(years):
        investment = investment + investment * interest/100
        print(f"Year {i+1}: ${investment:.2f}")