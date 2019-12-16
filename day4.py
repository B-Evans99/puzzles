answer = []
bad = []

for i in range(254032, 789860):
    good = True
    for (index, x) in enumerate(str(i)[:-1]):
        if(int(x) > int(str(i)[index+1])):
            good = False
    if(good):
        duo = False
        iStr = str(i)
        for j in range(0, len(iStr)-1):
            if(j == 0):
                if(iStr[j] == iStr[j+1] and iStr[j+1] != iStr[j+2]):
                    duo = True
            elif(j == 4):
                if(iStr[j-1] != iStr[j] and iStr[j] == iStr[j+1]):
                    duo = True
            else:
                if(iStr[j-1] != iStr[j] and iStr[j] == iStr[j+1] and iStr[j+1] != iStr[j+2]):
                    duo = True
        good = duo
    if(good):
        answer.append(i)
    else:
        bad.append(i)

print(len(answer))
