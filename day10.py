import math
import copy
from fractions import Fraction
from colorama import init, Fore
init()

asteroids = {}
fieldWidth = 0
fieldHeight = 0
soul = ""

for (index, i) in enumerate(open("asteroids.txt")):
    fieldWidth = len(i)
    fieldHeight += 1
    for (inner, j) in enumerate(i):
        if(j == "#"):
            asteroids[str(inner)+","+str(index)] = 0


def printField():
    print()
    for i in range(fieldHeight):
        for j in range(fieldWidth):
            if str(j)+","+str(i) in asteroids:
                if(str(j)+","+str(i) == soul):
                    print(Fore.RED+"#"+Fore.WHITE, end="")
                else:
                    print("#", end="")
            else:
                print(".", end="")
        print()


def getCoords(coords):
    x = int(coords.split(",")[0])
    y = int(coords.split(",")[1])
    return [x, y]


for i in asteroids:
    lines = []
    for j in asteroids:
        if(j != i):
            target = getCoords(i)
            asking = getCoords(j)
            frac = math.atan2(target[1]-asking[1], target[0]-asking[0])
            if(frac not in lines):
                lines.append(frac)
                asteroids[i] += 1

maxN = 0
for i in asteroids:
    if(asteroids[i] > maxN):
        maxN = asteroids[i]
        soul = i

print("SOUL "+soul+" "+str(maxN))
printField()

print(asteroids)

lines = {}
for j in asteroids:
    if(j != soul):
        target = getCoords(soul)
        asking = getCoords(j)
        frac = math.atan2(target[1]-asking[1], target[0]-asking[0])
        distance = math.sqrt(
            ((asking[0]-target[0])**2)+((asking[1]-target[1])**2))
        if(frac not in lines):
            lines[frac] = []
        lines[frac].append((distance, asking))


for i in lines:
    lines[i] = sorted(lines[i], key=lambda x: x[0])

angles = list(lines.keys())
angles.sort()

start = 0
for (i, index) in enumerate(angles):
    if(index == math.pi/2):
        start = i


count = 0
target = len(asteroids)-1
while(count < target):
    if(len(lines[angles[start]]) > 0):
        count += 1
        del asteroids[str(lines[angles[start]][0][1]
                          [0])+","+str(lines[angles[start]][0][1][1])]
        print("DESTROY "+str(count)+" "+str(lines[angles[start]][0][1]
                                            [0])+","+str(lines[angles[start]][0][1][1]))
        lines[angles[start]] = lines[angles[start]][1:]

    start += 1
    if(start > len(angles)-1):
        start = 0
