#Practical 15
#define function based on info from sheet
#define 2nd function to print progression
#while loop asking for input with exit if null/negative
#prints result or exit


import sys
def fn(a):
    if a== 1:
        return 2
    else:
        return a + fn(a- 1)
def fn2(b):
    for i in range(1, b+ 1):
        if i== 1:
            print('fn(',i,') is ',fn(i),)
        else:
            print('fn(',i,') is ',fn(i), ' is ',i, ' + ',(fn(i) - i),' is ',i,'+ ','fn(',(i -1),')')
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
