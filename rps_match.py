import random


def rps_match(user_input_param):
    
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

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