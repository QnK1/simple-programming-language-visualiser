# Generated from d:/Desktop/tkik_new/simple_programming_language_visualiser/simple_programming_language_visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by SPLVParser#statementInControlBlock.
    def enterStatementInControlBlock(self, ctx:SPLVParser.StatementInControlBlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#statementInControlBlock.
    def exitStatementInControlBlock(self, ctx:SPLVParser.StatementInControlBlockContext):
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


    # Enter a parse tree produced by SPLVParser#type.
    def enterType(self, ctx:SPLVParser.TypeContext):
        pass

    # Exit a parse tree produced by SPLVParser#type.
    def exitType(self, ctx:SPLVParser.TypeContext):
        pass


    # Enter a parse tree produced by SPLVParser#parenthesesExpression.
    def enterParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#parenthesesExpression.
    def exitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#inOperatorExpression.
    def enterInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#inOperatorExpression.
    def exitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#additiveOperatorExpression.
    def enterAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def exitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def enterComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def exitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def enterMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def exitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#booleanOperatorExpression.
    def enterBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def exitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#listSlicingExpression.
    def enterListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#listSlicingExpression.
    def exitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#notOperatorExpression.
    def enterNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#notOperatorExpression.
    def exitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#listIndexingExpression.
    def enterListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#listIndexingExpression.
    def exitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        pass


    # Enter a parse tree produced by SPLVParser#literalExpression.
    def enterLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#literalExpression.
    def exitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
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


    # Enter a parse tree produced by SPLVParser#controlBlock.
    def enterControlBlock(self, ctx:SPLVParser.ControlBlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#controlBlock.
    def exitControlBlock(self, ctx:SPLVParser.ControlBlockContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionBlock.
    def enterFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionBlock.
    def exitFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by SPLVParser#returnStatement.
    def enterReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#returnStatement.
    def exitReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionArgumentList.
    def enterFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionArgumentList.
    def exitFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionIdentifier.
    def enterFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionIdentifier.
    def exitFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        pass


    # Enter a parse tree produced by SPLVParser#functionArgument.
    def enterFunctionArgument(self, ctx:SPLVParser.FunctionArgumentContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionArgument.
    def exitFunctionArgument(self, ctx:SPLVParser.FunctionArgumentContext):
        pass


    # Enter a parse tree produced by SPLVParser#controlStatement.
    def enterControlStatement(self, ctx:SPLVParser.ControlStatementContext):
        pass

    # Exit a parse tree produced by SPLVParser#controlStatement.
    def exitControlStatement(self, ctx:SPLVParser.ControlStatementContext):
        pass


    # Enter a parse tree produced by SPLVParser#controlStatementInsideFunction.
    def enterControlStatementInsideFunction(self, ctx:SPLVParser.ControlStatementInsideFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#controlStatementInsideFunction.
    def exitControlStatementInsideFunction(self, ctx:SPLVParser.ControlStatementInsideFunctionContext):
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


    # Enter a parse tree produced by SPLVParser#ifStatementInsideFunction.
    def enterIfStatementInsideFunction(self, ctx:SPLVParser.IfStatementInsideFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#ifStatementInsideFunction.
    def exitIfStatementInsideFunction(self, ctx:SPLVParser.IfStatementInsideFunctionContext):
        pass


    # Enter a parse tree produced by SPLVParser#whileStatementInsideFunction.
    def enterWhileStatementInsideFunction(self, ctx:SPLVParser.WhileStatementInsideFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#whileStatementInsideFunction.
    def exitWhileStatementInsideFunction(self, ctx:SPLVParser.WhileStatementInsideFunctionContext):
        pass


    # Enter a parse tree produced by SPLVParser#loopStatementInsideFunction.
    def enterLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        pass

    # Exit a parse tree produced by SPLVParser#loopStatementInsideFunction.
    def exitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        pass


    # Enter a parse tree produced by SPLVParser#loopStatementIterator.
    def enterLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        pass

    # Exit a parse tree produced by SPLVParser#loopStatementIterator.
    def exitLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        pass



del SPLVParser