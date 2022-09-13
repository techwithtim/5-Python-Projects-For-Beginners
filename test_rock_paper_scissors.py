import rock_paper_scissors
from rock_paper_scissors import rps_match


def test_rps_match():
    computer_pick = "rock"
    assert rock_paper_scissors.rps_match("paper") == "You won!"

