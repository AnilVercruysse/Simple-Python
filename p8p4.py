#practical
#start range counters
#start loop runing with positive integers and input repeat
#id range and add to range counter
#if negative- break look and provide summary of input

range_a, range_b,range_c,range_d,range_e,range_f,range_g=0,0,0,0,0,0,0

while True:
    try:
        a=1
        while a>-1:
            a= int(input('Enter positive integer to begin input and a negative integer to exit: '))
            if a==0:
                range_a+=1
                print(a ,'equals 0')
            elif 0<a<=20:
                range_b+=1
                print(a, ' is greater than 0 and less than or equal to 20')
            elif 20<a<=40:
                range_c+=1
                print(a, 'is greater than 20 and less than or equal to 40')
            elif 40<a<=60:
                range_d+=1
                print(a, ' is greater than 40 and less than or equal to 60')
            elif 60<a<=80:
                range_e+=1
                print(a,'is greater than 60 and less than or equal to 80')
            elif 80<a<=100:
                range_f+=1
                print(a, ' is greater than 80 and less than or equal to 100')
            elif a>100:
                range_g+=1
                print(a,' is greater than 100')
        break
    finally:
        print('program ended with negative integer')
        print('input analysis: ')
        print('input equal to 0:', range_a)
        print('input greater than 0 and less than or equal to 20:', range_b)
        print('input greater than 20 and less than or equal to 40:', range_c)
        print('input greater than 40 and less than or equal to 60:', range_d)
        print('input greater than 60 and less than or equal to 80:', range_e)
        print('input greater than 80 and less than or equal to 100:', range_f)
        print('input greater than 100: ', range_g)
