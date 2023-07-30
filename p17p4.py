#Practical 17 - fully based on lecture notes
#Program to check whether a string is a palindromes
# Prompts the user for strings and checks each one
# Exits when an empty string is entered

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
# Start with an empty string
        letterstring = ''
# Go through s...
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring

    def isPal(s):
        if len(s) <= 1:
# A palindrome of length 0 or 1 is a palindrome
            return True
        else:
# Compare the first and the last letters and check the remainder
# of the string
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))

str = input('Enter a string (empty string to exit): ')
while str != '':
    if isPalindrome(str):
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')
        
    str = input('Enter a string (empty string to exit): ')
print('Finished!')

