import rps_match
import random

from unittest.mock import MagicMock


def test_rps_match_paper_rock():
    random.randint = MagicMock(return_value=0)
    assert rps_match.rps_match("paper") == "user_wins"


def test_rps_match_paper_paper():
    random.randint = MagicMock(return_value=1)
    assert rps_match.rps_match("paper") == "nobody wins"


def test_rps_match_paper_scissors():
    random.randint = MagicMock(return_value=2)
    assert rps_match.rps_match("paper") == "computer_wins"


def test_rps_match_scissors_rock():
    random.randint = MagicMock(return_value=0)
    assert rps_match.rps_match("scissors") == "computer_wins"


def test_rps_match_scissors_paper():
    random.randint = MagicMock(return_value=1)
    assert rps_match.rps_match("scissors") == "user_wins"


def test_rps_match_scissors_scissors():
    random.randint = MagicMock(return_value=2)
    assert rps_match.rps_match("scissors") == "nobody wins"


def test_rps_match_rock_rock():
    random.randint = MagicMock(return_value=0)
    assert rps_match.rps_match("rock") == "nobody wins"


def test_rps_match_rock_paper():
    random.randint = MagicMock(return_value=1)
    assert rps_match.rps_match("rock") == "computer_wins"


def test_rps_match_rock_scissors():
    random.randint = MagicMock(return_value=2)
    assert rps_match.rps_match("rock") == "user_wins"

