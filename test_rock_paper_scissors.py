import rps_match
import random

from unittest.mock import MagicMock

random.randint = MagicMock(return_value=0)


def test_rps_match():
    #    computer_pick = "rock"
    assert rps_match.rps_match("paper") == "user_wins"
