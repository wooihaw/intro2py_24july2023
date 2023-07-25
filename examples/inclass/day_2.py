# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 09:52:20 2023

@author: wooihaw
"""

#%% Dictionary methods

adict = dict(a=1, b=2.5, c='abc')
adict['d'] = [3, 4, 5]  # Add new key-value pair
print(f"{adict = }")

print(f"{adict['c'] = }")

# print(f"{adict['e'] = }")  # KeyError as the key 'e' does not exist
print(f"{adict.get('e', 0) = }")  # The get() method returns the default value if the key does not exist

print(f"{adict.setdefault('e', 789) = }")
print(f"{adict = }")

#%% Join 2 dictionaries

d1 = {'a':1, 'b':2, 'c':3}
d2 = dict(x=4, y=5, z=6)

# Method 1
d3 = d1.copy()
d3.update(d2)
print(f"{d3 = }")

# Method 2
d4 = d1 | d2
print(f"{d4 = }")

#%% Set operations

alist = [1, 2, 1, 3, 4, 1, 5, 2, 0, 2.5, 1, 'abc']
blist = list(set(alist))

print(f"{alist = }")
print(f"{blist = }")

#%% Set methods

name1 = ['Ali', 'Baba', 'Cloud', 'Dave', 'Edward']
name2 = ['John', 'Chan', 'Ali', 'Dave', 'Ahmed']

common_names = list(set(name1) & set(name2))
all_names = list(set(name1) | set(name2))
uncommon_names = list(set(name1).symmetric_difference(set(name2)))

print(f"{common_names = }")
print(f"{all_names = }")
print(f"{uncommon_names = }")

#%% Conditional statement

a = 49
if a >= 50:
    print("Statement 1")
    print("Statement 2")
    print("Statement 3")
else:
    print("Statement 4")
    print("Statement 5")
    print("Statement 6")    
print("Outside of if-else statement.")

#%% Ternary operator
num = int(input("Enter an integer: "))
print(f"This is an {'even' if num % 2 == 0 else 'odd'} number")

# Use if-else statement to perform the same operation
if num % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#%% False value testing
alist = []

# Method 1 - Use len() to check whether a list is empty
if len(alist) > 0:
    print("Not empty")
else:
    print("Empty")
    
# Method 2 - Just check the list itself (empty is evaluated to be false)
if alist:
    print("Not empty")
else:
    print("Empty")

#%% For loop example

# Use zip() to iterate multiple lists (limitted by the shortest list)
names = ['ali', 'baba', 'cloud', 'data']
ages = [13, 37, 23, 32, 45, 57]
blood_types = ['A', 'O', 'O', 'B', 'AB']

for i, j, k in zip(names, ages, blood_types):
    print(f"{i.capitalize()} is {j} years old with blood type {k}")

# Automatically add an index to each iteration using enumerate()
for h, (i, j, k) in enumerate(zip(names, ages, blood_types), start=1):
    print(f"{h}. {i.capitalize()} is {j} years old with blood type {k}")
    
#%% Using break and continue to control loop

while True:
    name = input("Enter your name: ") or "Noname"
    print(f"Hello {name}")
    ...
    ans = input("Do you want to repeat? ").lower()
    if ans in ('y', 'yes'):
        continue
    elif ans in ('n', 'no'):
        print("Bye!")
    else:
        print("Invalid choice!")
    break

#%% List comprehension example 1
# Select the words that start with vowels
words = ('ant', 'boy', 'egg', 'cat', 'donkey', 'whale', 'orange')

# Use for loop
vowel_words1 = []
for w in words:
    if w[0].lower() in 'aeiou':
        vowel_words1.append(w)
print(f"{vowel_words1 = }")

# Use list comprehension
vowel_words2 = [w for w in words if w[0].lower() in 'aeiou']
print(f"{vowel_words2 = }")

#%% List comprehension example 2
# Calculate the number of odd numbers in a list
from random import randint
numbers = [randint(1, 100) for _ in range(100)]

# Use for loop
count = 0
for i in numbers:
    if i%2 == 1:
        count += 1
print(f"There are {count} odd numbers in the list")

# Use list comprehension
count2 = sum([i%2 for i in numbers])
print(f"There are {count2} odd numbers in the list")

#%% Dictionary comprehension example

prices = dict(apple=1.5, orange=2.5, durian=20, mango=9)

# Create a new dictionary with discounted price (10%)

# Use for loop
discount1 = {}
for k in prices:
    discount1[k] = 0.9 * prices[k]
print(f"{discount1 = }")

# Use dictionary comprehension
discount2 = {k: 0.9*prices[k] for k in prices}
print(f"{discount2 = }")

#%% Using pass and ellipsis

for i in range(5):
    pass

for j in range(10):
    ...

#%% Use any() function
words = ('apple', 'boy', 'cat', 'dog')

# Check whether any of the word in the tuple starts with a vowel

# Use for loop
ans = False
for w in words:
    if w[0].lower() in 'aeiou':
        ans = True
if ans:
    print("There is a word starting with a vowel in the tuple")
else:
    print("There is no word starting with a vowel in the tuple")

# Use any() and list comprehension
if any(True if w[0].lower() in 'aeiou' else False for w in words):
    print("There is a word starting with a vowel in the tuple")
else:
    print("There is no word starting with a vowel in the tuple")

# Use all() and list comprehension
if all(True if w[0].lower() in 'aeiou' else False for w in words):
    print("All words start with a vowel in the tuple")
else:
    print("Not all words start with a vowel in the tuple")

#%% Use pickle to store dictory into a file

from pickle import dump
data = {}
ans = 'y'
while ans.lower() in ('y', 'yes'):
    name = input("Enter name: ") or "Noname"
    age = input("Enter age: ") or "0"
    data[name] = age
    ans = input("Do you want to enter another data? ") or 'y'
    
print(f"{data = }")
    
with open("name_age.pkl", "bw") as f:
    dump(data, f)

#%% Using pickle to load a dictionary from file

from pickle import load
with open("name_age.pkl", "br") as f:
    d = load(f)
    
print(f"{d = }")

#%% Exception handling

while True:
    try:
        num = int(input("Enter an integer: "))
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"You have entered {num}")
        break

#%% Function example 1

def add_one(x):
    print(x + 1)

a = add_one(10)
print(f"{a = }")

def add_two(y):
    return y + 2

b = add_two(20)
print(f"{b = }")
    


























