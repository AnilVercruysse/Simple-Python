#Practical 6
#Pseudocode section
#set initial count
#create loop with under 4 count condition to enter password and display relevant messages
#created condition to deny access at 4th count

#Python code

import sys

count=0

while count<4:
    password=input('Enter password: ')
    if password=='malala saved us':
        sys.exit('You have been successfully logged in')
    else:
        print('Incorrect password')
        count+=1
if count >=4:
    sys.exit('You have been denied acces')
