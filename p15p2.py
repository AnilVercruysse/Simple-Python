#Practical 15
#define function based on sheet
#define function to print progression
#while loop asking for input 
#result or exit if negative

import sys
def fn(a):
    if a== 1:
        return 1
    else:
        return fn(a- 1)+2**(a-1)
def fn2(b):
    for i in range(1, b+ 1):
        if i== 1:
            print('fn(',i,') is ',fn(i),)
        else:
            print('fn(',i,') is ',fn(i), ' is ','fn(',(i-1),')+2 in the power of(',i,'-1)')
    return 
while True:
    try:
        c= int(input('Enter an integer greater than 1. Enter a null or negative integer to exit: '))
        if 0 <c:
            print(fn2(c))
        else:
            print('Program exited')
            sys.exit()
    finally:
        print()
