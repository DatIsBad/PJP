class Variable():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class VirtualMachine():
    def __init__(self) -> None:
        self.lines = []     #lines to process
        self.buffer = []    #datas in buffer
        self.variables = [] #list of variables
        self.labels = {}
        self.whereAmI = 0

    def loadData(self, temp:list):
        self.lines = temp

    def loadDataFromFile(self, filename:str):
        for line in open(filename, 'r'):
            self.lines.append(line)


    #-------------------------------------------------
    def startMachine(self):
        if len(self.lines) == 0:
            print('VIRTUAL MACHINE HAVE NO COMMANDS TO PROCESS')
            return

        self.loadLabels()

        while self.whereAmI < (len(self.lines) ):
            self.lineProcess()
            self.whereAmI += 1
            pass


    def loadLabels(self):
        for i in range( 0, len(self.lines)):
            line = self.lines[i].split(' ', 2) #split line to get [command type text] 

            if(line[0] == 'label'):
                self.labels[line[1]] = i



    def lineProcess(self):
        line = self.lines[self.whereAmI].split(' ', 2) #split line to get [command type text] 

        match line[0]:
            case 'push':
                self.push(line[1], line[2])
            case 'save':
                self.save(line[1], line[2])
            case 'load':
                self.load(line[1], line[2])

            case 'itof':
                self.itof()
            case 'mul':
                self.mul()
            case 'div':
                self.div()
            case 'mod':
                self.mod()
            case 'add':
                self.add()
            case 'sub':
                self.sub()
            case 'concat':
                self.concat()
            case 'uminus':
                self.uminus()

            case 'jmp':
                self.jmp(line[1])
            case 'fjmp':
                self.fjmp(line[1])
            case 'eq':
                self.eq()
            case 'lt':
                self.lt()
            case 'gt':
                self.gt()

            case 'not':
                self.notF()
            case 'and':
                self.andF()
            case 'or':
                self.orF()

            case 'pop':
                self.pop()
            case 'write':
                self.write(line[1])
            case 'read':
                self.read(line[1])

            case _:
                pass



            





    #-------------------------------------------------
    def push(self, valType, value):
        #append into buffer new value
        match valType:
            case 'int':
                self.buffer.append(int(value))
            case 'float':
                self.buffer.append(float(value))
            case 'string':
                self.buffer.append(value.strip('"'))
            case 'bool':
                if value == 'true' or value == True:
                    self.buffer.append(True)
                else:
                    self.buffer.append(False)


    #---------------
    def save(self, valType:str, varName:str):
        isdeclared = False

        for i in range(0, len(self.variables)):
            #check if variable is already declared
            if self.variables[i].name == varName:
                self.variables[i].value = self.buffer[len(self.buffer) - 1]
                isdeclared = True
                break
        
        if isdeclared == False:
            #create new variable
            self.variables.append( Variable(varName, valType, self.buffer[len(self.buffer) - 1]) )

        #get rid of last value in buffer
        self.buffer.pop()


    #---------------
    def itof(self):
        value = self.buffer[-1:]
        self.buffer[len(self.buffer) - 1 ] = float(value[0])


    #---------------
    def load(self, valType, valName):
        for item in self.variables:
            if item.name == valName:
                self.push(item.type, item.value)
                break


    #---------------
    def mul(self):
        numbers = self.buffer[-2:]
        result = numbers[0] * numbers[1]

        self.buffer.pop()
        self.buffer.pop()
        
        self.buffer.append(result)
    

    #---------------
    def div(self):
        numbers = self.buffer[-2:]

        if(type(numbers[0]).__name__ == 'int'):
            result = int(numbers[0] / numbers[1])
        else:
            result = numbers[0] / numbers[1]

        self.buffer.pop()
        self.buffer.pop()
        
        self.buffer.append(result)
    

    #---------------
    def mod(self):
        numbers = self.buffer[-2:]

        result = numbers[0] % numbers[1]

        self.buffer.pop()
        self.buffer.pop()

        self.buffer.append(result)


    #---------------
    def add(self):
        numbers = self.buffer[-2:]
        result = numbers[0] + numbers[1]

        self.buffer.pop()
        self.buffer.pop()
        
        self.buffer.append(result)


    #---------------
    def sub(self):
        numbers = self.buffer[-2:]
        result = numbers[0] - numbers[1]

        self.buffer.pop()
        self.buffer.pop()
        
        self.buffer.append(result)

        
    #---------------
    def concat(self):
        numbers = self.buffer[-2:]
        result = f'{numbers[0]}{numbers[1]}'

        self.buffer.pop()
        self.buffer.pop()

        self.buffer.append(result)

    #---------------
    def uminus(self):
        self.buffer[ len(self.buffer) - 1 ] = self.buffer[ len(self.buffer) - 1 ] * (-1)


    #---------------
    def jmp(self, label):
        self.whereAmI = self.labels[label]


    #---------------
    def fjmp(self, label):
        values = self.buffer[-1:]
        if values[0] == False:
            self.whereAmI = self.labels[label]
        self.buffer.pop()

    #---------------
    def eq(self):
        values = self.buffer[-2:]
        self.buffer.pop()
        self.buffer.pop()
        if values[0] == values[1]:
            self.buffer.append(True)
        else:
            self.buffer.append(False)


    #---------------
    def lt(self):
        values = self.buffer[-2:]
        self.buffer.pop()
        self.buffer.pop()
        if values[0] < values[1]:
            self.buffer.append(True)
        else:
            self.buffer.append(False)


    #---------------
    def gt(self):
        values = self.buffer[-2:]
        self.buffer.pop()
        self.buffer.pop()
        if values[0] > values[1]:
            self.buffer.append(True)
        else:
            self.buffer.append(False)
    

    #---------------
    def notF(self):
        values = self.buffer[-1:]
        self.buffer.pop()
        self.buffer.append(not values[0])
        

    #---------------
    def andF(self):
        values = self.buffer[-2:]
        self.buffer.pop()
        self.buffer.pop()
        self.buffer.append(values[1] and values[0])
        

    #---------------
    def orF(self):
        values = self.buffer[-2:]
        self.buffer.pop()
        self.buffer.pop()
        self.buffer.append(values[1] or values[0])


    #---------------
    def pop(self):
        self.buffer.pop()
        

    #---------------
    def write(self, temp):
        toprint = self.buffer[-(int(temp)):]
        tempstr = ""
        for item in toprint:
            tempstr = tempstr + str(item)
            self.buffer.pop()
        print(tempstr)
         

    #---------------
    def read(self, valtype):
        user_input = input()

        if valtype == 'int':
            self.buffer.append(int(user_input))
        elif valtype == 'float':
            self.buffer.append(float(user_input))
        elif valtype == 'string':
            self.buffer.append(str(user_input))
        elif valtype == 'bool':
            self.buffer.append(bool(user_input))
        







