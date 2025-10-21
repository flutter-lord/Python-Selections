import random as r

num1 = r.randint(0, 9)
num2 = r.randint(0, 9)

if num1 < num2:
    num1, num2 = num2, num1

subtraction = num1 - num2

questions = eval(input("What is" + " " + str(num1) + " - " + str(num2) + " : "))

if subtraction == questions:
    print("Your answer is correct")

else:
    print("Your answer is incorrect")