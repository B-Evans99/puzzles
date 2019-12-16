import math
import time

passed = []
stored = []

orbits = {"COM": ["ZGB"]}

for i in open("orbits.txt"):
    parent = i.split(")")[0]
    child = i.split(")")[1]
    if(parent not in orbits.keys()):
        orbits[parent] = []
    orbits[parent].append(child.strip())


def dive(state, distance):
    if(state not in orbits.keys()):
        return distance
    total = 0
    for i in orbits[state]:
        total += dive(i, distance+1)
    return total + distance


def search(state, goal):
    if(state == goal):
        return True
    if(state not in orbits.keys()):
        return False
    ret = False
    for i in orbits[state]:
        if(i == goal):
            return True
        ret = search(i, goal) or ret
    return ret


print(dive("COM", 0))

you = ""
san = ""

for i in orbits.keys():
    if("YOU" in orbits[i]):
        you = i
    if("SAN" in orbits[i]):
        san = i

print(you+" "+san)
counter = 0
while(you != san):
    counter += 1
    found = False
    for i in orbits[you]:
        if(search(i, san)):
            print("going down"+str(orbits[i]))
            you = i
            found = True
            break
    if(not found):
        for i in orbits.keys():
            if(you in orbits[i]):
                print("going up "+str(orbits[i]))
                you = i

                break

print(counter)
