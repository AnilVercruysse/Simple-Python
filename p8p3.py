#practical 8
# user inputs a
#start count and while loop with limit between 0 and 20
#repeat the multiplication of a with count in increments of 1 


a = int(input('Enter an integer '))

count = 0

print('multiplication table of ',a,'by 0 to 20')
while count<=20:
    a=a*1
    print(a,'x',count,'=',a*count)
    count+=1
