#practical 13
#copied from lecture 15 
#define the print_max function
#within this, define the max fuction 
#asks for user input and prints
#whole function can be executed with just print_max()

def print_max():
    def max(a, b):
        if a > b:
            return a
        else:
            return b

    number_a = float(input('Enter the first float: '))

    number_b = float(input('Enter the second float: '))

    print('The largest of the two numbers entered is', max(number_a, number_b))

    return

print_max()



