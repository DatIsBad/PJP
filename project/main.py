from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser

input_stream = FileStream("input.txt")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.start_()

