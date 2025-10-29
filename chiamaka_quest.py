import math

num1, num2, num3, num4 = eval(input("Enter your four numbers: "))

mean = (num1 + num2 + num3 + num4) / 4

spread = 0
spread += round(pow((num1 - mean), 2), 2)
spread += round(pow((num2 - mean), 2), 2)
spread += round(pow((num3 - mean), 2), 2)
spread += round(pow((num4 - mean), 2), 2)

variance = spread / 4

standard_deviation = math.sqrt(variance)

print("The standard deviation for the four numbers",num1, num2, num3, num4,
      "is", format(standard_deviation, ".2f"))