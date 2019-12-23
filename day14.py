import math


class Chemical:
    def __init__(self, reaction, ammount, name):
        self.reaction = reaction
        self.result = int(ammount)
        self.name = name

    def need(self):
        raw = self.reaction.split(",")
        cleanRet = {}
        for i in raw:
            cleanRet[i.split()[1]] = int(i.split()[0])
        return cleanRet

    def __str__(self):
        return str(self.reaction)+" => "+str(self.ammount)+" "+str(self.name)


chemicals = {}

for i in open("reactions.txt"):
    chemicals[i.split("=>")[1].split()[1]] = Chemical(i.split("=>")[0], int(
        i.split("=>")[1].split()[0]), i.split("=>")[1].split()[1])

need = {}


def expand():
    queued = ["FUEL"]
    requirements = {"FUEL": 1}
    completed = ["FUEL"]
    total = 0
    baseNeeded = {}

    for i in chemicals[queued[0]].need():
        if(i != "ORE" and i not in completed):
            queued.append(i)
    queued = queued[1:]

    while(len(queued) != 0):
        print(queued)
        for i in chemicals[queued[0]].need():
            if(i != "ORE" and i not in completed and i not in queued):
                queued.append(i)

        findNeed = 0
        skip = False
        for i in chemicals:
            if(queued[0] in chemicals[i].need()):
                if(i not in completed):
                    if(i in queued):
                        queued.remove(i)
                    queued.insert(0, i)
                    skip = True
                if(not skip):
                    minCanMake = math.ceil(
                        requirements[i]/chemicals[i].result)

                    findNeed += chemicals[i].need()[queued[0]] * minCanMake

        if(skip):
            continue
        requirements[queued[0]] = findNeed
        completed.append(queued[0])
        queued = queued[1:]
        total += 1

    retReduce = {}

    for i in requirements:
        if("ORE" in chemicals[i].need()):
            retReduce[i] = requirements[i]

    return retReduce


def getMin(required):
    total = 0
    print("\n\n")
    for i in required:
        total += math.ceil(
            need[i]/chemicals[i].result)*chemicals[i].need()["ORE"]
    return total


need = expand()
print(str(need))
print("ORE NEEDED: "+str(getMin(need)))
