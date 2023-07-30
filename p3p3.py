#Practical Sheet Exercise 3 relating to tax computation
#Amounts are expressed in EUR

initial_amount = 222024.74
first_tax_bracket = initial_amount*0.6
second_tax_bracket = initial_amount*0.4
total_tax_liability = (first_tax_bracket*0.135)+(second_tax_bracket*0.23)
total = initial_amount+total_tax_liability

print('Initial Amount of EUR',initial_amount,'+','Tax Liability of EUR',total_tax_liability,'=','TOTAL of EUR',total)

