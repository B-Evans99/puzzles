from computer import Computer
from colorama import *
init()

comp = Computer("arcade.txt")
world = {}
result = 0
score = 0


def display():
    maxY = 0
    minY = 0
    maxX = 0
    minX = 0

    for i in world:
        if("True" not in i):
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
    print("SCHORE "+str(score))
    for i in range(minY, maxY+1):
        for j in range(minX, maxX+1):
            if(str(j)+","+str(i) in world and world[str(j)+","+str(i)] == 1):
                print(Fore.WHITE+"█"+Fore.WHITE, end="")
            elif(str(j)+","+str(i) in world and world[str(j)+","+str(i)] == 2):
                print(Fore.RED+"█"+Fore.WHITE, end="")
            elif(str(j)+","+str(i) in world and world[str(j)+","+str(i)] == 3):
                print(Fore.CYAN+"█"+Fore.WHITE, end="")
            elif(str(j)+","+str(i) in world and world[str(j)+","+str(i)] == 4):
                print(Fore.MAGENTA+"█"+Fore.WHITE, end="")
            else:
                print(Fore.BLACK+"█"+Fore.WHITE, end="")
        print("")


def getInput():
    paddle = 0
    ball = 0
    for i in world:
        if(world[i] == 3):
            paddle = int(i.split(",")[0])
        elif(world[i] == 4):
            ball = int(i.split(",")[0])
    ret = -1 if ball < paddle else 0 if ball == paddle else 1
    return ret


while(type(result) is int):
    x = comp.getOutput(userInput=getInput)
    y = comp.getOutput(userInput=getInput)
    result = comp.getOutput(userInput=getInput)
    if(x == -1 and y == 0):
        score = result
    else:
        world[str(x)+","+str(y)] = result

display()
print("FINAL SCOREH"+str(score))
