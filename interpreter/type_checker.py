from antlr4 import *
from dataclasses import dataclass
from enum import StrEnum

from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor

class TypeNames(StrEnum):
    INT = "int"
    FLOAT = "flo"
    STRING = "str"
    BOOL = "bol"
    LIST = "lst"


class TypeChecker(SPLVParserVisitor):
    @dataclass
    class Variable:
        type: str

        def __eq__(self, value):
            if self.type == TypeNames.LIST and TypeNames.LIST in value.type:
                return True
            elif value.type == TypeNames.LIST and TypeNames.LIST in self.type:
                return True
            
            # print(f"types: {self.type}, {value.type}")
            return self.type == value.type
        
        def getListElementType(self):
            return TypeChecker.Variable(self.type.strip(TypeNames.LIST)[1:-1])
    

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

        # registering the functions arguments in the function's scope
        # and the function itself in the global scope
        args = []
        for c in ctx.functionArgumentList().getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                args.append(t)
                self._addDefinition(name, self.Variable(t))

        function_name = ctx.functionIdentifier().Identifier().getText()
        return_type = ctx.functionIdentifier().functionReturnType().getText()

        self._addDefinition(function_name, self.Function(return_type, args), glob=True)

        self.visitChildren(ctx)
        self.scopes.pop()


    def visitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.append(self.Scope())
        
        name = ctx.loopStatementIterator().Identifier().getText();
        t = None

        for c in ctx.loopStatementIterator().getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()

        self._addDefinition(name, self.Variable(t))

        self.visitChildren(ctx)

        self.scopes.pop()


    def visitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.scopes.append(self.Scope())
        
        name = ctx.loopStatementIterator().Identifier().getText();
        t = None

        for c in ctx.loopStatementIterator().getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()

        self._addDefinition(name, self.Variable(t))

        self.visitChildren(ctx)

        self.scopes.pop()
        


    def visitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
        t = None
        name = ctx.Identifier().getText()
        glob = True if ctx.GlobalTypeModifier() is not None else False

        for c in ctx.getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()
        
        self._addDefinition(name, self.Variable(t), glob=glob)

        self.visitChildren(ctx)

    
    ###
    # type checking

    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        name = ctx.Identifier().getText()
        
        for scope in self.scopes[::-1]:
            if name in scope.types:
                return scope.types[name]


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        exps = ctx.expression()
        list_exp = exps[0]
        bounds = exps[1:]

        list_type = self.visit(list_exp)
        bound_types = [self.visit(b) for b in bounds]

        if list_type != self.Variable(TypeNames.LIST):
            raise Exception("Slcing operator can only be applied to lists")
        elif not all(t == self.Variable(TypeNames.INT) for t in bound_types):
            raise Exception("List slicing bounds must be integers")
        
        return list_type.getListElementType()


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        fun_name = ctx.functionCall().Identifier().getText()

        return self.Variable(self.scopes[0].types[fun_name].return_type)


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        exp = ctx.expression()
        type = self.visit(exp)

        if type != self.Variable(TypeNames.BOOL):
            raise Exception("NOT operator requires bool operand")
        
        return self.Variable(TypeNames.BOOL)


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        exps = ctx.expression()
        [list_exp, index] = exps
        list_type = self.visit(list_exp)
        index_type = self.visit(index)

        if not list_type == self.Variable(TypeNames.LIST):
            raise Exception("Indexing operator can only be applied to lists")
        elif not index_type == self.Variable(TypeNames.INT):
            raise Exception("List index has to be an integer")
        else:
            return list_type.getListElementType()



    # Visit a parse tree produced by SPLVParser#literalExpression.
    def visitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        literal = ctx.literal()

        if literal.IntLiteral() is not None:
            return self.Variable(TypeNames.INT)
        elif literal.FloatLiteral() is not None:
            return self.Variable(TypeNames.FLOAT)
        elif literal.StringLiteral() is not None:
            return self.Variable(TypeNames.STRING)
        elif literal.BoolLiteral() is not None:
            return self.Variable(TypeNames.BOOL)
        elif literal.listLiteral() is not None:
            return self.visit(literal.listLiteral())
    

    def visitListFromRangeLiteral(self, ctx:SPLVParser.ListFromRangeLiteralContext):
        expressions = ctx.expression()
        types = [self.visit(e) for e in expressions]

        if all(t == self.Variable(TypeNames.INT) for t in types):
            return self.Variable(f"{TypeNames.LIST}[{TypeNames.INT}]")
        else:
            raise Exception("List definition from range requires integer range boundaries")



    def visitListFromElementsLiteral(self, ctx:SPLVParser.ListFromElementsLiteralContext):
        expressions = ctx.expression()

        types = [self.visit(e) for e in expressions]

        if all([t == types[0] for t in types]):
            return self.Variable(f"{TypeNames.LIST}[{types[0].type}]")
        else:
            raise Exception("Non-matching types in list literal")



    def visitEmptyListLiteral(self, ctx:SPLVParser.EmptyListLiteralContext):
        return self.Variable(TypeNames.LIST)


    def _addDefinition(self, name:str, t: Variable | Function, glob: bool = False):
        scope = self.scopes[-1] if not glob else self.scopes[0]

        scope.types[name] = t
