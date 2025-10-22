your_number = eval(input("Enter your number : "))

if your_number % 2 == 0 and your_number % 3 == 0:
    print(your_number, "is divisible by both 2 and 3")

if your_number % 2 == 0 or your_number % 3 == 0:
    print(your_number, "is divisible by 2 or 3")

if (your_number % 2 == 0 or your_number % 3 == 0 and not \
        (your_number % 2 == 0 and your_number % 3 == 0)):
    print(your_number, "is divisible by 2 or 3 but not both 2 and 3")