import random

i = 3
u = 2

leftQ = "i"
rightQ = "3u"

left = i
right = 3*u

varis = ["a", "b", "c", "d", "e", "f", "g", "h", "j"]


def passing(left, right):
    return left < right


for i in range(0, 10):
    add = random.randint(-50, 50)

    vari = random.choice(varis)
    left += add
    right += add

    div = random.randint(0, 2) == 2

    if(div):
        vari2 = random.choice(varis)
        divC = random.randint(-50, 50)
        times = random.randint(1, 4)
        leftQ += " + "+str(times*add)+vari+"/"+str(times*divC)+vari2
        rightQ += " + "+str(add)+vari+"/"+str(divC)+vari2
    else:
        leftQ += " + "+str(add)+vari
        rightQ += " + "+str(add)+vari


print(leftQ)
print(rightQ)
