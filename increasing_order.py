num1, num2, num3 = eval(input("Enter three integers, and i'll help you arrange in ascending order: "))

max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)
middle_num = 0

if (num1 > min_num) and (num1 < max_num):
    middle_num = num1

elif (num2 > min_num) and (num2 < max_num):
    middle_num = num2

else:
    middle_num = num3

print(num1,num2,num3, "in ascending order is",min_num,",",middle_num,",",max_num)
