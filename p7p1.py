#Practical 7 pseudocode
#Prompt the user for a year
#Read the year
#if year ≥ 0 then
    #if (year mod 4 = 0 and year mod 100 != 0)
            #or year mod 400 = 0 then
        #Print(“Year is a leap year”)
    #else
        #Print(“Year is not a leap year”)
#else
    #Tell the user that the year must be ≥ 0
#Program finishes

import sys

year=int(input('Enter the year: '))
print(year)

if year >=0:
    if (year %4==0 and year %100!=0) or year %400==0:
            print(year,'is a leap year')
    else:
        print(year,'is not a leap year')
else:
    print('year must be greater than 0')
sys.exit('finished!')
