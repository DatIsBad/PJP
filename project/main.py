from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from TypeCheck import TypeCheck
from CodeGenerator import CodeGenerator
from VirtualMachine import VirtualMachine


filename = "input3.txt"
input_stream = FileStream(filename)
lexer = ExprLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.program()


#typeChecker = TypeCheck()
#typeChecker.visit(tree)


codeGen = CodeGenerator()
codeGen.visit(tree)
codeGen.intofile(filename)
print(codeGen)
print('--------------')

vMachine = VirtualMachine()
vMachine.loadData(codeGen.lines)
vMachine.startMachine()

#print(type(True).__name__)

#print(tree.toStringTree(recog=parser))
