from antlr4 import *
from .base.SPLVParser import SPLVParser
from .base.SPLVParserListener import SPLVParserListener


# a listener class that ensures type correctness, usage of previously defined identifiers
class DeclarationChecker(SPLVParserListener):
    class Scope:
        def __init__(self):
            self.names: set[str] = set()
    
    def __init__(self):
        self.scopes = [self.Scope()]
    
    
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

        self._addDefinition(name)

    def exitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.pop()
    
    def exitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.scopes.pop()
    
    
    def exitFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        
        for c in ctx.getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                self._addDefinition(name, False)
    
    
    def exitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        t = None
        name = ctx.Identifier().getText()
        glob = True if ctx.GlobalTypeModifier() is not None else False

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()
        
        self._addDefinition(name, glob=glob)


    def exitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        name = ctx.Identifier().getText()

        self._checkIfDefined(name)
    

    def exitLValue(self, ctx:SPLVParser.LValueContext):
        name = ctx.Identifier().getText()

        self._checkIfDefined(name)


    def _addDefinition(self, name:str, glob: bool = False):
        scope = self.scopes[-1] if not glob else self.scopes[0]

        if name in scope.names:
            raise Exception(f"{name} has already been defined in this scope")
        
        scope.names.add(name)


    def _checkIfDefined(self, name: str):
        for scope in self.scopes:
            if name in scope.names:
                return

        raise Exception(f"{name} has not been defined")
    