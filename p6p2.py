#Practical sheet 6
#Pseudocode section

#input integers a, b and c
#first check if a is even, if so, check if b is even, if so, check if c is even, if so 'all even'
#if a even, b even, c not - c largest odd
#if a even, b not, c not even but less than b or c even, b largest odd
#if a even, b not, c not and larger than b, c largest odd
#if b even, c even or smaller than a, which is odd, a largest odd
#if b even, c not and a not but smaller than c, print c
#if c even, a and b not, but b smaller than a, print a
#if c even, a and b not, but a smaller than b, print b
#if a, b, c odd and a largest, print a
#if a, b, c odd and b largest, print b
#if a,b ,c off and c largest, print c


#python code section

import sys

a = int(input('Enter integer a '))
b = int(input('Enter integer b '))
c = int(input('Enter integer c '))



if a%2 == 0:
    if b%2 == 0:
        if c%2 == 0:
            sys.exit('All the integers entered are even')
        else:
            print('the largest odd integer is',c)
            sys.exit()
    elif b > c or c%2 == 0:
        print('the largest odd integer is',b)
        sys.exit()
    else:
        print('the largest odd integer is',c)
        sys.exit()
elif b%2 == 0:
    if c%2 == 0 or a > c:
        print('the largest odd integer is',a)
        sys.exit()
    else:
        print('the largest odd integer is',c)
        sys.exit()
elif c%2 == 0:
    if a > b:
        print('the largest odd integer is',a)
        sys.exit()
    else:
        print('the largest odd integer is',b)
        sys.exit()
else:
    if a > b and a > c:
        print('the largest odd integer is',a)
        sys.exit()
    elif b > c:
        print('the largest odd integer is',b)
        sys.exit()
    else:
        print('the largest odd integer is',c)
        sys.exit()
