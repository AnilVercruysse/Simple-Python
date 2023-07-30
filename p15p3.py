#Practical 15
#define function from sheet 
#define function to print progression
#while loop user input
#print or exit 



import sys
def fn(a):
    if a==0:
        return 13
    elif a==1:
        return 8
    else:
        return fn(a- 2)+13*fn(a-1)
def fn2(b):
    for i in range(0, b+ 1):
        if i== 1:
            print('fn(',i,') is ',fn(i),)
        elif i==0:
            print('fn(',i,') is ',fn(i),)
        else:
            print('fn(',i,') is ',fn(i), ' is ','fn(',(i-2),')+13*fn(',(i - 1),')')
    return 
while True:
    try:
        c= int(input('Enter an integer greater than -1. Enter a negative integer to exit: '))
        if -1 <c:
            print(fn2(c))
        else:
            print('Program exited')
            sys.exit()
    finally:
        print()
