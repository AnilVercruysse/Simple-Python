#Practical sheet 5 Exercise 4

initial_amount = int(input('Enter the amount '))

if initial_amount == 0:
    print('Number is equal to 0')
if 0 < initial_amount <= 20:
    print('Number is greater than 0 and less than or equal to 20')
if 20 < initial_amount <= 40:
    print('Number is greater than 20 and less than or equal to 40')
if 40 < initial_amount <= 60:
    print('Number is greater than 40 and less than or equal to 60')
if 60 < initial_amount <= 80:
    print('Number is greater than 60 and less than or equal to 80')
if 80 < initial_amount <= 100:
    print('Number is greater than 80 and less than or equal to 100')
if 100 < initial_amount:
    print('Number is greater than 100')
if initial_amount < 0:
    print('the integer entered has a negative value')
