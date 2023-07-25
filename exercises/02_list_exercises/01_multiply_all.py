# Write a Python script to multiply all the items in a list.
alist = [12, 43, 57, 98, 83, -103, 256, -1]
print(f'{alist=}')

ans = 1
for i in alist:
    ans = ans * i  # ans *= i
print(ans)