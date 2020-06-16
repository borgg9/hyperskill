import math
import argparse

# Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['diff', 'annuity'])
parser.add_argument('--payment', type=float, default=0)
parser.add_argument('--principal', type=float, default=0)
parser.add_argument('--periods', type=int, default=0)
parser.add_argument('--interest', type=float, default=0)
args = parser.parse_args()

monthly_interest = args.interest / 100 / 12 # Annual in monthly %

# Differential
if args.type == 'diff':
    if args.principal > 0 and args.periods > 0 and args.interest > 0 and args.payment == 0:
        sum_pagos = 0
        for period in range(1, args.periods + 1):
            pago_periodo = (args.principal / args.periods) + monthly_interest * (
                args.principal - ((args.principal * (period - 1)) / args.periods))

            print('Month {}: paid out {}'.format(period, math.ceil(pago_periodo)))
            sum_pagos += math.ceil(pago_periodo)
        print('\nOverpayment = {}'.format(math.ceil(sum_pagos - args.principal)))    
    else:
        print('Incorrect parameters')

#  Annuity
if args.type == 'annuity':
    # Annuity and overpayment?
    if args.principal > 0 and args.periods > 0 and args.interest > 0 and args.payment == 0:
        annuity = args.principal * ((monthly_interest * (1 + monthly_interest)**args.periods) / ((1 + monthly_interest)**args.periods - 1))
        print('Your annuity payment = {}!'.format(math.ceil(annuity)))
        overpayment = (math.ceil(annuity) * args.periods) - args.principal
        print('Overpayment = {}!'.format(math.ceil(overpayment)))

    # Peridos?
    elif args.payment > 0 and args.principal > 0 and args.interest > 0 and args.periods == 0:
        periods = math.log(args.payment / (args.payment - monthly_interest * args.principal), 1 + monthly_interest)
        periods = math.ceil(periods)
        years = periods // 12
        months = periods % 12
        if months == 1: print('You need {} month to repay this credit!'.format(months))
        elif years == 0 and months > 1: print('You need {} months to repay this credit!'.format(months))    
        elif years == 1 and months == 0: print('You need {} year to repay this credit!'.format(years))
        elif years > 1 and months == 0: print('You need {} years to repay this credit!'.format(years))
        elif years >= 1 and months >= 1: print('You need {} years and {} months to repay this credit!'.format(years, months))
        print(f'Overpayment = {math.ceil((args.payment * periods) - args.principal)}')
    
    # Principal¿
    elif args.payment > 0 and args.periods > 0 and args.interest > 0 and args.principal == 0:
        principal = args.payment / ((monthly_interest * (1 + monthly_interest) ** args.periods) / ((1 + monthly_interest) ** args.periods - 1))
        principal = math.ceil(principal)
        print('Your credit principal = {}!',format(principal))
        print('Overpayment = {}'.format(math.ceil((args.payment * args.periods) - principal)))
    
    # Don't following parameters: Error
    else:
        print('Incorrect parameters')
