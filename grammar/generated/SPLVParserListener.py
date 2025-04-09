# Generated from d:/Desktop/SPLV/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by SPLVParser#innerStatement.
    def enterInnerStatement(self, ctx:SPLVParser.InnerStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#innerStatement.
    def exitInnerStatement(self, ctx:SPLVParser.InnerStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#literal.
    def enterLiteral(self, ctx:SPLVParser.LiteralContext):
        pass

    # Exit a parse tree produced by SPLVParser#literal.
    def exitLiteral(self, ctx:SPLVParser.LiteralContext):
        pass


    # Enter a parse tree produced by SPLVParser#listLiteral.
    def enterListLiteral(self, ctx:SPLVParser.ListLiteralContext):
        pass

    # Exit a parse tree produced by SPLVParser#listLiteral.
    def exitListLiteral(self, ctx:SPLVParser.ListLiteralContext):
        pass


    # Enter a parse tree produced by SPLVParser#expression.
    def enterExpression(self, ctx:SPLVParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#expression.
    def exitExpression(self, ctx:SPLVParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionCall.
    def enterFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionCall.
    def exitFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SPLVParser#variableDefinition.
    def enterVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by SPLVParser#variableDefinition.
    def exitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by SPLVParser#variableAssignment.
    def enterVariableAssignment(self, ctx:SPLVParser.VariableAssignmentContext):
        pass

    # Exit a parse tree produced by SPLVParser#variableAssignment.
    def exitVariableAssignment(self, ctx:SPLVParser.VariableAssignmentContext):
        pass


    # Enter a parse tree produced by SPLVParser#block.
    def enterBlock(self, ctx:SPLVParser.BlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#block.
    def exitBlock(self, ctx:SPLVParser.BlockContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SPLVParser#controlStatement.
    def enterControlStatement(self, ctx:SPLVParser.ControlStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#controlStatement.
    def exitControlStatement(self, ctx:SPLVParser.ControlStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#ifStatement.
    def enterIfStatement(self, ctx:SPLVParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#ifStatement.
    def exitIfStatement(self, ctx:SPLVParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#whileStatement.
    def enterWhileStatement(self, ctx:SPLVParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#whileStatement.
    def exitWhileStatement(self, ctx:SPLVParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#loopStatement.
    def enterLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#loopStatement.
    def exitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        pass



del SPLVParser