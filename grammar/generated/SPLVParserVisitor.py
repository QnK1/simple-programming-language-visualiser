# Generated from d:/Users/Kacper/Desktop/tkik/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SPLVParser import SPLVParser
else:
    from SPLVParser import SPLVParser

# This class defines a complete generic visitor for a parse tree produced by SPLVParser.

class SPLVParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SPLVParser#program.
    def visitProgram(self, ctx:SPLVParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#statement.
    def visitStatement(self, ctx:SPLVParser.StatementContext):
        return self.visitChildren(ctx)



del SPLVParser