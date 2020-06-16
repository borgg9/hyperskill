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

calcu = input("""What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal: 
""")

if calcu == 'n':
    P = float(input('Enter the credit principal:'))
    A = ((int(input('Enter monthly payment: '))) )
    i = (((float(input('Enter credit interest: '))) / 12) / 100)
    
    n_pagos = math.log((A / (A - i * P)), (1 + i))
    a = (n_pagos) / 12
    b = math.floor(a) # years
    c = a - b
    d = c * 12
    e = math.ceil(d) # months
    
    if a >= 1:
        if e == 0:
            print('You need {} months to repay this credit!'.format(str(e)))
        elif e == 12:
            f = b + 1
            print('You need {} years to repay this credit!'.format(str(f)))
        else:
            print('You need {} years and {} months to repay this credit!'.format(str(b), str(e)))
    else:
        print('You need {} months to repay this credit!'.format(str(e)))
        

if calcu == 'a':
    P = float(input('Enter the credit principal:'))
    n = ((int(input('Enter count of periods: '))) )
    i = (((float(input('Enter credit interest: '))) / 12) / 100)
    A = P * ((i * (1+i)**n) / (((1+i)**n) - 1))
    print('Your annuity payment = {}!'.format(math.ceil(A)))

    
if calcu == 'p':
    A = float(input('Enter monthly payment:'))
    n = ((int(input('Enter count of periods: '))) )
    i = (((float(input('Enter credit interest: '))) / 12) / 100)
    P = A / ((i * ((1 + i) ** n)) / (((1 + i) ** n) - 1))
    print('Your credit principal = {}!'.format(round(P)))
