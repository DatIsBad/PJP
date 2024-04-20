# Generated from c:/Users/kphan/OneDrive/Plocha/School - all/PJP - 3rd/project/Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#primitiveType.
    def visitPrimitiveType(self, ctx:ExprParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#blockOfStatements.
    def visitBlockOfStatements(self, ctx:ExprParser.BlockOfStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for.
    def visitFor(self, ctx:ExprParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifElse.
    def visitIfElse(self, ctx:ExprParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while.
    def visitWhile(self, ctx:ExprParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#readStatement.
    def visitReadStatement(self, ctx:ExprParser.ReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#writeStatement.
    def visitWriteStatement(self, ctx:ExprParser.WriteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printExpr.
    def visitPrintExpr(self, ctx:ExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#emptyStatement.
    def visitEmptyStatement(self, ctx:ExprParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDivMod.
    def visitMulDivMod(self, ctx:ExprParser.MulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parens.
    def visitParens(self, ctx:ExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#negation.
    def visitNegation(self, ctx:ExprParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparison.
    def visitComparison(self, ctx:ExprParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bool.
    def visitBool(self, ctx:ExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalAnd.
    def visitLogicalAnd(self, ctx:ExprParser.LogicalAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#float.
    def visitFloat(self, ctx:ExprParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx:ExprParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#relation.
    def visitRelation(self, ctx:ExprParser.RelationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSubCon.
    def visitAddSubCon(self, ctx:ExprParser.AddSubConContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryMinus.
    def visitUnaryMinus(self, ctx:ExprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#id.
    def visitId(self, ctx:ExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#logicalOr.
    def visitLogicalOr(self, ctx:ExprParser.LogicalOrContext):
        return self.visitChildren(ctx)



del ExprParser