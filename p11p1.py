#practical 11
#while loop continuously asking for positive integer
#if negative - print and break loop
#any other value: while loop with fact formula from lecture


while True:
    try:
        a = int(input('Enter a positive integer: '))
        if a < 0:
             print('Error, a negative integer was entered')
             break
        else:
                fact= 1
                counter= a
                while 1 < counter:
                        fact *= counter
                        counter -= 1
                print(a, '! =',fact)
    finally:
        print('')
