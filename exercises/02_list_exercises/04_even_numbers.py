# Write a Python script that takes a list of numbers and returns a new list containing only the even numbers from the original list.
alist = [12, 43, 57, 98, 83, -103, 256, -55, 168, -6]
print(f'{alist=}')

# Use for loop
blist = []
for i in alist:
    if i % 2 == 0:
        blist.append(i)
print(f"{blist = }")

# Use list comprehension
clist = [i for i in alist if i%2 == 0]
print(f"{clist = }")