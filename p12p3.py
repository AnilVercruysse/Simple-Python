#practical 12
#define squarerootfinder function (copied from lecture 12)
#create user input for float to execute function
#create user input for margin of tolerance 
#execute function with variables


def squarerootfinder(a,epsilon):
    step=epsilon**2
    root=0.0
    numguess=0
    while epsilon<=abs(a-root**2) and root**2<=a:
        root+=step
        numguess+=1
        if numguess%100000==0:
            print('Still running. Number of guesses:', numguess)
        else:
            pass
    print('Number of guesses:', numguess)
    if abs(a -root**2)<epsilon:
            print('The approximate square root of',a, 'is equal to',root)
    else:
        print('Failed to print the square root of ',a)
    print('Finished')

b = float(input('Enter a positive float for which you want the square root: '))
if b<0:
    print('the program can only run on a positive float')
userepsilon= float(input('Enter a positive float for your margin of tolerance: '))
if userepsilon <0:
    print('a positive value is required')
elif userepsilon==0:
    print('a null margin of tolerance cannot be executed')
squarerootfinder(b,userepsilon)
