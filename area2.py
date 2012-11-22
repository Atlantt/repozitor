print " This program is designed to solve simple tasks of plane geometry "
print " Enter the type of shape that you want to work. "
z=1
p=3.14
h="Enter the value of side a "
k="Enter the value of side b "
def circle(r):
    print " The area is equal to ", p*r**2
def rectangle(a,b):
    print " The area is equal to ", a*b
def square(a):
    print " The area is equal to ", a**2
while z != 4:
    z = input(" 1 for a square, 2 for rectangle, 3 for the circle, 4 to exit ")
    if z < 1:
       print " ERROR ! "
    elif z == 1:
       square(input("Enter the value of side "))
    elif z == 2:
       rectangle(input(h),input(k))
    elif z == 3:
       circle(input( " Enter the radius " ))
    elif z > 4:
      print " ERROR ! " 
                 
