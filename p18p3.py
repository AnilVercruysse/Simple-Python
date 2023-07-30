#Practical 18
#define function including variations for 'code'
#for loop checking for each variation 
#print result

Input = input('Enter the string to detect how many times "code" and its variations appears: ')

def InputCodeCounter(a):
    variants='ABCDEFGHIJKLMNOPQRSTUWXYZabcdefghijklmnopqrstuvwxyz'
    Count = 0
    for i in variants:
        code = 'co' + i +'e'
        Count +=a.count(code)
    return Count
print(InputCodeCounter(Input))
