from antlr4 import *
from enum import Enum
from typing import Self

from .base.SPLVParser import SPLVParser
from .base.SPLVParserVisitor import SPLVParserVisitor
from .run_utils import *



class Runner(SPLVParserVisitor):
    def __init__(self):
        self.result: list[Statement] = []

    def visitProgram(self, ctx:SPLVParser.ProgramContext):
        self.visitChildren(ctx)

        return self.result
    

    def visitStatement(self, ctx:SPLVParser.StatementContext):
        if ctx.variableDefinition() is not None:
            n, t, f, e = self._defineVariable(ctx)
            
            self.result.append(VariableDefinitionStatement(ctx.start.line, ctx.start.column, n, t, f, e))
        elif ctx.variableAssignment() is not None:
            self.result.append(VariableAssignmentStatement(ctx.start.line, ctx.start.column))
        elif ctx.functionDefinition() is not None:
            self.result.append(FunctionDefinitionStatement(ctx.start.line, ctx.start.column))
        elif ctx.functionCall() is not None:
            self.result.append(FunctionCallStatement(ctx.start.line, ctx.start.column))
        elif ctx.controlStatement().ifStatement() is not None:
            self.result.append(IfStatement(ctx.start.line, ctx.start.column))
        elif ctx.controlStatement().whileStatement() is not None:
            self.result.append(WhileStatement(ctx.start.line, ctx.start.column))
        elif ctx.controlStatement().loopStatement() is not None:
            self.result.append(LoopStatement(ctx.start.line, ctx.start.column))


    # def visitVariableDefinition(self, ctx:SPLVParser.VariableDefinitionContext):
    #     counter = ExpressionCounter()
    #     c = counter.visit(ctx.expression())
    #     print(c)

    
    def _defineVariable(self, ctx):
        rhs_exp = ctx.variableDefinition().expression()

        calculator = ExpressionCalculator()
        calculator.calculate(rhs_exp)


        
        return None, None, None, None

class ExpressionCalculator(SPLVParserVisitor):
    def __init__(self):
        self.original_expression = None
        self.depth = None
        self.starting_depth = None
    
    def calculate(self, exp):
        self.original_expression = exp.getText()

        counter = ExpressionCounter()
        self.starting_depth = counter.visit(exp)
        stages = []

        while self.starting_depth >= 0:
            # print(f"depth: {self.starting_depth}")
            self.depth = self.starting_depth
            stages.append(Expression.Stage(self.visit(exp)))
            self.starting_depth = self.starting_depth - 1
        
        print("Stages:")
        for stage in stages:
            print(stage.content)
    
    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        content = self.visit(ctx.expression())
        
        if start_depth > 0:
            return f"({content})"
        else:
            return content



    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        if start_depth > 0:
            return f"{left_content}+{right_content}"
        else:
            return left_content + right_content


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        start_depth = self.depth
        self.depth = self.depth - 1

        left_exp = ctx.expression()[0]
        right_exp = ctx.expression()[1]

        left_content = self.visit(left_exp)
        right_content = self.visit(right_exp)
        
        if start_depth > 0:
            return f"{left_content}*{right_content}"
        else:
            return left_content * right_content


    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SPLVParser#literalExpression.
    def visitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        if ctx.literal().listLiteral() is None:
            # print(f"start depth: {self.depth}, return val: {self._getLiteralValue(ctx.literal())}")
            return self._getLiteralValue(ctx.literal())
        
        if isinstance(ctx.literal().listLiteral(), SPLVParser.EmptyListLiteralContext):
            return ListValue([])
        elif isinstance(ctx.literal().listLiteral(), SPLVParser.ListFromElementsLiteralContext):
            start_depth = self.depth

            exps = ctx.literal().listLiteral().expression()
            content = [self.visit(e) for e in exps]

            if start_depth > 0:
                return f"{ListValue(content)}"
            else:
                return ListValue(content)
        elif isinstance(ctx.literal().listLiteral(), SPLVParser.ListFromRangeLiteralContext):
            start_depth = self.depth

            exp1 = ctx.literal().listLiteral().expression()[0]
            exp2 = ctx.literal().listLiteral().expression()[1]
            
            content1 = self.visit(exp1)
            content2 = self.visit(exp2)

            if start_depth > 0:
                return f"[{content1}..{content2}]"
            else:
                return ListValue([i for i in range(content1.value, content2.value)])


    

    def _getLiteralValue(self, ctx):
        if ctx.IntLiteral() is not None:
            literal = ctx.IntLiteral()
            val = IntValue(int(literal.getText()))
        elif ctx.FloatLiteral() is not None:
            literal = ctx.FloatLiteral()
            val = FloatValue(float(literal.getText()))
        elif ctx.StringLiteral() is not None:
            literal = ctx.StringLiteral()
            val = StringValue(literal.getText()[1:-1])
        elif ctx.BoolLiteral() is not None:
            literal = ctx.BoolLiteral()
            val = BoolValue(True if literal.getText().lower() == "true" else False)
        
        return val



class ExpressionCounter(SPLVParserVisitor):
    # Visit a parse tree produced by SPLVParser#parenthesesExpression.
    def visitParenthesesExpression(self, ctx:SPLVParser.ParenthesesExpressionContext):
        return 1 + self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#inOperatorExpression.
    def visitInOperatorExpression(self, ctx:SPLVParser.InOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#additiveOperatorExpression.
    def visitAdditiveOperatorExpression(self, ctx:SPLVParser.AdditiveOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#comparisonOperatorExpression.
    def visitComparisonOperatorExpression(self, ctx:SPLVParser.ComparisonOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#multiplicativeOperatorExpression.
    def visitMultiplicativeOperatorExpression(self, ctx:SPLVParser.MultiplicativeOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#booleanOperatorExpression.
    def visitBooleanOperatorExpression(self, ctx:SPLVParser.BooleanOperatorExpressionContext):
        exps = ctx.expression()
        return 1 + self.visit(exps[0]) + self.visit(exps[1])


    # Visit a parse tree produced by SPLVParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:SPLVParser.IdentifierExpressionContext):
        return 1


    # Visit a parse tree produced by SPLVParser#listSlicingExpression.
    def visitListSlicingExpression(self, ctx:SPLVParser.ListSlicingExpressionContext):
        exps = ctx.expression()
        list_exp = exps[0]
        ind_exp1 = exps[1] if len(exps) >= 2 else None
        ind_exp2 = exps[2] if len(exps) == 3 else None

        count1 = self.visit(ind_exp1) if ind_exp1 is not None else 0
        count2 = self.visit(ind_exp2) if ind_exp2 is not None else 0

        return 1 + self.visit(list_exp) + count1 + count2 - (1 if type(list_exp) == SPLVParser.IdentifierExpressionContext else 0)


    # Visit a parse tree produced by SPLVParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:SPLVParser.FunctionCallExpressionContext):
        exps = ctx.functionCall().passedParametersList().expression()

        return 1 + sum([self.visit(e) for e in exps])


    # Visit a parse tree produced by SPLVParser#notOperatorExpression.
    def visitNotOperatorExpression(self, ctx:SPLVParser.NotOperatorExpressionContext):
        return 1 + self.visit(ctx.expression())


    # Visit a parse tree produced by SPLVParser#listIndexingExpression.
    def visitListIndexingExpression(self, ctx:SPLVParser.ListIndexingExpressionContext):
        exps = ctx.expression()


        return 1 + sum([self.visit(e) for e in exps]) - (1 if type(exps[0]) == SPLVParser.IdentifierExpressionContext else 0)


    # Visit a parse tree produced by SPLVParser#literalExpression.
    def visitLiteralExpression(self, ctx:SPLVParser.LiteralExpressionContext):
        res = 0
        if ctx.literal().listLiteral() is not None and type(ctx.literal().listLiteral()) != SPLVParser.EmptyListLiteralContext:
            res += sum([self.visit(e) for e in ctx.literal().listLiteral().expression()])

        
        return res