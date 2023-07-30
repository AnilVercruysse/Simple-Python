#practical 10
#while loop continuously askignfor string input
#start vowel counter 
#if empty string exit message
#if string entered, add +1 to counter for each vowel detected and print result
#repeat untless empty string entered

while True:
     try:
          string = input('Enter a string to find number of vowels: ')
          counter= 0
          if not string:
               print('Empty string entered - Program exited')
               break
          else:
               for a in string:
                    if a == 'a' or a== 'e' or a== 'i' or a== 'o' or a== 'u':
                         counter+= 1
                    else:
                         pass
               print('There are', counter, 'vowels')
     finally:
          print('')
