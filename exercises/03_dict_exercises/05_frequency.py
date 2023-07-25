# Write a Python script to find the frequency of occurance for each alphabet in a string.
astring = 'The quick brown fox jumps over the lazy dog.'

# Clean and normalize the text
alist = [c.lower() for c in astring if c.isalpha()]
print(alist)

# Use dictionary comprehension
freq = {k : alist.count(k) for k in sorted(set(alist))}
print(f"{freq = }")