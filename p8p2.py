#practical 8
#table based on lecture note - i cannot make it square after  hours of research
#ask for table size
#set coutner for i
#while loop until i reaches table size
#set j counter and print i*j until table size reached with increments in 1



table_size=int(input('Enter desired size of multiplication table: '))

i=1
while i<= table_size:
    j=1
    while j<=i:
        print(i*j,'',end='')
        j+=1
    print()
    i+=1
