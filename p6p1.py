#Practical sheet 6
#Pseudocode section

#input numbers x and y
#if x + y > 100 -> print sum result and "That is a big number" and exit program
#if x + y <= 100 -> print sum result and exit program

#python code section

import sys

number_x = float(input('Enter number x '))
number_y = float(input('Enter number y '))

sum_of_x_and_y = number_x + number_y

if sum_of_x_and_y > 100:
    print(sum_of_x_and_y)
    sys.exit('That is a big number!')
else: 
    sys.exit(sum_of_x_and_y)
