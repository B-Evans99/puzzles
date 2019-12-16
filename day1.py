total = 0

for i in open("nums.txt"):
    subTotal = int(i)//3-2
    moreFuel = subTotal//3-2
    while(moreFuel > 0):
        print(moreFuel)
        subTotal += moreFuel
        moreFuel = moreFuel//3-2
    total += subTotal


print(total)
