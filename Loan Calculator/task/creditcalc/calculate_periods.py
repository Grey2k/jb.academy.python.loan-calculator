import math

from utils import nominal_interest_rate


def calculate_months(principal: float, payment: float, interest: float) -> int:
    interest_rate = nominal_interest_rate(interest)

    x = payment / (payment - interest_rate * principal)
    months = math.log(x, 1 + interest_rate)

    return math.ceil(months)


def months_to_period(period_months: int) -> str:
    years = period_months // 12
    months = period_months % 12

    if years == 0:
        return '{months} {months_plural}'.format(
            months=months, months_plural='month' if months == 1 else 'months',
        )

    return '{years} {years_plural} and {months} {months_plural}'.format(
        years=years, years_plural='year' if years == 1 else 'years',
        months=months, months_plural='month' if months == 1 else 'months',
    )


def run():
    print('Enter the loan principal:')
    principal = float(input().strip())

    print('Enter the monthly payment:')
    payment = float(input().strip())

    print('Enter the loan interest:')
    interest = float(input().strip())

    months = calculate_months(principal, payment, interest)

    print('It will take {period}'.format(period=months_to_period(months)))
