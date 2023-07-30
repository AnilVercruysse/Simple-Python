#Practical 16
#define function based on sheet info
#define function printing progression
#while loop asking for input
#if not smaller than 1 proceed, if so exit

import sys
def fn(a):
    if a== 1:
        return 2
    else:
        return fn(a-1)*2

def FnProg(b):
    for i in range(1, b+1):
        if i==1:
            print('fn(',i,') is ',fn(i))
        else:
            print('fn(',i,') is ',fn(i),' is 2*','fn(',(i-1),')')
while True:
    try:
        c = int(input('Enter an integer greater than null to continue or smaller than 1 to exit: '))
        if 0 <c:
            print(FnProg(c))
        else:
            print('Program exited')
            sys.exit()
    finally:
        print('thanks')
     
