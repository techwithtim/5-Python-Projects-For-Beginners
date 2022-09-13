import random

options = ["rock", "paper", "scissors"]


def rps_match(user_input_param):

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input_param == "rock" and computer_pick == "scissors":
        return "user_wins"

    elif user_input_param == "paper" and computer_pick == "rock":
        return "user_wins"

    elif user_input_param == "scissors" and computer_pick == "paper":
        return "user_wins"

    else:
        return "computer_wins"
