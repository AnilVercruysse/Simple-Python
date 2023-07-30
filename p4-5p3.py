#Practical Sheet 4.5 Exercise 3 relating to tax computation
#Amounts are expressed in EUR

import sys

initial_amount = float(input('Enter the amount '))
first_tax_bracket = (initial_amount*0.6)*0.23
second_tax_bracket = (initial_amount*0.4)*0.41
total_tax_liability = (first_tax_bracket)+(second_tax_bracket)
total = initial_amount+total_tax_liability

if initial_amount >= 0:
    print('Initial Amount of EUR:',initial_amount)
    print('Tax Amount I of EUR :',first_tax_bracket)
    print('Tax Amount II of EUR:',second_tax_bracket)
    print('Total Tax Liability of EUR',total_tax_liability)
    print()
    print('TOTAL EUR =', total)

if initial_amount < 0:
   sys.exit('Amount must be >= 0. Please try again.')
