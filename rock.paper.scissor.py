import random
winner = " "

userAction = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors:"))

while userAction > 0:
    computerAction = random.randrange(1,4)
    print ("computerAction:", computerAction)

    if userAction == computerAction:
        print("round finished and winner is: draw")
    elif userAction == 1:
        if computerAction == 3:
            winner = "human"
            print("round finished and winner is:", winner)
        else:
            winner = "computer"
            print("round finished and winner is:", winner)
    elif userAction == 2:
        if computerAction == 1:
            winner = "human"
            print("round finished and winner is:", winner)
        else:
            winner = "computer"
            print("round finished and winner is:", winner)
    elif userAction == 3:
        if computerAction == 2:
            winner = "human"
            print("round finished and winner is:", winner)
        else:
            winner = "computer"
            print("round finished and winner is:", winner)
    else:
        winner = "invalid"
        print("round finished and winner is:", winner)
    userAction = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors:"))
