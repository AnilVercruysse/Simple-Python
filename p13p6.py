#practical 13
#copied from last slide lecture 15
#defined function factorial
#ask for input
#if negative error
#if non-negative: proceed with function
#note: couldnt figure out part (c) of the question

def fact(x):
    if x== 0:
        return 1
    else:
        return x * fact(x - 1)

a=int(input('Enter a non negative integer: '))

if a<0:
    print('Error, negative integer entered')
else:
    print('the factorial of',a,'is',fact(a))
