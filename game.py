import rps_match
from rps_match import options


def game():
    user_wins = 0
    computer_wins = 0

    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input not in options:
            continue

        result = rps_match.rps_match(user_input)

        if result == "user_wins":
            print("You won!")
            user_wins += 1

        elif result == "computer_wins":
            print("You lost!")
            computer_wins += 1
        else:
            print("Nobody wins!")

    print("You won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")
    print("Goodbye!")

