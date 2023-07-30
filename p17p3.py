#Practical 17
#created 2 variables
#create string input
#if condition detecting whether the counts of dog and cat are same and print message
#else condition cover other cases with message 

cat ='cat'
dog ='dog'

enter_text = input('Enter any string to detect whether the words "cat" and "dog" appear the same number of times: ')

if enter_text.count(cat)==enter_text.count(dog):
	print('cat and dog appear the same number of times in the given string')
else:
	print('cat and dog do not appear the same number of times in the diven string')
