# calculate monthly payment
def calculate(p: int, months: int, rate: float):
    return (rate/12) * (1/(1-(1+rate/12)**(-months)))*p



