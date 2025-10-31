decision = eval(input("Enter 0 to convert dollars to CHY and 1 vice versa: "))

if decision > 1:
    print("input 0 and 1 only")
    decision = eval(input("Enter 0 to convert dollars to CHY and 1 vice versa: "))

if decision == 0:
    print("You are converting USD(US dollar) to CHY(Chinese yuan)\n")

    dollar = eval(input("Enter the dollar: "))
    yuan = 6.81 * dollar

    print("$",dollar,"dollar(USD) is equals to", yuan,"yuan(CHY)")

elif decision == 1:
    print("You are converting CHY(Chinese yuan) to USD(US dollar)\n")
    yuan = eval(input("Enter the  yuan: "))
    dollar = yuan / 6.81

    print(yuan,"yuan(CHY) is equals to $",dollar,"dollar(USD)")

else:
    print("input 0 and 1 only")
    decision = eval(input("Enter 0 to convert dollars to CHY and 1 vice versa: "))