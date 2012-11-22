print "Hello"
spisok1 = []
peremen1=0
def spisok():
    while len(spisok1) in range(15):
        s=input("Enter number ")
        spisok1.append(s)
    return spisok1
spisok()
maximum=spisok1[0]
while peremen1 != 15:
    if maximum < spisok1[peremen1]:
        maximum=peremen1
        peremen1=peremen1+1
    elif maximum >= spisok1[peremen1]:
        peremen1=peremen1+1
print "Maximum is " , maximum
print "Index is " , spisok1.index(maximum)
