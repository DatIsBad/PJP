from antlr4 import *
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor



class TypeCheck(ExprVisitor):
    def __init__(self):
        #all declared variables
        self.variables = {}



    #--------------
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

        print("Type check was sucessful")
    


    #--------------
    def visitDeclaration(self, ctx: ExprParser.DeclarationContext):
        #primitive type of declaration
        varType = ctx.primitiveType().getText()

        for identifier in ctx.IDENTIFIER():
            varName = identifier.getText()

            #check if it already exist
            if varName in self.variables:
                raise ValueError(f"Variable '{varName}' has already been declared")
            else:
                #if variable doesn't exist, add to variables
                self.variables[varName] = varType

    

    #--------------
    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        #get identifier of assignment
        varName = ctx.IDENTIFIER().getText()
        if varName not in self.variables:
            raise ValueError(f"Variable '{varName}' has not been declared")
        
        varType = self.variables[varName]
        exprType = self.visit(ctx.expr())    #get expression type; TODO check type of mul/div/add etc

        if varType != exprType:
            raise TypeError(f"Type mismatch in assignment: '{varType}' != '{exprType}'")



    #--------------
    def visitRelation(self, ctx: ExprParser.RelationContext):
        leftType = self.visit(ctx.left)
        rightType = self.visit(ctx.right)

        # Ensure that both operands are of compatible types
        if leftType != rightType:
            raise TypeError("Operands in a relational expression must have the same type")

        # Check if the types are valid for comparison
        if leftType not in ['int', 'float', 'string']:
            raise TypeError(f"Relational expression is not supported for type '{leftType}'")
        
        # Return the result type of the relational expression
        return 'bool'

    

    #--------------
    def visitMulDivMod(self, ctx: ExprParser.MulDivModContext):
        leftType = self.visit(ctx.left)
        rightType = self.visit(ctx.right)

        if leftType not in ['int', 'float'] or rightType not in ['int', 'float'] :
            raise TypeError(f"MulDivMod expressions are not supported for types other than ['int', 'float']")

        if leftType != rightType:
            raise TypeError(f"Type mismatch in MulDivMod: '{leftType}' != '{rightType}'")
        
        return leftType
    


    #--------------
    def visitAddSubCon(self, ctx: ExprParser.AddSubConContext):
        leftType = self.visit(ctx.left)
        rightType = self.visit(ctx.right)

        if leftType not in ['int', 'float'] or rightType not in ['int', 'float'] :
            raise TypeError(f"AddSubCon expressions are not supported for types other than ['int', 'float']")

        if leftType != rightType:
            raise TypeError(f"Type mismatch in AddSubCon: '{leftType}' != '{rightType}'")

        return leftType
















    #------------------ small visits ------------------
    def visitId(self, ctx: ExprParser.IdContext):
        identifier = ctx.IDENTIFIER().getText()
        if identifier not in self.variables:
            raise ValueError(f"Variable '{identifier}' has not been declared")
        
        #if found, will return type of variable
        return self.variables[identifier]  

    def visitBool(self, ctx: ExprParser.BoolContext):
        return 'bool'

    def visitInt(self, ctx: ExprParser.IntContext):
        return 'int'

    def visitFloat(self, ctx: ExprParser.FloatContext):
        return 'float'

    def visitString(self, ctx: ExprParser.StringContext):
        return 'string'