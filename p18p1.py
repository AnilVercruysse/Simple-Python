#Practical 18
#ispals function from previous sheet and adapted in iterative form
#same input structure as previous sheet


def isPal(s):
    print('isPal function called with argument', s)
    if len(s) <= 1:
        print('About to return True from isPal from the base case')
        return True
    else:
        for i in range(0,(len(s)//2)+1):
            if s[i]==s[-i-1]:
                pass
            else:
                return False
        return True

str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPal(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
        
    str = input('Enter a string (empty string to exit): ')
print('Finished!')
