#Practical 19
#defined function including list for hexa case
#power alines to lenght of string - 1
#for loop applying conversion
#user input and print
#based on multiple web sources

def decimal(string_input, base):
    hexa_letters = 'abcdefABCDEF'
    power= len(string_input) -1
    counter= 0
    for a in string_input:
        if a in hexa_letters:
            a = hexa_letters.index(a.lower()) + 10
        a = int(a)
        counter += a*(base *power)
        power -= 1
    return counter

string = input('Enter a string of numbers to convert it to decimal version: ')
base = int(input('Enter the base of the string: '))
print('Your result is: ',decimal(string, base))


