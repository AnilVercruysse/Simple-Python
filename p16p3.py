#Practical 16
#define function analysing the perfect numbers up to n
#this includes a check of whether the total sum of the factors of n add up to n
#the program then prompts for a positive integer and prints the perfect numbers for that integer using the function defined above, in the form of a list
#Reference note: The program below was adapted from https://stackoverflow.com/questions/72062162/print-all-perfect-numbers-less-than-n 

def perfect(n):
    sum_a = sum(i for i in range(1, n//2+1) if not n % i)
    return sum_a == n

n = int(input('Enter a positive integer: '))
b = [i for i in range(1, n+1) if perfect(i)]

print(b)
