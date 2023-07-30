#Practical 19
#ask user for file name to analyse
#read the file 
#list the types of brackets to analyse
#start counters for each types
#for loop accumulating the matching bracket
#for loop printing the counters with appropriate message
#closure of the file
#this code is heavily based on code found on github given the imminent examination

name = input('Enter the name of the file you wish to analyze: ')
f = open(name, 'r')
s = f.read()
bracket_types =['<', '>', '(', ')', '[', ']', '{', '}']
bracket_counter =[]

for i in bracket_types:
    bracket_counter.append(s.count(i))
for i in range(0, len(bracket_counter), 2):
    if bracket_counter[i] == bracket_counter[i + 1]:
        print(bracket_types[i] +  bracket_types[i+1] + ' are balanced (' + str(bracket_counter[i]) + ' - ' + str(bracket_counter[i+1]) + ') ')
    else:
        print(bracket_types[i] + bracket_types[i+1] + ' are not balanced (' + str(bracket_counter[i]) + ' - ' + str(bracket_counter[i+1]) + ') ')
f.close()


