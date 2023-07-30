#Practical 18
#user input 
#function detection 'code' 
#print function

Input = input('Enter the string to detect how many times "code" appears: ')

def InputCodeCounter(a):
    return a.count('code')
print(InputCodeCounter(Input))
