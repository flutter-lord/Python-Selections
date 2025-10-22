day = 0

question1 = "Is your birthday in table1 below?\n" + \
    "1\t3\t5\t7\n" + \
    "9\t11\t13\t15\n" + \
    "17\t19\t21\t23\n" + \
    "25\t27\t29\t31\n" + \
    "Enter 0 for No and 1 for Yes: "
answer = eval(input(question1))

if answer == 1:
    day+= 1

question2 = "\nIs your birthday in table2 below?\n" + \
    "2\t3\t6\t7\n" + \
    "10\t11\t14\t15\n" + \
    "18\t19\t22\t23\n" + \
    "26\t27\t30\t31\n" + \
    "Enter 0 for No and 1 for Yes: "
answer = eval(input(question2))\

if answer == 1:
    day+= 2

question3 = "\nIs your birthday in  table3 below?\n" + \
    "4\t5\t6\t7\n" + \
    "12\t13\t14\t15\n" + \
    "20\t21\t22\t23\n" + \
    "28\t29\t30\t31\n" + \
    "Enter 0 for No and 1 for Yes : "
answer = eval(input(question3))

if answer == 1:
    day+= 4

question4 = "\nIs your birthday in table4 below?\n" + \
    "8\t9\t10\t11\n" + \
    "12\t13\t14\t15\n" + \
    "24\t25\t26\t27\n" + \
    "28\t29\t30\t31\n" + \
    "Enter 0 for No and 1 for Yes :"
answer = eval(input(question4))

if answer == 1:
    day+= 8

question5 = "\nIs your birthday in table5 below?\n" + \
    "16\t17\t18\t19\n" + \
    "20\t21\t22\t23\n" + \
    "24\t25\t26\t27\n" + \
    "28\t29\t30\t31\n" + \
    "Enter 0 for No and 1 for Yes : "
answer = eval(input(question5))

if answer == 1:
    day += 16

print("\nYour birthday is" + " " + str(day) + "!")
