from math import ceil

from utils import nominal_interest_rate, annuity_payment


def calculate_annuity_payment(principal: float, periods: float, interest: float) -> float:
    interest_rate = nominal_interest_rate(interest)
    return annuity_payment(principal, periods, interest_rate)


def run():
    print('Enter the loan principal:')
    principal = float(input().strip())

    print('Enter the number of periods:')
    periods = float(input().strip())

    print('Enter the loan interest:')
    interest = float(input().strip())

    payment = calculate_annuity_payment(principal, periods, interest)

    print('Your monthly payment = {}!'.format(ceil(payment)))
