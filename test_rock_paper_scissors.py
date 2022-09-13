import rps_match


def test_rps_match():
    computer_pick = "rock"
    assert rps_match.rps_match("paper") == "You won!"

