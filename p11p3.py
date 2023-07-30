#practical 11
#while loop continuously asking for input
#set counters and range - here we use 01 as starting terms for fibonacci series
#if <=0 - exit with message
#for loop based on lecture slides



while True:
    try:
        a = int(input('Enter an integer that is not negative or equal to 0: '))
        f1=0
        f2=1
        fn=0
        range_a=range(1,a+1,1)
        if a<=0:
            print('Please ensure the input is not negative or equal to zero')
            break
        else:
            for b in range_a:
                if b== 1:
                    print('fibonacci term',b,' = ', f1)
                elif b== 2:
                    print('fibonacci term',b,' = ', f2)
                else:
                    fn = f1 + f2
                    f1, f2 = f2, fn
                    print('fibonacci term',b,' = ', fn)
                b += 1
    finally:
        print()
