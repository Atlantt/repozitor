# -*- coding: cp1251 -*-
import math
print " This program is designed to solve quadratic equations, such as a*x^2+b*x+c=0 "
a = input( " Enter the number a " )
b = input( " Enter the number b " )
c = input( " Enter the number c " )
d=b**2-4*a*c
if d < 0:
    print " The discriminant is equal to less than zero ", d

elif d == 0:
    x=-b/2*a
    print " equation has a root and it is equal to ", x
else:
    print " equation has two roots "
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print " x1=",x1
    print " x2=",x2
