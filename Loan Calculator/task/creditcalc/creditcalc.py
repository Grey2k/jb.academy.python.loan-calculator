import math

###
interest = 0

COMMAND_BY_PERIODS = 'p'
COMMAND_BY_MONTHLY_PAYMENT = 'm'


def welcome_command(command: str) -> None:
    if command == COMMAND_BY_MONTHLY_PAYMENT:
        print('Enter the monthly payment:')

    if command == COMMAND_BY_PERIODS:
        print('Enter the number of months:')


def count_payments(months: int) -> None:
    if principal % months == 0:
        monthly = principal / months
        print('Your monthly payment = {monthly}'.format(monthly=monthly))
        return

    monthly = math.ceil(principal / months)

    last_month = principal - ((months - 1) * monthly)

    print('Your monthly payment = {monthly} and the last payment = {last_month}.'.format(
        monthly=monthly, last_month=last_month
    ))


def count_months(payment: int) -> None:
    months = math.ceil(principal / payment)

    print('It will take {months} {plural} to repay the loan'.format(
        months=months, plural='months' if months > 1 else 'month'
    ))


def run_command(command, param) -> None:
    if command == COMMAND_BY_MONTHLY_PAYMENT:
        count_months(payment=param)

    if command == COMMAND_BY_PERIODS:
        count_payments(months=param)


print('Enter the loan principal:')
principal = int(input().strip())

print('What do you want to calculate?')
print('type "m" for number of monthly payments,')
print('type "p" for the monthly payment')

cmd = input().strip()

welcome_command(cmd)

run_command(cmd, int(input().strip()))
