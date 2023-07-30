#Converting GBP to EUR
#Exchange rate according xe.com on 24/09/22 is 1.00 GBP = 1.1197943 EUR


gbp_eur_conversion = 1.1197943
gbp_amount = float(input('Enter the GBP amount to convert to EUR '))
eur_amount = gbp_amount*gbp_eur_conversion

print('Conversion rate from GBP to EUR:', gbp_eur_conversion)
print('Amount in GBP:', gbp_amount)
print('Amount in EUR :', eur_amount)

