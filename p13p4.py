#practical 13
#implemented program on slide 12 lecture 15
#defined function f
#defined variables x y z
#give 'in function' x value to z by applying the function 


def f(x):
    print('in function f: ')
    x+=1
    y=1
    print('x is',x)
    print('y is',y)
    print('z is',z)
    return x

x,y,z=5,10,15
print('before function f')
print('x is',x)
print('y is',y)
print('z is',z)

z=f(x)
print('after function f')
print('x is',x)
print('y is',y)
print('z is',z)
