print "Hello"
spisok1 = []
peremen1=0
def spisok():
    while len(spisok1) in range(15):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
minimum=spisok1[0]
while peremen1 != 15:
    if minimum > spisok1[peremen1]:
        minimum=peremen1
        peremen1=peremen1+1
    elif minimum <= spisok1[peremen1]:
        peremen1=peremen1+1
print "Minimum is " , minimum
print "Index is " , spisok1.index(minimum)
