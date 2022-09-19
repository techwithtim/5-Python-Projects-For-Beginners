import pytest

from monthly_payment_calculator import calculate


def test_calculate_egymillio_negyev_tizszazalek():
    assert round(calculate(1000000, 48, 0.1)) == 25363


def test_calculate_negymillio_tizev_tizszazalek():
    assert round(calculate(4000000, 120, 0.1)) == 52860


def test_calculate_hárommillio_ötev_tizenketszazalek():
    assert round(calculate(3000000, 60, 0.12)) == 66733


def test_calculate_nulla_negyev_tizszazalek():
    assert round(calculate(0, 48, 0.1)) == 0


def test_calculate_egymillio_negyev_nullaszazalek():
    assert round(calculate(1000000, 48, 0)) == 20833


def test_calculate_egymillio_nulla_tizszazalek():
    with pytest.raises(ZeroDivisionError):
        assert round(calculate(1000000, 0, 0.1)) == 25363