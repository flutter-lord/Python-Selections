import turtle as t

x, y = eval(input("Enter a point inside the rectangle: "))
t.speed(1)
t.penup()
t.goto(x, y)
t.write("(" + str(x) + " , " + str(y) + ")")
t.dot(5, "red")
t.pendown()

t.penup()
t.goto(-50, -50)
t.pendown()
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)

t.penup()
t.forward(30)
t.pendown()
t.write("The point" + " " +  "(" +str(x) + ", " + str(y) +")" + " you entered is inside the rectangle" if (x, y) < (100, 50) else
      "The point you entered is outside the rectangle")

t.hideturtle()

t.done()