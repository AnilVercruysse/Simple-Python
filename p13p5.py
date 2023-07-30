#practical 13
#implemented program on slide 12 lecture 15
#defined function f
#defined variables x y z
#give 'in function' x value to z by applying the function 


def f(x):
    print('in function f: ')
    x+=1
    y=1
    b=455
    a=-b*z
    print('x is',x)
    print('y is',y)
    print('z is',z)
    print('a is',a)
    print('b is',b)
    return x

x,y,z,a,b=5,10,15,550,456985
print('before function f')
print('x is',x)
print('y is',y)
print('z is',z)
print('a is',a)
print('b is',b)

z=-f(x)/2
print('after function f')
print('x is',x)
print('y is',y)
print('z is',z)
print('a is',a)
print('b is',b)
