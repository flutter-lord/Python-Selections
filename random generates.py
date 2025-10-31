import random
import string

your_number = eval(input("Enter the sum of the number (1 - 18) : "))

random_number = random.randint(10, 99)
print(random_number, "is the original number")

random_number_dig1 = random_number // 10
random_number_dig2 = random_number % 10

random_sum = random_number_dig1 + random_number_dig2
print(random_sum,"is the sum of the integers in the original number\n")

print("You guessed correctly" if your_number == random_sum else "You guessed wrongly")

string_letter = random.choice(string.ascii_lowercase)
print(string_letter)


