from leap_year import leap_year


def test_leap_year_divisible_by_4():
    assert leap_year(4) == True
    assert leap_year(8) == True
    assert leap_year(12) == True
    assert leap_year(16) == True


def test_leap_year_divisible_by_100():
    assert leap_year(100) == False
    assert leap_year(200) == False
    assert leap_year(500) == False
    assert leap_year(1000) == False
    assert leap_year(2000) == False





