from antlr4 import *
from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor


# a visitor class that ensures return statements are present in functions
class ReturnChecker(SPLVParserVisitor):
    def __init__(self):
        self.current_function = None
    

    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.visitChildren(ctx)
        self.current_function = None

    def visitFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        self.current_function = ctx.Identifier().getText()
        self.visitChildren(ctx)
        
    
    def visitFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        returns = False
        
        for statement in ctx.statementInFunction():
            if self.visit(statement) is True:
                returns = True
                break

        if not returns:
            raise Exception(f"Function {self.current_function} doesn't return a value in all control paths. Note that loop/while statements require outside return statements.")
    


    def visitStatementInFunction(self, ctx:SPLVParser.StatementInFunctionContext):
        if ctx.returnStatement() is not None:
            return True
        elif ctx.controlStatementInsideFunction() is not None:
            return self.visit(ctx.controlStatementInsideFunction())
        else:
            return False

    
    def visitControlStatementInsideFunction(self, ctx:SPLVParser.ControlStatementInsideFunctionContext):
        if ctx.whileStatementInsideFunction() is not None or ctx.loopStatementInsideFunction() is not None:
            return False
        
        return self.visit(ctx.ifStatementInsideFunction())


    def visitIfStatementInsideFunction(self, ctx:SPLVParser.IfStatementInsideFunctionContext):
        return all([self.visit(block) for block in ctx.functionControlBlock()])


    def visitFunctionControlBlock(self, ctx:SPLVParser.FunctionControlBlockContext):
        returns = False
        
        for statement in ctx.statementInFunction():
            if self.visit(statement) is True:
                returns = True
                break

        return returns