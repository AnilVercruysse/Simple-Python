#practical 11
#set various counters
#while loop for int input
#if negative warning message and break loop
#if positive use formula from lecture - here we start with 01 and not 11
#print out until term 'n'


f1=0
f2=1
fn=0
counter=1

while True:
    try:
        a = int(input('Enter an integer that is not negative or equal to 0: '))
        if a<1:
            print('Please ensure the input is not negative or equal to zero')
            break
        else:
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
    finally:
        print()
