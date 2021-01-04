import math

from utils import nominal_interest_rate


def calculate_principal(payment: float, periods: float, interest: float) -> float:
    n = periods
    i = nominal_interest_rate(interest)

    principal = payment / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    return principal


def run():
    print('Enter the annuity payment:')
    payment = float(input().strip())

    print('Enter the number of periods:')
    periods = float(input().strip())

    print('Enter the loan interest:')
    interest = float(input().strip())

    principal = calculate_principal(payment, periods, interest)

    print('Your loan principal = {}!'.format(principal))
