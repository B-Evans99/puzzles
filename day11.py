from computer import Computer
from colorama import *
init()

comp = Computer("painter.txt")

x = 0
y = 0
world = {}
direction = 0
world[str(x)+","+str(y)] = 1
painting = True

while(painting):
    result = comp.getOutput(world[str(x)+","+str(y)])
    if(result == 1):
        world[str(x)+","+str(y)] = 1
    else:
        world[str(x)+","+str(y)] = 0
    result = comp.getOutput()
    if(result == 1):
        direction = direction-1 if direction > 0 else 3
    else:
        direction = direction+1 if direction < 3 else 0
    if(direction == 0):
        y += 1
    elif(direction == 1):
        x += 1
    elif(direction == 2):
        y -= 1
    else:
        x -= 1
    if(str(x)+","+str(y) not in world):
        world[str(x)+","+str(y)] = 0
    if(result == True and result != 1):
        print("it should be over now")
    if(result == True and type(result) is not int):
        painting = False

print(len(world))


maxY = 0
minY = 0
maxX = 0
minX = 0

for i in world:
    x, y = i.split(",")
    x = int(x)
    y = int(y)
    if(x < minX):
        minX = x
    if(x > maxX):
        maxX = x
    if(y < minY):
        minY = y
    if(y > maxY):
        maxY = y

print(range(minY, maxY))
print(range(minX, maxX))

for i in world:
    if(world[i] == 1):
        print(i)


for i in range(minY, maxY+1)[::-1]:
    for j in range(minX, maxX+1)[::-1]:
        if(str(j)+","+str(i) in world and world[str(j)+","+str(i)] == 1):
            print(Fore.WHITE+"█"+Fore.WHITE, end="")
        else:
            print(Fore.RED+"█"+Fore.WHITE, end="")
    print("")
