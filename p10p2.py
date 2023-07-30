#practical 10
#while loop continuously asking for integer
#if negative while loop : formula to find cube root and option in case not eprfect
#if positive similar adapted loop with also option in case not perfect cube
#if zero: break loop and finish program


while True:
     try:
          a = int(input('Enter a negative or positive integer different from zero: '))
          counter = 0
          if a < 0:
               while a<= counter**3:
                    if a != counter**3:
                         counter-= 1
                    else:
                         print(a, '= ', counter, '^3')
                         break
               else:
                    print(a, 'is not a perfect cube')
          elif a > 0:
               while counter**3 <=a:
                    if a!= counter**3:
                         counter += 1
                    else:
                         print(a,'= ', counter, '^3')
                         break
               else:
                    print(a,'is not a perfect cube')
          else:
               print('Error, you have entered zero')
               break
     finally:
          print('')

