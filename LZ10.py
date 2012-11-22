print "Hello"
peremen1=0
peremen2=0
spisok1 = []
def spisok():
    while len(spisok1) in range(10):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
while peremen1 != 10:
    if spisok1[peremen1] > 0:
        peremen2=peremen2+1
    peremen1=peremen1+1
print "The number of positive numbers ", peremen2        

