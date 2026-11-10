import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# Each option beats the one it maps to.
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower().strip()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid choice. Please type rock, paper or scissors.")
        continue

    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif beats[user_input] == computer_pick:
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
