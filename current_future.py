# h = days of the week in digit e.g 0 for Saturday, 1 for Sunday ....6 for friday etc
# q = the day of the month.
# m = the month (3: March, 4: April, ..., 12: December). January and February are
# counted as months 13 and 14 of the previous year
# j = the century (e.g ....year \ 100)
# k = the year of the century (i.e... year % 100)

year, m, q, = eval(input("Enter the year, month and the day in the month separated by a comma e.g (2003, 5, 24): "))
j = (year // 100) + 1
k = year % 100

h = int(q + (26 * (m + 1) / 10) + k + (k / 4) + (j / 4) + (5 * j)) % 7
days_in_week = ""

if h == 0:
    days_in_week = "Sunday"

elif h == 1:
    days_in_week = "Monday"

elif h == 2:
    days_in_week = "Tuesday"

elif h == 3:
    days_in_week = "Wednesday"

elif h == 4:
    days_in_week = "Thursday"

elif h == 5:
    days_in_week = "Friday"

else:
    days_in_week = "Saturday"

print("The day of the week of",q,"-", m,"-", year,"is",days_in_week)

