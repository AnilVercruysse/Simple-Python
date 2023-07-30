#practical 12
#define factorial function for a
#asking for input 
#negative entry triggers message 
#if positive print the factorial with defined function


def factorial(a):
        result=1
        while a > 0:
            result *=a
            a-= 1
        return result
b=int(input('Enter a non-negative integer to proceed: '))
if b<0:
    print('This is a negative integer')
else:
    print(b,'!=', factorial(b))
