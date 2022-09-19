from monthly_payment_calculator import calculate


def test_calculate():
    assert round(calculate(1000000, 48, 0.1)) == 25363
