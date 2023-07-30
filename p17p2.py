#Practical 17
#defined divisor function with different range formula based on sheet info
#for result, extend an existing list containing b and 1, add the results to this existing list (save for b and 1)
#sort the list and return the final result
#ask for user input twice


def Divisors(a):
    range_a = range(2, (a// 2) + 1, 1)
    if a>0:
        result= [i for i in range_a if a%i==0]
        result.extend([1, a])
        result = list(set(result))
        result.sort()
        return result

b = int(input('Enter an integer to find its divisors: '))
c = int(input('Enter a second integer to find its divisors: '))
print('the divisors of your chosen integers', b,c, 'are', Divisors(b),'and',Divisors(c))
       
