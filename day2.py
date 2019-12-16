answer = 0
noun = 0
verb = 0
for i in range(99):
    if(answer != 19690720):
        for j in range(99):
            program = []

            for x in open("intcode.txt"):
                for y in x.split(","):
                    program.append(int(y))

            stopped = False
            position = 0
            program[1] = i
            program[2] = j

            while(not stopped):
                code = program[position]
                if(code == 1):
                    program[program[position+3]] = program[program[position+1]
                                                           ] + program[program[position+2]]
                elif(code == 2):
                    program[program[position+3]] = program[program[position+1]
                                                           ] * program[program[position+2]]
                elif(code == 99):
                    stopped = True
                else:
                    print("hm bad")
                position += 4
            answer = program[0]
            if(answer == 19690720):
                noun = i
                verb = j
                break

print(100*noun+verb)
