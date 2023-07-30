#Practical 7
#enter year
#if year not evenly divisible by 4 = common
#if yes, is it evenly divisible by 100? if not = leap
#if yes, is it evenly divisible by 400? if not = common
#if yes, leap year

#Python code

year=int(input('enter the year: '))

if year%4!=0:
    print(year,'is a common year')
if year%4==0:
    if year%100!=0:
        print(year,'is a leap year')
    elif year%100==0:
        if year%400==0:
            print(year,'is a leap year')
        elif year%400!=0:
            print(year,'is a common year')
    
        
