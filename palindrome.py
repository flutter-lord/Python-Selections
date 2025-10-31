number = int(input("Enter a number from 100 to 999: "))

num1 = number // 100
num2 = (number // 10) % 10
num3 = number % 10

is_palindrome = num1 == num3
print(is_palindrome)
print(number,"is palindrome" if int(is_palindrome) > 0  else "is not palindrome")