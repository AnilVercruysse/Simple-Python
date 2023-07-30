#Practical Sheet 4.5 Exercise 2 relating to geometric calculations
#Values are expressed in centimeters (cm)


import math
import sys
length = float(input('Enter the length '))
formula_square_area = length*length
formula_square_volume = length*length*length
pi = math.pi
formula_area_circle = (pi)*formula_square_area
formula_volume_sphere = (4*pi/3)*formula_square_volume
formula_volume_cylinder = pi*formula_square_volume

if length >= 0: 
    print('area for square:',formula_square_area ,'cm²')
    print()
    print('volume for cube:',formula_square_volume,'cm³')
    print()
    print('area for circle:',formula_area_circle,'cm²')
    print()
    print('volume for sphere',formula_volume_sphere,'cm³')
    print()
    print('volume for cylinder',formula_volume_cylinder,'cm³')

if length < 0:
   sys.exit('Amount must be >= 0. Please try again.')
