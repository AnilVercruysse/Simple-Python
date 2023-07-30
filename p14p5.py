#practical 14
#define fibonacci function
#define recursive function
#user input
#print result if non negative



def Fibonacci(a):
    if a== 0:
        return a
    elif a== 1:
        return a
    else:
        return Fibonacci(a- 2) + Fibonacci(a- 1)

def RF2(b):
    for i in range(0,b+ 1, 1):
        if i == 0:
            print('Fibonacci of 0 is 0')
        elif i == 1:
            print('Fibonacci of 1 is 1')
        else:
                    print('Fibonacci(',i,') is ', Fibonacci(i),'is Fibonacci(',i-2,')+','Fibonacci(',(i-1),')')
    return 

d= int(input('Enter a non-negative integer: '))
if -1 <d:
    print(RF2(d))
else:
    print('Negative integer')

