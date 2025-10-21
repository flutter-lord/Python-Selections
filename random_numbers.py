import random

num1 = round(random.random(), 2)
num2 = round(random.random(), 2)

summation = num1 + num2

question = eval(input("What is " + str(num1) +  " +" + " " + str(num2) + " : " ))

if summation == question:
    print("Your answer is correct")

else:
    print("Your answer is incorrect")