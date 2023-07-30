#Practical 7 pseudocode
#create total_sum variable where the sum will be accumulated
#set initial value of the loop as 1
#create while loop where a has a max value of 5000
#accumulate the value of a into total
#move to next value
#print total of sum

total_sum = 0
a = 1
while a <=5000:
    total_sum = total_sum + a
    a = a + 1
print('the total sum of the 5000 first consecutive integers is ',total_sum)
