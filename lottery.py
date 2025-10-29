import random

lottery = random.randint(10, 99)
your_guess = eval(input("Enter a number from 10 to 99 : "))

lottery_digit1 = lottery // 10
lottery_digit2 = lottery % 10

your_guess_digit1 = your_guess // 10
your_guess_digit2 = your_guess % 10

print("The original number is", lottery)

if your_guess == lottery:
    print("You guessed correctly, You've won $10,000")

elif your_guess_digit1 == lottery_digit2 and your_guess_digit1 == lottery_digit1:
    print("You tried,Both the number you predicted came,You've won $3,000")

elif your_guess_digit1 == lottery_digit1 \
       or your_guess_digit2 == lottery_digit2 \
       or your_guess_digit1 == lottery_digit2 \
       or your_guess_digit2 == lottery_digit1:
    print("You match one digit, You've won $1,000")

else:
    print("You guessed wrong, Please Try again or better go back home >>")