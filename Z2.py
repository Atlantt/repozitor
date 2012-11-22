print " This program is designed to solve simple tasks of plane geometry "
print " Enter the type of shape that you want to work. "
z = input( " 1 for a square, 2 for rectangle, 3 for the circle. " )
if z < 1:
    print " EROR ! "
elif z == 1:
    print " Selected square. "
    a1 = input( " Enter the value of side " )
    P1=4*a1
    S1=a1**2
    print " The perimeter is equal to ", P1
    print " The area is equal to ", S1
elif z == 2:
    print " Selected rectangle. "
    a2 = input( " Enter the value of side a " )
    b2 = input( " Enter the value of side b " )
    P2=2*a2+2*b2
    S2=a2*b2
    print " The perimeter is equal to ", P2
    print " The area is equal to ", S2
elif z == 3:
    print " Selected circle. "
    r = input( " Enter the radius " )
    p=3.141592
    L=p*r*2
    S3=p*r**2
    print " The circumference is equal to ", L
    print " The area is equal to ", S3
elif z > 3:
    print " EROR ! "


