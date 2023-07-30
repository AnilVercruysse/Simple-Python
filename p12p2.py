#practical 12
#define fibonacci function for a
#ask for input integer positive and non null
#if negative or null print message
#if positive return fibonacci series


def fibonacci(a):
    f1=0
    f2=1
    fn=0
    counter=1
    while counter <a + 1:
        if counter== 1:
            print('fibonacci term', counter,' = ', f1)
        elif counter== 2:
            print('fibonacci term',counter,' = ', f2)
        else:
            fn = f1 + f2
            f1, f2 = f2, fn
            print('fibonacci term',counter,' = ', fn)
        counter += 1
b= int(input('Enter an integer that is not negative or equal to 0: '))
if b<1:
    print('The integer entered is negative or null')
else:
    fibonacci(b)
