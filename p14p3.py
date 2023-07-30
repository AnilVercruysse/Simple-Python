#Practical 14 - copied from lecture 13 page 16
#Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers
#prime = a number that is divisible only by itself and 1


for number in range(2, 20):
    for i in range(2, number):
        if number % i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        print(number, 'is a prime number')
print('Finished!')
