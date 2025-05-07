from antlr4 import *
from base.SPLVParser import SPLVParser
from base.SPLVParserListener import SPLVParserListener
from enum import Enum


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
    
    
    # change the current scope to FUNCTION when entering a function definition
    # this is sufficient, as the grammar doesn't support nested function definitions
    def enterFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.current_scope = self.Scope.FUNCTION
    
    
    # change the current scope to GLOBAL when exiting a function definition
    # this is sufficient, as the grammar doesn't support nested function definitions
    def exitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.current_scope = self.Scope.GLOBAL
        self.types[self.Scope.FUNCTION] = {}
    
    
    # register variables from a function's argument list
    def exitFunctionArgumentList(self, ctx:SPLVParser.FunctionArgumentListContext):
        for c in ctx.getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                self._addDefinition(name, t)
    
    
    def _addDefinition(self, name:str, t:str):
        scope = self.types[self.current_scope]
        
        if name in scope.keys():
            raise Exception()
        
        scope[name] = t