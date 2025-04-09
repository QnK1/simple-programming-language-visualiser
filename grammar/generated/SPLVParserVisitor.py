# Generated from d:/Desktop/SPLV/simple-programming-language-visualiser/grammar/SPLVParser.g4 by ANTLR 4.13.1
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


    # Visit a parse tree produced by SPLVParser#innerStatement.
    def visitInnerStatement(self, ctx:SPLVParser.InnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#literal.
    def visitLiteral(self, ctx:SPLVParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#listLiteral.
    def visitListLiteral(self, ctx:SPLVParser.ListLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#expression.
    def visitExpression(self, ctx:SPLVParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#functionCall.
    def visitFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#variableDefinition.
    def visitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#variableAssignment.
    def visitVariableAssignment(self, ctx:SPLVParser.VariableAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#block.
    def visitBlock(self, ctx:SPLVParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#functionBlock.
    def visitFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#returnStatement.
    def visitReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#controlStatement.
    def visitControlStatement(self, ctx:SPLVParser.ControlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#ifStatement.
    def visitIfStatement(self, ctx:SPLVParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#whileStatement.
    def visitWhileStatement(self, ctx:SPLVParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#loopStatement.
    def visitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        return self.visitChildren(ctx)



del SPLVParser