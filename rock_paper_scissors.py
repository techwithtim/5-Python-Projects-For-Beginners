import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# implementing basic function
def win(user_input, computer_pick):
    # conditions is p > r, r > s, s > p
    if (user_input == "rock" and computer_pick == "scissors") or (user_input == "scissor" and computer_pick == "paper") \
            or (user_input == "paper" and computer_pick == "rock"):
        return True
    return False

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    # rock: 0, paper: 1, scissors: 2
    # choosing from option lists
    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    # adding draw condition
    if user_input == computer_pick:
        print("Draw!")

    elif win(user_input, computer_pick):
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
