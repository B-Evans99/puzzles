import time

answer = 0
noun = 0
verb = 0

program = []

for x in open("intcode.txt"):
    for y in x.split(","):
        program.append(int(y))

stopped = False
position = 0

while(position < len(program) and not stopped):
    sig = str(program[position])
    code = int(sig[-1])
    in1 = in2 = 0
    if(len(sig) > 1):
        code = int(sig[-2:])

    if(len(sig) == 3):
        in1 = int(sig[0])
    elif(len(sig) == 4):
        in1 = int(sig[1])
        in2 = int(sig[0])

    if(code == 1):
        num1 = program[position +
                       1] if in1 == 1 else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]

        program[program[position+3]] = num1+num2

        position += 4
    elif(code == 2):
        num1 = program[position +
                       1] if (in1 == 1) else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]
        program[program[position+3]] = num1*num2

        position += 4
    elif(code == 3):
        program[program[position+1]
                ] = int(input("Input for position "+str(position)+": "))
        position += 2
    elif(code == 4):
        print("Output: "+str(program[program[position+1]]))
        position += 2
    elif(code == 5):
        num1 = program[position +
                       1] if (in1 == 1) else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]
        if(num1 != 0):
            position = num2
        else:
            position += 3
    elif(code == 6):
        num1 = program[position +
                       1] if (in1 == 1) else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]
        if(num1 == 0):
            position = num2
        else:
            position += 3
    elif(code == 7):
        num1 = program[position +
                       1] if (in1 == 1) else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]

        program[program[position+3]] = 1 if num1 < num2 else 0

        position += 4
    elif(code == 8):
        num1 = program[position +
                       1] if (in1 == 1) else program[program[position+1]]
        num2 = program[position +
                       2] if (in2 == 1) else program[program[position+2]]

        program[program[position+3]] = 1 if num1 == num2 else 0
        position += 4
    elif(code == 99):
        stopped = True
    else:
        print("cap we didnt know she could do this")
