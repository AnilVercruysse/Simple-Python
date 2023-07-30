#Practical 19
#defined function to convert to base b, the base of an integer a in base 10 (based on multiple web sources)
#created input for both itnegers checking if they are negative / great than 1
#apply function

print('This program will convert the first base 10 integer you enter to the base of the second integer you enter. Ensure you read the entry requirements')
def Base(a, b):
    conv= []
    while a> 0:
        c= a// b
        d = a% b
        conv.insert(0, d)
        a =c
    result = ''
    for i in conv:
        result += str(i)
    return int(result)
base10 = input('Enter a positive integer in base 10: ')
if int(base10) < 0:
    print('negative entry')
else:
    base10 = int(base10)
convert_base = input('Enter a positive integer of at least 2 to convert previous number to this new base: ')
if int(convert_base) < 1:
    print('Error, entry bellow 2')
else:
    convert_base = int(convert_base)   
print(Base(base10, convert_base))
 
