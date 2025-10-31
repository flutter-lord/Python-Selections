x1, y1 = eval(input("Enter a point, let's check if it is in or outside the circle: "))

import math as m

determinant = m.sqrt(x1*x1 + y1*y1) <= 10
print("The point(" + str(x1) + "," + str(y1) +")","is on the circle" if determinant == True else "is not on the circle")