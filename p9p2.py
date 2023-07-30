#practical 9
#while loop continuously asking for input
#in case >=0 use for loop to calculate sum of integers up to input
#print and restart loop
#unless negative value entered: message and break loop


while True:
    try:
        x = int(input('Enter the non-negative integer: '))
        print('You entered: ',x)

        if x>=0:
            a = 1
            i = range(1,x+1)
            for j in i:
                numbers = range(1,j+1)
            print('the total sum is', int(sum(numbers)))
        else:
            print('the integer you entered is negative')
            break
    finally:
            print()
