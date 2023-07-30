#Practical 17 - fully based on slides and sheet
#defines function explaining in detail the process for palindrome analysis
#   function implements same palindrome check as previous exercise



def isPal(s):
    print('isPal function called with argument', s)
    if len(s) <= 1:
# A palindrome of length 0 or 1 is a palindrome
        print('About to return True from isPal from the base case')
        return True
    else:
# Compare the first and the last letters and check the remainder of the string
        result = s[0] == s[-1] and isPal(s[1:-1])
        print('About to return result', result, 'from isPal with argument', s)
        return result

str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPal(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
        
    str = input('Enter a string (empty string to exit): ')
print('Finished!')
