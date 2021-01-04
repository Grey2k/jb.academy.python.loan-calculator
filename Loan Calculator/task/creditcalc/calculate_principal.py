import math

from utils import nominal_interest_rate, overpayment


def calculate_principal(payment: float, periods: float, interest: float) -> float:
    n = periods
    i = nominal_interest_rate(interest)

    principal = payment / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    return principal


def run(payment: float, periods: float, interest: float) -> None:
    principal = calculate_principal(payment, periods, interest)
    overpay = overpayment(principal, periods * payment)

    print('Your loan principal = {}!'.format(int(principal)))
    print('Overpayment {}'.format(math.ceil(overpay)))
