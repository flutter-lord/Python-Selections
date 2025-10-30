import random
your_number = eval(input("Enter the sum of the number from 1 - 27: "))

random_number = random.randint(100, 999)
print(random_number,"is the original number")
print("The sum of the original number is", end = " ")

random_number_dig1 = random_number // 100
random_number_dig2 = (random_number // 10) % 10
random_number_dig3 = random_number % 10

random_sum = random_number_dig1 + random_number_dig2 + random_number_dig3
print(random_sum,"\n")

print(your_number,"is the sum of the original number you guessed")

print("The sum of the number you guessed with the original number  is correct >>" if your_number == random_sum else
      "The sum of the number you guessed with the original is incorrect")
