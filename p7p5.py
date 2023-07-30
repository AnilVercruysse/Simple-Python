#Practical 7
#create total variable to accumulate
#create sum specifying that only numbers from the range that are divisible by 3 or 5 should be added up
#print total

total = sum(i for i in range(1,10000,1) if i %3==0 or i%5==0)
print('the sum of integers in the range 1-10000 that are divisible by 3 or 5 is equal to',total)
