import math


def nominal_interest_rate(interest_percent: float) -> float:
    return interest_percent / (100 * 12)


def annuity_payment(principal: float, payments: float, n_interest_rate: float) -> float:
    i = n_interest_rate
    n = payments

    annuity = principal * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
    return annuity
