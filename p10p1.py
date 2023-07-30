#practical 10
#loop to input integer
#if input positive - while exhaustive enumeration loop based on lecture notes to find square root
#sub option for numbers that are not perfect squares
#exception for negative numbers with message




while True:
     try:
          a = int(input('Enter a positive integer: '))
          if a > -1:
               counter= 0
               while counter**2 <=a:
                    if a != counter**2:
                         counter +=1
                    else:
                         print(a, ' = ', counter,'^2')
                         break
               else:
                    print(a, ' isnt a perfect square')
          else:
               print("Error this is a negative integer")
               break
     finally:
          print('')

