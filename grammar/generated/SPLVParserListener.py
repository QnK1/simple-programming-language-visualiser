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


    # Enter a parse tree produced by SPLVParser#statementInblock.
    def enterStatementInblock(self, ctx:SPLVParser.StatementInblockContext):
        pass

    # Exit a parse tree produced by SPLVParser#statementInblock.
    def exitStatementInblock(self, ctx:SPLVParser.StatementInblockContext):
        pass


    # Enter a parse tree produced by SPLVParser#statementInFunction.
    def enterStatementInFunction(self, ctx:SPLVParser.StatementInFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#statementInFunction.
    def exitStatementInFunction(self, ctx:SPLVParser.StatementInFunctionContext):
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


    # Enter a parse tree produced by SPLVParser#functionBlock.
    def enterFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionBlock.
    def exitFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by SPLVParser#voidFunctionBlock.
    def enterVoidFunctionBlock(self, ctx:SPLVParser.VoidFunctionBlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#voidFunctionBlock.
    def exitVoidFunctionBlock(self, ctx:SPLVParser.VoidFunctionBlockContext):
        pass


    # Enter a parse tree produced by SPLVParser#voidReturnStatement.
    def enterVoidReturnStatement(self, ctx:SPLVParser.VoidReturnStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#voidReturnStatement.
    def exitVoidReturnStatement(self, ctx:SPLVParser.VoidReturnStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#returnStatement.
    def enterReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#returnStatement.
    def exitReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#returningFunction.
    def enterReturningFunction(self, ctx:SPLVParser.ReturningFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#returningFunction.
    def exitReturningFunction(self, ctx:SPLVParser.ReturningFunctionContext):
        pass


    # Enter a parse tree produced by SPLVParser#voidFunction.
    def enterVoidFunction(self, ctx:SPLVParser.VoidFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#voidFunction.
    def exitVoidFunction(self, ctx:SPLVParser.VoidFunctionContext):
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