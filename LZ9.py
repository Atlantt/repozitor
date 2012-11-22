print "Hello"
peremen1=0
peremen2=0
L=0
spisok1 = []
def spisok():
    while len(spisok1) in range(10):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
while peremen1 != 10:
    if spisok1[peremen1] < 0:
        L=L+spisok1[peremen1]
    peremen1=peremen1+1
print " The amount of negative ", L        

