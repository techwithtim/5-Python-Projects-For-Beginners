from tud_test_base import set_keyboard_input, get_display_output
from divisibility import divisibility


def test_divisibility_none():
    set_keyboard_input([3])
    divisibility()
    assert get_display_output() == [' Please Enter any Positive Integer : ', "Given Number 3 is Not Divisible by 5 and 11"]


def test_divisibility_only_5():
    set_keyboard_input([15])
    divisibility()
    assert get_display_output() == [' Please Enter any Positive Integer : ', "Given Number 15 is Not Divisible by 5 and 11"]


def test_divisibility_only_11():
    set_keyboard_input([22])
    divisibility()
    assert get_display_output() == [' Please Enter any Positive Integer : ', "Given Number 22 is Not Divisible by 5 and 11"]


def test_divisibility_both():
    set_keyboard_input([55])
    divisibility()
    assert get_display_output() == [' Please Enter any Positive Integer : ', "Given Number 55 is Divisible by 5 and 11"]
