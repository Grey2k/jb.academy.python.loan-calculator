import math

from utils import nominal_interest_rate, overpayment


def calculate_monthly_payment(principal: float, interest: float, periods: int, current_month: int) -> float:
    i = nominal_interest_rate(interest)
    p = principal
    n = periods
    m = current_month
    diff_payment = p / n + i * (p - (p * (m - 1)) / n)

    return diff_payment


def run(principal: float, periods: float, interest: float) -> None:
    total = 0

    for i in range(int(periods)):
        payment = calculate_monthly_payment(principal, interest, int(periods), i + 1)

        total += math.ceil(payment)
        print('Month {month}: payment is {payment}'.format(month=i + 1, payment=math.ceil(payment)))

    overpay = overpayment(principal, total)
    print("\nOverpayment {}".format(math.ceil(overpay)))
