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

    def loadData(self, input:list):
        self.lines = input

    def loadDataFromFile(self, filename:str):
        for line in open(filename, 'r'):
            self.lines.append(line)


    #-------------------------------------------------
    def startMachine(self):
        if len(self.lines) == 0:
            print('VIRTUAL MACHINE HAVE NO COMMANDS TO PROCESS')
            return

        self.loadLabels()

        while self.whereAmI < (len(self.lines) - 1):
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
            case 'add':
                self.add()
            case 'sub':
                self.sub()
            case 'jmp':
                self.jmp(line[1])
            case 'jeq':
                self.jeq(line[1])
            case 'jneq':
                self.jneq(line[1])
            case 'jlt':
                self.jlt(line[1])
            case 'jgt':
                self.jgt(line[1])
            case 'pop':
                self.pop()
            case 'write':
                self.write(line[1])
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
        result = numbers[0] / numbers[1]

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
    def jmp(self, label):
        self.whereAmI = self.labels[label]


    #---------------
    def jeq(self, label):
        values = self.buffer[-2:]
        if values[0] == values[1]:
            self.whereAmI = self.labels[label]
        self.buffer.pop()
        self.buffer.pop()


    #---------------
    def jneq(self, label):
        values = self.buffer[-2:]
        if values[0] != values[1]:
            self.whereAmI = self.labels[label]
        self.buffer.pop()
        self.buffer.pop()


    #---------------
    def jlt(self, label):
        values = self.buffer[-2:]
        if values[0] < values[1]:
            self.whereAmI = self.labels[label]
        self.buffer.pop()
        self.buffer.pop()


    #---------------
    def jgt(self, label):
        values = self.buffer[-2:]
        if values[0] > values[1]:
            self.whereAmI = self.labels[label]
        self.buffer.pop()
        self.buffer.pop()


    #---------------
    def pop(self):
        self.buffer.pop()
        

    #---------------
    def write(self, input):
        if input[0] == '"' and str(input[-1:]) == '"':
            print(input)
            return
        
        for variable in self.variables:
            if input == variable.name:
                print(variable.value)
                return
        
        needEval = False
        for operation in ['+','-','*','/']:
            if operation in input:
                needEval = True
                break
        
        if needEval == True:
            print(self.evaluate(input))
        else:
            print(input)



    #---------------
    def evaluate(self, input):
        evalstr = input.replace('+', ' ')
        evalstr = evalstr.replace('-', ' ')
        evalstr = evalstr.replace('/', ' ')
        evalstr = evalstr.replace('*', ' ')
        evallist = evalstr.split()

        dic = {}

        for item in evallist:
            for var in self.variables:
                if item == var.name:
                    dic[var.name] = var.value

        return eval(input, dic)








