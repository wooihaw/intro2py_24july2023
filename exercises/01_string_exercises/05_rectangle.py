# Write a Python script to ask for the length and width of a rectangle, 
# calculate and print the perimeter and area of the rectangle.
# E.g.
# Enter length: 5
# Enter width: 3
# perimeter = 16, area = 15.

l = input("Enter length: ")
w = input("Enter width: ")

if l.isdigit() and w.isdigit():
    l, w = int(l), int(w)
    perimeter = 2*l + 2*w
    area = l * w
    print(f"{perimeter = }, {area = }")
else:
    print("Invalid length and/or width")
    