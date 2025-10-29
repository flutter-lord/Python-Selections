years = eval(input("Enter a year: "))
if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
    print("The", years, "is a leap year.",)

else:
    print("The", years, "is not a leap year.")