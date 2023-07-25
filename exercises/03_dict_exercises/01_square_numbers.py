# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Expected results:
# square =  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


# Method 1
keys = range(1, 16)
values = [k*k for k in keys]
d = dict(zip(keys, values))
print(f"{d = }")

# Method 2 - Use dictionary comprehension
d2 = {k: k*k for k in range(1, 16)}
print(f"{d2 = }")

# Method 3 - Use for loop
d3 = {}
for k in range(1, 16):
    d3[k] = k * k
print(f"{d3 = }")