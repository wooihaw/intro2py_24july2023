# Write a Python script to print the sum of all values in the dictionary where the values are numbers.
# Expected results:
# adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}
# Sum of all values in the dictionary: 239

adict =  {'a': 66, 'b': 33, 'c': 39, 'd': 7, 'e': 80, 'f': 5, 'g': 9}

# Method 1 - Use for loop
ans1 = 0
for k in adict:
    ans1 += adict[k]
print(f"Sum of all values in the dictionary: {ans1}")

# Method 2
ans2 = sum(adict[k] for k in adict)
print(f"Sum of all values in the dictionary: {ans2}")

# Method 3
ans3 = sum(adict.values())
print(f"Sum of all values in the dictionary: {ans3}")