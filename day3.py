wire = {}

i = 0
for line in open("wires.txt"):
    wire[i] = line
    i += 1

crossing = []

bigList1 = []
bigList2 = []
x = 0
y = 0

for i in wire[0].split(","):
    if(i[0] == "U"):
        for j in range(int(i[1:])):
            y += 1
            bigList1.append((x, y))
    if(i[0] == "D"):
        for j in range(int(i[1:])):
            y -= 1
            bigList1.append((x, y))
    if(i[0] == "R"):
        for j in range(int(i[1:])):
            x += 1
            bigList1.append((x, y))
    if(i[0] == "L"):
        for j in range(int(i[1:])):
            x -= 1
            bigList1.append((x, y))

x = 0
y = 0

for i in wire[1].split(","):
    if(i[0] == "U"):
        for j in range(int(i[1:])):
            y += 1
            bigList2.append((x, y))
    if(i[0] == "D"):
        for j in range(int(i[1:])):
            y -= 1
            bigList2.append((x, y))
    if(i[0] == "R"):
        for j in range(int(i[1:])):
            x += 1
            bigList2.append((x, y))
    if(i[0] == "L"):
        for j in range(int(i[1:])):
            x -= 1
            bigList2.append((x, y))

crossing = list(set(bigList1) & set(bigList2))
crossDistances = []
smallestWalk = 100000000

for i in crossing:
    sub1 = 0
    for j in bigList1:
        sub1 += 1
        if(j == i):
            break
    sub2 = 0
    for j in bigList2:
        sub2 += 1
        if(j == i):
            break
    sub = sub1+sub2
    if(sub < smallestWalk):
        smallestWalk = sub

print(smallestWalk)
