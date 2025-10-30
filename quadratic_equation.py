import sys

a, b, c = eval(input("Enter a, b, c for your quadratic equation : "))

import math as m

discriminant = m.pow(b, 2) - (4 * a * c)

if discriminant < 0:
    print("Your equation has no roots")
    sys.exit(0)

root1 = (-b + m.sqrt(discriminant)) / (2 * a)
root2 = (-b - m.sqrt(discriminant)) / (2 * a)


print(("Your equation has one root which is", root1) if discriminant == 0 else
      ("Your equation has two roots which are", format(root1, ".4f"), "and", format(root2, ".4f")))





