import math

from utils import nominal_interest_rate, overpayment


def calculate_months(principal: float, payment: float, interest: float) -> int:
    interest_rate = nominal_interest_rate(interest)

    x = payment / (payment - interest_rate * principal)
    months = math.log(x, 1 + interest_rate)

    return math.ceil(months)


def months_to_period(period_months: int) -> str:
    years = period_months // 12
    months = period_months % 12

    periods = []

    if years > 0:
        periods.append('{years} {years_plural}'.format(
            years=years, years_plural='year' if years == 1 else 'years'
        ))

    if months > 0:
        periods.append('{months} {months_plural}'.format(
            months=months, months_plural='month' if months == 1 else 'months',
        ))

    return ' and '.join(periods)


def run(principal: float, payment: float, interest: float) -> None:
    months = calculate_months(principal, payment, interest)
    overpay = overpayment(principal, math.ceil(months) * payment)

    print('It will take {period} to repay this loan!'.format(period=months_to_period(months)))
    print('Overpayment {}'.format(math.ceil(overpay)))
