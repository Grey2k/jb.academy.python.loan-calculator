import argparse

import calculate_periods
import calculate_principal
import calculate_annuity
import calculate_diff


class ArgumentParserError(Exception): pass


class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)


def positive_float(value):
    i_value = float(value)
    if i_value < 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive float value" % value)
    return i_value


parser = ThrowingArgumentParser(description="Loan Calculator")

parser.add_argument('--type', '-t', choices=['annuity', 'diff'], help='Type of calculation')
parser.add_argument('--principal', '-p', help='Loan Principle', type=positive_float)
parser.add_argument('--periods', '-m', help='Payment periods (months)', type=positive_float)
parser.add_argument('--payment', '-a', help='Monthly payment amount', type=positive_float)
parser.add_argument('--interest', '-i', help='Loan Interest', required=True, default=0, type=positive_float)

TYPE_DIFF = 'diff'
TYPE_ANNUITY = 'annuity'

try:
    args = parser.parse_args()

    if args.type == TYPE_DIFF and args.payment is not None:
        raise argparse.ArgumentError(argument=None, message='Invalid Combination')

    if args.payment is None \
            and args.principal is not None \
            and args.periods is not None \
            and args.interest is not None:

        if args.type == TYPE_ANNUITY:
            calculate_annuity.run(args.principal, args.periods, args.interest)
        else:
            calculate_diff.run(args.principal, args.periods, args.interest)
        exit(0)

    if args.principal is None \
            and args.type == TYPE_ANNUITY \
            and args.payment is not None \
            and args.periods is not None \
            and args.interest is not None:
        calculate_principal.run(args.payment, args.periods, args.interest)
        exit(0)

    if args.periods is None \
            and args.type == TYPE_ANNUITY \
            and args.principal is not None \
            and args.payment is not None \
            and args.interest is not None:
        calculate_periods.run(args.principal, args.payment, args.interest)
        exit(0)

    raise argparse.ArgumentError(argument=None, message='Invalid Combination')

except ArgumentParserError as e:
    print('Incorrect parameters')
    # raise e
