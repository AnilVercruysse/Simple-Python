#Practical 18
#ask for user input
#defined function with counter accumulating 'xyz' string
#remove from counter any string 'xyz' preceded by a '.'
#print function

Input = input('Enter a string to apply the function: ')
def xyz(a):
    Counter= 0
    Counter += a.count("xyz")
    Counter-= a.count(".xyz")
    return Counter
print(xyz(Input))
