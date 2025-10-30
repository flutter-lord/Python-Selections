import random
your_number = eval(input("Enter your guess between 111 and 999: "))

random_number = random.randint(100, 999)
print(random_number,"is the original number")
print("The sum of the original number is", end = " ")

random_number_dig1 = random_number // 100
random_number_dig2 = (random_number // 10) % 10
random_number_dig3 = random_number % 10

random_sum = random_number_dig1 + random_number_dig2 + random_number_dig3
print(random_sum,"\n")

your_number_dig1 = your_number // 100
your_number_dig2 = (your_number // 10) % 10
your_number_dig3 = your_number  % 10

print(your_number,"is the number you guessed")
print("The sum of the number you guessed is", end = " ")

your_number_sum = your_number_dig1 + your_number_dig2 + your_number_dig3
print(your_number_sum,"\n")

print("The sum of the number you guessed with the original number  is correct >>" if your_number_sum == random_sum else
      "The sum of the number you guessed with the original is incorrect")
