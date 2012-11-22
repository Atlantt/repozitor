print "To move in this program and use the arrow keys a, s, d, w "
print "to the left click a "
print "to the right click d "
print "to the up click w "
print "to the down click s "
print "to the exit click q "
print "Your character is at a point 5.5"
p=1
x=5
y=5
while p != "q":
    p = raw_input( " Enter the direction " )
    if x > 10:
        print "Error"
        p="q"
    elif x < 0:
        print "Error"
        p="q"
    elif y > 10:
        print "Error"
        p="q"
    elif y < 0:
        print "Error"
        p="q"
    elif p == "a":
        x=x-1
        print x,".",y
    elif p == "d":
        x=x+1
        print x,".",y
    elif p == "w":
        y=y+1
        print x,".",y
    elif p == "s":
        y=y-1
        print x,".",y
