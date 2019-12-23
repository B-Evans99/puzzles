import time


class Computer:
    def __init__(self, filename):
        self.program = {}
        self.position = 0
        self.relativeBase = 0

        for x in open(filename):
            for (i, y) in enumerate(x.split(",")):
                self.program[i] = int(y)

    def getOutput(self, inputVar="", userInput=False):
        stopped = False

        while(self.position < len(self.program) and not stopped):
            code, param1, param2, insertTo = self.parseSignature(
                self.program[self.position])

            if(code == 1):
                self.setPosition(insertTo, param1+param2)
                self.position += 4
            elif(code == 2):
                self.setPosition(insertTo, param1*param2)
                self.position += 4
            elif(code == 3):
                if(callable(userInput)):
                    self.setPosition(insertTo, userInput())
                else:
                    self.setPosition(insertTo,
                                     inputVar)
                self.position += 2
            elif(code == 4):
                self.position += 2
                return param1
            elif(code == 5):
                if(param1 != 0):
                    self.position = param2
                else:
                    self.position += 3
            elif(code == 6):
                if(param1 == 0):
                    self.position = param2
                else:
                    self.position += 3
            elif(code == 7):
                if(param1 < param2):
                    self.setPosition(insertTo, 1)
                else:
                    self.setPosition(insertTo, 0)
                self.position += 4
            elif(code == 8):
                if(param1 == param2):
                    self.setPosition(insertTo, 1)
                else:
                    self.setPosition(insertTo, 0)
                self.position += 4
            elif(code == 9):
                self.relativeBase += param1
                self.position += 2
            elif(code == 99):
                stopped = True

        return True

    def setPosition(self, position, value):
        self.program[position] = value

    def getParamValue(self, mode, paramNum):
        if(mode == 0):
            if(self.position+paramNum not in self.program):
                self.program[self.position+paramNum] = 0
            if(self.program[self.position+paramNum] not in self.program):
                self.program[self.program[self.position+paramNum]] = 0
            return self.program[self.program[self.position+paramNum]]
        elif(mode == 1):
            if(self.position+paramNum not in self.program):
                self.program[self.position+paramNum] = 0
            return self.program[self.position+paramNum]
        else:
            if(self.program[self.position+paramNum]+self.relativeBase not in self.program):
                self.program[self.program[self.position +
                                          paramNum]+self.relativeBase] = 0
            return self.program[self.program[self.position+paramNum]+self.relativeBase]

    def getParamInsert(self, mode, paramNum):
        if(mode == 0):
            if(self.position+paramNum not in self.program):
                self.program[self.position+paramNum] = 0
            return self.program[self.position+paramNum]
        elif(mode == 1):
            return self.position+paramNum
        else:
            if(self.program[self.position+paramNum]+self.relativeBase not in self.program):
                self.program[self.program[self.position +
                                          paramNum]+self.relativeBase] = 0
            return self.program[self.position+paramNum]+self.relativeBase

    def parseSignature(self, sig):
        sig = str(sig)
        p1Mode = p2Mode = p3Mode = 0
        param1 = param2 = insertTo = 0

        code = int(sig[-1])
        if(len(sig) > 1):
            code = int(sig[-2:])

        if(len(sig) == 3):
            p1Mode = int(sig[0])
        elif(len(sig) == 4):
            p1Mode = int(sig[1])
            p2Mode = int(sig[0])
        elif(len(sig) == 5):
            p1Mode = int(sig[2])
            p2Mode = int(sig[1])
            p3Mode = int(sig[0])

        if(code == 1):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
            insertTo = self.getParamInsert(p3Mode, 3)
        elif(code == 2):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
            insertTo = self.getParamInsert(p3Mode, 3)
        elif(code == 3):
            insertTo = self.getParamInsert(p1Mode, 1)
        elif(code == 4):
            param1 = self.getParamValue(p1Mode, 1)
        elif(code == 5):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
        elif(code == 6):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
        elif(code == 7):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
            insertTo = self.getParamInsert(p3Mode, 3)
        elif(code == 8):
            param1 = self.getParamValue(p1Mode, 1)
            param2 = self.getParamValue(p2Mode, 2)
            insertTo = self.getParamInsert(p3Mode, 3)
        elif(code == 9):
            param1 = self.getParamValue(p1Mode, 1)

        sig = (code, param1, param2, insertTo)

        return sig
