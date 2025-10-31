import sys

month, years = eval(input("Enter the month and year: e.g 1 for January, ..... 12 for December : "))

days = 0
month_in_word = ""
if month > 12:
    print("Your month cannot be greater than 12.\nDecember(12) is the last month of the year\n")
    print("invalid input, Month is from 1 to 12.")
    sys.exit()

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31

    if month == 1:
        month_in_word = "January"

    elif month == 3:
        month_in_word = "March"

    elif month == 5:
        month_in_word = "May"

    elif month == 7:
        month_in_word = "July"

    elif month == 8:
        month_in_word = "August"

    elif month == 10:
        month_in_word = "October"

    elif month == 12:
        month_in_word = "December"


elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30

    if month == 4:
        month_in_word = "April"

    elif month == 6:
        month_in_word = "June"

    elif month == 9:
        month_in_word = "September"

    elif month == 11:
        month_in_word = "November"

elif month == 2:
    month_in_word = "February"
    days = 28

    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        days = 29

print(month_in_word,", year",years, "has", days, "days")

