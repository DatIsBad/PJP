# Generated from c:/Users/kphan/OneDrive/Plocha/School - all/PJP - 3rd/project/Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,38,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,1,1,1,1,3,1,20,8,1,1,2,1,2,5,2,24,8,2,10,2,
        12,2,27,9,2,1,2,1,2,1,2,1,2,1,2,5,2,34,8,2,10,2,12,2,37,9,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,58,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,70,
        8,2,10,2,12,2,73,9,2,1,2,1,2,1,2,1,2,1,2,5,2,80,8,2,10,2,12,2,83,
        9,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,91,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,106,8,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,126,8,3,10,3,12,
        3,129,9,3,1,3,0,1,6,4,0,2,4,6,0,5,1,0,5,6,1,0,22,24,2,0,21,21,25,
        26,1,0,27,28,1,0,30,31,155,0,9,1,0,0,0,2,19,1,0,0,0,4,90,1,0,0,0,
        6,105,1,0,0,0,8,10,3,4,2,0,9,8,1,0,0,0,10,11,1,0,0,0,11,9,1,0,0,
        0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,0,0,0,15,20,5,
        11,0,0,16,20,5,10,0,0,17,20,5,12,0,0,18,20,5,9,0,0,19,15,1,0,0,0,
        19,16,1,0,0,0,19,17,1,0,0,0,19,18,1,0,0,0,20,3,1,0,0,0,21,25,5,1,
        0,0,22,24,3,4,2,0,23,22,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,28,1,0,0,0,27,25,1,0,0,0,28,91,5,2,0,0,29,30,3,2,1,0,
        30,35,5,34,0,0,31,32,5,20,0,0,32,34,5,34,0,0,33,31,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,1,0,0,0,37,35,1,0,0,0,
        38,39,5,19,0,0,39,91,1,0,0,0,40,41,5,18,0,0,41,42,5,3,0,0,42,43,
        3,6,3,0,43,44,5,19,0,0,44,45,3,6,3,0,45,46,5,19,0,0,46,47,3,6,3,
        0,47,48,5,4,0,0,48,49,3,4,2,0,49,91,1,0,0,0,50,51,5,15,0,0,51,52,
        5,3,0,0,52,53,3,6,3,0,53,54,5,4,0,0,54,57,3,4,2,0,55,56,5,17,0,0,
        56,58,3,4,2,0,57,55,1,0,0,0,57,58,1,0,0,0,58,91,1,0,0,0,59,60,5,
        16,0,0,60,61,5,3,0,0,61,62,3,6,3,0,62,63,5,4,0,0,63,64,3,4,2,0,64,
        91,1,0,0,0,65,66,5,13,0,0,66,71,5,34,0,0,67,68,5,20,0,0,68,70,5,
        34,0,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,
        74,1,0,0,0,73,71,1,0,0,0,74,91,5,19,0,0,75,76,5,14,0,0,76,81,3,6,
        3,0,77,78,5,20,0,0,78,80,3,6,3,0,79,77,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,19,
        0,0,85,91,1,0,0,0,86,87,3,6,3,0,87,88,5,19,0,0,88,91,1,0,0,0,89,
        91,5,19,0,0,90,21,1,0,0,0,90,29,1,0,0,0,90,40,1,0,0,0,90,50,1,0,
        0,0,90,59,1,0,0,0,90,65,1,0,0,0,90,75,1,0,0,0,90,86,1,0,0,0,90,89,
        1,0,0,0,91,5,1,0,0,0,92,93,6,3,-1,0,93,106,5,34,0,0,94,106,7,0,0,
        0,95,106,5,35,0,0,96,106,5,36,0,0,97,106,5,38,0,0,98,99,5,3,0,0,
        99,100,3,6,3,0,100,101,5,4,0,0,101,106,1,0,0,0,102,103,5,34,0,0,
        103,104,5,7,0,0,104,106,3,6,3,1,105,92,1,0,0,0,105,94,1,0,0,0,105,
        95,1,0,0,0,105,96,1,0,0,0,105,97,1,0,0,0,105,98,1,0,0,0,105,102,
        1,0,0,0,106,127,1,0,0,0,107,108,10,7,0,0,108,109,7,1,0,0,109,126,
        3,6,3,8,110,111,10,6,0,0,111,112,7,2,0,0,112,126,3,6,3,7,113,114,
        10,5,0,0,114,115,7,3,0,0,115,126,3,6,3,6,116,117,10,4,0,0,117,118,
        7,4,0,0,118,126,3,6,3,5,119,120,10,3,0,0,120,121,5,32,0,0,121,126,
        3,6,3,4,122,123,10,2,0,0,123,124,5,33,0,0,124,126,3,6,3,3,125,107,
        1,0,0,0,125,110,1,0,0,0,125,113,1,0,0,0,125,116,1,0,0,0,125,119,
        1,0,0,0,125,122,1,0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,
        1,0,0,0,128,7,1,0,0,0,129,127,1,0,0,0,11,11,19,25,35,57,71,81,90,
        105,125,127
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'('", "')'", "'true'", 
                     "'false'", "'='", "<INVALID>", "'bool'", "'float'", 
                     "'int'", "'string'", "'read'", "'write'", "'if'", "'while'", 
                     "'else'", "'for'", "';'", "','", "'.'", "'*'", "'/'", 
                     "'%'", "'+'", "'-'", "'<'", "'>'", "'!'", "'=='", "'!='", 
                     "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "WS", "BOOLEAN", "FLOAT", "INT", "STRING", "READ", 
                      "WRITE", "IF", "WHILE", "ELSE", "FOR", "SEMI", "COMMA", 
                      "CON", "MUL", "DIV", "MOD", "ADD", "SUB", "LES", "GRE", 
                      "NEG", "EQ", "NEQ", "AND", "OR", "IDENTIFIER", "DECIMAL_LITERAL", 
                      "FLOAT_LITERAL", "BOOL_LITERAL", "STRING_LITERAL" ]

    RULE_program = 0
    RULE_primitiveType = 1
    RULE_statement = 2
    RULE_expr = 3

    ruleNames =  [ "program", "primitiveType", "statement", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    WS=8
    BOOLEAN=9
    FLOAT=10
    INT=11
    STRING=12
    READ=13
    WRITE=14
    IF=15
    WHILE=16
    ELSE=17
    FOR=18
    SEMI=19
    COMMA=20
    CON=21
    MUL=22
    DIV=23
    MOD=24
    ADD=25
    SUB=26
    LES=27
    GRE=28
    NEG=29
    EQ=30
    NEQ=31
    AND=32
    OR=33
    IDENTIFIER=34
    DECIMAL_LITERAL=35
    FLOAT_LITERAL=36
    BOOL_LITERAL=37
    STRING_LITERAL=38

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.statement()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 395137908330) != 0)):
                    break

            self.state = 13
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type_ = None # Token

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(ExprParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = ExprParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primitiveType)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                localctx.type_ = self.match(ExprParser.INT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                localctx.type_ = self.match(ExprParser.FLOAT)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                localctx.type_ = self.match(ExprParser.STRING)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 18
                localctx.type_ = self.match(ExprParser.BOOLEAN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyStatement" ):
                listener.enterEmptyStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyStatement" ):
                listener.exitEmptyStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyStatement" ):
                return visitor.visitEmptyStatement(self)
            else:
                return visitor.visitChildren(self)


    class WriteStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WRITE(self):
            return self.getToken(ExprParser.WRITE, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStatement" ):
                listener.enterWriteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStatement" ):
                listener.exitWriteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStatement" ):
                return visitor.visitWriteStatement(self)
            else:
                return visitor.visitChildren(self)


    class BlockOfStatementsContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockOfStatements" ):
                listener.enterBlockOfStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockOfStatements" ):
                listener.exitBlockOfStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockOfStatements" ):
                return visitor.visitBlockOfStatements(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.init = None # ExprContext
            self.cond = None # ExprContext
            self.update = None # ExprContext
            self.loop = None # StatementContext
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class ReadStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def READ(self):
            return self.getToken(ExprParser.READ, 0)
        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDENTIFIER)
            else:
                return self.getToken(ExprParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReadStatement" ):
                listener.enterReadStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReadStatement" ):
                listener.exitReadStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReadStatement" ):
                return visitor.visitReadStatement(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class DeclarationContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitiveType(self):
            return self.getTypedRuleContext(ExprParser.PrimitiveTypeContext,0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDENTIFIER)
            else:
                return self.getToken(ExprParser.IDENTIFIER, i)
        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.pos = None # StatementContext
            self.neg = None # StatementContext
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ExprParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = ExprParser.BlockOfStatementsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(ExprParser.T__0)
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 395137908330) != 0):
                    self.state = 22
                    self.statement()
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 28
                self.match(ExprParser.T__1)
                pass
            elif token in [9, 10, 11, 12]:
                localctx = ExprParser.DeclarationContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.primitiveType()
                self.state = 30
                self.match(ExprParser.IDENTIFIER)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 31
                    self.match(ExprParser.COMMA)
                    self.state = 32
                    self.match(ExprParser.IDENTIFIER)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(ExprParser.SEMI)
                pass
            elif token in [18]:
                localctx = ExprParser.ForContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(ExprParser.FOR)
                self.state = 41
                self.match(ExprParser.T__2)
                self.state = 42
                localctx.init = self.expr(0)
                self.state = 43
                self.match(ExprParser.SEMI)
                self.state = 44
                localctx.cond = self.expr(0)
                self.state = 45
                self.match(ExprParser.SEMI)
                self.state = 46
                localctx.update = self.expr(0)
                self.state = 47
                self.match(ExprParser.T__3)
                self.state = 48
                localctx.loop = self.statement()
                pass
            elif token in [15]:
                localctx = ExprParser.IfElseContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(ExprParser.IF)
                self.state = 51
                self.match(ExprParser.T__2)
                self.state = 52
                localctx.cond = self.expr(0)
                self.state = 53
                self.match(ExprParser.T__3)
                self.state = 54
                localctx.pos = self.statement()
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 55
                    self.match(ExprParser.ELSE)
                    self.state = 56
                    localctx.neg = self.statement()


                pass
            elif token in [16]:
                localctx = ExprParser.WhileContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(ExprParser.WHILE)
                self.state = 60
                self.match(ExprParser.T__2)
                self.state = 61
                self.expr(0)
                self.state = 62
                self.match(ExprParser.T__3)
                self.state = 63
                self.statement()
                pass
            elif token in [13]:
                localctx = ExprParser.ReadStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 65
                self.match(ExprParser.READ)
                self.state = 66
                self.match(ExprParser.IDENTIFIER)
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 67
                    self.match(ExprParser.COMMA)
                    self.state = 68
                    self.match(ExprParser.IDENTIFIER)
                    self.state = 73
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 74
                self.match(ExprParser.SEMI)
                pass
            elif token in [14]:
                localctx = ExprParser.WriteStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.match(ExprParser.WRITE)
                self.state = 76
                self.expr(0)
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 77
                    self.match(ExprParser.COMMA)
                    self.state = 78
                    self.expr(0)
                    self.state = 83
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 84
                self.match(ExprParser.SEMI)
                pass
            elif token in [3, 5, 6, 34, 35, 36, 38]:
                localctx = ExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 86
                self.expr(0)
                self.state = 87
                self.match(ExprParser.SEMI)
                pass
            elif token in [19]:
                localctx = ExprParser.EmptyStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 89
                self.match(ExprParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivModContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(ExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def MOD(self):
            return self.getToken(ExprParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivMod" ):
                listener.enterMulDivMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivMod" ):
                listener.exitMulDivMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivMod" ):
                return visitor.visitMulDivMod(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool" ):
                return visitor.visitBool(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING_LITERAL(self):
            return self.getToken(ExprParser.STRING_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class LogicalAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAnd" ):
                listener.enterLogicalAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAnd" ):
                listener.exitLogicalAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAnd" ):
                return visitor.visitLogicalAnd(self)
            else:
                return visitor.visitChildren(self)


    class FloatContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT_LITERAL(self):
            return self.getToken(ExprParser.FLOAT_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DECIMAL_LITERAL(self):
            return self.getToken(ExprParser.DECIMAL_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)


    class RelationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def LES(self):
            return self.getToken(ExprParser.LES, 0)
        def GRE(self):
            return self.getToken(ExprParser.GRE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelation" ):
                listener.enterRelation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelation" ):
                listener.exitRelation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelation" ):
                return visitor.visitRelation(self)
            else:
                return visitor.visitChildren(self)


    class AddSubConContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def ADD(self):
            return self.getToken(ExprParser.ADD, 0)
        def SUB(self):
            return self.getToken(ExprParser.SUB, 0)
        def CON(self):
            return self.getToken(ExprParser.CON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubCon" ):
                listener.enterAddSubCon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubCon" ):
                listener.exitAddSubCon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubCon" ):
                return visitor.visitAddSubCon(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class LogicalOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOr" ):
                listener.enterLogicalOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOr" ):
                listener.exitLogicalOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOr" ):
                return visitor.visitLogicalOr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 93
                self.match(ExprParser.IDENTIFIER)
                pass

            elif la_ == 2:
                localctx = ExprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                localctx = ExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 95
                self.match(ExprParser.DECIMAL_LITERAL)
                pass

            elif la_ == 4:
                localctx = ExprParser.FloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 96
                self.match(ExprParser.FLOAT_LITERAL)
                pass

            elif la_ == 5:
                localctx = ExprParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 97
                self.match(ExprParser.STRING_LITERAL)
                pass

            elif la_ == 6:
                localctx = ExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 98
                self.match(ExprParser.T__2)
                self.state = 99
                self.expr(0)
                self.state = 100
                self.match(ExprParser.T__3)
                pass

            elif la_ == 7:
                localctx = ExprParser.AssignmentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 102
                self.match(ExprParser.IDENTIFIER)
                self.state = 103
                self.match(ExprParser.T__6)
                self.state = 104
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.MulDivModContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 107
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 108
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 109
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.AddSubConContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 110
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 111
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 102760448) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 112
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.RelationContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 113
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 114
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 115
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ComparisonContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 116
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 117
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==30 or _la==31):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 118
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = ExprParser.LogicalAndContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 119
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 120
                        self.match(ExprParser.AND)
                        self.state = 121
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = ExprParser.LogicalOrContext(self, ExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 123
                        self.match(ExprParser.OR)
                        self.state = 124
                        self.expr(3)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




