from antlr4 import *
from .base.SPLVParser import SPLVParser
from .base.SPLVParserListener import SPLVParserListener
from enum import Enum
from program.block import Block

# a listener class that ensures type correctness, usage of previously defined identifiers
# and inclusion of return statements in functions
class Listener(SPLVParserListener):
    class Scope(Enum):
        GLOBAL = 1
        FUNCTION = 2
    
    def __init__(self):
        self.current_scope = self.Scope.GLOBAL
        self.types = {
            self.Scope.GLOBAL : {},
            self.Scope.FUNCTION : {},
        }
        self.current_loop_iterator = None
    
    
    # change the current scope to FUNCTION when entering a function definition
    # this is sufficient, as the grammar doesn't support nested function definitions
    def enterFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.current_scope = self.Scope.FUNCTION
    
    
    # change the current scope to GLOBAL when exiting a function definition
    # this is sufficient, as the grammar doesn't support nested function definitions
    def exitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.current_scope = self.Scope.GLOBAL
        self.types[self.Scope.FUNCTION] = {}
    

    # temporarily add loop iterator to current scope
    def exitLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        name = ctx.Identifier().getText()
        t = None

        self.current_loop_iterator = name
        
        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()

        self._addDefinition(name, t, self.current_scope)


    # remove loop iterator from current scope
    def exitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.types[self.current_scope].pop(self.current_loop_iterator, None)
        self.current_loop_iterator = None
    
    
    # register variables from a function's argument list
    def exitFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        for c in ctx.getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                self._addDefinition(name, t, self.current_scope)
    

    # register a variable definition
    def exitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        t = None
        name = ctx.Identifier().getText()
        glob = True if ctx.GlobalTypeModifier() is not None else False

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()
        
        self._addDefinition(name, t, self.Scope.GLOBAL if glob else self.current_scope)

    # register a function's identifier and type in the global scope
    def exitFunctionIdentifier(self, ctx:SPLVParser.FunctionIdentifierContext):
        name = ctx.Identifier().getText()
        t = None

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()
        if t == None:
            t = ctx.VoidType().getText()
        
        self._addDefinition(name, f"fun:{t}", self.Scope.GLOBAL)


    # checking whether the identifier inside an expression has been previously defined
    def exitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        name = ctx.Identifier().getText()

        if name not in self.types[self.current_scope].keys():
            raise Exception(f"{name} has not been defined")
    

    # checking whether the function being called has been defined
    def exitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        name = ctx.getChild(0).Identifier().getText()
        
        if name not in self.types[self.current_scope].keys():
            raise Exception(f"{name} has not been defined")
    

    def _addDefinition(self, name:str, t:str, scope):
        scope = self.types[scope]
        
        if name in scope.keys():
            raise Exception(f"{name} has already been defined in this scope")
        
        scope[name] = t
    