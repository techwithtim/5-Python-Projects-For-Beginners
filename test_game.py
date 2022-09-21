from tud_test_base import set_keyboard_input, get_display_output
import game


def test_game():

    set_keyboard_input(["paper"])
    game.game()
    output = get_display_output()

    assert output == ["valami","valami"]
