#Practical 6
#Pseudocode section
#input password
#right or wrong condition
#if right sucess message
#if wrong start loop to 3 correct entry - 1 incorrect = termination

#Python code

import sys

password=input('Enter password: ')

if password=='html':
    sys.exit('You have been successfully logged in')

elif password!='html':
    print('Sorry, the password is wrong')
    counter = 0
    while counter <3:
        password_a=(input('Enter password (three correct entries required): '))
        if password_a=='html':
            counter+=1
            if counter==3:
                    sys.exit('You have been successfully logged in')
        elif password_a!='html':
           sys.exit('You have been denied acces')






