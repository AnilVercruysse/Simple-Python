#practical 8
#loop asking for input until number is negative
#check divisibility by 2 3 5 7 and print accordingly
#message in case of negative integer


print('Program to check if the number you entered is divisible by 2,3,5, and 7')

while True:
    try:
        a = 1
        while a>-1:
            a = int(input('Enter the non-negative integer: '))
            print('You entered: ',a)
            if a<0:
                break
            if a%2==0:
                print('the number is divisible by 2')
            if a%3==0:
                print('the number is divisible by 3')
            if a%5==0:
                print('the number is divisible by 5')
            if a%7==0:
                print('the number is divisible by 7')
        break
    finally:
        print('Error a negative integer was entered')
