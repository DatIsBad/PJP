from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


class CodeGenerator(ExprVisitor):
    def __init__(self) -> None:
        self.lines = []                 #list of all lines
        self.identifiers = {}           #dictionary of identifiers
        self.nextjump = 1               #used to number labels 
        self.isAssignment = 0           #check if expression is part assignment
        self.needPop = False            #check to see if pop is needed
        self.bufftype = "int"           

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
        self.isAssignment += 1
        varName = ctx.IDENTIFIER().getText()
        varType = self.identifiers[ctx.IDENTIFIER().getText()]

        self.visit(ctx.expr())

        self.lines.append(f"save {varType} {varName}")

        
        

        if self.isAssignment >= 2:
            self.lines.append(f"load {varType} {varName}")

        if varType == 'float':
            self.forceItoF()
        self.isAssignment -= 1



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

        if(self.isAssignment == 0):
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
            self.lines.append("concat")
        
        if(self.isAssignment == 0):
            self.needPop = True



    #--------------
    def visitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        varType = ''
        varName = ''

        for identifier in ctx.IDENTIFIER():
            varName = identifier.getText()
            varType = self.identifiers[varName]

            self.lines.append(f"read {varType}")
            self.lines.append(f"save {varType} {varName}")
            





    #--------------
    def visitWriteStatement(self, ctx: ExprParser.WriteStatementContext):
        howmany = 0

        for expr in ctx.expr():
            self.visit(expr)
            howmany += 1
            self.isAssignment = 0 
            self.needPop = False
        
        self.lines.append(f"write {howmany}")



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
            self.lines.append("eq")
            self.lines.append("not")



    #--------------
    def visitFor(self, ctx: ExprParser.ForContext):
        label1 = self.nextjump
        self.nextjump += 1

        #assignment of identifier
        self.visit(ctx.init)

        #create first label (to enter for loop)
        self.lines.append(f"label ForStart{label1}")

        #create cmp
        self.visit(ctx.cond)

        #jump to end loop if condition is FALSE
        self.lines.append(f"fjmp ForEnd{label1}")

        #looping statements
        self.visit(ctx.loop)

        #update identifier before jumping
        self.visit(ctx.update)

        #jump to repeat loop
        self.lines.append(f"jmp ForStart{label1}")

        #create second label (to leave for loop)
        self.lines.append(f"label ForEnd{label1}")

    

    #--------------
    def visitWhile(self, ctx:ExprParser.WhileContext):
        label1 = self.nextjump
        self.nextjump += 1
        
        #create first label (to enter for loop)
        self.lines.append(f"label WhileStart{label1}")

        #create cmp
        self.visit(ctx.cond)

        #jump to end loop if condition is FALSE
        self.lines.append(f"fjmp WhileEnd{label1}")

        #looping statements
        self.visit(ctx.loop)

        #jump to repeat loop
        self.lines.append(f"jmp WhileStart{label1}")

        #create second label (to leave for loop)
        self.lines.append(f"label WhileEnd{label1}")



    #--------------
    def visitIfElse(self, ctx: ExprParser.IfElseContext):
        label1 = self.nextjump
        self.nextjump += 1


        #create cmp
        self.visit(ctx.cond)

        #jump to ElseContinue if condition is false
        self.lines.append(f"fjmp ElseContinue{label1}")

        #statements inside if
        self.visit(ctx.pos)

        #if ELSE exist, create jmp to ElseEnd to skip ELSE statements
        if ctx.neg != None:
            self.lines.append(f"jmp ElseEnd{label1}")

        #create label ElseContinue to process ELSE statements (if they exists)
        self.lines.append(f"label ElseContinue{label1}")

        #if ELSE exist, visit all statements and create label ElseEnd
        if ctx.neg != None:
            self.visit(ctx.neg)

            self.lines.append(f"label ElseEnd{label1}")



    #--------------
    def visitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        self.lines.append(f"and")
   


    #--------------
    def visitLogicalOr(self, ctx: ExprParser.LogicalOrContext):
        self.visit(ctx.left)
        self.visit(ctx.right)
        self.lines.append(f"or")
   


    #--------------
    def visitNegation(self, ctx:ExprParser.NegationContext):
        self.visit(ctx.right)
        self.lines.append(f"not")



    def visitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        self.visit(ctx.right)
        self.lines.append(f"uminus")














    #------------------------------------------------------------
    def visitId(self, ctx: ExprParser.IdContext):
        idType = self.identifiers[ctx.getText()]
        self.lines.append(f'load {idType} {ctx.getText()}')

        self.bufftype = idType
        return idType

    def visitBool(self, ctx: ExprParser.BoolContext):
        self.lines.append(f"push bool {ctx.getText()}")
        self.bufftype = "bool"
        return 'bool'

    def visitInt(self, ctx: ExprParser.IntContext):
        self.lines.append(f"push int {ctx.getText()}")
        self.bufftype = "int"
        return 'int'

    def visitFloat(self, ctx: ExprParser.FloatContext):
        self.lines.append(f"push float {ctx.getText()}")
        self.bufftype = "float"
        return 'float'

    def visitString(self, ctx: ExprParser.StringContext):
        self.lines.append(f"push string {ctx.getText()}")
        self.bufftype = "string"
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
            self.bufftype = "float"


                    #print(f'--------------- {self.lines[ len(self.lines) - i ]}')
        else:
            self.bufftype = "int"
                    
                


    def forceItoF(self):
        number1 = 2
        needbreak = False
        length = len(self.lines)

        while(needbreak == False):
            needbreak = True
            for substring in ['push', 'mul', 'div', 'mod', 'add', 'sub', 'con', 'itof']:
                if substring in self.lines[length - number1]:
                    needbreak = False
            
            print(f'{self.lines[ length - number1 ]} --------------------------- {needbreak} {number1}')
            if 'push int' in self.lines[ length - number1 ]:
                if number1 == 1:
                    self.lines.append('itof')
                elif self.lines[ length - number1] != 'itof':
                    self.lines.insert(length - number1 + 1 , 'itof')

            number1 = number1 + 1


