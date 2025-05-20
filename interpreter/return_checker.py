from antlr4 import *
from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor
from .errors import ReturnException


# a visitor class that ensures return statements are present in functions
class ReturnChecker(SPLVParserVisitor):
    VOID_KEYWORD = 'nul'
    
    def __init__(self):
        self.current_function = None
        self.current_function_is_void = False
    

    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.visitChildren(ctx)
        self.current_function = None
        self.current_function_is_void = False

    def visitFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        self.current_function = ctx.Identifier().getText()
        self.current_function_is_void = ctx.functionReturnType().getText() == self.VOID_KEYWORD
        self.visitChildren(ctx)
        
    
    def visitFunctionBlock(self, ctx:SPLVParser.FunctionBlockContext):
        returns = False
        
        for statement in ctx.statementInFunction():
            if self.visit(statement) is True:
                returns = True
                break

        if not self.current_function_is_void and not returns:
            raise ReturnException(f"Function {self.current_function} doesn't return a value in all control paths.", ctx.start.line, ctx.start.column)
        elif self.current_function_is_void and returns:
            raise ReturnException(f"Void function cannot return a value", ctx.start.line, ctx.start.column)


    def visitStatementInFunction(self, ctx:SPLVParser.StatementInFunctionContext):
        if ctx.returnStatement() is not None and ctx.returnStatement().expression() is not None:
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