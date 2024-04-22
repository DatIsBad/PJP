# Generated from c:/Users/kphan/OneDrive/Plocha/School - all/PJP - 3rd/project/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#primitiveType.
    def enterPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#primitiveType.
    def exitPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#blockOfStatements.
    def enterBlockOfStatements(self, ctx:ExprParser.BlockOfStatementsContext):
        pass

    # Exit a parse tree produced by ExprParser#blockOfStatements.
    def exitBlockOfStatements(self, ctx:ExprParser.BlockOfStatementsContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#for.
    def enterFor(self, ctx:ExprParser.ForContext):
        pass

    # Exit a parse tree produced by ExprParser#for.
    def exitFor(self, ctx:ExprParser.ForContext):
        pass


    # Enter a parse tree produced by ExprParser#ifElse.
    def enterIfElse(self, ctx:ExprParser.IfElseContext):
        pass

    # Exit a parse tree produced by ExprParser#ifElse.
    def exitIfElse(self, ctx:ExprParser.IfElseContext):
        pass


    # Enter a parse tree produced by ExprParser#while.
    def enterWhile(self, ctx:ExprParser.WhileContext):
        pass

    # Exit a parse tree produced by ExprParser#while.
    def exitWhile(self, ctx:ExprParser.WhileContext):
        pass


    # Enter a parse tree produced by ExprParser#readStatement.
    def enterReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#readStatement.
    def exitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#writeStatement.
    def enterWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#writeStatement.
    def exitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#printExpr.
    def enterPrintExpr(self, ctx:ExprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ExprParser#printExpr.
    def exitPrintExpr(self, ctx:ExprParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ExprParser#emptyStatement.
    def enterEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#emptyStatement.
    def exitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDivMod.
    def enterMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDivMod.
    def exitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        pass


    # Enter a parse tree produced by ExprParser#parens.
    def enterParens(self, ctx:ExprParser.ParensContext):
        pass

    # Exit a parse tree produced by ExprParser#parens.
    def exitParens(self, ctx:ExprParser.ParensContext):
        pass


    # Enter a parse tree produced by ExprParser#comparison.
    def enterComparison(self, ctx:ExprParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ExprParser#comparison.
    def exitComparison(self, ctx:ExprParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ExprParser#bool.
    def enterBool(self, ctx:ExprParser.BoolContext):
        pass

    # Exit a parse tree produced by ExprParser#bool.
    def exitBool(self, ctx:ExprParser.BoolContext):
        pass


    # Enter a parse tree produced by ExprParser#string.
    def enterString(self, ctx:ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#string.
    def exitString(self, ctx:ExprParser.StringContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalAnd.
    def enterLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalAnd.
    def exitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        pass


    # Enter a parse tree produced by ExprParser#float.
    def enterFloat(self, ctx:ExprParser.FloatContext):
        pass

    # Exit a parse tree produced by ExprParser#float.
    def exitFloat(self, ctx:ExprParser.FloatContext):
        pass


    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx:ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx:ExprParser.IntContext):
        pass


    # Enter a parse tree produced by ExprParser#relation.
    def enterRelation(self, ctx:ExprParser.RelationContext):
        pass

    # Exit a parse tree produced by ExprParser#relation.
    def exitRelation(self, ctx:ExprParser.RelationContext):
        pass


    # Enter a parse tree produced by ExprParser#addSubCon.
    def enterAddSubCon(self, ctx:ExprParser.AddSubConContext):
        pass

    # Exit a parse tree produced by ExprParser#addSubCon.
    def exitAddSubCon(self, ctx:ExprParser.AddSubConContext):
        pass


    # Enter a parse tree produced by ExprParser#id.
    def enterId(self, ctx:ExprParser.IdContext):
        pass

    # Exit a parse tree produced by ExprParser#id.
    def exitId(self, ctx:ExprParser.IdContext):
        pass


    # Enter a parse tree produced by ExprParser#logicalOr.
    def enterLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass

    # Exit a parse tree produced by ExprParser#logicalOr.
    def exitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        pass



del ExprParser