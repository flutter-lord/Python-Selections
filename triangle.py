x1, x2, x3 = eval(input("Enter the lengths of the three sides of the triangle: "))

if (x1 + x2 > x3) and (x1 + x3 > x2) and (x2 + x3 > x1):
    print("The triangle is has valid lengths")
    print(x1 + x2 + x3,"is the perimeter of the triangle")

else:
    print("The input is invalid")
