import math
import argparse


def number_monthly_payments(loan_principal, monthly_payment, loan_interest):
    def month_to_year(month_all):
        year = month_all // 12
        month = month_all % 12
        str_and = ' and ' if year and month else ''
        s_year = 's' if year > 1 else ''
        str_year = f'{year} year{s_year}' if year else ''
        s_month = 's' if month > 1 else ''
        str_month = f'{month} month{s_month}' if month else ''
        print(f'It will take {str_year}{str_and}{str_month} to repay this loan!')

    nominal_interest = loan_interest / (12 * 100)
    n = (monthly_payment / (monthly_payment - nominal_interest * loan_principal))
    number_payment = math.ceil(math.log(n, 1 + nominal_interest))
    month_to_year(number_payment)
    print(f'Overpayment ={math.ceil(monthly_payment * number_payment - loan_principal)}')


def monthly_payment(loan_principal, number_period, loan_interest):
    nominal_interest = loan_interest / (12 * 100)
    first = nominal_interest * ((1 + nominal_interest) ** number_period)
    second = ((1 + nominal_interest) ** number_period) - 1
    annuitly_payment = math.ceil(loan_principal * (first / second))
    print(f'Your annuity payment = {annuitly_payment}!')
    print(f'Overpayment = {math.ceil(number_period * annuitly_payment - loan_principal)}')


def loan_principal(annuity_payment, number_period, loan_interest):
    nominal_interest = loan_interest / (12 * 100)
    first = nominal_interest * (1 + nominal_interest) ** number_period
    second = ((1 + nominal_interest) ** number_period) - 1
    loan_principal = math.floor(annuity_payment / (first / second))
    print(f'Your loan principal = {loan_principal}!')
    print(f'Overpayment ={math.ceil(annuity_payment * number_period - loan_principal)}')


def incorrect():
    print('Incorrect parameters')


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()
ctype, cprincipal, cperiod, cinterest, cpayment = args.type, args.principal, args.periods, args.interest, args.payment
clist = [ctype, cprincipal, cperiod, cpayment, cinterest]
if clist.count(None) == 1 and cinterest and cinterest > 0:
    if ctype == 'diff':
        if cprincipal and cprincipal > 0 and cperiod and cperiod > 0:
            interest = cinterest / (12 * 100)
            payments_list = []
            for i in range(1, cperiod + 1):
                first = cprincipal - (cprincipal * (i - 1) / cperiod)
                payments_list.append(math.ceil((cprincipal / cperiod) + interest * first))
                print(f'Month {i}: payment is {payments_list[-1]}')
            print()
            print(f'Overpayment = {math.ceil(sum(payments_list) - cprincipal)}')
        else:
            incorrect()
    elif ctype == 'annuity':
        if cprincipal is None:
            loan_principal(cpayment, cperiod, cinterest)
        if cperiod is None:
            number_monthly_payments(cprincipal, cpayment, cinterest)
        if cpayment is None:
            monthly_payment(cprincipal, cperiod, cinterest)
    else:
        incorrect()
else:
    incorrect()
