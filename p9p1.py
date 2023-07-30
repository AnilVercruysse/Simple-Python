#practical 9
#create integer input
#start total sum to accumulate sum
#set initial value of loop at 1 and put limit to loop where a reaches x
#accumulate the value of a into total
#move to next value
#print total of sum

x = int(input('Enter the non-negative integer: '))
print('You entered: ',x) 

total_sum = 0
a = 1

while a <=x:
    total_sum = total_sum + a
    a = a + 1
print('the total sum of the consecutive integers until the number you entered is ',total_sum)

