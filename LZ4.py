print "Hello"
peremen1=0
peremen2=0
spisok1 = []
def spisok():
    while len(spisok1) in range(15):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
while peremen2 == 0:
    if spisok1[peremen1] == 0:
        print " Index is " , spisok1.index(spisok1[peremen1])
        peremen2=1
    peremen1=peremen1+1
