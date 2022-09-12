import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    def rps_match(user_input_param):

        if user_input_param == "rock" and computer_pick == "scissors":
            print("You won!")
            return "user_wins"

        elif user_input_param == "paper" and computer_pick == "rock":
            print("You won!")
            return "user_wins"

        elif user_input_param == "scissors" and computer_pick == "paper":
            print("You won!")
            return "user_wins"

        else:
            print("You lost!")
            return "computer_wins"


    if rps_match(user_input) == "user_wins":
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
