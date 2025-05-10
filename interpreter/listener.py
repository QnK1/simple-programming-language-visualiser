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
    

    






     # Enter a parse tree produced by SPLVParser#parenthesesExpression.
    def enterParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#parenthesesExpression.
    def exitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#inOperatorExpression.
    def enterInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#inOperatorExpression.
    def exitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#additiveOperatorExpression.
    def enterAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def exitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def enterComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def exitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def enterMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def exitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#booleanOperatorExpression.
    def enterBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def exitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#listSlicingExpression.
    def enterListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#listSlicingExpression.
    def exitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#notOperatorExpression.
    def enterNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#notOperatorExpression.
    def exitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#listIndexingExpression.
    def enterListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#listIndexingExpression.
    def exitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#literalExpression.
    def enterLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by SPLVParser#literalExpression.
    def exitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        print(ctx.getText())


    # Enter a parse tree produced by SPLVParser#functionCall.
    def enterFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SPLVParser#functionCall.
    def exitFunctionCall(self, ctx:SPLVParser.FunctionCallContext):
        print(ctx.getText())