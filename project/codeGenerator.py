from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class CodeGenerator(ExprVisitor):
    def __init__(self) -> None:
        self.lines = []                 #list of all lines
        self.identifiers = {}           #dictionary of identifiers
        self.nextjump = 1               #used to number labels 
        self.isAssignment = False       #check if expression is part assignment
        self.needPop = False            #check to see if pop is needed


    def __str__(self) -> str:
        strtemp = ""

        for line in self.lines:
            strtemp += line + "\n"

        strtemp = strtemp[:-1]

        return strtemp


    def intofile(self, name):
        file = open("output/"+name, 'w')
        for line in self.lines:
            file.write(line+'\n')




    #--------------
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)
            if self.needPop == True:
                self.lines.append("pop")
                self.needPop = False
                


    #--------------
    def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
        #primitive type of declaration
        varType = ctx.primitiveType().getText()

        #get names of all identifiers and save them; add default value
        for identifier in ctx.IDENTIFIER():
            varName = identifier.getText()
            self.identifiers[varName] = varType

            #default values
            if varType == 'int':
                self.lines.append('push int 1')
                self.lines.append(f'save {varType} {identifier}')

            elif varType == 'float':
                self.lines.append('push float 1.0')
                self.lines.append(f'save {varType} {identifier}')

            elif varType == 'bool':
                self.lines.append('push bool false')
                self.lines.append(f'save {varType} {identifier}')

            elif varType == 'string':
                self.lines.append('push string "temp"')
                self.lines.append(f'save {varType} {identifier}')

    

    #--------------
    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        self.isAssignment = True
        varName = ctx.IDENTIFIER().getText()
        varType = self.identifiers[ctx.IDENTIFIER().getText()]

        self.visit(ctx.expr())

        self.lines.append(f"save {varType} {varName}")
        self.isAssignment = False



    #--------------
    def visitMulDivMod(self, ctx: ExprParser.MulDivModContext):
        leftType = self.visit(ctx.left)
        rightType = self.visit(ctx.right)

        self.checkItoF()

        operator = ctx.op.text

        if operator == "*":
            self.lines.append("mul")
        elif operator == "/":
            self.lines.append("div")
        elif operator == "%":
            self.lines.append("mod")

        if(self.isAssignment == False):
            self.needPop = True

        



    #--------------
    def visitAddSubCon(self, ctx: ExprParser.AddSubConContext):
        leftType = self.visit(ctx.left)
        rightType = self.visit(ctx.right)
        
        self.checkItoF()

        operator = ctx.op.text

        if operator == "+":
            self.lines.append("add")
        elif operator == "-":
            self.lines.append("sub")
        elif operator == ".":
            self.lines.append("con")
        
        if(self.isAssignment == False):
            self.needPop = True



    #--------------
    def visitWriteStatement(self, ctx: ExprParser.WriteStatementContext):
        for expr in ctx.expr():
            self.lines.append(f"write {expr.getText()}")



    #-------------
    def visitRelation(self, ctx: ExprParser.RelationContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        operator = ctx.op.text

        if operator == "<":
            self.lines.append("lt")
        elif operator == ">":
            self.lines.append("gt")



    #-------------
    def visitComparison(self, ctx: ExprParser.ComparisonContext):
        self.visit(ctx.left)
        self.visit(ctx.right)

        operator = ctx.op.text

        if operator == "==":
            self.lines.append("eq")
        elif operator == "!=":
            self.lines.append("neq")



    #--------------
    def visitFor(self, ctx: ExprParser.ForContext):
        label1 = self.nextjump
        label2 = self.nextjump + 1
        self.nextjump += 2

        

        #assignment of identifier
        self.visit(ctx.init)

        #create first label (to enter for loop)
        self.lines.append(f"label ForStart{label1}")

        #create cmp
        self.visit(ctx.cond)

        #jump to ForContinue if condition is trie
        self.lines.append(f"tjmp ForContinue{label1}")

        #jump to end loop
        self.lines.append(f"jmp ForEnd{label2}")

        #create label ForContinue to signify that condition is true and can continue
        self.lines.append(f"label ForContinue{label1}")

        #looping statements
        self.visit(ctx.loop)

        #update identifier before jumping
        self.visit(ctx.update)

        #jump to repeat loop
        self.lines.append(f"jmp ForStart{label1}")

        #create second label (to leave for loop)
        self.lines.append(f"label ForEnd{label2}")










    #------------------------------------------------------------
    def visitId(self, ctx: ExprParser.IdContext):
        idType = self.identifiers[ctx.getText()]
        self.lines.append(f"load {idType} {ctx.getText()}")
        return idType

    def visitBool(self, ctx: ExprParser.BoolContext):
        self.lines.append(f"push bool {ctx.getText()}")
        return 'bool'

    def visitInt(self, ctx: ExprParser.IntContext):
        self.lines.append(f"push int {ctx.getText()}")
        return 'int'

    def visitFloat(self, ctx: ExprParser.FloatContext):
        self.lines.append(f"push float {ctx.getText()}")
        return 'float'

    def visitString(self, ctx: ExprParser.StringContext):
        self.lines.append(f"push string {ctx.getText()}")
        return 'string'



    #------------------------------------------------------------
    def checkItoF(self):
        fromline = 0
        need = False
        needbreak = True

        #check what is newest calculation
        for i in range(1, len(self.lines) ):
            needbreak = True
            fromline = len(self.lines) - i - 1
            for substring in ['push', 'mul', 'div', 'mod', 'add', 'sub', 'con', 'itof']:
                if substring in self.lines[ len(self.lines) - i ]:
                    needbreak = False

            if needbreak == True:
                fromline = len(self.lines) - i
                break

        #print(f"{fromline} --------")


        for i in range(fromline, len(self.lines)):
            if 'push float' in self.lines[ i ]:
                need = True
                break
        
        #print(f"{need} --------")

        if need == True:
            for i in range(1, len(self.lines) - fromline):
                if 'push int' in self.lines[ len(self.lines) - i ]:
                    if i == 1:
                        self.lines.append('itof')
                    elif self.lines[ len(self.lines) - i + 1] != 'itof':
                        self.lines.insert(len(self.lines) - i + 1 , 'itof')



                    #print(f'--------------- {self.lines[ len(self.lines) - i ]}')
                    
                





