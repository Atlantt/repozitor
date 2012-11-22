print "Hello"
peremen1=0
peremen2=0
L=1
spisok1 = []
def spisok():
    while len(spisok1) in range(10):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
while peremen2 == 0:
    if spisok1[peremen1] != 0:
        L=L*spisok1[peremen1]
        peremen1=peremen1+1
    elif spisok1[peremen1] == 0:
        peremen2=1
print "Multiplication before the first zero is ", L
