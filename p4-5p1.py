#Converting GBP to EUR
#Exchange rate according xe.com on 28/09/22 is 1.00 GBP = 1.1164446 EUR

import sys

gbp_eur_conversion = 1.1164446
gbp_amount = float(input('Enter the GBP amount to convert to EUR '))
eur_amount = gbp_amount*gbp_eur_conversion

if gbp_amount >= 0:
    print('Conversion rate from GBP to EUR:', gbp_eur_conversion)
    print('Amount in GBP:', gbp_amount)
    print('Amount in EUR :', eur_amount)


if gbp_amount < 0:
   sys.exit('Amount must be >= 0. Please try again.')
