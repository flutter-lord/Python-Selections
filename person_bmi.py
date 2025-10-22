weight_in_pounds = eval(input("Enter weight in pounds : "))
height_in_inches = eval(input("Enter height in inches : "))

weight_in_kg = weight_in_pounds * 0.45359237
height_in_metres = height_in_inches * 0.0254

bmi = weight_in_kg / pow(height_in_metres, 2)

print(format(bmi ,".2f"))

print("Your bmi is", end = " ")
if bmi < 18.5:
    print("Underweight")

elif bmi < 25:
    print("Normal")

elif bmi < 30:
    print("Overweight")

else:
    print("Obese")

