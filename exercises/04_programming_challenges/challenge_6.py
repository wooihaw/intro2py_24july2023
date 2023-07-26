# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:38:02 2023

@author: wooihaw
"""

class Circle:
    pi = 3.1416
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * self.radius ** 2
    def circumference(self):
        return 2 * Circle.pi * self.radius
    
c1 = Circle(4)

print(f"{c1.area() = }")
print(f"{c1.circumference() = }")