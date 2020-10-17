import random
print("welcome to Snack Water Gun Game")
print("its a game against computer and 10 games will be played to see the result")
comp = 0
player = 0
complist = []
playerlst = []
n= 0
print("S for snake, W for water ,G for Gun")
while n<10:
    print("Round ",n+1)
    playerchoice = input("Enter your choice")
    playerchoice.capitalize()
    lst = ["S","W","G"]
    computerresponse = random.choice(lst)
    if playerchoice == "S":
        if computerresponse == "S":
            print("Computer choice is Snake. the game is draw")
            comp = comp +1
            player = player + 1
        elif computerresponse == "W":
            print("Computer choice is Water. you win")
            player+=2
        else:
            print("Computer choice is Gun. computer win")
            comp +=2
    elif playerchoice == "W":
        if computerresponse == "W":
            print("Computer choice is Water. the game is draw")
            comp = comp +1
            player = player + 1
        elif computerresponse == "G":
            print("Computer choice is Gun. you win")
            player+=2
        else:
            print("Computer choice is Snake. computer win")
            comp +=2
    elif playerchoice == "G":
        if computerresponse == "G":
            print("Computer choice is Gun. the game is draw")
            comp = comp +1
            player = player + 1
        elif computerresponse == "S":
            print("Computer choice is Snake. you win")
            player+=2
        else:
            print("Computer choice is Water. computer win")
            comp +=2
    else:
        print("Error!!! you entered the wrong choice")
    n+=1
print("Your Score: ",player)
print("computer Score: ",comp)
if player > comp:
    print("*** CONGRATULATIONS ***")
    print("You are Wnner")
elif player == comp:
    print("The game is Draw")
else:
    print("You Lost the game")
print("THANKS FOR PLAYING")

