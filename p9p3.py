#practical 9
#ask for user input 
#first if to exclude negatives
#else possibility a = if 0 or 1 return result of 1
#else possibility b= for loop adapted from lecture to find factorial


a = int(input('Enter a positive integer: '))

if a < 0:
     print('Error negative integer')
else:
     fact =1
     if a==0 or  a==1:
          print(a, '! = ', fact)
     else:
          for n in range(1, a + 1, 1):
               fact *= n
          print(a, '! = ' , fact)
