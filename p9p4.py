#practical 9
#while loop repeatidly asking for input
#if input negative close with message
#if input 0 or 1 factorial returned is 1
#while loop based on lecture notes returning factorial 

while True:
    try:
        a = int(input('Enter a positive integer: '))
        if a<0:
            print('This is a negative integer')
            break
        else:
            while a >-1:
                fact= 1
                if a==0 or a== 1:
                    print(a, '! = ', fact)
                else:
                     i = 1
                     while i <a + 1:
                         fact *= i
                         i+=1
                     print(a,'! = ', fact)
                break
    finally:
        print('')
