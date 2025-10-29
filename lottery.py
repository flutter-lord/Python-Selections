import random

lottery = random.randint(10, 99)
your_guess = eval(input("Enter your lottery guess from 10 to 99 : "))

lottery_digit1 = lottery // 10
lottery_digit2 = lottery % 10

your_guess_digit1 = your_guess // 10
your_guess_digit2 = your_guess % 10

print("The original number is", lottery, "\n")

if your_guess == lottery:
    print("All digits match, You've won $10,000\n")

elif your_guess_digit1 == lottery_digit2 and your_guess_digit1 == lottery_digit1:
    print("You tried,Both the number you predicted came but in different order,You've won $3,000\n")

elif your_guess_digit1 == lottery_digit1 \
       or your_guess_digit2 == lottery_digit2 \
       or your_guess_digit1 == lottery_digit2 \
       or your_guess_digit2 == lottery_digit1:
    print("You match one digit, You've won $1,000\n")

else:
    print("Sorry no match, Please Try again or better go back home >>\n")