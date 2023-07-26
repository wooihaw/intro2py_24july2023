# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 10:31:14 2023

@author: wooihaw
"""

#%% Function which returns multiple values
def func1(x: int, y: int, z: int) -> tuple[int]:
    '''This is a function which return 3 values'''
    x = x + 1
    y = y - 1
    z = z * 2
    return x, y, z

a = func1(1.5, 2, 3)
print(a, type(a))

b, c, d = func1(4, 5, 6)
print(b, c, d)

#%% Functions are objects
def func1(x):
    return x + 1

def func2(y):
    return y - 2

def func3(z):
    return z * 2

functions = (func1, func2, func3)
for f in functions:
    print(f(5))
    
d_func = {'function1': func1, 'function2': func2, 'function3': func3}
for k in d_func:
    print(f"{k} output: {d_func[k](5)}")
    
#%% Lambda function example 1
# Sort in ascending order according to the 3rd element of each tuple in the list

alist = [(1, 2, 3), (11, 4, 1), (7, 9, 2)]
blist = sorted(alist)
print(f"{blist = }")

clist = sorted(alist, key=lambda x:x[2])  # return the 3rd element of each tuple
print(f"{clist = }")

#%% Lambda function example 2
# Sort the list according to the ID numbers
ID = ['ID21', 'ID7', 'ID55', 'ID101', 'ID3', 'ID82', 'ID12']

print(sorted(ID))
print(sorted(ID, key=lambda y: int(y[2:])))

print(min(ID, key=lambda y: int(y[2:])))
print(max(ID, key=lambda y: int(y[2:])))

#%% map() function
# Reverse each string and put them into a new list
words = ['apple', 'bell', 'cat', 'donkey', 'egg']

# Method 1 - Use for loop
r1 = []
for w in words:
    r1.append(w[::-1])
print(f"{r1 = }")

# Method 2 - List comprehension
r2 = [w[::-1] for w in words]
print(f"{r2 = }")

# Method 3 - Use map() function
r3 = list(map(lambda w: w[::-1], words))
print(f"{r3 = }")

#%% filter() function
# Select only the palindrome from a list of words
words = ('ant', 'boy', 'civic', 'dad', 'madam', 'fish')

# Method 1 - Use for loop
p1 = []
for w in words:
    if w == w[::-1]:
        p1.append(w)
print(f"{p1 = }")

# Method 2 - Use list comprehension
p2 = [w for w in words if w == w[::-1]]
print(f"{p2 = }")

# Method 3 - Use filter() function
p3 = list(filter(lambda w: w == w[::-1], words))
print(f"{p3 = }")

#%% Combine map() and filter()
# Find the square of even numbers from 1 to 20

# Method 1 - Use for loop
sqr1 = []
for i in range(1, 21):
    if i%2 == 0:
        sqr1.append(i*i)
print(f"{sqr1 = }")

# Method 2 - Use list comprehension
sqr2 = [i*i for i in range(1, 21) if i%2 == 0]
print(f"{sqr2 = }")

# Method 3 - Use map() and filter()
sqr3 = list(map(lambda i: i*i, filter(lambda i: i%2 == 0, range(1, 21))))
print(f"{sqr3 = }")

#%% OOP example 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"Rectangle with length of {self.length} and width of {self.width}"
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2*self.length + 2*self.width
    def __eq__(self, other):
        return self.area() == other.area()
    def __gt__(self, other):
        return self.area() > other.area()
    def __repr__(self):
        return f"Rectangle ({self.length}, {self.width})"

class Square(Rectangle):    
    def __init__(self, length):
        super().__init__(length, length)
        self.__secret = length
    def __str__(self):
        return f"Square with side of {self.length}. The secret is {self.__secret}"
    def __repr__(self):
        return f"Square ({self.length})"
    
    
rec1 = Rectangle(3, 5)
print(rec1)
print(rec1.area())
print(rec1.perimeter())

rec2 = Rectangle(5, 3)
print(rec1 == rec2)
print(rec1 > rec2)

rec3 = Rectangle(4, 6)
print(rec3 > rec1)
print(rec1 < rec3)

rectangles = [rec1, rec2, rec3]
print(rectangles)

sqr1 = Square(3)
print(sqr1)
print(sqr1.area())
print(sqr1.perimeter())

sqr2 = Square(5)
print(sqr1 == sqr2)
print(sqr1 < sqr2)
print(sqr1.length)
# print(sqr1.__secret)










