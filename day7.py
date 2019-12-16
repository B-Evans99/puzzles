import itertools
from computer import Computer
import time

guesses = [5, 6, 7, 8, 9]
source = list(itertools.permutations(guesses, 5))


maxN = 0
for i in source:
    print("\n\n\n")
    nums = list(i)
    print(nums)

    ampA = Computer(nums[0])
    ampB = Computer(nums[1])
    ampC = Computer(nums[2])
    ampD = Computer(nums[3])
    ampE = Computer(nums[4])

    amps = [ampA, ampB, ampC, ampD, ampE]
    atAmp = 0

    subTotal = 0
    running = True

    while(running):
        answer = amps[atAmp].getOutput(subTotal)
        if not isinstance(answer, bool):
            subTotal = answer
            atAmp = atAmp + 1 if atAmp < 4 else 0
        else:
            running = False

    if(subTotal > maxN):
        maxN = subTotal
        print(subTotal)

print(maxN)
