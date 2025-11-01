x1, y1 = eval(input("Enter the point coordinates: "))
discriminant = x1 <= 50 and y1 <= 2.5

print("The point", x1, y1,"is inside the rectangle" if discriminant else "is not inside the rectangle")