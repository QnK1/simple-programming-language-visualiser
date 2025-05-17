from antlr4 import *
from dataclasses import dataclass

from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor


class TypeChecker(SPLVParserVisitor):
    @dataclass
    class Variable:
        type: str
    

    @dataclass
    class Function:
        return_type: str
        args: list[str]
    

    class Scope:
        def __init__(self):
            self.types = {}


    def __init__(self):
        self.scopes = [self.Scope()]

    
    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        self.scopes.append(self.Scope())
        self.visitChildren(ctx)
        self.scopes.pop()
    

    def visitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.append(self.Scope())
        self.visitChildren(ctx)
        self.scopes.pop()



    # temporarily add loop iterator to current scope
    def visitLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        print(ctx.Identifier())
        
        name = ctx.Identifier().getText()
        t = None

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()

        self._addDefinition(name, self.Variable(t))


    # remove loop iterator from current scope
    def exitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.pop()

    

    def _addDefinition(self, name:str, t: Variable | Function, glob: bool = False):
        scope = self.scopes[-1] if not glob else self.scopes[0]

        scope.types[name] = t
