from math import ceil

from utils import nominal_interest_rate, annuity_payment, overpayment


def calculate_annuity_payment(principal: float, periods: float, interest: float) -> float:
    interest_rate = nominal_interest_rate(interest)
    return annuity_payment(principal, periods, interest_rate)


def run(principal: float, periods: float, interest: float) -> None:
    payment = ceil(calculate_annuity_payment(principal, periods, interest))
    overpay = overpayment(principal, periods * payment)

    print('Your monthly payment = {}!'.format(payment))
    print('Overpayment {}'.format(ceil(overpay)))
