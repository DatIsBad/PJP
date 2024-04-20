from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprInterp import TypeCheck
from codeGenerator import CodeGenerator


input_stream = FileStream("input2.txt")
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.program()


#typeChecker = TypeCheck()
#typeChecker.visit(tree)


codeGen = CodeGenerator()
codeGen.visit(tree)
codeGen.intofile("code.txt")
print(codeGen)



#print(tree.toStringTree(recog=parser))