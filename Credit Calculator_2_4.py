credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)

import math

credit_principal = float(input('Enter the credit principal:'))

calcu = input("""What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment""")

if calcu == 'm':
    months = int(input('Enter monthly payment:'))
    print('It takes %s month to repay the credit' % (round((credit_principal / months))))

elif calcu == 'p':
    months = int(input('Enter count of months:'))
    
    if months * math.ceil(credit_principal / months) > credit_principal:
        print('Your monthly payment = %s with last month payment = %s.' % (math.ceil(credit_principal / months), math.ceil(credit_principal / months + (credit_principal - math.ceil(credit_principal / months) * months))))
    else:
        print('Your monthly payment = %s' % (round(credit_principal / months)))
