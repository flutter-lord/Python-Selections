your_value = eval(input("Enter any number : "))

if your_value % 5 == 0:
    print("highFive")

if your_value % 2 == 0:
    print("highEven")

else:
    print("Your number is", your_value, end = ", ")
    print("it can be divided by 2 and 5")