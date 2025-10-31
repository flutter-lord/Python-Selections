import sys

today_day = eval(input("Enter today day(e.g 1 for Monday, 2 for Tuesday....., 0 for Sunday): "))

future_day_digit = eval(input("Enter the days after: "))
future_days = (today_day + future_day_digit) % 7

today_day_in_week = ""
future_day_in_week = ""

if today_day >= 7:
    print("The day value for the day you input is greater than or equals to 7")
    print("Try entering days lower than 7")
    sys.exit()


if today_day == 0:
    today_day_in_week = "Sunday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)

elif today_day == 1:
    today_day_in_week = "Monday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit,"days after",today_day_in_week,"is", future_day_in_week)

elif today_day == 2:
    today_day_in_week = "Tuesday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)

if today_day == 3:
    today_day_in_week = "Wednesday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)

elif today_day == 4:
    today_day_in_week = "Thursday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)

elif today_day == 5:
    today_day_in_week = "Friday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)


else:
    today_day_in_week = "Saturday"

    if future_days == 0:
        future_day_in_week = "Sunday"

    elif future_days == 1:
        future_day_in_week = "Monday"

    elif future_days == 2:
        future_day_in_week = "Tuesday"

    elif future_days == 3:
        future_day_in_week = "Wednesday"

    elif future_days == 4:
        future_day_in_week = "Thursday"

    elif future_days == 5:
        future_day_in_week = "Friday"

    else:
        future_day_in_week = "Saturday"

    print(future_day_digit, "days after", today_day_in_week, "is", future_day_in_week)