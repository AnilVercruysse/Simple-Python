#practical 13
#implemented program from slide 5 lecture 15
#define max function
#ask for user input
#print result applying max function with max function in print instruction


def max(a, b):
    if a > b:
        return a
    else:
        return b

number_a = float(input('Enter the first float: '))

number_b = float(input('Enter the second float: '))

print('The largest of the two numbers entered is', max(number_a, number_b))

print('Finished!')
