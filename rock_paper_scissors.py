import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors, Q to quit, R to Reset ").strip().lower()
    if user_input == "q":
        break

    if user_input == "r": # Score reset
        user_wins = 0
        computer_wins = 0
        continue

    if user_input not in options:
        print("Invalid input.")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a draw!!") # Handling draws

    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("\nFinal Results:") # Adding summary to the end
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")

if user_wins > computer_wins:
    print("You beat the computer! 🎉")
elif user_wins < computer_wins:
    print("The computer won overall. 😢")
else:
    print("It's a draw overall!")

print("Goodbye!")


