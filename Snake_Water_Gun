import random

# Snake Water Gun or Rock Paper Scissors
def gameWin(computer, you):
    # If two values are equal, declare a tie!
    if computer == you:
        return None

    # Check for all possibilities when computer chose s
    elif computer == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif computer == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif computer == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
RandomNo = random.randint(1, 3) 
if RandomNo == 1:
    computer = 's'
elif RandomNo == 2:
    computer = 'w'
elif RandomNo == 3:
    computer = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
