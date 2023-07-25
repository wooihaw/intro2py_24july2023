# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 11:54:34 2023

@author: wooihaw
"""

#%% Numeric data types
a = 1234567890
b = a ** 100
print(a, b)
print(a.__sizeof__())
print(b.__sizeof__())

#%% Binary and hexadecimal numbers
a = 0b10110011
b = 0x123cafe
c = a + b

print(a, b, c)
print(bin(c), hex(c))

#%% Variables
# class = 1  # Using keyword as variable name will cause a syntax error

# 123num = 4567  # Variable name cannot start with digit
_123num = 4567  # It can begin with an underscore

#%% Convert between data types
a, b, c = 1, 2.5, 'hello'

d = float(a)  # Convert a to floating-point value
e = int(b)  # Convert b to integer
# f = int(c)  # Cannot convert string with non-numeric characters to integer

g = '123abc'  # A string representing a hexadecimal number
h = int(g, base=16)
print(h, hex(h))

#%% Arithmetic operator
ans1 = -2 ** 2
print(ans1)

ans2 = (-2) ** 2
print(ans2)

#%% Comparison operators
a = 10
b = 25
print(a < b)
print(a > b)
print(a == b)
print(a != b)

print(0<= a < 20)
print(50<= b < 100)

#%% String indexing and slicing

s = "Introduction to Python"
print("First character: ", s[0])
print("Last character: ", s[-1])

print("First 12 characters: ", s[:12])
print("Last 6 characters: ", s[-6:])

print("Reverse string: ", s[::-1])

#%% String methods

s = "Introduction to Python"

print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace('on', 'um'))
print(s)  # The string s does not change

#%% String methods part 2

s1 = 'Abc'
s2 = '123'
s3 = s1 + s2

print(s1.isalpha())
print(s2.isdigit())
print(s3.isalpha())
print(s3.isdigit())
print(s3.isalnum())

print(s3.replace('A', 'U').swapcase())  # String methods can be chained

#%% f-string formatting

a = 123
b = 45.6789

print(f"{a=}, {a=:04x}, {a=:016b}")

print(f"{b=:.0f}, {b=:.1f}, {b=:.2f}")

print("Python is a \N{snake}")

#%% Getting input

ans = input("Enter a number: ")

print(ans, type(ans))

if ans.isdigit():
    print(f"10 times of the number is {10 * int(ans)}")
else:
    print("Invalid number!")

#%% List join, append and extend

alist = [1, 2, 3]
print(f"{alist = }")

alist = alist + [4]  # joining two lists
print(f"{alist = }")

alist += [5]  # Similar to alist = alist + [5]
print(f"{alist = }")

alist.append(6)  # append an item to the end of the list
print(f"{alist = }")

alist.extend([7, 8])  # Extending the list eith another list
print(f"{alist = }")

print(f"{len(alist) = }")

#%% Sorting a list

blist = [1, 2.5, 'abc', [3, 4], -5]
# clist = sorted(blist)  # Cannot sort list with different data types

dlist = [3, 1, 4, 2, 6, 5, 0]
elist = sorted(dlist)  # sorted in ascending order
flist = sorted(dlist, reverse=True)  # sorted in descending order

print(dlist, elist, flist, sep="\n")

dlist.sort()  # the list is sorted inplace in ascending order
print(f"{dlist = }")

#%% List methods

alist = [1, 2, 3.4, 'abc', [5, 6.78], 'xyz', 1, 'a']

print(f"{alist.count(1) = }")
print(f"{alist.count('a') = }")

print(f"{alist.index(1) = }")  # Only return the index of the first occcurance

alist.remove(1)
print(f"{alist = }")

alist.insert(3, 99)
print(f"{alist = }")

r = alist.pop(1)
print(r)
print(f"{alist = }")

#%% Indexing nested list

alist = [1, 2, [3.45, 6, 7], 8.9, 0.1]


# To acces 3.45 from the list
a = alist[2][0]
print(a)












