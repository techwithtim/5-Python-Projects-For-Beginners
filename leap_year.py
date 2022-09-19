#függvény, aminek egy bemenete van, és egy kimenete, a bemenet az évszám,
#kimenet pedig igaz vagy hamis, igaz, ha szökőév, hamis, ha nem az.

def leap_year(year: int):
    if year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

