from antlr4 import *
from .base.SPLVParser import SPLVParser
from .base.SPLVParserListener import SPLVParserListener
from .errors import DeclarationException


# a listener class that ensures type correctness, usage of previously defined identifiers
class DeclarationChecker(SPLVParserListener):
    class Scope:
        def __init__(self):
            self.names: set[str] = set()
    
    def __init__(self):
        self.scopes = [self.Scope()]
        self.errors = []
    
    
    def enterFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.scopes.append(self.Scope())
    
    
    def exitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.scopes.pop()
    

    def enterLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.append(self.Scope())

    def enterLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.scopes.append(self.Scope())

    def exitLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        name = ctx.Identifier().getText()

        self._addDefinition(name, ctx)

    def exitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.pop()
    
    def exitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.scopes.pop()
    
    
    def exitFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        
        for c in ctx.getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                self._addDefinition(name, ctx, False)
    
    
    def exitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        t = None
        name = ctx.Identifier().getText()
        glob = True if ctx.GlobalTypeModifier() is not None else False

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()
        
        self._addDefinition(name, ctx, glob=glob)


    def exitFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        name = ctx.Identifier().getText()
        self._addDefinition(name, ctx, glob=True)


    def exitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        name = ctx.Identifier().getText()

        self._checkIfDefined(name, ctx)


    def exitFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        name = ctx.Identifier().getText()

        self._checkIfDefined(name, ctx)
    

    def exitLValue(self, ctx:SPLVParser.LValueContext):
        name = ctx
        while name.Identifier() is None:
            name = name.lValue()
        
        name = name.Identifier().getText()

        self._checkIfDefined(name, ctx)


    def _addDefinition(self, name:str, ctx, glob: bool = False):
        scope = self.scopes[-1] if not glob else self.scopes[0]

        if name in scope.names:
            raise DeclarationException(f"{name} has already been defined in this scope", ctx.start.line, ctx.start.column)
        
        scope.names.add(name)


    def _checkIfDefined(self, name: str, ctx):
        for scope in self.scopes:
            if name in scope.names:
                return

        raise DeclarationException(f"{name} has not been defined", ctx.start.line, ctx.start.column)
    
    