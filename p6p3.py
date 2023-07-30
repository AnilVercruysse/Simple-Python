#Practical 6
#pseudocode section:

#input string for name
#check if name is mine (Anil), if so print relevant message and exit
#if above not true, check if name is M.M. or S.S., if so print relevant message and exit
#if above not true, create condition for all other cases with relevant message and exit

import sys

name = str(input('Enter your name '))

if name == ('Anil'):
    sys.exit('That is a cool name')
elif name == ('Mickey Mouse'):
    sys.exit('I am not sure about that name')
elif name == ('Spongebob Squarepants'):
    sys.exit('I am not sure about that name')
else:
    sys.exit('You have a nice name')

