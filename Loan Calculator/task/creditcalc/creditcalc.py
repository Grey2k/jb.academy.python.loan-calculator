import math

import calculate_periods
import calculate_principal
import calculate_annuity

###
COMMAND_CALCULATE_PERIOD = 'n'
COMMAND_CALCULATE_ANNUITY_PAYMENT = 'a'
COMMAND_CALCULATE_PRINCIPAL = 'p'


def welcome_command(command: str) -> None:
    if command == COMMAND_CALCULATE_PRINCIPAL:
        calculate_principal.run()

    if command == COMMAND_CALCULATE_PERIOD:
        calculate_periods.run()

    if command == COMMAND_CALCULATE_ANNUITY_PAYMENT:
        calculate_annuity.run()


print('What do you want to calculate?')
print('type "{}" for number of monthly payments,'.format(COMMAND_CALCULATE_PERIOD))
print('type "{}" for annuity monthly payment amount,'.format(COMMAND_CALCULATE_ANNUITY_PAYMENT))
print('type "{}" for loan principal:'.format(COMMAND_CALCULATE_PRINCIPAL))

cmd = input().strip()

welcome_command(cmd)
