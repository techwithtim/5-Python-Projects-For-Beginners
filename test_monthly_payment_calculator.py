from monthly_payment_calculator import calculate


def test_calculate_egymillio_negyev_tizszazalek():
    assert round(calculate(1000000, 48, 0.1)) == 25363
