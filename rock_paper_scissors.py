import random
import sys

your_pick = eval(input("Input your pick e.g 0 for scissors, 1 for rock and 2 for paper: "))
computer_pick = random.randint(0,2)

if your_pick > 2:
    print("No such input, try again")
    sys.exit()

if computer_pick == 0:

    if your_pick == 1:
        print("computer pick is scissors and your pick is rock\nYou Win")

    elif your_pick == 2:
        print("computer pick is scissors and your pick is paper\nYou Lose")

    else:
        print("computer pick is scissors and your pick is also scissors\nIt's a draw")


elif computer_pick == 1:

    if your_pick == 0:
        print("computer pick is rock and your pick is scissors\nYou lose")

    elif your_pick == 2:
        print("computer pick is rock and your pick is paper\nYou Win")

    else:
        print("computer pick is rock and your pick is also rock\nIt's a draw")

else:

    if your_pick == 0:
        print("computer pick is paper and your pick is scissors\nYou win")

    elif your_pick == 1:
        print("computer pick is paper and your pick is rock\nYou lose")

    else:
        print("computer pick is paper and your pick is also paper\nIt's a draw")