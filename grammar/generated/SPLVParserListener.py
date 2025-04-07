# Generated from d:/Users/Kacper/Desktop/tkik/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SPLVParser import SPLVParser
else:
    from SPLVParser import SPLVParser

# This class defines a complete listener for a parse tree produced by SPLVParser.
class SPLVParserListener(ParseTreeListener):

    # Enter a parse tree produced by SPLVParser#program.
    def enterProgram(self, ctx:SPLVParser.ProgramContext):
        pass

    # Exit a parse tree produced by SPLVParser#program.
    def exitProgram(self, ctx:SPLVParser.ProgramContext):
        pass


    # Enter a parse tree produced by SPLVParser#statement.
    def enterStatement(self, ctx:SPLVParser.StatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#statement.
    def exitStatement(self, ctx:SPLVParser.StatementContext):
        pass



del SPLVParser