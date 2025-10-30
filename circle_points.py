x1, y1 = eval(input("Enter the point of the circle x, y : "))
radius = eval(input("Enter the radius of the circle : "))
x2, y2 = eval(input("Enter the point x, y : "))

import turtle as t
t.penup()
t.goto(x1, y1 - radius)
t.pendown()
t.circle(radius)

t.penup()
t.goto(x2, y2)
t.pendown()
t.dot(6, "red")
t.penup()

t.penup()
t.goto(x1 - 70, y1 - radius - 20)
t.pendown()
import math as m
distance = m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))
t.write("The point is inside the circle" if distance <= radius  else \
        "The point is outside the circle" )

t.hideturtle()
t.done()