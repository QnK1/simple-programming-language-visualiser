from antlr4 import *
from dataclasses import dataclass
from enum import StrEnum

from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor
from .errors import TypeException

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
            elif TypeNames.LIST in value.type and TypeNames.LIST in self.type:
                return self.getListElementType() == value.getListElementType()
            
            return self.type == value.type
        
        def __str__(self):
            return self.type
        
        def getListElementType(self):
            return TypeChecker.Variable(self.type.strip(TypeNames.LIST)[1:-1])
    

    @dataclass
    class Function:
        return_type: str
        args: list
    

    class Scope:
        def __init__(self, name: str):
            self.types = {}
            self.name = name


    def __init__(self):
        self.scopes = [self.Scope("global")]

    
    def visitFunctionDefinition(self, ctx:SPLVParser.FunctionDefinitionContext):
        function_name = ctx.functionIdentifier().Identifier().getText()
        
        self.scopes.append(self.Scope(function_name))

        # registering the functions arguments in the function's scope
        # and the function itself in the global scope
        args = []
        for c in ctx.functionArgumentList().getChildren():
            if type(c) == SPLVParser.FunctionArgumentContext:
                t = c.getChild(0).getText()
                name = c.getChild(1).getText()
                args.append(t)
                self._addDefinition(name, self.Variable(t))

        return_type = self.Variable(ctx.functionIdentifier().functionReturnType().getText())

        self._addDefinition(function_name, self.Function(return_type, [self.Variable(a) for a in args]), glob=True)

        self.visitChildren(ctx)
        self.scopes.pop()


    def visitLoopStatement(self, ctx:SPLVParser.LoopStatementContext):
        self.scopes.append(self.Scope(None))
        
        name = ctx.loopStatementIterator().Identifier().getText();
        t = None

        for c in ctx.loopStatementIterator().getChildren():
            if type(c) == SPLVParser.TypeContext:
                t = c.getText()

        self._addDefinition(name, self.Variable(t))

        self.visitChildren(ctx)

        self.scopes.pop()


    def visitLoopStatementInsideFunction(self, ctx:SPLVParser.LoopStatementInsideFunctionContext):
        self.scopes.append(self.Scope(None))
        
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
        

        exp = ctx.expression()
        exp_type = self.visit(exp)

        if self.Variable(t) != exp_type:
            raise TypeException(f"Assignment of {exp_type} value to {t} variable.", ctx.start.line, ctx.start.column)

        self._addDefinition(name, self.Variable(t), glob=glob)

        self.visitChildren(ctx)

    
    ###
    # type checking

    # Visit a parse tree produced by SPLVParser#variableAssignment.
    def visitVariableAssignment(self, ctx:SPLVParser.VariableAssignmentContext):
        l_type = self.visit(ctx.lValue())
        exp_type = self.visit(ctx.expression())

        if l_type != exp_type:
            raise TypeException(f"Assignment of {exp_type} value to {l_type} variable", ctx.start.line, ctx.start.column)
    

    # Visit a parse tree produced by SPLVParser#lValue.
    def visitLValue(self, ctx:SPLVParser.LValueContext):
        base_type = self._getType(ctx.Identifier().getText())
        exp = ctx.expression()

        if exp is None:
            return base_type
        else:
            exp_type = self.visit(exp)

            if base_type != self.Variable(TypeNames.LIST):
                raise TypeException(f"{base_type} type is not subscriptable", ctx.start.line, ctx.start.column)
            
            if exp_type != self.Variable(TypeNames.INT):
                raise TypeException("List index must be integer", ctx.start.line, ctx.start.column)
            
            return base_type.getListElementType()
    


    def visitReturnStatement(self, ctx:SPLVParser.ReturnStatementContext):
        exp = ctx.expression()

        if exp is None:
            return

        t = self.visit(exp)

        scope = None
        for s in self.scopes[::-1]:
            if s.name is not None:
                scope = s
                break
        
        name = scope.name
        return_type = self.scopes[0].types[name].return_type

        if t != return_type:
            raise TypeException(f"Function {name} should return {return_type}, not {t}", ctx.start.line, ctx.start.column)
    

    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        exps = ctx.expression()
        types = [self.visit(e) for e in exps]

        if types[0] == types[1].getListElementType():
            return self.Variable(TypeNames.BOOL)
        elif types[0] == self.Variable(TypeNames.STRING) == types[1]:
            return self.Variable(TypeNames.BOOL)


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        exps = ctx.expression()
        types = [self.visit(e) for e in exps]
        op = ctx.AdditiveOperator().getText()

        if op == "+":
            if types[0] == types[1] and not any([t == self.Variable(TypeNames.BOOL) for t in types]):
                return types[0]
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.LIST) and types[0].getListElementType() == types[1]:
                return types[0]
            elif types[1] == self.Variable(TypeNames.LIST) and types[1].getListElementType() == types[0]:
                return types[1]
            else:
                raise TypeException(f"Types {types[0]} and {types[1]} invalid for + operator", ctx.start.line, ctx.start.column)
        elif op == "-":
            if types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.INT)
            else:
                raise TypeException(f"Types {types[0]} and {types[1]} invalid for - operator", ctx.start.line, ctx.start.column)


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        exps = ctx.expression()
        types = [self.visit(exp) for exp in exps]
        op = ctx.ComparisonOperator().getText()

        if op in ("==", "!="):
            if types[0] != types[1]:
                raise TypeException("Matching types required for comparison operator", ctx.start.line, ctx.start.column)
        else:
            if types[0] == self.Variable(TypeNames.BOOL) or types[1] == self.Variable(TypeNames.BOOL):
                raise TypeException(f"Bool type not supported for operator {op}", ctx.start.line, ctx.start.column)
            elif types[0] == self.Variable(TypeNames.STRING) or types[1] == self.Variable(TypeNames.STRING):
                raise TypeException(f"String type not supported for operator {op}", ctx.start.line, ctx.start.column)
            elif types[0] == self.Variable(TypeNames.LIST) or types[1] == self.Variable(TypeNames.LIST):
                raise TypeException(f"List type not supported for operator {op}", ctx.start.line, ctx.start.column)
        
        return self.Variable(TypeNames.BOOL)


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        exps = ctx.expression()
        types = [self.visit(e) for e in exps]
        op = ctx.MultiplicativeOperator().getText()

        if op == "*":
            if types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.INT)
            elif types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            else:
                raise TypeException(f"TYpes {types[0]} and {types[1]} invalid for * operator", ctx.start.line, ctx.start.column)
        elif op == "/":
            if types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.FLOAT):
                return self.Variable(TypeNames.FLOAT)
            elif types[0] == self.Variable(TypeNames.FLOAT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.FLOAT)
            else:
                raise TypeException(f"TYpes {types[0]} and {types[1]} invalid for / operator", ctx.start.line, ctx.start.column)
        elif op == "%":
            if types[0] == self.Variable(TypeNames.INT) and types[1] == self.Variable(TypeNames.INT):
                return self.Variable(TypeNames.INT)
            else:
                raise TypeException(f"TYpes {types[0]} and {types[1]} invalid for % operator", ctx.start.line, ctx.start.column)

    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        exps = ctx.expression()
        types = [self.visit(exp) for exp in exps]
        op = ctx.BooleanOperator().getText()

        if types[0] != self.Variable(TypeNames.BOOL) or types[1] != self.Variable(TypeNames.BOOL):
            raise TypeException(f"Operand of types bool, bool required for {op} operator", ctx.start.line, ctx.start.column)
        
        return self.Variable(TypeNames.BOOL)


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        return self._getType(ctx.Identifier().getText())


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        exps = ctx.expression()
        list_exp = exps[0]
        bounds = exps[1:]

        list_type = self.visit(list_exp)
        bound_types = [self.visit(b) for b in bounds]

        if list_type != self.Variable(TypeNames.LIST):
            raise TypeException("Slcing operator can only be applied to lists", ctx.start.line, ctx.start.column)
        elif not all(t == self.Variable(TypeNames.INT) for t in bound_types):
            raise TypeException("List slicing bounds must be integers", ctx.start.line, ctx.start.column)
        
        return list_type


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        fun_name = ctx.functionCall().Identifier().getText()

        self.visit(ctx.functionCall())

        return self.scopes[0].types[fun_name].return_type


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        fun_name = ctx.Identifier().getText()

        if not isinstance(self.scopes[0].types[fun_name], self.Function):
            raise TypeException(f"{fun_name} is not callable", ctx.start.line, ctx.start.column)

        defined_types = self.scopes[0].types[fun_name].args
        passed_args = ctx.passedParametersList().expression()
        passed_types = [self.visit(arg) for arg in passed_args]
        

        if len(defined_types) != len(passed_types):
            raise TypeException(f"Incorrect number of arguments ({len(passed_types)}) passed for function with {len(defined_types)} arguments", ctx.start.line, ctx.start.column)

        for p, d in zip(passed_types, defined_types):
            if p != d:
                raise TypeException(f"Invalid type {p} for argument of type {d}", ctx.start.line, ctx.start.column)


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        exp = ctx.expression()
        type = self.visit(exp)

        if type != self.Variable(TypeNames.BOOL):
            raise TypeException("NOT operator requires bool operand", ctx.start.line, ctx.start.column)
        
        return self.Variable(TypeNames.BOOL)


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        exps = ctx.expression()
        [list_exp, index] = exps
        list_type = self.visit(list_exp)
        index_type = self.visit(index)

        if not list_type == self.Variable(TypeNames.LIST):
            raise TypeException("Indexing operator can only be applied to lists", ctx.start.line, ctx.start.column)
        elif not index_type == self.Variable(TypeNames.INT):
            raise TypeException("List index has to be an integer", ctx.start.line, ctx.start.column)
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
            raise TypeException("List definition from range requires integer range boundaries", ctx.start.line, ctx.start.column)



    def visitListFromElementsLiteral(self, ctx:SPLVParser.ListFromElementsLiteralContext):
        expressions = ctx.expression()

        types = [self.visit(e) for e in expressions]

        if all([t == types[0] for t in types]):
            return self.Variable(f"{TypeNames.LIST}[{types[0].type}]")
        else:
            raise TypeException("Non-matching types in list literal", ctx.start.line, ctx.start.column)



    def visitEmptyListLiteral(self, ctx:SPLVParser.EmptyListLiteralContext):
        return self.Variable(TypeNames.LIST)
    

    # Visit a parse tree produced by SPLVParser#loopStatementIterator.
    def visitLoopStatementIterator(self, ctx:SPLVParser.LoopStatementIteratorContext):
        t = self.Variable(ctx.type_().getText())
        exp = ctx.expression()
        exp_type = self.visit(exp)

        if exp_type not in (self.Variable(TypeNames.STRING), self.Variable(TypeNames.LIST)):
            raise TypeException(f"{exp_type} is not iterable", ctx.start.line, ctx.start.column)
        
        if not (t == self.Variable(TypeNames.STRING) == exp_type or t == exp_type.getListElementType() or len(exp_type.getListElementType().type) == 0):
            raise TypeException(f"Iterator of type {t} invalid for {exp_type}", ctx.start.line, ctx.start.column)
    

    # Visit a parse tree produced by SPLVParser#ifStatementInsideFunction.
    def visitIfStatementInsideFunction(self, ctx:SPLVParser.IfStatementInsideFunctionContext):
        t = self.visit(ctx.expression())
        
        if t != self.Variable(TypeNames.BOOL):
            raise TypeException(f"If statement condition has to be bool type, not {t}", ctx.start.line, ctx.start.column)

        self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#whileStatementInsideFunction.
    def visitWhileStatementInsideFunction(self, ctx:SPLVParser.WhileStatementInsideFunctionContext):
        t = self.visit(ctx.expression())
        
        if t != self.Variable(TypeNames.BOOL):
            raise TypeException(f"While statement condition has to be bool type, not {t}", ctx.start.line, ctx.start.column)
        
        self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#ifStatement.
    def visitIfStatement(self, ctx:SPLVParser.IfStatementContext):
        t = self.visit(ctx.expression())
        
        if t != self.Variable(TypeNames.BOOL):
            raise TypeException(f"If statement condition has to be bool type, not {t}", ctx.start.line, ctx.start.column)
        
        self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#whileStatement.
    def visitWhileStatement(self, ctx:SPLVParser.WhileStatementContext):
        t = self.visit(ctx.expression())
        
        if t != self.Variable(TypeNames.BOOL):
            raise TypeException(f"While statement condition has to be bool type, not {t}", ctx.start.line, ctx.start.column)
        
        self.visitChildren(ctx)


    def _addDefinition(self, name:str, t: Variable | Function, glob: bool = False):
        scope = self.scopes[-1] if not glob else self.scopes[0]

        scope.types[name] = t
    

    def _getType(self, name: str):
        for scope in self.scopes[::-1]:
            if name in scope.types:
                return scope.types[name]
